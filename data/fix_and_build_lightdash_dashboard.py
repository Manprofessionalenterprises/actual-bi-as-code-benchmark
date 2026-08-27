import requests
import json

SERVER_URL = "https://app.lightdash.cloud"
API_KEY = "ldpat_74449a0f7ca1283fb57edf2b920f74c3"
PROJECT_UUID = "c9e5a221-4b16-435b-97b3-c657eed1a28d"

headers = {
    "Authorization": f"ApiKey {API_KEY}",
    "Content-Type": "application/json"
}

print("🚀 1. Récupération des graphiques existants sur Lightdash Cloud...")
resp = requests.get(f"{SERVER_URL}/api/v1/projects/{PROJECT_UUID}/charts", headers=headers)
print("Status Code:", resp.status_code)
charts = resp.json().get("results", [])
print(f"Nombre de graphiques trouvés : {len(charts)}")

for c in charts:
    print(f" - Chart: {c['name']} (UUID: {c['uuid']}, Slug: {c['slug']})")

print("\n🚀 2. Récupération des espaces (Spaces)...")
resp_space = requests.get(f"{SERVER_URL}/api/v1/projects/{PROJECT_UUID}/spaces", headers=headers)
spaces = resp_space.json().get("results", [])
space_uuid = spaces[0]["uuid"] if spaces else None
print(f"Space UUID: {space_uuid}")

# Création/Mise à jour des 4 graphiques réels
chart_definitions = [
    {
        "name": "1. Performance par Agence (CA & Marge)",
        "tableName": "fct_placements",
        "metricQuery": {
            "exploreName": "fct_placements",
            "dimensions": ["fct_placements_nom_agence"],
            "metrics": ["fct_placements_total_chiffre_affaires", "fct_placements_total_marge_brute"],
            "sorts": [{"fieldId": "fct_placements_total_chiffre_affaires", "descending": True}],
            "tableCalculations": [],
            "filters": {}
        },
        "chartConfig": {
            "type": "cartesian",
            "config": {
                "layout": {
                    "xField": "fct_placements_nom_agence",
                    "yField": ["fct_placements_total_chiffre_affaires", "fct_placements_total_marge_brute"]
                }
            }
        }
    },
    {
        "name": "2. CA par Secteur Client",
        "tableName": "fct_placements",
        "metricQuery": {
            "exploreName": "fct_placements",
            "dimensions": ["fct_placements_client_secteur"],
            "metrics": ["fct_placements_total_chiffre_affaires"],
            "sorts": [{"fieldId": "fct_placements_total_chiffre_affaires", "descending": True}],
            "tableCalculations": [],
            "filters": {}
        },
        "chartConfig": {
            "type": "pie",
            "config": {
                "groupFieldId": "fct_placements_client_secteur",
                "metricId": "fct_placements_total_chiffre_affaires"
            }
        }
    },
    {
        "name": "3. CA & Rentabilité par Région",
        "tableName": "fct_placements",
        "metricQuery": {
            "exploreName": "fct_placements",
            "dimensions": ["fct_placements_agence_region"],
            "metrics": ["fct_placements_total_chiffre_affaires", "fct_placements_total_marge_brute"],
            "sorts": [{"fieldId": "fct_placements_total_chiffre_affaires", "descending": True}],
            "tableCalculations": [],
            "filters": {}
        },
        "chartConfig": {
            "type": "cartesian",
            "config": {
                "layout": {
                    "xField": "fct_placements_agence_region",
                    "yField": ["fct_placements_total_chiffre_affaires", "fct_placements_total_marge_brute"]
                }
            }
        }
    },
    {
        "name": "4. Détail des Placements & Clients",
        "tableName": "fct_placements",
        "metricQuery": {
            "exploreName": "fct_placements",
            "dimensions": ["fct_placements_nom_agence", "fct_placements_client_nom", "fct_placements_candidat_metier"],
            "metrics": ["fct_placements_total_chiffre_affaires", "fct_placements_total_marge_brute"],
            "sorts": [{"fieldId": "fct_placements_total_chiffre_affaires", "descending": True}],
            "tableCalculations": [],
            "filters": {}
        },
        "chartConfig": {
            "type": "table"
        }
    }
]

created_chart_uuids = []

for c_def in chart_definitions:
    # Check if chart exists
    existing = next((c for c in charts if c["name"] == c_def["name"]), None)
    if existing:
        print(f"  ✅ Graphique existant conservé: {existing['name']} ({existing['uuid']})")
        created_chart_uuids.append((existing['uuid'], existing['name']))
    else:
        payload = {
            "name": c_def["name"],
            "tableName": c_def["tableName"],
            "metricQuery": c_def["metricQuery"],
            "chartConfig": c_def["chartConfig"],
            "spaceUuid": space_uuid
        }
        res = requests.post(f"{SERVER_URL}/api/v1/projects/{PROJECT_UUID}/saved", headers=headers, json=payload)
        if res.status_code in [200, 201]:
            chart_uuid = res.json()["results"]["uuid"]
            print(f"  🎉 Graphique créé: {c_def['name']} ({chart_uuid})")
            created_chart_uuids.append((chart_uuid, c_def['name']))
        else:
            print(f"  ❌ Erreur création graphique {c_def['name']}: {res.status_code} - {res.text}")

print("\n🚀 3. Récupération des Dashboards existants...")
resp_dash = requests.get(f"{SERVER_URL}/api/v1/projects/{PROJECT_UUID}/dashboards", headers=headers)
dashboards = resp_dash.json().get("results", [])
comex_dashboard = next((d for d in dashboards if "COMEX" in d["name"]), None)

tiles = []
positions = [
    {"x": 0, "y": 0, "w": 12, "h": 9},
    {"x": 12, "y": 0, "w": 12, "h": 9},
    {"x": 0, "y": 9, "w": 12, "h": 9},
    {"x": 12, "y": 9, "w": 12, "h": 9}
]

for idx, (uuid, name) in enumerate(created_chart_uuids):
    pos = positions[idx % len(positions)]
    tiles.append({
        "type": "saved_chart",
        "x": pos["x"],
        "y": pos["y"],
        "w": pos["w"],
        "h": pos["h"],
        "properties": {
            "savedChartUuid": uuid,
            "title": name,
            "belongsToDashboard": False
        }
    })

dashboard_payload = {
    "name": "GROUPE ACTUAL — PILOTAGE STRATÉGIQUE COMEX",
    "description": "Dashboard de pilotage exécutif connecté en direct à Snowflake pour la Direction Générale du Groupe Actual.",
    "tiles": tiles,
    "filters": {
        "dimensions": [],
        "metrics": [],
        "tableCalculations": []
    }
}

if comex_dashboard:
    dash_uuid = comex_dashboard["uuid"]
    print(f"  🔨 Mise à jour du Dashboard COMEX existant (UUID: {dash_uuid})...")
    res_dash = requests.patch(f"{SERVER_URL}/api/v1/dashboards/{dash_uuid}", headers=headers, json=dashboard_payload)
    if res_dash.status_code == 200:
        print("  🎉 DASHBOARD COMEX RE-RELIÉ ET MIS À JOUR AVEC SUCCÈS SUR LIGHTDASH CLOUD !")
    else:
        print(f"  ❌ Erreur mise à jour Dashboard: {res_dash.status_code} - {res_dash.text}")
else:
    dashboard_payload["spaceUuid"] = space_uuid
    res_dash = requests.post(f"{SERVER_URL}/api/v1/projects/{PROJECT_UUID}/dashboards", headers=headers, json=dashboard_payload)
    if res_dash.status_code in [200, 201]:
        print("  🎉 NOUVEAU DASHBOARD COMEX CRÉÉ ET LIÉ AVEC SUCCÈS !")
    else:
        print(f"  ❌ Erreur création Dashboard: {res_dash.status_code} - {res_dash.text}")

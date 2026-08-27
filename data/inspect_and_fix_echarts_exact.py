import requests
import json

SERVER_URL = "https://app.lightdash.cloud"
API_KEY = "ldpat_74449a0f7ca1283fb57edf2b920f74c3"
PROJECT_UUID = "c9e5a221-4b16-435b-97b3-c657eed1a28d"

headers = {
    "Authorization": f"ApiKey {API_KEY}",
    "Content-Type": "application/json"
}

chart1_uuid = "bb3ea95b-05ea-41c9-9e3b-9f4ab9622629"
chart3_uuid = "540027f6-69ce-44d4-9c1b-19d4b696622e"

print("🔍 1. Inspection des détails de Chart 1 avant modification...")
res1 = requests.get(f"{SERVER_URL}/api/v1/saved/{chart1_uuid}", headers=headers)
print("Chart 1 HTTP GET:", res1.status_code)
chart1_data = res1.json().get("results", {})
print("Current chartConfig Chart 1:")
print(json.dumps(chart1_data.get("chartConfig"), indent=2))

# Fabrication de la structure eCharts complète conforme au schéma Lightdash
echarts_cartesian_config_chart1 = {
    "type": "cartesian",
    "config": {
        "layout": {
            "xField": "fct_placements_nom_agence",
            "yField": ["fct_placements_total_chiffre_affaires"]
        },
        "eChartsConfig": {
            "series": [
                {
                    "type": "bar",
                    "encode": {
                        "xRef": {
                            "fieldId": "fct_placements_nom_agence"
                        },
                        "yRef": {
                            "fieldId": "fct_placements_total_chiffre_affaires"
                        }
                    }
                }
            ]
        }
    }
}

print("\n🛠️ 2. Envoi du correctif pour Chart 1...")
patch1 = {
    "chartConfig": echarts_cartesian_config_chart1
}
res1_patch = requests.patch(f"{SERVER_URL}/api/v1/saved/{chart1_uuid}", headers=headers, json=patch1)
print("Chart 1 PATCH Status:", res1_patch.status_code)

print("\n🔍 3. Vérification de la réponse serveur après PATCH...")
res1_check = requests.get(f"{SERVER_URL}/api/v1/saved/{chart1_uuid}", headers=headers)
print("Check Status:", res1_check.status_code)
print("Updated chartConfig Chart 1:")
print(json.dumps(res1_check.json().get("results", {}).get("chartConfig"), indent=2))

# Pour Chart 3 (Régions)
echarts_cartesian_config_chart3 = {
    "type": "cartesian",
    "config": {
        "layout": {
            "xField": "fct_placements_agence_region",
            "yField": ["fct_placements_total_chiffre_affaires"]
        },
        "eChartsConfig": {
            "series": [
                {
                    "type": "bar",
                    "encode": {
                        "xRef": {
                            "fieldId": "fct_placements_agence_region"
                        },
                        "yRef": {
                            "fieldId": "fct_placements_total_chiffre_affaires"
                        }
                    }
                }
            ]
        }
    }
}

print("\n🛠️ 4. Envoi du correctif pour Chart 3...")
patch3 = {
    "chartConfig": echarts_cartesian_config_chart3
}
res3_patch = requests.patch(f"{SERVER_URL}/api/v1/saved/{chart3_uuid}", headers=headers, json=patch3)
print("Chart 3 PATCH Status:", res3_patch.status_code)

res3_check = requests.get(f"{SERVER_URL}/api/v1/saved/{chart3_uuid}", headers=headers)
print("Check Status Chart 3:", res3_check.status_code)

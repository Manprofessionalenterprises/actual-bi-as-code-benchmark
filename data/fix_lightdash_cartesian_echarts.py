import requests
import json

SERVER_URL = "https://app.lightdash.cloud"
API_KEY = "ldpat_74449a0f7ca1283fb57edf2b920f74c3"
PROJECT_UUID = "c9e5a221-4b16-435b-97b3-c657eed1a28d"

headers = {
    "Authorization": f"ApiKey {API_KEY}",
    "Content-Type": "application/json"
}

# 1. Chart 1: Performance par Agence
chart1_uuid = "bb3ea95b-05ea-41c9-9e3b-9f4ab9622629"
chart1_payload = {
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
            },
            "eChartsConfig": {
                "series": [
                    {
                        "type": "bar",
                        "encode": {
                            "xRef": {"fieldId": "fct_placements_nom_agence"},
                            "yRef": {"fieldId": "fct_placements_total_chiffre_affaires"}
                        }
                    },
                    {
                        "type": "bar",
                        "encode": {
                            "xRef": {"fieldId": "fct_placements_nom_agence"},
                            "yRef": {"fieldId": "fct_placements_total_marge_brute"}
                        }
                    }
                ]
            }
        }
    }
}

res1 = requests.patch(f"{SERVER_URL}/api/v1/saved/{chart1_uuid}", headers=headers, json=chart1_payload)
print("Chart 1 update (Cartesian Bar):", res1.status_code)

# 2. Chart 3: CA & Rentabilité par Région
chart3_uuid = "540027f6-69ce-44d4-9c1b-19d4b696622e"
chart3_payload = {
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
            },
            "eChartsConfig": {
                "series": [
                    {
                        "type": "bar",
                        "encode": {
                            "xRef": {"fieldId": "fct_placements_agence_region"},
                            "yRef": {"fieldId": "fct_placements_total_chiffre_affaires"}
                        }
                    },
                    {
                        "type": "bar",
                        "encode": {
                            "xRef": {"fieldId": "fct_placements_agence_region"},
                            "yRef": {"fieldId": "fct_placements_total_marge_brute"}
                        }
                    }
                ]
            }
        }
    }
}

res3 = requests.patch(f"{SERVER_URL}/api/v1/saved/{chart3_uuid}", headers=headers, json=chart3_payload)
print("Chart 3 update (Cartesian Bar):", res3.status_code)

# Now update the dashboard tiles layout
dash_uuid = "136326bd-e9dd-471f-b8fb-1fbe7472d54f"
dashboard_payload = {
    "name": "GROUPE ACTUAL — PILOTAGE STRATÉGIQUE COMEX",
    "description": "Dashboard de pilotage exécutif connecté en direct à Snowflake pour la Direction Générale du Groupe Actual.",
    "tiles": [
        {
            "type": "saved_chart",
            "x": 0,
            "y": 0,
            "w": 12,
            "h": 9,
            "properties": {
                "savedChartUuid": chart1_uuid,
                "title": "1. Performance par Agence (CA & Marge)",
                "belongsToDashboard": False
            }
        },
        {
            "type": "saved_chart",
            "x": 12,
            "y": 0,
            "w": 12,
            "h": 9,
            "properties": {
                "savedChartUuid": "7429e013-23a5-4610-829e-b3ae9eb44808",
                "title": "2. CA par Secteur Client",
                "belongsToDashboard": False
            }
        },
        {
            "type": "saved_chart",
            "x": 0,
            "y": 9,
            "w": 12,
            "h": 9,
            "properties": {
                "savedChartUuid": chart3_uuid,
                "title": "3. CA & Rentabilité par Région",
                "belongsToDashboard": False
            }
        },
        {
            "type": "saved_chart",
            "x": 12,
            "y": 9,
            "w": 12,
            "h": 9,
            "properties": {
                "savedChartUuid": "40f4ea01-b171-4f2d-8d48-2dee89129d19",
                "title": "4. Détail des Placements & Clients",
                "belongsToDashboard": False
            }
        }
    ],
    "filters": {
        "dimensions": [],
        "metrics": [],
        "tableCalculations": []
    }
}

res_dash = requests.patch(f"{SERVER_URL}/api/v1/dashboards/{dash_uuid}", headers=headers, json=dashboard_payload)
print("Dashboard update status:", res_dash.status_code)
print("🎉 Mise à jour eCharts terminée avec succès !")

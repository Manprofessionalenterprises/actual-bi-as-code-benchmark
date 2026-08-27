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

# Exact eCharts Cartesian Config
chart_config_payload = {
    "chartConfig": {
        "type": "cartesian",
        "config": {
            "layout": {
                "xField": "fct_placements_nom_agence",
                "yField": [
                    "fct_placements_total_chiffre_affaires",
                    "fct_placements_total_marge_brute"
                ]
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
                    },
                    {
                        "type": "bar",
                        "encode": {
                            "xRef": {
                                "fieldId": "fct_placements_nom_agence"
                            },
                            "yRef": {
                                "fieldId": "fct_placements_total_marge_brute"
                            }
                        }
                    }
                ]
            }
        }
    }
}

print("🛠️ Envoi de eChartsConfig complet pour Chart 1...")
res = requests.patch(f"{SERVER_URL}/api/v1/saved/{chart1_uuid}", headers=headers, json=chart_config_payload)
print("PATCH Status:", res.status_code)

print("\n🔍 Vérification immédiate du GET apres PATCH :")
check_res = requests.get(f"{SERVER_URL}/api/v1/saved/{chart1_uuid}", headers=headers).json().get("results", {})
saved_config = check_res.get("chartConfig", {})

print("Returned chartConfig:")
print(json.dumps(saved_config, indent=2))

if "eChartsConfig" in saved_config.get("config", {}):
    print("\n✅ TROP FORT ! eChartsConfig EST DÉSORMAIS SAUVEGARDÉ DANS LIGHTDASH CLOUD !!!")
else:
    print("\n❌ eChartsConfig n'est pas retourné dans config.")

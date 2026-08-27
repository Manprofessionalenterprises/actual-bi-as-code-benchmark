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

# Full payload for Chart 1 with type: "table"
full_payload_1 = {
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
        "type": "table"
    }
}

print("🛠️ Envoi du PATCH complet pour Chart 1...")
res1 = requests.patch(f"{SERVER_URL}/api/v1/saved/{chart1_uuid}", headers=headers, json=full_payload_1)
print("Status Code Chart 1:", res1.status_code)

# Full payload for Chart 3 with type: "table"
full_payload_3 = {
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
        "type": "table"
    }
}

print("🛠️ Envoi du PATCH complet pour Chart 3...")
res3 = requests.patch(f"{SERVER_URL}/api/v1/saved/{chart3_uuid}", headers=headers, json=full_payload_3)
print("Status Code Chart 3:", res3.status_code)

print("\n🔍 Vérification stricte des retours API après modification complète :")
get1 = requests.get(f"{SERVER_URL}/api/v1/saved/{chart1_uuid}", headers=headers).json().get("results", {})
get3 = requests.get(f"{SERVER_URL}/api/v1/saved/{chart3_uuid}", headers=headers).json().get("results", {})

print("Chart 1 type vérifié:", get1.get("chartConfig", {}).get("type"))
print("Chart 3 type vérifié:", get3.get("chartConfig", {}).get("type"))

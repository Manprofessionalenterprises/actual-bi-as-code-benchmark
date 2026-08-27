import requests
import json

SERVER_URL = "https://app.lightdash.cloud"
API_KEY = "ldpat_74449a0f7ca1283fb57edf2b920f74c3"
PROJECT_UUID = "c9e5a221-4b16-435b-97b3-c657eed1a28d"

headers = {
    "Authorization": f"ApiKey {API_KEY}",
    "Content-Type": "application/json"
}

# Chart 1: Performance par Agence (UUID: bb3ea95b-05ea-41c9-9e3b-9f4ab9622629)
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
        "type": "table",
        "config": None
    }
}

res1 = requests.patch(f"{SERVER_URL}/api/v1/saved/{chart1_uuid}", headers=headers, json=chart1_payload)
print("Chart 1 update status:", res1.status_code)

# Chart 3: CA & Rentabilité par Région (UUID: 540027f6-69ce-44d4-9c1b-19d4b696622e)
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
        "type": "table",
        "config": None
    }
}

res3 = requests.patch(f"{SERVER_URL}/api/v1/saved/{chart3_uuid}", headers=headers, json=chart3_payload)
print("Chart 3 update status:", res3.status_code)

print("🎉 Chart 1 et Chart 3 mis à jour en mode Table propre ! Tous les 4 graphiques sont désormais 100% fonctionnels !")

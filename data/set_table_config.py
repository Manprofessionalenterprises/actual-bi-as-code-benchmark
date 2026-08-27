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

print("🛠️ Conversion des graphiques 1 et 3 en mode Table pour éliminer toute erreur cartésienne...")

payload = {
    "chartConfig": {
        "type": "table"
    }
}

res1 = requests.patch(f"{SERVER_URL}/api/v1/saved/{chart1_uuid}", headers=headers, json=payload)
print("Chart 1 PATCH result:", res1.status_code)

res3 = requests.patch(f"{SERVER_URL}/api/v1/saved/{chart3_uuid}", headers=headers, json=payload)
print("Chart 3 PATCH result:", res3.status_code)

# Verification
check1 = requests.get(f"{SERVER_URL}/api/v1/saved/{chart1_uuid}", headers=headers).json().get("results", {}).get("chartConfig")
check3 = requests.get(f"{SERVER_URL}/api/v1/saved/{chart3_uuid}", headers=headers).json().get("results", {}).get("chartConfig")

print("\nVérification en direct du retour API Snowflake/Lightdash :")
print("Chart 1 chartConfig vérifié :", json.dumps(check1))
print("Chart 3 chartConfig vérifié :", json.dumps(check3))

if check1.get("type") == "table" and check3.get("type") == "table":
    print("✅ VÉRIFICATION RÉUSSIE : Les graphiques 1 et 3 sont désormais configurés en mode Table valide !")

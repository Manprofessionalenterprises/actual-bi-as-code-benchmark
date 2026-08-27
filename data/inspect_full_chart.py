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

# Let's inspect the entire response of GET /api/v1/saved/bb3ea95b-05ea-41c9-9e3b-9f4ab9622629
res = requests.get(f"{SERVER_URL}/api/v1/saved/{chart1_uuid}", headers=headers)
data = res.json().get("results", {})

print("FULL CHART 1 JSON:")
print(json.dumps(data, indent=2))

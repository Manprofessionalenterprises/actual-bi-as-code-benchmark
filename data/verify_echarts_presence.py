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

res1 = requests.get(f"{SERVER_URL}/api/v1/saved/{chart1_uuid}", headers=headers).json().get("results", {})
res3 = requests.get(f"{SERVER_URL}/api/v1/saved/{chart3_uuid}", headers=headers).json().get("results", {})

print("--- VERIFICATION CHART 1 ---")
print("chartConfig:")
print(json.dumps(res1.get("chartConfig"), indent=2))

print("\n--- VERIFICATION CHART 3 ---")
print("chartConfig:")
print(json.dumps(res3.get("chartConfig"), indent=2))

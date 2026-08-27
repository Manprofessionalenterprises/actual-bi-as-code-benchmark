import requests
import json

SERVER_URL = "https://app.lightdash.cloud"
API_KEY = "ldpat_74449a0f7ca1283fb57edf2b920f74c3"
PROJECT_UUID = "c9e5a221-4b16-435b-97b3-c657eed1a28d"

headers = {
    "Authorization": f"ApiKey {API_KEY}",
    "Content-Type": "application/json"
}

resp = requests.get(f"{SERVER_URL}/api/v1/projects/{PROJECT_UUID}/charts", headers=headers)
charts = resp.json().get("results", [])

for c in charts:
    chart_uuid = c["uuid"]
    chart_name = c["name"]
    print(f"\n--- Chart: {chart_name} ({chart_uuid}) ---")
    detail_resp = requests.get(f"{SERVER_URL}/api/v1/saved/{chart_uuid}", headers=headers)
    detail = detail_resp.json().get("results", {})
    print("chartConfig:", json.dumps(detail.get("chartConfig"), indent=2))

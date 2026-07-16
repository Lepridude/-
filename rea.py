import json
import requests

with open("config.json", "r", encoding="utf-8") as f:
    cfg = json.load(f)["rea"]


def get_my_data():
    headers = {
        "apikey": cfg["jwt"],
        "Authorization": f"Bearer {cfg['jwt']}"
    }

    params = {
        "select": "*",
        "competitive_group_id": f"eq.{cfg['competitive_group_id']}",
        "order": "rating.asc",
        "offset": 0,
        "limit": 2000
    }

    r = requests.get(
        "https://abitrating.rea.ru/rest/v1/entrants",
        headers=headers,
        params=params,
        timeout=30
    )

    r.raise_for_status()

    data = r.json()

    for row in data:
        if str(row.get("unique_code_profile")) == cfg["profile"]:
            return row

    return None

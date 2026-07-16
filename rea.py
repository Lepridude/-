import json
import requests

with open("config.json", "r", encoding="utf-8") as f:
    cfg = json.load(f)["rea"]

headers = {
    "apikey": cfg["jwt"],
    "Authorization": f"Bearer {cfg['jwt']}"
}


def get_all_my_data():
    # Ищем все направления, где есть твой код
    r = requests.get(
        "https://abitrating.rea.ru/rest/v1/entrants",
        headers=headers,
        params={
            "select": "*",
            "unique_code_profile": f"eq.{cfg['profile']}",
            "limit": 100
        },
        timeout=30
    )

    r.raise_for_status()
    return r.json()

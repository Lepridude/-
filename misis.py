import requests
from bs4 import BeautifulSoup

BASE_URL = (
    "https://misis.ru/applicants/admission/progress/"
    "baccalaureate-and-specialties/"
    "spiskipodavshihzayavleniya/list-p/"
)

MY_CODE = "2164745"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0 Safari/537.36"
    )
}


def get_group_info(group_id: str):
    r = requests.get(
        BASE_URL,
        params={"id": group_id},
        headers=HEADERS,
        timeout=30,
    )
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")

    table = soup.find("table")
    if table is None:
        raise RuntimeError("Таблица не найдена")

    tbody = table.find("tbody")
    if tbody is None:
        raise RuntimeError("Тело таблицы не найдено")

    rows = tbody.find_all("tr")

    direction = soup.find("direction").get_text(strip=True)
    places = int(soup.find("itog").get_text(strip=True))

    result = {
        "update_time": soup.find("date").get_text(strip=True),
        "direction": direction,
        "places": places,
        "my": None,
    }

    for row in rows:
        cols = [td.get_text(" ", strip=True) for td in row.find_all("td")]

        if not cols or MY_CODE not in cols:
            continue

        place = int(cols[0])
        priority = int(cols[3])
        achievements = int(cols[4])
        scores = int(cols[5])

        result["my"] = {
            "place": place,
            "priority": priority,
            "id": achievements,
            "scores": scores,
            "to_pass": place - places,
        }

        break

    return result

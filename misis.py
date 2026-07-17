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
        raise RuntimeError("tbody не найден")

    rows = tbody.find_all("tr")


    result = {
        "update_time": soup.find("date").get_text(strip=True),
        "direction": soup.find("direction").get_text(strip=True),
        "places": int(soup.find("itog").get_text(strip=True)),
        "my": None,
    }


    for row in rows:

        cols = [
            td.get_text(" ", strip=True)
            for td in row.find_all("td")
        ]

        if not cols or MY_CODE not in cols:
            continue


        print("MISIS COLS:", cols)


        result["my"] = {
            "place": int(cols[0]),
            "priority": cols[3],
            "scores": cols[4],
            "id": None,
            "to_pass": int(cols[0]) - result["places"],
        }


        # ищем колонку ИД
        for i, value in enumerate(cols):

            try:
                num = int(value)

                if i > 5 and num <= 10:
                    result["my"]["id"] = value
                    break

            except ValueError:
                pass


        if result["my"]["id"] is None:
            result["my"]["id"] = "0"


        break


    return result

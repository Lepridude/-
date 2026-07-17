import requests
from bs4 import BeautifulSoup


MY_CODE = "2164745"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 Chrome/138 Safari/537.36"
    )
}


def get_group_info(url):

    r = requests.get(
        url,
        headers=HEADERS,
        timeout=30
    )

    r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")

    table = soup.find("table")

    result = {
        "direction": "МТУСИ",
        "my": None
    }

    if not table:
        print("ТАБЛИЦА НЕ НАЙДЕНА")
        return result


    rows = table.find_all("tr")


    for row in rows:

        cols = [
            td.get_text(" ", strip=True)
            for td in row.find_all("td")
        ]

        if cols:
            print("MTUCI COLS:", cols)


        if MY_CODE in cols:

            print("НАШЕЛ МОЙ КОД")

            result["my"] = {
                "place": cols[0],
                "scores": cols,
                "id": None,
                "priority": None,
                "to_pass": "-"
            }

            break


    return result

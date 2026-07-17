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

    print("STATUS:", r.status_code)
    print("LENGTH:", len(r.text))

    soup = BeautifulSoup(r.text, "html.parser")


    tables = soup.find_all("table")

    print("TABLE COUNT:", len(tables))


    table = None

    for t in tables:
        txt = t.get_text(" ", strip=True)

        if MY_CODE in txt:
            table = t
            break


    if table is None:
        print("МОЯ ТАБЛИЦА НЕ НАЙДЕНА")
        return {
            "direction": "МТУСИ",
            "my": None
        }


    rows = table.find_all("tr")


    result = {
        "direction": "МТУСИ",
        "my": None
    }


    for index, row in enumerate(rows):

        cols = [
            td.get_text(" ", strip=True)
            for td in row.find_all("td")
        ]


        if not any(MY_CODE in x for x in cols):
            continue


        print("MTUCI COLS:", cols)


        result["my"] = {
            "place": cols[0],
            "scores": cols[3] if len(cols) > 3 else "-",
            "id": cols[8] if len(cols) > 8 else "-",
            "priority": cols[9] if len(cols) > 9 else "-",
        }


        break


    return result

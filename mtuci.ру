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

    if not table:
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

        if MY_CODE in cols:

            result["my"] = {
                "place": index,
                "scores": cols[3],
                "id": cols[8],
                "priority": cols[9],
                "to_pass": "-"
            }

            break


    return result

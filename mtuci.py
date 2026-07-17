import requests
from bs4 import BeautifulSoup

MY_CODE = "2164745"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0 Safari/537.36"
    )
}


def get_group_info(url):

    result = {
        "direction": "МТУСИ",
        "my": None
    }

    r = requests.get(url, headers=HEADERS, timeout=30)
    print("MTUCI STATUS:", r.status_code)
    print("MTUCI URL:", r.url)
    print("MTUCI HTML[:500]:", r.text[:500])
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")

    tables = soup.find_all("table")
    print("MTUCI TABLES:", len(tables))

    for table in tables:

        for row in table.find_all("tr"):

            cols = [td.get_text(strip=True) for td in row.find_all("td")]

            if MY_CODE not in cols:
                continue

            print("MTUCI FOUND:", cols)

            result["my"] = {
                "place": cols[0],
                "id": cols[7],
                "scores": cols[3],
                "priority": cols[9]
            }

            return result

    return result

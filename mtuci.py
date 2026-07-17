import requests
from bs4 import BeautifulSoup


MY_CODE = "2164745"


def get_group_info(url):

    r = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
        timeout=30
    )

    r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")


    result = {
        "direction": "МТУСИ",
        "my": None
    }


    for row in soup.find_all("tr"):

        cols = [
            td.get_text(" ", strip=True)
            for td in row.find_all("td")
        ]


        if not cols:
            continue


        if MY_CODE in cols:

            print("MTUCI COLS:", cols)


            result["my"] = {
                "place": cols[0] if len(cols) > 0 else "-",
                "id": cols[2] if len(cols) > 2 else "-",
                "scores": cols[3] if len(cols) > 3 else "-",
                "priority": cols[9] if len(cols) > 9 else "-"
            }


            break


    return result

import requests
from bs4 import BeautifulSoup


url = "https://abitur.mtuci.ru/ranked_lists/spisok.php?valueSearch=2164745&priznakViev=budg&levelTarget=bak_main&form=%D0%9E%D1%87%D0%BD%D0%B0%D1%8F&originalFilter=&search_type=uniqueID&originalView=all"


r = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=30
)


print("STATUS:", r.status_code)
print("РАЗМЕР HTML:", len(r.text))

print("КОД В HTML:", "2164745" in r.text)


soup = BeautifulSoup(r.text, "html.parser")


print("ТАБЛИЦ:", len(soup.find_all("table")))
print("СТРОК TR:", len(soup.find_all("tr")))


# первые найденные строки
for i, row in enumerate(soup.find_all("tr")[:10]):
    print(
        i,
        row.get_text(" ", strip=True)
    )

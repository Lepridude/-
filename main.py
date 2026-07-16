import requests

url = "https://abitrating.rea.ru/group/6c2f167c-11ad-11f1-8dba-5cba2c649f58?profile=2162745"

response = requests.get(url, timeout=30)

print("Status:", response.status_code)
print("Length:", len(response.text))

with open("page.html", "w", encoding="utf-8") as f:
    f.write(response.text)

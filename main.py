import re

from misis import get_group_info as get_misis_group
from rea import get_all_my_data, get_group_info
from telegram import send


def clean_name(name):
    name = name.replace("Только", "")
    name = name.replace("только РФ", "")
    name = name.replace("РФ", "")
    name = name.replace("Очная", "")
    name = name.replace("очная", "")
    name = name.replace("ВШКМиС", "")
    name = name.replace("РЭУ им. Г.В. Плеханова", "")
    name = name.replace("РЭУ", "")
    name = name.replace("Москва", "")

    name = re.sub(r"(,\s*)+", ", ", name)
    name = " ".join(name.split()).strip(" ,-()")

    return name


text = ""


# =========================
# РЭУ Плеханова
# =========================

text += "🏛 РЭУ Плеханова\n\n"

rows = get_all_my_data()

for row in rows:
    group = get_group_info(row["competitive_group_id"])

    print("GROUP FROM REA:", group)

    if group:

        group_name = group.get(
            "competitive_group_name",
            group.get("speciality_name", "Неизвестное направление")
        )

        group_name = clean_name(group_name)

        places = group.get("admission_volume", 0)

    else:
        group_name = "Неизвестное направление"
        places = 0


    to_pass = (
        row["rating"] - places
        if places
        else "-"
    )


    text += (
        f"📚 {group_name}\n"
        f"📍 Место: {row['rating']}\n"
        f"🎯 Приоритет: {row['priority']}\n"
        f"🏅 ИД: {row['achievements_mark']}\n"
        f"📈 Сумма: {row['sum_mark']}\n"
        f"🎓 Мест: {places}\n"
        f"📉 До прохода: {to_pass}\n"
        "━━━━━━━━━━━━━━\n\n"
    )


# =========================
# МИСИС
# =========================

text += "🏛 МИСИС\n\n"


groups = [
    {
        "id": "BVO-BUDJ-O-090000-NITU_MISIS-OKM-000006867",
        "type": "Бюджет"
    },
    {
        "id": "BVO-BUDJ-O-270303-NITU_MISIS-OKM-000007070",
        "type": "Бюджет"
    },
    {
        "id": "BVO-BUDJ-O-380305-NITU_MISIS-OKM-000007050",
        "type": "Бюджет"
    },
    {
        "id": "BVO-BUDJ-O-010304-NITU_MISIS-OKM-000006850",
        "type": "Бюджет"
    },
]


for group in groups:

    misis = get_misis_group(group["id"])

    if not misis["my"]:
        continue

    me = misis["my"]


    text += (
        f"📚 {misis['direction']} — {group['type']}\n"
        f"📍 Место: {me['place']}\n"
        f"🎯 Приоритет: {me['priority']}\n"
        f"🏅 ИД: {me['id']}\n"
        f"📈 Баллы: {me['scores']}\n"
        f"🎓 Мест: {misis['places']}\n"
        f"📉 До прохода: {me['to_pass']}\n"
        "━━━━━━━━━━━━━━\n\n"
    )


send(text)

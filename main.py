import re

from misis import get_group_info as get_misis_group
from rea import get_all_my_data, get_group_info
from telegram import send


rows = get_all_my_data()

text = "🏛 РЭУ Плеханова\n\n"


# =========================
# РЭУ
# =========================

for row in rows:
    group = get_group_info(row["competitive_group_id"])

    if group:
        group_name = group.get("competitive_group_name", "")

        group_name = group_name.replace("Только", "")
        group_name = group_name.replace("только РФ", "")
        group_name = group_name.replace("РФ", "")
        group_name = group_name.replace("Очная", "")
        group_name = group_name.replace("очная", "")
        group_name = group_name.replace("ВШКМиС", "")
        group_name = group_name.replace("РЭУ им. Г.В. Плеханова", "")
        group_name = group_name.replace("РЭУ", "")
        group_name = group_name.replace("Москва", "")

        group_name = re.sub(r"(,\s*)+", ", ", group_name)
        group_name = " ".join(group_name.split()).strip(" ,-()")

    else:
        group_name = "Неизвестное направление"


    text += (
        f"📚 {group_name}\n"
        f"📍 Место: {row['rating']}\n"
        f"🎯 Приоритет: {row['priority']}\n"
        f"🏅 ИД: {row['achievements_mark']}\n"
        f"📈 Сумма: {row['sum_mark']}\n"
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

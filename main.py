import re

from rea import get_all_my_data, get_group_info
from telegram import send

rows = get_all_my_data()

text = "🏛 РЭУ Плеханова\n\n"

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

send(text)

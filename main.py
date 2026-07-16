import re

from rea import get_all_my_data, get_group_info
from telegram import send

rows = get_all_my_data()

for row in rows:
    group = get_group_info(row["competitive_group_id"])

    if group:
        group_name = group.get("competitive_group_name", "")

        group_name = group_name.replace("только РФ", "")
        group_name = group_name.replace("РФ", "")
        group_name = group_name.replace("Очная", "")
        group_name = group_name.replace("очная", "")
        group_name = group_name.replace("ВШКМиС", "")
        group_name = group_name.replace("РЭУ им. Г.В. Плеханова", "")
        group_name = group_name.replace("РЭУ", "")
        group_name = group_name.replace("Москва", "")

        # Убираем подряд идущие запятые
        group_name = re.sub(r"(,\s*)+", ", ", group_name)

        # Убираем пробелы и запятые по краям
        group_name = " ".join(group_name.split()).strip(" ,-()")
    else:
        group_name = "Неизвестное направление"

    text = (
        "🏛 РЭУ Плеханова\n\n"
        f"📚 {group_name}\n"
        f"📍 Место: {row['rating']}\n"
        f"🎯 Приоритет: {row['priority']}\n"
        f"🏅 ИД: {row['achievements_mark']}\n"
        f"📈 Сумма: {row['sum_mark']}\n"
    )

    send(text)

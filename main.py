from rea import get_all_my_data, get_group_info
from telegram import send

rows = get_all_my_data()

if not rows:
    send("❌ Не найдено ни одного направления.")
    raise SystemExit

text = "🏛 РЭУ Плеханова\n\n"

for row in rows:
    group = get_group_info(row["competitive_group_id"])

    if group:
        text += (
            f"📚 {group['speciality_name']}\n"
            f"🏫 {group['faculty_name']}\n"
            f"📍 Место: {row['rating']}\n"
            f"🎯 Приоритет: {row['priority']}\n"
            f"📊 Баллы: {row['sum_mark']}\n"
            f"📄 Статус: {row['application_status'] or '—'}\n\n"
        )

send(text)

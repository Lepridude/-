from rea import get_all_my_data
from telegram import send

rows = get_all_my_data()

if not rows:
    send("❌ Не найдено ни одного направления.")
    raise SystemExit

text = "🏛 РЭУ Плеханова\n\n"

for row in rows:
    group = row["group"]

    text += (
        f"📚 {group['speciality_name']}\n"
        f"🏫 {group['faculty_name']}\n"
        f"📍 Место: {row['rating']}\n"
        f"🎯 Приоритет: {row['priority']}\n"
        f"📊 Баллы: {row['sum_mark']}\n"
        f"📄 Статус: {row['application_status'] or '—'}\n"
        f"━━━━━━━━━━━━━━\n"
    )

send(text)

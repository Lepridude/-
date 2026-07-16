from rea import get_all_my_data, get_group_info
from telegram import send

rows = get_all_my_data()

text = "🏛 РЭУ Плеханова\n\n"

for row in rows:
    group = get_group_info(row["competitive_group_id"])

    text += (
        f"DEBUG:\n{group}\n\n"
        f"👤 Код: {row['unique_code_profile']}\n"
        f"📍 Место: {row['rating']}\n"
        f"🎯 Приоритет: {row['priority']}\n"
        f"📊 Баллы ЕГЭ: {row['entrance_test_mark']}\n"
        f"🏅 ИД: {row['achievements_mark']}\n"
        f"📈 Сумма: {row['sum_mark']}\n"
        f"📄 Статус: {row['application_status'] or '—'}\n"
        f"📝 Согласие: {'Да' if row['agreement'] else 'Нет'}\n"
        "━━━━━━━━━━━━━━\n\n"
    )

send(text)

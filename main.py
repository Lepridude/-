from rea import get_my_data
from telegram import send

row = get_my_data()

if row is None:
    send("❌ Не удалось найти твой код в рейтинге.")
    raise SystemExit

text = f"""🏛 РЭУ

👤 Код: {row['unique_code_profile']}

📍 Место: {row['rating']}

🎯 Приоритет: {row['priority']}

📊 Баллы: {row['entrance_test_mark']}

📄 Статус: {row['application_status']}
"""

send(text)

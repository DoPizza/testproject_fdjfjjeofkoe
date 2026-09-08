
import requests
import datetime

# Наш Stormkit backend
BACKEND_URL = "https://fangdenim-lwsvow.stormkit.dev/api/add-event"

# Текущее время
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Тестовое мероприятие
event_data = {
    "title": f"Тестовый парсер Ульяновска ({current_time})",
    "status": "pending",
    "description": "Мероприятие добавлено тестовым Python-парсером"
}

try:
    response = requests.post(
        BACKEND_URL,
        json=event_data,
        timeout=15
    )

    print("Статус код ответа:", response.status_code)

    try:
        print("Ответ от сервера:", response.json())
    except Exception:
        print("Ответ от сервера:", response.text)

    if response.ok:
        print("✅ Мероприятие успешно добавлено!")
    else:
        print("❌ Сервер вернул ошибку.")

except requests.exceptions.RequestException as e:
    print("❌ Ошибка соединения с сервером:", e)

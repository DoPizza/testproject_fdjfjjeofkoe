import requests
import datetime

# Сюда вставьте вашу реальную ссылку на бэкенд Cloudflare (которую вы получили при деплое)
# Не забудьте в конце добавить /api/add-event
BACKEND_URL = "https://ulsk-backend.ps3040678.workers.dev/api/add-event"

# Генерируем тестовое мероприятие с текущим временем
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
event_data = {
    "title": f"Соси за хуй в Ульяновске ({current_time})"
}

try:
    # Отправляем POST-запрос на ваш бэкенд
    response = requests.post(BACKEND_URL, json=event_data)
    
    print("Статус код ответа:", response.status_code)
    print("Ответ от сервера:", response.json())
except Exception as e:
    print("Произошла ошибка при отправке:", e)

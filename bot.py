import time
import requests
from config import ADMIN_ID, BASE_URL
from handlers import handle_user_message, handle_admin_reply


def get_updates(offset=None):
    """Получение обновлений от Telegram API"""
    url = f"{BASE_URL}/getUpdates"
    params = {'timeout': 100, 'offset': offset}
    try:
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка подключения: {e}")
        return {}


def main():
    last_update_id = None

    while True:
        updates = get_updates(last_update_id)

        if "result" in updates:
            for update in updates["result"]:
                last_update_id = update["update_id"] + 1

                if "message" in update:
                    message = update["message"]
                    chat_id = message["chat"]["id"]
                    text = message.get("text", "")

                    if str(chat_id) == ADMIN_ID and text.startswith("/reply"):
                        handle_admin_reply(text)
                    else:
                        handle_user_message(chat_id, text)

        time.sleep(1)


if __name__ == "__main__":
    main()

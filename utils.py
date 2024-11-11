import logging
from datetime import datetime
import requests
from config import BASE_URL

logging.basicConfig(filename="bot.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

last_message_time = {}


def send_message(chat_id, text):
    """Отправка сообщения через Telegram API"""
    url = f"{BASE_URL}/sendMessage"
    payload = {'chat_id': chat_id, 'text': text}
    requests.post(url, data=payload)
    logging.info(f"Sent message to {chat_id}: {text}")


def is_message_allowed(user_id, cooldown):
    """Проверка частоты сообщений"""
    now = datetime.now()
    if user_id in last_message_time:
        elapsed_time = (now - last_message_time[user_id]).total_seconds()
        if elapsed_time < cooldown:
            return False
    last_message_time[user_id] = now
    return True

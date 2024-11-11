from config import ADMIN_ID, MESSAGE_COOLDOWN
from utils import send_message, is_message_allowed
from filters import contains_blocked_words

user_message_map = {}


def handle_user_message(chat_id, text):
    """Обработка сообщения от пользователя"""
    if not is_message_allowed(chat_id, MESSAGE_COOLDOWN):
        send_message(chat_id, "Пожалуйста, не отправляйте сообщения слишком часто.")
        return

    if contains_blocked_words(text):
        send_message(chat_id, "Ваше сообщение содержит запрещенные слова.")
        return

    forward_text = f"Сообщение от {chat_id}: {text}"
    send_message(ADMIN_ID, forward_text)
    send_message(chat_id, "Ваше сообщение отправлено администратору.")


def handle_admin_reply(text):
    """Обработка ответа от администратора"""
    try:
        _, user_id, reply_text = text.split(maxsplit=2)
        send_message(user_id, reply_text)
    except ValueError:
        send_message(ADMIN_ID, "Используйте формат: /reply <user_id> <message>")

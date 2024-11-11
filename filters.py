from config import BLOCKED_WORDS


def contains_blocked_words(text):
    """Проверка сообщения на наличие запрещенных слов"""
    for word in BLOCKED_WORDS:
        if word.lower() in text.lower():
            return True
    return False

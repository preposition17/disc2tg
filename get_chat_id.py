from telebot import TeleBot

from config import (
    TELEGRAM_TOKEN
)


tg_bot = TeleBot(TELEGRAM_TOKEN)


@tg_bot.message_handler()
def print_chat_id(message):
    print(message.text)
    print(message.chat.id)
    print()


if __name__ == '__main__':
    tg_bot.infinity_polling()
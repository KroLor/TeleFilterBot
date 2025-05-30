from logger import *
from filter import searching
import app as mapp
import telebot
from waitress import serve

def paused():
    input("Запуск приостановлен. Нажмите Enter, если исправили это.")

def startBot(API_TOKEN, public_ip):
    bot = telebot.TeleBot(API_TOKEN)

    mapp.setWebhook(public_ip)

    @bot.message_handler(func=lambda message: True)
    def handler_message(message):
        print("BOT")
        if message.content_type == "text":
            message_text = message.text
            prohibited = searching(message_text)
            if prohibited == True:
                log_and_print("info", f"Обнаружен запрещенный контент в чате {message.chat.title} от @{message.from_user.username}.")
                try:
                    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
                    log_and_print("info", f"Сообщение @{message.from_user.username} удалено.")
                except Exception as e:
                    log_and_print("error", f"Не удалось удалить сообщение @{message.from_user.username} в чате {message.chat.title}: {e}.")
                    log_and_print("debug", f"Не удалось удалить сообщение @{message.from_user.username} из чата {message.chat.title} ({message.chat}):\n{message_text}")

    log_and_print("info", "Бот запущен.")
    mapp.startServer(bot)

    # Запуск Flask приложения с waitress
    serve(mapp.app, host='0.0.0.0', port=8443)
from logger import *
from filter import searching
import telebot

def paused():
    input("Запуск приостановлен. Нажмите Enter, если исправили это.")

# def checkStatusBot():
#     log_and_print("info", "Инициализация...")

#     updates = bot.get_updates()

#     while (True):
#         if not updates:
#             log_and_print("error", "Бот находится не в группе, убедитесь, что он добавлен в неё.")
#             return 1
#         elif updates[-1].message:
#             last_update = updates[-1]
#             break
#         else:
#             log_and_print("error", "Сообщений не обнаружено, бот не знает в какой он группе.")
#             paused()
#             updates = bot.get_updates()
#             continue
    
#     chat = bot.get_chat(last_update.message.chat.id)

#     member = bot.get_chat_member(chat.id, bot.get_me().id)
#     if member.status != "administrator" or member.can_delete_messages == False:
#         log_and_print("warning", "Бот не является администратором или ему запрещено удалять сообщения, " + 
#                       "возможности бота ограничены.")
#         log_and_print("debug", f"Статус: status: {member.status}, can_delete_messages: {member.can_delete_messages}")
#         return -1
#     else:
#         log_and_print("info", "Успешно.")
#         chat_name = chat.title if chat.title else chat.username
#         log_and_print("debug", f"Бот в группе: {chat_name}, id: {chat.id}")
#         return 0

def startBot(API_TOKEN):
    global bot

    bot = telebot.TeleBot(API_TOKEN)
    bot.delete_webhook()

    # status = checkStatusBot()
    # while (status != 0):
    #     paused()
    #     status = checkStatusBot()
    
    @bot.message_handler(func=lambda message: True)
    def handler_message(message):
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
    bot.polling(none_stop=True, interval=0, timeout=20)
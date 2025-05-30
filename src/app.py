import os
from flask import Flask, request, abort
import telebot
import subprocess

from constants import *

app = Flask(__name__)
bot = telebot.TeleBot(API_TOKEN)

def startServer(bot):
    # Здесь можно добавить код для запуска сервера, если это необходимо
    pass

def setWebhook(public_ip):
    bot.delete_webhook()
    bot.set_webhook(url=f'https://{public_ip}:8443/webhook')

    print(bot.get_webhook_info())

@app.route('/webhook', methods=['POST'])
def webhook():
    print("HOOK")
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        abort(403)
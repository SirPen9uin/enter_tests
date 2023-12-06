import os
import telebot
import json
import modules

from pprint import pprint
from dotenv import load_dotenv

load_dotenv()
bot = telebot.TeleBot(os.getenv('VSRATO_TOKEN'))


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Шалом, это копия бота Всратослава, я умею наносить раномные смешные надписи на картинки, например так'
    bot.send_message(message.chat.id, mess)
    modules.add_text_to_pic('img.png', 'img_new.jpg')
    photo = open('img_new.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)


bot.polling(none_stop=True)
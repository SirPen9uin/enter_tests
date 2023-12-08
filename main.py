import os
import random
import telebot
import json
import modules
import datetime as dt

from PIL import Image, ImageDraw, ImageFont
from random import choice
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()
bot = telebot.TeleBot(os.getenv('VSRATO_TOKEN'))
original_photos_path = 'original'
remake_photos_path = 'remake'

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    username = message.from_user.username

    modules.create_user_directory(user_id, username)

    users_photo = bot.get_user_profile_photos(user_id)
    if users_photo.photos:
        for i, photo in enumerate(users_photo.photos):
            file_info = bot.get_file(photo[-1].file_id)
            file_path = file_info.file_path
            download_photo = bot.download_file(file_path)

            photo_filename = f'{user_id}_{username}/photo_{i}.jpg'
            with open(photo_filename, 'wb') as photo_file:
                photo_file.write(download_photo)

            modules.add_photo_description(user_id, username, i, photo_filename)

    photos_list = f'{user_id}_{username}/{user_id}_{username}.txt'
    with open(photos_list, 'r') as f:
        lines = f.readlines()
        random.shuffle(lines)
        random_photo_path = random.choice(lines).strip()

    with open('cool_phrases.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        random.shuffle(lines)
        random_phrase = random.choice(lines).strip()

    path = random_photo_path
    image = Image.open(path)
    draw = ImageDraw.Draw(image)
    font_path = 'arial.ttf'
    font_size = 42
    font_color = (255, 0, 0)
    font = ImageFont.truetype(font_path, font_size)
    draw.text([250, 500], text=random_phrase, font=font, fill=font_color)
    new_photo = f'new_profile_pic_{message.from_user.username}.jpg'
    image.save(new_photo)

    mess = f'Шалом {username}, это копия бота Всратослава, я умею наносить рандомные смешные надписи на картинки, например так'
    bot.send_message(message.chat.id, mess)
    bot.send_photo(message.chat.id, open(new_photo, 'rb'))

@bot.message_handler(content_types=['text'])
def echo(message):
    mess = f'Отправиь картинку, не хочу говорить'
    bot.send_message(message.chat.id, mess)


@bot.message_handler(content_types=['photo'])
def remake_pic(message):
    name = f'{dt.datetime.now().strftime("%Y-%m-%d_%H-%M")}_{message.from_user.id}.jpg'
    photo = message.photo[-1].file_id
    info = bot.get_file(photo)
    photo_path = info.file_path
    dowload_file = bot.download_file(photo_path)
    try:
        os.mkdir(original_photos_path)
    except FileExistsError:
        pass
    save_photo = f'{original_photos_path}/{name}.jpg'
    with open(save_photo, 'wb') as new:
        new.write(dowload_file)

    with open('cool_phrases.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        random.shuffle(lines)
        random_phrase = random.choice(lines).strip()

    try:
        os.mkdir(remake_photos_path)
    except FileExistsError:
        pass

    path = f'{save_photo}'
    image = Image.open(path)
    draw = ImageDraw.Draw(image)
    font_path = 'arial.ttf'
    font_size = 42
    font_color = (255, 0, 0)
    font = ImageFont.truetype(font_path, font_size)
    draw.text([300, 500], text=random_phrase, font=font, fill=font_color)
    new_photo = f'new_profile_pic_{message.from_user.username}.jpg'
    image.save(f'{remake_photos_path}/{new_photo}')
    new_photo_path = f'{remake_photos_path}/{new_photo}'
    bot.send_photo(message.chat.id, open(new_photo_path, 'rb'))


bot.polling(none_stop=True)
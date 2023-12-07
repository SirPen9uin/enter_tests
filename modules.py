from PIL import Image, ImageDraw, ImageFont
import datetime as dt
import os


def add_dir(dir):
    try:
        os.mkdir(dir)
    except FileExistsError:
        pass

    return dir


def get_pic(pic, dir):
    path = add_dir(dir)
    name = dt.datetime.now().strftime('%Y-%m-%d_%H-%M') + '.jpg'
    save_path = os.path.join(path, name)
    original_pic = Image.open(pic)
    original_pic.save(save_path)
    return name


def add_text_to_pic(image_path, save_path):
    path = image_path
    image = Image.open(path)
    draw = ImageDraw.Draw(image)
    font_path = 'arial.ttf'
    font_size = 42
    font_color = (255, 0, 0)
    font = ImageFont.truetype(font_path, font_size)
    draw.text([300, 500], text='Пидрила катит', font=font, fill=font_color)
    image.save(save_path)


def create_user_directory(user_id, username):
    try:
        os.mkdir(f'{user_id}_{username}')
    except FileExistsError:
        pass


def add_photo_description(user_id, username, photo_index, photo_path):
    with open(f'{user_id}_{username}/{user_id}_{username}.txt', 'a') as f:
        f.write(f'{photo_path}\n')

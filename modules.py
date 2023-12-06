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


def add_text_to_pic(image_path, save_path):
    path = image_path
    image = Image.open(path)
    draw = ImageDraw.Draw(image)
    font_path = 'arial.ttf'  # Укажите полный путь, если шрифт не находится в текущей директории
    font_size = 42
    font_color = (255, 0, 0)
    font = ImageFont.truetype(font_path, font_size)
    draw.text([300, 500], text='Пидрила катит', font=font, fill=font_color)
    image.save(save_path)

# add_dir('original_pics')
# get_pic('img.png', 'original_pics')
add_text_to_pic('img.png', 'ing_new.jpg')
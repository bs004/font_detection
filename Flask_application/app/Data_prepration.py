# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import os
import pytesseract
import random

from data_utils import *

Font_list = ['Oswald', 'Roboto', 'Open_Sans', 'Ubuntu', 'PT_Serif', 'Dancing_Script', 'Fredoka_One', 'Arimo',
             'Noto_Sans', 'Patua_One']

# For different font sizes
Font_sizes = [i for i in range(28, 40, 4)]
# For Different starting positions of text
Start_points = list(zip([i for i in range(10, 25, 5)], [i for i in range(10, 25, 5)]))
base_path = 'font_data/images'
base_font_path = os.sep.join([base_path, 'Font_files'])
for i in range(len(Font_list)):
    for j in range(40):
        img = Image.new('RGB', (400, 150), color=(255, 255, 255))
        size = random.choice(Font_sizes)

        start_position = random.choice(Start_points)
        Font_path = os.sep.join([base_font_path, Font_list[i]]) + '.ttf'

        new_font = ImageFont.truetype(Font_path, size=size)
        d = ImageDraw.Draw(img)
        d.text(start_position, "Hello, World!", font=new_font, fill=(0, 0, 0))

        image_name = f"{Font_list[i]}_{j}.jpg"
        img.save(os.sep.join([base_path, 'Output_images', image_name]))
        try:
            coords = get_yolo_points(img)

            text_file_name = f"{Font_list[i]}_{j}.txt"
            text = f"{i}  {round(coords[0], 4)} {round(coords[1], 4)} {round(coords[2], 4)} {round(coords[3], 4)}"
            with open(os.sep.join([base_path, 'Output_images', text_file_name]), 'w') as f:
                f.write(text)
        except:
            print(image_name)

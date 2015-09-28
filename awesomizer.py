#!/usr/bin/env python
# coding: utf-8

import sys
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def calc_font_size(image_size):
    margin = int(image_size[0] * 0.03)
    font_size = min(image_size) - margin * 2
    return font_size


def calc_paste_pos(image_size, paste_image_size):
    image_center = (image_size[0] / 2, image_size[1] / 2)
    image_pos = (int(image_center[0] - paste_image_size[0] / 2), int(image_center[1] - paste_image_size[1] / 2))

    return image_pos


def get_image_file_name():
    if len(sys.argv) < 2:
        sys.exit("please set image file")
    return sys.argv[1]

image_file_name = get_image_file_name()
file_name = os.path.basename(image_file_name)
save_file_name = "./awesomized_%s" % (file_name)

image = Image.open(image_file_name)

text = u"最高"
font_color = (255, 255, 255)
font_file = "./fonts/YasashisaAntique.otf"
font_size = calc_font_size(image.size)
font_pos = (font_size * len(text), font_size)
font = ImageFont.truetype(font_file, font_size, encoding='utf-8')

awesome = Image.new('RGBA', font_pos, (255, 255, 255, 0))
alpha_filter = Image.new('RGBA', image.size, (255, 255, 255, 100))

shadow_color = (170, 191, 217)
shadow_pos = (int(font_size * 0.008), int(font_size * 0.008))
paste_pos = calc_paste_pos(image.size, awesome.size)

draw = ImageDraw.Draw(awesome)
draw.text(shadow_pos, text, fill=shadow_color, font=font)
draw.text((0, 0), text, fill=font_color, font=font)


image.paste(alpha_filter, (0, 0), alpha_filter)
image.paste(awesome, paste_pos, awesome)

image.save(save_file_name)

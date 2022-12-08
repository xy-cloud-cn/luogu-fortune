# -*- coding: utf-8 -*-
'''
@Author   : xy_cloud
@IDE      : PyCharm
@Project  : Python Project
@File     : main.py
@Time     : 2022/12/7 13:42
'''
import random
import textwrap
from PIL import Image, ImageDraw, ImageFont
import json

with open('todo.json','r',encoding='utf-8') as r:
    j=json.load(r)
todolist,nottodolist=j['able'],j['not']

bg_size = (400, 350)
# 生成背景
# Generating backgrounds
img = Image.new('RGB', bg_size, (255, 255, 255))
draw = ImageDraw.Draw(img)
# 导入字体
# Importing Fonts
Title_Font=ImageFont.truetype(font=Bold_Font, size=20)
Fortune_Font = ImageFont.truetype(font=Bold_Font, size=60)
Suitable_To_Do_Font_Bold = ImageFont.truetype(font=Bold_Font, size=16)
Suitable_To_Do_Font = ImageFont.truetype(font=Normal_Font, size=16)
Detail_Font = ImageFont.truetype(font=Normal_Font, size=12)
# 初始化内容
# Initial content
card='xy_cloud'
title=card+'的运势'
fortune = '§ ' + random.choice(Fortune_List) + ' §'
fortune_width = Fortune_Font.getbbox(fortune)[2]
suitable_to_do,detail = random.choice([['诸事不宜','在家躺一天']] if fortune[2:-2] == '大凶' else todolist)
suitable_to_do,detail = textwrap.fill(suitable_to_do, width=8),textwrap.fill(detail, width=12)

unsuitable_to_do, detail2 = random.choice([['诸事皆宜', '去做想做的事情吧']] if fortune[2:-2] == '大吉' else nottodolist)
unsuitable_to_do, detail2 = textwrap.fill(unsuitable_to_do, width=8), textwrap.fill(detail2, width=12)
while unsuitable_to_do==suitable_to_do:
    unsuitable_to_do,detail2 = random.choice([['诸事皆宜','去做想做的事情吧']] if fortune[2:-2] == '大吉' else nottodolist)
    unsuitable_to_do,detail2 = textwrap.fill(unsuitable_to_do, width=8),textwrap.fill(detail2, width=12)

title='xy_cloud'+'的运势'
fortune=random.choice(['大凶', '凶', '小凶', '小吉', '中吉', '大吉', '吉你太美']) #分离运势 避免后面大量使用切片
rp = '§ ' + fortune + ' §'
renpin_width = renpin.getbbox(rp)[2]
things_to_do,det = random.choice([['诸事不宜','在家躺一天']] if fortune == '大凶' else todolist)
things_to_do,det = textwrap.fill(things_to_do, width=8),textwrap.fill(det, width=12)

things_not_to_do, det2 = random.choice([['诸事皆宜', '去做想做的事情吧']] if fortune == '大吉' else nottodolist)
things_not_to_do, det2 = textwrap.fill(things_not_to_do, width=8), textwrap.fill(det2, width=12)
while things_not_to_do==things_to_do:
    things_not_to_do,det2 = random.choice([['诸事皆宜','去做想做的事情吧']] if fortune == '大吉' else nottodolist)
    things_not_to_do,det2 = textwrap.fill(things_not_to_do, width=8),textwrap.fill(det2, width=12)

things_to_do2,det3 = random.choice([['','']] if fortune == '大凶' else todolist)
things_to_do2,det3 = textwrap.fill(things_to_do2, width=8),textwrap.fill(det3, width=12)
while things_to_do2==things_to_do or things_to_do2==things_not_to_do:
    things_to_do2, det3 = random.choice([['', '']] if fortune == '大凶' else todolist)
    things_to_do2, det3 = textwrap.fill(things_to_do2, width=8), textwrap.fill(det3, width=12)

things_not_to_do2,det4 = random.choice([['','']] if fortune == '大吉' else nottodolist)
things_not_to_do2,det4 = textwrap.fill(things_not_to_do2, width=8),textwrap.fill(det4, width=12)
while things_not_to_do2==things_to_do or things_not_to_do2==things_not_to_do or things_not_to_do2==things_to_do2:
    things_not_to_do2, det4 = random.choice([['', '']] if fortune == '大吉' else nottodolist)
    things_not_to_do2, det4 = textwrap.fill(things_not_to_do2, width=8), textwrap.fill(det4, width=12)
ttd_width = thing.getbbox(('' if fortune == '大凶' else ' ' * 6) + things_to_do)[2] if len(things_to_do) <= 8 else 152
tntd_width = thing.getbbox(('' if fortune == '大吉' else ' ' * 6) + things_not_to_do)[2] if len(things_not_to_do) <= 8 else 152
ttd_width2 = thing.getbbox(' ' * 6 + things_to_do2)[2] if len(things_to_do2) <= 8 else 152
tntd_width2 = thing.getbbox(' ' * 6 + things_not_to_do2)[2] if len(things_not_to_do2) <= 8 else 152
det_width = detail.getbbox(det)[2] if len(det) <= 12 else 144
det2_width = detail.getbbox(det2)[2] if len(det2) <= 12 else 144
det3_width = detail.getbbox(det3)[2] if len(det3) <= 12 else 144
det4_width = detail.getbbox(det4)[2] if len(det4) <= 12 else 144
name_width = name.getbbox(title)[2]

draw.text(xy=(bg_size[0] / 2 - name_width / 2, 10), text=title, fill='#000000', font=name)
draw.text(xy=(bg_size[0] / 2 - renpin_width / 2, 50), text=rp, fill='#e74c3c' if fortune in ['小吉', '中吉', '大吉', '吉你太美'] else '#3f3f3f', font=renpin)
begin_pos_y=150
draw.text(xy=(bg_size[0] / 4 - ttd_width / 2, begin_pos_y), text='诸事不宜' if fortune == '大凶' else '宜:', fill='#e74c3c', font=yi)
draw.text(xy=(bg_size[0] / 4 - ttd_width / 2, begin_pos_y), text='' if fortune == '大凶' else ' ' * 6 + things_to_do, fill='#e74c3c', font=thing)
draw.text(xy=(bg_size[0] / 4 * 3 - tntd_width / 2, begin_pos_y), text='诸事皆宜' if fortune == '大吉' else '忌:', fill='#000000', font=yi)
draw.text(xy=(bg_size[0] / 4 * 3 - tntd_width / 2, begin_pos_y), text='' if fortune == '大吉' else ' ' * 6 + things_not_to_do, fill='#000000', font=thing)
len_ttd=len(things_to_do.split('\n'))

print(len_ttd)
begin_pos_y+=25+25*(len_ttd-1)
draw.text(xy=(bg_size[0] / 4 - detail_width / 2, begin_pos_y), text=detail, fill='#7f7f7f', font=Detail_Font)
draw.text(xy=(bg_size[0] / 4 * 3 - detail2_width / 2, begin_pos_y), text=detail2, fill='#7f7f7f', font=Detail_Font)
begin_pos_y=250
draw.text(xy=(bg_size[0] / 4 - ttd_width2 / 2, begin_pos_y), text='' if fortune == '大凶' else '宜:', fill='#e74c3c', font=yi)
draw.text(xy=(bg_size[0] / 4 - ttd_width2 / 2, begin_pos_y), text=' ' * 6 + things_to_do2, fill='#e74c3c', font=thing)
draw.text(xy=(bg_size[0] / 4 * 3 - tntd_width2 / 2, begin_pos_y), text='' if fortune == '大吉' else '忌:', fill='#000000', font=yi)
draw.text(xy=(bg_size[0] / 4 * 3 - tntd_width2 / 2, begin_pos_y), text=' ' * 6 + things_not_to_do2, fill='#000000', font=thing)
len_ttd2=len(things_to_do2.split('\n'))

print(len_ttd2)
begin_pos_y+=25+25*(len_ttd2-1)
draw.text(xy=(bg_size[0] / 4 - detail3_width / 2, begin_pos_y), text=detail3, fill='#7f7f7f', font=Detail_Font)
draw.text(xy=(bg_size[0] / 4 * 3 - detail4_width / 2, begin_pos_y), text=detail4, fill='#7f7f7f', font=Detail_Font)

img.show()

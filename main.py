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
todolist=[
    ['刷B站','承包一天笑点'],
    ['在QQ群聊天','遇见好朋友'],
    ['被撅','哼哼哼啊啊啊啊啊'],
    ['写作业','蒙的全对'],
    ['唱跳RAP篮球','只因你太美'],
    ['打游戏','杀疯了'],
    ['摸鱼','摸鱼不被发现']
]
nottodolist=[
    ['刷B站','视频加载不出来'],
    ['在QQ群聊天','被小鬼气死'],
    ['被撅','休息一天~'],
    ['写作业','全错了'],
    ['唱跳RAP篮球','被ikun人参公鸡'],
    ['打游戏','送人头'],
    ['摸鱼','摸鱼被发现']
]
Fortune_List=['大凶', '凶', '小凶', '小吉', '中吉', '大吉', '吉你太美']
Bold_Font='./ttf/SourceHanSansCN-Bold.otf'
Normal_Font='./ttf/SourceHanSansCN-Normal.otf'
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

unsuitable_to_do, det2 = random.choice([['诸事皆宜', '去做想做的事情吧']] if fortune[2:-2] == '大吉' else nottodolist)
unsuitable_to_do, det2 = textwrap.fill(unsuitable_to_do, width=8), textwrap.fill(det2, width=12)
while unsuitable_to_do==suitable_to_do:
    unsuitable_to_do,det2 = random.choice([['诸事皆宜','去做想做的事情吧']] if fortune[2:-2] == '大吉' else nottodolist)
    unsuitable_to_do,det2 = textwrap.fill(unsuitable_to_do, width=8),textwrap.fill(det2, width=12)

suitable_to_do2,det3 = random.choice([['','']] if fortune[2:-2] == '大凶' else todolist)
suitable_to_do2,det3 = textwrap.fill(suitable_to_do2, width=8),textwrap.fill(det3, width=12)
while suitable_to_do2==suitable_to_do or suitable_to_do2==unsuitable_to_do:
    suitable_to_do2, det3 = random.choice([['', '']] if fortune[2:-2] == '大凶' else todolist)
    suitable_to_do2, det3 = textwrap.fill(suitable_to_do2, width=8), textwrap.fill(det3, width=12)

unsuitable_to_do2,det4 = random.choice([['','']] if fortune[2:-2] == '大吉' else nottodolist)
unsuitable_to_do2,det4 = textwrap.fill(unsuitable_to_do2, width=8),textwrap.fill(det4, width=12)
while unsuitable_to_do2==suitable_to_do or unsuitable_to_do2==unsuitable_to_do or unsuitable_to_do2==suitable_to_do2:
    unsuitable_to_do2, det4 = random.choice([['', '']] if fortune[2:-2] == '大吉' else nottodolist)
    unsuitable_to_do2, det4 = textwrap.fill(unsuitable_to_do2, width=8), textwrap.fill(det4, width=12)
ttd_width = Suitable_To_Do_Font.getbbox(('' if fortune[2:-2] == '大凶' else ' ' * 6) + suitable_to_do)[2] if len(suitable_to_do) <= 8 else 152
tntd_width = Suitable_To_Do_Font.getbbox(('' if fortune[2:-2] == '大吉' else ' ' * 6) + unsuitable_to_do)[2] if len(unsuitable_to_do) <= 8 else 152
ttd_width2 = Suitable_To_Do_Font.getbbox(' ' * 6 + suitable_to_do2)[2] if len(suitable_to_do2) <= 8 else 152
tntd_width2 = Suitable_To_Do_Font.getbbox(' ' * 6 + unsuitable_to_do2)[2] if len(unsuitable_to_do2) <= 8 else 152
det_width = Detail_Font.getbbox(detail)[2] if len(detail) <= 12 else 144
det2_width = Detail_Font.getbbox(det2)[2] if len(det2) <= 12 else 144
det3_width = Detail_Font.getbbox(det3)[2] if len(det3) <= 12 else 144
det4_width = Detail_Font.getbbox(det4)[2] if len(det4) <= 12 else 144
name_width = Title_Font.getbbox(title)[2]
# 绘制
# Draw
draw.text(xy=(bg_size[0] / 2 - name_width / 2, 10), text=title, fill='#000000', font=Title_Font)
draw.text(xy=(bg_size[0] / 2 - fortune_width / 2, 50), text=fortune, fill='#e74c3c' if fortune[2:-2] in ['小吉', '中吉', '大吉', '吉你太美'] else '#3f3f3f', font=Fortune_Font)
begin_pos_y=150
draw.text(xy=(bg_size[0] / 4 - ttd_width / 2, begin_pos_y), text='诸事不宜' if fortune[2:-2] == '大凶' else '宜:', fill='#e74c3c', font=Suitable_To_Do_Font_Bold)
draw.text(xy=(bg_size[0] / 4 - ttd_width / 2, begin_pos_y), text='' if fortune[2:-2] == '大凶' else ' ' * 6 + suitable_to_do, fill='#e74c3c', font=Suitable_To_Do_Font)
draw.text(xy=(bg_size[0] / 4 * 3 - tntd_width / 2, begin_pos_y), text='诸事皆宜' if fortune[2:-2] == '大吉' else '忌:', fill='#000000', font=Suitable_To_Do_Font_Bold)
draw.text(xy=(bg_size[0] / 4 * 3 - tntd_width / 2, begin_pos_y), text='' if fortune[2:-2] == '大吉' else ' ' * 6 + unsuitable_to_do, fill='#000000', font=Suitable_To_Do_Font)
len_ttd=len(suitable_to_do.split('\n'))
print(len_ttd)
begin_pos_y+=25+25*(len_ttd-1)
draw.text(xy=(bg_size[0] / 4 - det_width / 2, begin_pos_y), text=detail, fill='#7f7f7f', font=Detail_Font)
draw.text(xy=(bg_size[0] / 4 * 3 - det2_width / 2, begin_pos_y), text=det2, fill='#7f7f7f', font=Detail_Font)

begin_pos_y=250
draw.text(xy=(bg_size[0] / 4 - ttd_width2 / 2, begin_pos_y), text='' if fortune[2:-2] == '大凶' else '宜:', fill='#e74c3c', font=Suitable_To_Do_Font_Bold)
draw.text(xy=(bg_size[0] / 4 - ttd_width2 / 2, begin_pos_y), text=' ' * 6 + suitable_to_do2, fill='#e74c3c', font=Suitable_To_Do_Font)
draw.text(xy=(bg_size[0] / 4 * 3 - tntd_width2 / 2, begin_pos_y), text='' if fortune[2:-2] == '大吉' else '忌:', fill='#000000', font=Suitable_To_Do_Font_Bold)
draw.text(xy=(bg_size[0] / 4 * 3 - tntd_width2 / 2, begin_pos_y), text=' ' * 6 + unsuitable_to_do2, fill='#000000', font=Suitable_To_Do_Font)
len_ttd2=len(suitable_to_do2.split('\n'))
print(len_ttd2)
begin_pos_y+=25+25*(len_ttd2-1)
draw.text(xy=(bg_size[0] / 4 - det3_width / 2, begin_pos_y), text=det3, fill='#7f7f7f', font=Detail_Font)
draw.text(xy=(bg_size[0] / 4 * 3 - det4_width / 2, begin_pos_y), text=det4, fill='#7f7f7f', font=Detail_Font)

img.show()

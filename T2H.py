# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 11:59:04 2023

@author: jaisi
"""

from PIL import ImageFont, ImageDraw, Image

# draw = ImageDraw.Draw(r"C:\Users\jaisi\Documents\Jai\Projects\Text_to_Handwriting\page.jpg")
# font = ImageFont.load(r"C:\Users\jaisi\Documents\Jai\Projects\Text_to_Handwriting\sweetly-broken\Sweetly Broken.ttf")

font_1 = ImageFont.truetype(font=r'C:\Users\jaisi\Documents\Jai\Projects\Text_to_Handwriting\always-forever\always forever.ttf', size=500)
font_2 = ImageFont.truetype(font=r'C:\Users\jaisi\Documents\Jai\Projects\Text_to_Handwriting\angelina\angelina.ttf', size=500)
font_3 = ImageFont.truetype(font=r'C:\Users\jaisi\Documents\Jai\Projects\Text_to_Handwriting\jennifer-lynne\Jennifer Lynne.ttf', size=500)
font_4 = ImageFont.truetype(font=r'C:\Users\jaisi\Documents\Jai\Projects\Text_to_Handwriting\prestige-signature-script\Prestige Signature Script - Demo\Prestige Signature Script - Demo.ttf', size=500)
font_5 = ImageFont.truetype(font=r'C:\Users\jaisi\Documents\Jai\Projects\Text_to_Handwriting\sweetly-broken\Sweetly Broken.ttf', size=500)
image = Image.open(r"C:\Users\jaisi\Documents\Jai\Projects\Text_to_Handwriting\page.jpg")
# Create an ImageDraw object onto which the font text will be placed
draw = ImageDraw.Draw(im=image)
# Draw the text onto our image
draw.text(xy=(5000, 1000), text="sphinx of the black quartz judge my vow", font=font_1, fill='black', anchor='mm')
draw.text(xy=(5000, 2000), text="sphinx of the black quartz judge my vow", font=font_2, fill='black', anchor='mm')
draw.text(xy=(5000, 3000), text="sphinx of the black quartz judge my vow", font=font_3, fill='black', anchor='mm')
draw.text(xy=(5000, 4000), text="sphinx of the black quartz judge my vow", font=font_4, fill='black', anchor='mm')
draw.text(xy=(5000, 5000), text="sphinx of the black quartz judge my vow", font=font_5, fill='black', anchor='mm')
image.show()

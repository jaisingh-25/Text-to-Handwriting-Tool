from PIL import ImageFont, ImageDraw, Image
import random as r
size=12
font_1 = ImageFont.truetype(font=r'...\OpenSans-Bold.ttf', size=size)
font_2 = ImageFont.truetype(font=r'...\OpenSans-Italic.ttf', size=size)
font_3 = ImageFont.truetype(font=r'...\OpenSans-Light.ttf', size=size)
font_4 = ImageFont.truetype(font=r'...\OpenSans-Regular.ttf', size=size)
font_5 = ImageFont.truetype(font=r'...\OpenSans-ExtraBold.ttf', size=size)
image = Image.open(r"...\page.jpg")
draw = ImageDraw.Draw(im=image)
text="sphinx of the blank quartz judge my vow"
count=0
for i in text:
    a=r.randrange(0,5)
    count+=12
    if a==0:
        draw.text(xy=(75+count, 50), text=i, font=font_1, fill='black', anchor='mm')
    elif a==1:
        draw.text(xy=(75+count, 50), text=i, font=font_2, fill='black', anchor='mm')
    elif a==2:
        draw.text(xy=(75+count, 50), text=i, font=font_3, fill='black', anchor='mm')
    elif a==3:
        draw.text(xy=(75+count, 50), text=i, font=font_4, fill='black', anchor='mm')
    else:
        draw.text(xy=(75+count, 50), text=i, font=font_5, fill='black', anchor='mm')
image.show()

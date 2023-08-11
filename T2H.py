from PIL import ImageFont, ImageDraw, Image
font_1 = ImageFont.truetype(font=r'...\always forever.ttf', size=500)
font_2 = ImageFont.truetype(font=r'...\angelina.ttf', size=500)
font_3 = ImageFont.truetype(font=r'...\Jennifer Lynne.ttf', size=500)
font_4 = ImageFont.truetype(font=r'...\Prestige Signature Script - Demo.ttf', size=500)
font_5 = ImageFont.truetype(font=r'...\Sweetly Broken.ttf', size=500)
image = Image.open(r"...\page.jpg")
draw = ImageDraw.Draw(im=image)
draw.text(xy=(5000, 1000), text="sphinx of the black quartz judge my vow", font=font_1, fill='black', anchor='mm')
draw.text(xy=(5000, 2000), text="sphinx of the black quartz judge my vow", font=font_2, fill='black', anchor='mm')
draw.text(xy=(5000, 3000), text="sphinx of the black quartz judge my vow", font=font_3, fill='black', anchor='mm')
draw.text(xy=(5000, 4000), text="sphinx of the black quartz judge my vow", font=font_4, fill='black', anchor='mm')
draw.text(xy=(5000, 5000), text="sphinx of the black quartz judge my vow", font=font_5, fill='black', anchor='mm')
image.show()

from PIL import ImageDraw, Image, ImageDraw2

img = Image.new('RGBA', (200, 200), 'white')
img2 = Image.new('RGBA', (400, 800), 'white')

draw = ImageDraw.Draw(img)
draw2 = ImageDraw2.Draw(img2)

draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='black')
draw.rectangle((20, 30, 60, 60), fill='blue')
draw.ellipse((120, 30, 160, 60), fill='red')
draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)), fill='brown')

for i in range(100, 200, 10):
    draw.line([(i, 0), (200, i - 100)], fill='green')
    img.save('drawing.png')

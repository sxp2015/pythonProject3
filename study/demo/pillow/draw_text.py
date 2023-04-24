# 导入Image、ImageDraw和ImageFont类
from PIL import Image, ImageDraw, ImageFont
# 导入os模块
import os

# 创建一个200x200的白色RGBA图像
im = Image.new('RGBA', (200, 200), 'white')

# 创建一个可用于在图像上绘制的对象
draw = ImageDraw.Draw(im)

# 在图像上添加文本 “hello world”，颜色为蓝色
draw.text((20, 20), 'hello world', fill='blue')

# 获取操作系统中arial字体的路径
fontsFolder = r'C:\Windows\Fonts'

try:
    # 加载arial字体，设置字体大小为32
    # truetype()函数，它有两个参数。第一个参数是字符串，表示字体的TrueType文件
    # truetype()函数，第二个参数是一个整数，表示字体大小的点数（而不是像素点）
    arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)
    # 在图像上添加文本 “Howdy”，颜色为灰色，字体为arial，位置为(100, 150)
    draw.text((100, 150), 'Howdy', fill='gray', font=arialFont)

except OSError:
    print('无法加载字体文件！')



# 保存图像
im.save('文字.png')
from PIL import Image, ImageColor

"""
如果想调用paste()，又要保持原始图像的未修改版本，
就需要先复制图像，然后在副本上调用paste()。
"""
# 定义图片路径
img_path = r'C:\Users\admin\PycharmProjects\pythonProject3\study\img\111.jpg'
my_avatar_path = r'C:\Users\admin\PycharmProjects\pythonProject3\study\img\avatar.png'
catIm_path = r'C:\Users\admin\PycharmProjects\pythonProject3\study\img\avatar.png'
faceIm_path = r'C:\Users\admin\PycharmProjects\pythonProject3\study\demo\pillow\a.png'

# 打开一张图片
img = Image.open(img_path)
avatar = Image.open(my_avatar_path)
# 解构宽和高
width, height = img.size

# 裁剪crop图片
cropped_img = img.crop((20, 20, 150, 150))
#  (100, 100, 330, 330) 粘贴时要对应，宽230，高230
avatar_cropped = avatar.crop((120, 120, 350, 350))
# 复制/合并图片
img_copied = img.copy()

#  (100, 100, 330, 330) 宽230，高230
img_copied.paste(avatar_cropped, (100, 100, 330, 330))

img_copied.save('merge.jpg')
# 另存为其他格式图片
cropped_img.save('a.png')

# 创建一张新图片,指定背景色为紫色
im = Image.new('RGB', (100, 200), 'Purple')
# 不指定背景色，默认为黑色
im2 = Image.new('RGBA', (300, 500))

im.save('purple.jpg')
im2.save('im2.png')

print('img size:', img.size)
print('img width:', width)
print('img height:', height)
print('img format:', img.format)
print('img format_description:', img.format_description)

# 打开图片
catIm = Image.open(catIm_path)
faceIm = Image.open(faceIm_path)
# 解构出宽和高
catImWidth, catImHeight = catIm.size
faceImWidth, faceImHeight = faceIm.size
# 复制一张图
catCopyTwo = catIm.copy()
# 遍历图片并粘贴
"""
range(开始,结束,步长)函数可以生成一个指定范围内的整数序列，用于循环和迭代。它有三个参数，分别是:
start：整数序列的起始值，默认为0。即生成的整数序列从哪个数字开始。
stop：整数序列的结束值，但不包括该值。即生成的整数序列不包括哪个数字。
step：生成数字的步长，默认为1。即相邻两个整数之间的差。
"""
for left in range(0, catImWidth, faceImWidth):
    for top in range(0, catImHeight, faceImHeight):
        print(left, top)
        catCopyTwo.paste(faceIm, (left, top))
        catCopyTwo.save('tiled.png')

# 调整图片尺寸
quarter_sizedIm = catIm.resize((int(width / 2), int(height / 2)))
quarter_sizedIm.save('quarter_sized.png')
svelteIm = catIm.resize((width, height + 300))
svelteIm.save('svelte.png')

# 旋转图片

catIm.rotate(90).save('rotated90.png')
catIm.rotate(180).save('rotated180.png')
catIm.rotate(270).save('rotated270.png')
# 旋转并放大
catIm.rotate(6).save('rotated6.png')
catIm.rotate(6, expand=True).save('rotated6_expanded.png')

# 左右翻转 和 垂直翻转
catIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
catIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')

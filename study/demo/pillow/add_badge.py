import os
from PIL import Image

# 定义填充尺寸
SQUARE_FIT_SIZE = 300
# 定义引用的文件
LOGO_FILENAME = 'water_mark/cat_img_resize.png'
# 打开文件
logoIm = Image.open(LOGO_FILENAME)
# 获取宽高
logoWidth, logoHeight = logoIm.size

# 创建文件夹
os.makedirs('添加水印的图片', exist_ok=True)

# 遍历目录下的所有文件
# 这个循环是为了避免程序出错，作个判断，即使不是图片文件，让程序继续执行
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == LOGO_FILENAME:
        continue
    im = Image.open(filename)
    width, height = im.size

    # 只有图片宽度 大于水印图片的宽度才执行程序【等比缩放】
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:  # 宽度 大于 高度 说明是横图 举例 300宽 * 150高
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:  # 不是上述情况，则说明是竖图 例如 300宽 * 600高
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        print('调整图片尺寸 %s 中...' % filename)

    im_resize = im.resize((width, height))

    im_resize.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
    im_resize.save(os.path.join('添加水印的图片', filename))

"""
paste(im, box=None, mask=None)
im参数表示要粘贴的源图像，box参数表示在目标图像上粘贴的位置，
mask参数表示一个可选的掩码图像，用于控制源图的哪些像素应该被粘贴，填写源图变量表示整个源图的像素。
如果省略了box参数，则源图像将被粘贴到目标图像的左上角。
"""
from PIL import Image
import os
# 定义填充尺寸
SQUARE_FIT_SIZE = 100
# 定义LOGO尺寸
LOGO_FILENAME = r'C:\Users\admin\PycharmProjects\pythonProject3\study\demo\pillow\cat.png'
# 复制LOGO
cat_img_copy = Image.open(LOGO_FILENAME).copy()

# 获取宽高
width, height = cat_img_copy.size

# 创建文件夹
os.makedirs('water_mark', exist_ok=True)

# 只有图片宽度 大于水印图片的宽度才执行程序【等比缩放】
if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
    if width > height:  # 宽度 大于 高度 说明是横图 举例 300宽 * 150高
        height = int((SQUARE_FIT_SIZE / width) * height)
        width = SQUARE_FIT_SIZE
    else:  # 不是上述情况，则说明是竖图 例如 300宽 * 600高
        width = int((SQUARE_FIT_SIZE / height) * width)
        height = SQUARE_FIT_SIZE

    cat_img_resize = cat_img_copy.resize((width, height))
    cat_img_resize.save('water_mark/cat_img_resize.png')
import tesserocr
from PIL import Image
import numpy as np

# pip install tesserocr pip如果可用的情况下安装
# tesseract --version 检查版本
# 选择版本 下载 https://github.com/simonflueckiger/tesserocr-windows_build/releases
# 安装方式：pip install <package_name>.whl
# 官方文档 ：https://pypi.org/project/tesserocr/
# windows下安装教程：https://segmentfault.com/a/1190000039929696
# windows安装成功的情况下 在CMD到图片的目录下，-l 参数指定了语言数据包的名称或路径，
# 用于让 tesseract 引擎识别对应语言的文字。其中，chi_sim 指的是简体中文语言数据包
#  tesseract test1.png result -l chi_sim

# 测试网站 https://captcha7.scrape.center/

# 定义 URL 地址
TARGET_URL_01 = 'https://captcha7.scrape.center/'

# 打开图像文件并赋值给变量
image1: Image.Image = Image.open('test_images/1.png')
image2: Image.Image = Image.open('test_images/2.png')

# 口1:像素用1位表示Python中表示为True或False即二值化。
# 口L:像素用8位表示，取值0-255，表示灰度图像，数字越小，颜色越黑。
# 口P:像素用8位表示，即调色板数据
# 口RGB:像素用3x8位表示即真彩色
# 口RGBA:像素用4x8位表示，即有透明通道的真彩色
# 口CMYK:像素用4x8位表示，即印刷四色模式。
# 口YCbCr:像素用3x8位表示即彩色视频格式
# I:像素用32位整型表示
# F:像素用 32位浮点型表示。


# 转化为灰度图像
image2: Image.Image = image2.convert('L')

# 灰度阀值
threshold: int = 50

# 将 PIL Image 对象转换为 Numpy 数组
img_arr1: np.ndarray = np.asarray(image1)

img_arr2: np.ndarray = np.asarray(image2)

# NumPy的where方法对数组进行筛选和处理，
# 其中指定将灰度大于值的图片的像素设置为255表示白色，否则设置为0，表示黑色
img_arr2: np.ndarray = np.where(img_arr2 > threshold, 255, 0)

# 获取 Numpy 数组的形状并赋值给变量
image1_np: tuple = np.array(img_arr1).shape
image2_np: tuple = np.array(img_arr2).shape

# image1_np: (41, 332, 3) 输出结果 41是图像的高,332是图像的宽,3是向量的值

# 使用 tesserocr 库提取图像中的文本信息并赋值给变量
result1: str = tesserocr.image_to_text(image1, lang='chi_sim')
result2: str = tesserocr.image_to_text(image2, lang='chi_sim')

# 输出结果和变量信息
print('result1:', result1)
print('image1 mode:', image1.mode)
print('image2 mode:', image2.mode)
print('image1_np:', image1_np)
print('result2:', result2)

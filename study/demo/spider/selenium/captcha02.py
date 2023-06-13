import time
import re
import tesserocr
from selenium import webdriver
from io import BytesIO
from PIL import Image
from retrying import retry
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import numpy as np

# 目标网站URL
TARGET_URL_01 = 'https://captcha7.scrape.center/'


def preprocess(image):
    # 将图片转为灰度图像
    image = image.convert('L')
    # 将灰度图像转为numpy数组
    array = np.array(image)
    # 将数组中大于50的像素点转为白色，其余的像素点转为黑色
    array = np.where(array > 105, 255, 0)
    # 将numpy数组转为图像
    image = Image.fromarray(array.astype('uint8'))
    return image


# 使用retrying库实现登录重试
@retry(stop_max_attempt_number=10, retry_on_result=lambda x: x is False)
def login():
    # 打开目标网站
    browser.get(TARGET_URL_01)
    # 输入用户名和密码
    browser.find_element(By.CSS_SELECTOR, '.username input[type="text"]').send_keys('admin')
    browser.find_element(By.CSS_SELECTOR, '.password input[type="password"]').send_keys('admin')
    # 获取验证码图片
    captcha = browser.find_element(By.CSS_SELECTOR, '#captcha')
    # 将验证码图片转为Image对象
    image = Image.open(BytesIO(captcha.screenshot_as_png))
    # 对验证码图片进行预处理
    image = preprocess(image)
    # print('image:', image)
    image.show()
    # 使用tesserocr库识别验证码
    captcha = tesserocr.image_to_text(image)
    # print('captcha:', captcha)
    # 移除验证码中的非字母数字字符
    captcha = re.sub('[^A-Za-z0-9]', '', captcha)

    # 输入识别出的验证码
    browser.find_element(By.CSS_SELECTOR, '.captcha input[type="text"]').send_keys(captcha)
    # 点击登录按钮
    browser.find_element(By.CSS_SELECTOR, '.login').click()

    try:
        # 等待登录成功页面加载完成
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//h2[contains(.,"登录成功")]')))
        # 等待10秒钟
        time.sleep(10)
        # 关闭浏览器窗口
        browser.close()
        # 返回True表示登录成功
        return True
    except TimeoutException:
        # 返回False表示登录失败，触发retry机制
        return False


if __name__ == '__main__':
    # 创建Chrome浏览器对象
    browser = webdriver.Chrome()
    # 调用login函数进行登录
    login()

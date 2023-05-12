import time

import pyautogui
# 导入selenium和webdriver模块
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 定义ChromeDriver及启动服务
driver_service = Service('C:\\Program Files\\chromedriver.exe')
driver_service.start()

# 最大化窗口
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# 创建selenium的 WebDriver对象
browser = webdriver.Chrome(service=driver_service, options=options)

# 定义及打开百家号网页
BaiJiaHao_URL = "https://baijiahao.baidu.com/builder/theme/bjh/login"
browser.get(BaiJiaHao_URL)

# 获取当前窗口句柄
current_window_handle = browser.current_window_handle
# 执行 JavaScript 语句，在新窗口中打开指定的网页
# browser.execute_script("window.open('https://mp.weixin.qq.com/')")
# 切换到新窗口
browser.switch_to.window(browser.window_handles[0])
# 等待5秒切换界面
time.sleep(5)
# 百家号输入账号和密码
input_userName = browser.find_element("id", "TANGRAM__PSP_4__userName")
input_password = browser.find_element("id", "TANGRAM__PSP_4__password")
button_submit = browser.find_element("id", "TANGRAM__PSP_4__submit")
input_userName.send_keys("风车百科")
input_password.send_keys("s。。。。。。。。。410")
button_submit.click()

# 等待滑块验证完成切换界面
time.sleep(12)

# 关闭提示框
pyautogui.moveTo(693, 686, 1)
pyautogui.click()
time.sleep(2)
pyautogui.moveTo(1068, 160, 1)
pyautogui.click()

# 等待验证页面关闭
time.sleep(3)

# 定义百家号的内容管理位置
BJ_NeiRongGuanLi = 'img/BJ_NeiRongGuanLi.png'
BJ_NeiRongGuanLi2 = 'img/BJ_NeiRongGuanLi2.png'
BJ_XiuGai = 'img/BJ_xiugai.png'
WX_GongZhongHao = 'img/WX_GongZhongHao.png'
CHE_HUI = 'img/chehui.png'
SHAN_CHU = 'img/shanchu.png'

# 在截图中查找指定的图片
locateBJ_NeiRongGuanLi = pyautogui.locateOnScreen(BJ_NeiRongGuanLi)
locateBJ_NeiRongGuanLi2 = pyautogui.locateOnScreen(BJ_NeiRongGuanLi2)
image_location = locateBJ_NeiRongGuanLi if locateBJ_NeiRongGuanLi else locateBJ_NeiRongGuanLi2
locate_WX_GongZhongHao = pyautogui.locateOnScreen(WX_GongZhongHao)
# 如果找到了图片，则输出图片的位置
if image_location:

    print('识别内容管理位置成功:', image_location)
    # x, y = pyautogui.center(image_location)
    pyautogui.click(image_location)
    # 点击识别成功的坐标
    # pyautogui.click(image_location)
    # 等待内容数据显示出来
    time.sleep(6)


    # 定义查找标签元素的方法
    def get_element_location(xpath: str):
        elements = browser.find_elements(By.XPATH, xpath)
        if not elements:
            return None
        # 获取窗口当前的滚动距离
        location = elements[0].location
        screen_x = location['x']
        screen_y = location['y']
        print('location: ==', location)
        print('screen_x:', screen_x, 'screen_y:', screen_y)
        return screen_x, screen_y


    while True:
        # 移动到更多
        pyautogui.moveTo(1234, 450, 1)
        # 等待下拉列表显示出来
        time.sleep(2)
        # 使用selenium获取更多列表的选项内容
        dropdown = browser.find_element(By.CLASS_NAME, 'cheetah-popover-inner-content')

        # 定义Xpath规则
        xpath_revoke = '//span[contains(text(), "撤回")]'
        xpath_delete = '//span[contains(text(), "删除")]'
        # 获取下拉文本列表
        dropdown_text = dropdown.text

        # 判断列表的内容
        if '删除' in dropdown_text:
            remove_location = get_element_location(xpath_delete)
            # 识别删除选项所在的位置
            locate_shan_chu = pyautogui.locateOnScreen(SHAN_CHU)
            if remove_location is not None:
                if locate_shan_chu:
                    print('删除位置识别成功', locate_shan_chu)
                    pyautogui.moveTo(locate_shan_chu.left + 25, locate_shan_chu.top + 5, duration=1)
                    pyautogui.click()
                    time.sleep(1)
                    pyautogui.moveTo(locate_shan_chu.left - 480, locate_shan_chu.top - 80, duration=1)
                    pyautogui.click()
                    time.sleep(5)
                    pyautogui.moveTo(1234, 450, 1)
                    time.sleep(2)
                    # 使用selenium获取更多列表的选项内容
                    dropdown = browser.find_element(By.CLASS_NAME, 'cheetah-popover-inner-content')
                    if not dropdown_text:
                        break
                    else:
                        continue
            else:
                print('位置获取失败')
                time.sleep(5)

        elif '撤回' in dropdown_text:
            return_location = get_element_location(xpath_revoke)
            # 识别撤回选项所在的位置
            locate_che_hui = pyautogui.locateOnScreen(CHE_HUI)
            if return_location is not None:
                if locate_che_hui:
                    print('撤回位置识别成功', locate_che_hui)
                    pyautogui.click(locate_che_hui)
                    time.sleep(1)
                    pyautogui.moveTo(locate_che_hui.left - 480, locate_che_hui.top - 140, duration=1)
                    pyautogui.click()
                    time.sleep(5)
                    pyautogui.moveTo(1234, 450, 1)
                    time.sleep(2)
                    # 使用selenium获取更多列表的选项内容
                    dropdown = browser.find_element(By.CLASS_NAME, 'cheetah-popover-inner-content')
                    if not dropdown_text:
                        break
                    else:
                        continue

            else:
                print('位置获取失败')
                time.sleep(5)

        if not dropdown_text:
            break
        else:
            continue

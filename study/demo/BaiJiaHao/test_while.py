import time, pathlib
# 导入selenium和webdriver模块
from selenium import webdriver
import pyautogui, pygetwindow
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
browser.execute_script("window.open('https://mp.weixin.qq.com/')")
# 切换到新窗口
browser.switch_to.window(browser.window_handles[0])
# 等待5秒切换界面
time.sleep(5)
# 百家号输入账号和密码
input_userName = browser.find_element("id", "TANGRAM__PSP_4__userName")
input_password = browser.find_element("id", "TANGRAM__PSP_4__password")
button_submit = browser.find_element("id", "TANGRAM__PSP_4__submit")
input_userName.send_keys("风车百科")
input_password.send_keys("s.............0")
button_submit.click()

# 等待滑块验证完成切换界面
time.sleep(15)

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
BJ_more = 'img/BJ_more.png'

# 在截图中查找指定的图片
locateBJ_NeiRongGuanLi = pyautogui.locateOnScreen(BJ_NeiRongGuanLi)
locateBJ_NeiRongGuanLi2 = pyautogui.locateOnScreen(BJ_NeiRongGuanLi2)
BJ_NeiRongGuanLi_location = locateBJ_NeiRongGuanLi if locateBJ_NeiRongGuanLi else locateBJ_NeiRongGuanLi2
locate_WX_GongZhongHao = pyautogui.locateOnScreen(WX_GongZhongHao)

# 如果找到了图片，则输出图片的位置
if BJ_NeiRongGuanLi_location:

    print('识别图片位置成功:', BJ_NeiRongGuanLi_location)
    # 点击识别成功的坐标
    pyautogui.click(BJ_NeiRongGuanLi_location)
    # 等待内容数据显示出来
    time.sleep(8)
    # 移动到更多
    pyautogui.moveTo(1230, 455, 1)
    # 等待下拉列表显示出来
    time.sleep(2)
    # 使用selenium获取更多列表的选项内容
    dropdown = browser.find_element(By.CLASS_NAME, 'cheetah-popover-inner-content')
    # 如果没有增加商品这个选项的样式，说明是文章内容
    # 输出文本
    # print('选项文字内容：', dropdown.text)

    while True:
        if dropdown:
            if dropdown.text.startswith('详细数据'):
                print('这项是视频')
                while True:
                    pyautogui.moveTo(1300, 455, 0.25)
                    time.sleep(0.5)
                    target = pyautogui.locateOnScreen('img/BJ_more.png')
                    if target:
                        target_center = pyautogui.center(target)
                        pyautogui.moveTo(target_center)
                        pyautogui.scroll(-75)
                        time.sleep(0.5)
                        pyautogui.moveTo(1230, 455, 0.25)
                        time.sleep(0.5)
                        new_dropdown = browser.find_element(By.CLASS_NAME, 'cheetah-popover-inner-content')
                        if new_dropdown and new_dropdown != dropdown:
                            dropdown = new_dropdown
                            if dropdown.text.startswith('详细数据'):
                                print('这项是视频')
                                continue
                            else:
                                print('这是一篇文章')
                                break
                        else:
                            continue

            else:
                print('这是一篇文章')
                locate_BJ_XiuGai = pyautogui.locateOnScreen(BJ_XiuGai)
                time.sleep(1)
                pyautogui.click(locate_BJ_XiuGai)
                time.sleep(5)
                pyautogui.moveTo(260, 350, 0.5)
                pyautogui.click()
                pyautogui.hotkey('ctrl', 'a')
                time.sleep(1)
                pyautogui.hotkey('ctrl', 'c')
                time.sleep(1)
                pyautogui.moveTo(600, 15, 0.5)
                pyautogui.click()

        else:
            print('没有找到下拉框')
            break
    # 测试执行完成后不关闭浏览器
    # input('Press any key to quit...')
    # browser.quit()
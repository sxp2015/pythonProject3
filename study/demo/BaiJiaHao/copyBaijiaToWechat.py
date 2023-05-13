import time

import pyautogui
# 导入selenium和webdriver模块
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 定义ChromeDriver及启动服务c
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
input_password.send_keys("s..........................0")
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
time.sleep(2)

# 定义百家号的内容管理位置
BJ_NeiRongGuanLi = 'img/BJ_NeiRongGuanLi.png'
BJ_NeiRongGuanLi2 = 'img/BJ_NeiRongGuanLi2.png'

CHE_HUI = 'img/chehui.png'
SHAN_CHU = 'img/shanchu.png'

# 在截图中查找指定的图片
locateBJ_NeiRongGuanLi = pyautogui.locateOnScreen(BJ_NeiRongGuanLi)
locateBJ_NeiRongGuanLi2 = pyautogui.locateOnScreen(BJ_NeiRongGuanLi2)
image_location = locateBJ_NeiRongGuanLi if locateBJ_NeiRongGuanLi else locateBJ_NeiRongGuanLi2

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
    def get_element_location(xpath_rule: str):
        elements = browser.find_elements(By.XPATH, xpath_rule)
        if not elements:
            return None
        # 获取窗口当前的滚动距离
        location = elements[0].location
        element_x = location['x'] + elements[0].size['width'] / 2
        element_y = location['y'] + elements[0].size['height'] / 2
        print('location: ==', location)
        print('element_x:', element_x, 'element_y:', element_y)
        return elements[0], element_x, element_y


    def element_click(element):
        ActionChains(browser).move_to_element(element).click().perform()


    def remove_or_revoke(option):
        button_xpath = '//span[contains(text(), "确 定")]'
        button_xpath2 = '//span[contains(text(), "撤回图文与视频")]'
        button_xpath3 = '//span[contains(text(), "确认并删除视频")]'
        if option is not None:
            print('option :', option[0], option[1], option[2])
            option_item_0 = option[0]
            element_click(option_item_0)
            time.sleep(2)
            button_confirm = get_element_location(button_xpath)
            button_revoke_article = get_element_location(button_xpath2)
            button_confirm_remove_videos = get_element_location(button_xpath3)
            if button_confirm is not None:
                print('button_confirm :', button_confirm)
                button_element_1 = button_confirm[0]
                element_click(button_element_1)
                pyautogui.scroll(-2000)
                pyautogui.moveTo(1234, 400, 1)

                time.sleep(2)
                return True

            elif button_revoke_article is not None:
                print('button_revoke_article:', button_revoke_article)
                button_element_2 = button_revoke_article[0]
                element_click(button_element_2)
                pyautogui.scroll(-2000)
                pyautogui.moveTo(1234, 400, 1)

                time.sleep(2)
                return True

            elif button_confirm_remove_videos is not None:
                print('button_confirm_remove_videos:', button_confirm_remove_videos)
                button_element_3 = button_confirm_remove_videos[0]
                element_click(button_element_3)
                pyautogui.scroll(-2000)
                pyautogui.moveTo(1234, 400, 1)
                time.sleep(2)
                return True

            return True


    def process_dropdown(dropdown_text):

        # 定义Xpath规则
        xpath_revoke = '//span[contains(text(), "撤回")]'
        xpath_delete = '//span[contains(text(), "删除")]'

        # 判断列表的内容
        if '删除' in dropdown_text:
            remove_location = get_element_location(xpath_delete)
            # 识别删除选项所在的位置
            # locate_shan_chu = pyautogui.locateOnScreen(SHAN_CHU)
            return remove_or_revoke(remove_location)
            # if remove_location is not None:
            #     # if locate_shan_chu:
            #     #     print('删除位置识别成功', locate_shan_chu)
            #     #     remove_x, remove_y = pyautogui.center(locate_shan_chu)
            #     #     pyautogui.moveTo(remove_x, remove_y, 1)
            #     #     pyautogui.click()
            #     #     time.sleep(1)
            #     #     pyautogui.moveTo(locate_shan_chu.left - 480, locate_shan_chu.top - 80, duration=1)
            #     #     pyautogui.click()
            #     #     return True
            #     print('remove_location', remove_location[0], remove_location[1], remove_location[2])
            #     remove_element = remove_location[0]
            #     element_click(remove_element)
            #     time.sleep(1)
            #     button_location = get_element_location(xpath_button)
            #     if button_location is not None:
            #         print('button_location', button_location)
            #         button_element = button_location[0]
            #         element_click(button_element)
            #         time.sleep(1)

        elif '撤回' in dropdown_text:
            return_location = get_element_location(xpath_revoke)
            # 识别撤回选项所在的位置
            # locate_che_hui = pyautogui.locateOnScreen(CHE_HUI)
            # if return_location is not None:
            #     # if locate_che_hui:
            #     #     print('撤回位置识别成功', locate_che_hui)
            #     #     return_x, return_y = pyautogui.center(locate_che_hui)
            #     #     pyautogui.moveTo(return_x, return_y, 1)
            #     #     pyautogui.click()
            #     #     time.sleep(1)
            #     #     pyautogui.moveTo(locate_che_hui.left - 480, locate_che_hui.top - 100, duration=1)
            #     #     pyautogui.click()
            #     #     return True
            return remove_or_revoke(return_location)
        return False


    while True:
        time.sleep(1)
        # 移动到更多
        pyautogui.moveTo(1234, 400, 1)
        pyautogui.click()
        pyautogui.scroll(-2000)
        # 等待下拉列表显示出来
        pyautogui.moveTo(1234, 465, 1)
        time.sleep(3)
        # 使用selenium获取更多列表的选项内容
        dropdown_text_list = browser.find_element(By.CLASS_NAME, 'cheetah-popover-inner-content').text

        while dropdown_text_list:
            if process_dropdown(dropdown_text_list):
                time.sleep(3)
                # 中断内层循环
                break
            else:
                # 中断外层循环的当前迭代
                dropdown_text_list = None
                continue

        if not dropdown_text_list:
            break

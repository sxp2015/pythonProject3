from typing import List
from selenium import webdriver
from selenium.common import UnexpectedAlertPresentException, NoAlertPresentException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def drag_and_drop(source_css_selector: str, target_css_selector: str) -> List[str]:
    """使用 selenium 模拟拖拽操作"""

    # 创建 Chrome 浏览器 WebDriver 对象
    browser = webdriver.Chrome()

    try:
        # 加载网页
        url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
        browser.get(url)

        # 切换到 iframe 中
        browser.switch_to.frame('iframeResult')

        # 找到拖拽元素
        source = browser.find_element(By.CSS_SELECTOR, source_css_selector)  # type: ignore

        # 找到放置元素
        target = browser.find_element(By.CSS_SELECTOR, target_css_selector)  # type: ignore

        # 模拟拖拽操作
        action = ActionChains(browser)
        action.drag_and_drop(source, target)
        action.perform()

        # 等待弹窗加载完毕
        wait = WebDriverWait(browser, 10)
        alert = wait.until(EC.alert_is_present())
        alert.accept()
        return [target.text]

    # except UnexpectedAlertPresentException:
    #     # 如果出现 Alert 弹窗，则关闭弹窗 执行 alert.dismiss() 方法通常相当于点击“取消”按钮
    #     # 执行“确认”操作，可以使用 alert.accept() 方法
    #     alert = browser.switch_to.alert
    #     alert.accept()

    except NoAlertPresentException:
        print('没有找到弹窗')

    finally:
        # 关闭浏览器
        browser.quit()


# 测试拖拽函数
if __name__ == '__main__':
    results = drag_and_drop('#draggable', '#droppable')
    for result in results:
        print(result)

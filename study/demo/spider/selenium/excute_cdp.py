import time

from selenium import webdriver
from selenium.webdriver import ChromeOptions

"""
现在有很多网站增加了对 Selenium 的检测，防止一些爬虫的恶意爬取，如果检测到有人使用Selenium打开浏览器，就直接屏蔽。
在Selenium中，可以用CDP(即Chrome Devtools Protocol，Chrome开发工具协议)解决这个问题，
利用它可以实现在每个页面刚加载的时候就执行 JavaScript 语句，将 webdriver 属性置空。
这里执行的CDP方法叫作 Page.addScriptToEvaluate0nNewDocument，
将JavaScript语句传人其中即可。另外，还可以加人几个选项来隐藏 webDriver 提示条和自动化扩展信息
"""
# 导入 time、webdriver 和 ChromeOptions
import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions

# 创建一个 ChromeOptions 对象
option = ChromeOptions()

# 添加实验性质选项，排除自动化测试选项
option.add_experimental_option('excludeSwitches', ['enable-automation'])

# 添加实验性质选项，关闭自动化扩展功能
option.add_experimental_option('useAutomationExtension', False)

# 创建一个浏览器对象，传入 ChromeOptions 对象
browser = webdriver.Chrome(options=option)

# 利用 CDP 机制，修改浏览器特征，避免被检测出使用自动化工具
# 具体是通过 JavaScript 修改 navigator.webdriver 属性，并返回 undefined。
browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                        {'source': 'Object.defineProperty(navigator,"webdriver",{get:()=>undefined})'})

# 打开待爬取的网站
browser.get('https://antispider1.scrape.center/')

# 等待 4 秒钟
time.sleep(4)


""""
这段代码是使用 Selenium + Chrome 避免反爬虫的一种方式，具体思路是利用 Chrome DevTools Protocol（CDP）来控制 Chrome 浏览器，并设置一些选项来降低被识别为自动化工具的可能性。

以下是对这段代码进行的详细解释：

ChromeOptions() 是 Chrome 的配置选项
add_experimental_option() 方法可以添加实验性质的选项
'excludeSwitches' 和 'useAutomationExtension' 这两项实验性质选项是用来关闭 Chrome 自动化漏洞的，即关闭 Chrome 自带的自动化测试功能
webdriver 是一个标识变量，被网站用来检测用户是否使用了自动化测试工具。我们通过在 CDP 中向页面添加 JavaScript，动态更改 navigator.webdriver 属性，使其在 JavaScript 中始终返回的是 undefined，从而欺骗网站。
execute_cdp_cmd() 方法可以执行 CDP 命令，这里使用了 Page.addScriptToEvaluateOnNewDocument 命令向浏览器添加了一个脚本。这条命令的作用是在每个新页面载入时执行 JavaScript 代码，修改了 navigator.webdriver 属性。
最后使用 get() 方法打开目标网站，并使用 time.sleep() 函数等待页面加载完成。
"""
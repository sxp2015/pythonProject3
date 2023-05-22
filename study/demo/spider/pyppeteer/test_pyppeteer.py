import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq


async def main():
    # 启动浏览器对象
    # --disable-infobars: 禁用浏览器中的一些信息栏，例如“chrome正在受到自动测试软件的控制”等提示。
    # --no-sandbox: 禁用沙箱模式，使浏览器在非沙箱环境下运行。沙箱模式可以提高浏览器安全性，但有时会导致一些运行问题。
    browser = await launch(headless=True)
    # 创建新页面
    page = await browser.newPage()
    try:
        # 跳转到指定页面
        await page.goto('https://spa2.scrape.center/')
        # 等待元素加载完成
        await page.waitForSelector('.item .name')
        # 解析网页内容，获取数据
        doc = pq(await page.content())
        names = [item.text() for item in doc('.item .name').items()]
        print('Names:', names)
    finally:
        # 关闭浏览器对象
        await browser.close()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())

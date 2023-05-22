import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq


async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto("https://www.baidu.com")
    await page.goto("https://spa2.scrape.center/")

    # 后退
    await page.goBack()
    # 前进
    await page.goForward()
    # 刷新
    await page.reload()
    # 保存PDF 该方法需要浏览器支持PrintToPDF协议，但是当前的Chromium浏览器可能没有实现该协议
    # await page.pdf()
    # 截图
    await page.screenshot()
    # 设置页面HTML
    await page.setContent('<h2>Hello World</h2>')
    # 设置User-Agent
    await page.setUserAgent('Python')
    # 设置Headers
    await page.setExtraHTTPHeaders(headers={})
    # HTML
    html = await page.content()
    print('html:', html)
    # cookies
    cookies = await page.cookies()
    print('cookies:', cookies)
    # 关闭
    await page.close()
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())

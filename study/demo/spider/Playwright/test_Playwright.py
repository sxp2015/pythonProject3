import asyncio

from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright

with sync_playwright() as p:
    for browser_type in [p.chromium, p.firefox, p.webkit]:
        # 如果不把 headless 参数设置为 False，就会以默认的无头模式启动浏览器，我们将看不到任何窗口。
        browser = browser_type.launch(headless=False)
        page = browser.new_page()
        page.goto('https://www.baidu.com')
        page.screenshot(path=f'screenshot-{browser_type.name}.png')
        print('title:', page.title())
        browser.close()


async def main():
    async with async_playwright() as ap:
        for browser_type2 in [ap.chromium, ap.firefox, ap.webkit]:
            browser2 = await browser_type2.launch()
            page2 = await browser2.new_page()
            await page2.goto('https://www.taobao.com/')
            await page2.screenshot(path=f'screenshot-async-{browser_type2.name}.png')
            print('title2:', await page2.title())
            await browser2.close()


asyncio.run(main())

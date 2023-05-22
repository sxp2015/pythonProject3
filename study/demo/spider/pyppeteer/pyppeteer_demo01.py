import asyncio
from pyppeteer import launch

width, height = 1366, 768


async def main():
    # 启动浏览器对象，headless选项表示是否在后台运行浏览器
    # headless=True 或者默认不设置，那么在启动的时候是看不到任何界面的。
    # 如果把它设置为 False，那么在启动的时候就可以看到界面了。
    browser = await launch(headless=False, args=['--disable-infobars', '--no-sandbox'])

    try:
        # 创建新页面对象
        page = await browser.newPage()

        # evaluateOnNewDocument 的方法，意思是在每次加载网页的时候执行某条语句
        # 利用它执行隐藏webdriver 属性的命令
        await page.evaluateOnNewDocument('Object.defineProperty(navigator,"webdriver",{get:()=>undefined})')

        # 设置页面大小
        await page.setViewport({'width': width, 'height': height})

        # 跳转到指定页面
        await page.goto('https://spa2.scrape.center/')

        # 等待元素加载完成
        await page.waitForSelector('.item .name')

        # 等待2秒钟，以确保所有资源加载完成
        await asyncio.sleep(2)

        # 截取当前页面的截图并保存到本地文件example.png中
        await page.screenshot(path='example.png')

        # 获取页面尺寸、设备像素比等信息，并保存到dimensions变量中
        dimensions = await page.evaluate('''()=>{return {width:document.documentElement.clientWidth,height:document.documentElement.clientHeight,
        deviceScaleFactor:window.devicePixelRatio}}''')

        # 打印页面尺寸、设备像素比等信息
        print(dimensions)
    finally:
        # 关闭浏览器对象，释放资源
        await browser.close()


# 运行主函数
asyncio.get_event_loop().run_until_complete(main())

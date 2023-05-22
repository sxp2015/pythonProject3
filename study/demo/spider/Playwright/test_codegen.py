#  在终端输入 playwright codegen -o script.py -b chromium 可实现录制操作生成代码
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.baidu.com/")
    page.locator("#kw").click()
    page.locator("#kw").press("CapsLock")
    page.locator("#kw").fill("NBA")
    page.locator("#kw").press("CapsLock")
    page.locator("#kw").press("Enter")
    page.goto("https://www.baidu.com/s?rsv_idx=1&wd=nba%E8%B5%9B%E7%A8%8B&fenlei=256&usm=1&ie=utf-8&base_query=NBA&tag_key=%E8%B5%9B%E7%A8%8B&rsv_dl=re_dl_tag_2&rsv_pq=b3e681510001a447&oq=NBA&rsv_t=7f1fz4gO8SdM5SDPaQgAqLgzNU1hIUKzuDhyJks06p9JJV%2B8yCzLRYUdHFc")
    page.goto("https://www.baidu.com/s?rsv_idx=1&wd=nba%E8%85%BE%E8%AE%AF&fenlei=256&usm=1&ie=utf-8&base_query=NBA&tag_key=%E8%85%BE%E8%AE%AF&rsv_dl=re_dl_tag_8&rsv_pq=b3e681510001a447&oq=NBA&rsv_t=9408T5L%2BY6Y3bX1Zpg2L6zuVAr1tld1aOO5fR%2FAhlcfGJ6JlOopxwmKt3Ck")
    page.get_by_role("link", name="全部").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

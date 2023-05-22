from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://spa6.scrape.center/')
    page.wait_for_load_state('networkidle')
    # page.fill('#sb_form_q', '爬虫开发')
    href = page.get_attribute('a.name', 'href')
    elements = page.query_selector_all('a.name')

    print('单个href:', href)

    print('========================')
    for index, element in enumerate(elements):
        print(f'第{index + 1}个：href属性是：{element.get_attribute("href")}，值是：{element.text_content()}')
    browser.close()

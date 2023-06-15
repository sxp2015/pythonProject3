from selenium import webdriver
proxy = "180.183.230.16:8080"
# proxy = "10.10.105.60:8080"
options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=http://%s' % proxy)
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://httpbin.org/get")
print(driver.page_source)
driver.quit()
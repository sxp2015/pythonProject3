# Scrapy settings for scrapysplashdemo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "scrapysplashdemo"

SPIDER_MODULES = ["scrapysplashdemo.spiders"]
NEWSPIDER_MODULE = "scrapysplashdemo.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "scrapysplashdemo (+http://www.yourdomain.com)"

# Obey robots.txt rules 是否遵从robots中的协议
ROBOTSTXT_OBEY = False

# Configure 更换Twister的Reactor 对象
# 定义了PyppeteerMiddleware之后，我们无须额外声明TWISTED REACTOR，可以把刚才TWISTED REACTOR的定义去掉。
# TWISTER_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
# 限制并发数
CONCURRENT_REQUESTS = 3

# 配置请求方式为无头模式,即没有User-Agent，不建议开启，因为我们要模拟成正常浏览器
GERAPY_PYPPETEER_HEADLESS = False
# 如果Splash 是在远程服务器运行的，那么此处就应该配置为远程的地址

# 忽略加载资源类型
# Pyppteer可以自定义忽略特定的资源类型的加载，比如忽略图片文件、字体文件的加载，这样做可以大大提高爬取效率，常见类型如下
# 比如我们想要在爬取过程中忽略图片、字体文件的加载，可以进行如下配置:
GERAPY_PYPPETEER_IGNORE_RESOURCE_TYPES = ['image', 'font']
# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "scrapysplashdemo.middlewares.ScrapysplashdemoSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 定义了PyppeteerMiddleware之后，我们无须额外声明TWISTED REACTOR，可以把刚才TWISTED REACTOR的定义去掉。
    # "scrapysplashdemo.middlewares.ScrapysplashdemoDownloaderMiddleware": 543,
    "scrapysplashdemo.middlewares.PyppeteerMiddleware": 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    "scrapysplashdemo.pipelines.ScrapysplashdemoPipeline": 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

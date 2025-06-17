# Scrapy settings for Nike project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "Demo"

SPIDER_MODULES = ["Demo.spiders"]
NEWSPIDER_MODULE = "Demo.spiders"

ADDONS = {}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "Nike (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en,en-GB;q=0.9,en-US;q=0.8,zh-CN;q=0.7,zh;q=0.6',
    'cache-control': 'max-age=0',
    'if-none-match': '"7f722-1x332fOyY6WkfKYb80L9QTAnt1o"',
    'priority': 'u=0, i',
    'referer': 'https://www.nike.com.cn/w/',
    'sec-ch-ua': '"Microsoft Edge";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-full-version-list': '"Microsoft Edge";v="137.0.3296.68", "Chromium";v="137.0.7151.69", "Not/A)Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0',
    # 'cookie': 'geoloc=cc=CN; sajssdk_2015_cross_new_user=1; anonymousId=DSWX092BF0B906D9ED416BC37EAACD002AC2; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22DSWX092BF0B906D9ED416BC37EAACD002AC2%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwx.mail.qq.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk3NzY3Njk5NDcxOWE5LTBkMzhhZDlkZDA2MWMzOC00YzY1N2I1OC0yMDczNjAwLTE5Nzc2NzY5OTQ4MjI5MiJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%221977676994719a9-0d38ad9dd061c38-4c657b58-2073600-197767699482292%22%7D; cdn_sec_tc=78ddde0217500643095932315ee1a994e730f81c5f8554239b75e66a31; acw_tc=1a0c63a417500643096854943e006391a74b722261bfa5a8bef92ac9607a75; ppd=pdp|nikecom>pdp>nike%20dri-fit%20club; sensorsdata2015jssdksession=%7B%22session_id%22%3A%2219777f62e30b6209f802cf301c184c657b58207360019777f62e312a6f%22%2C%22first_session_time%22%3A1750064311855%2C%22latest_session_time%22%3A1750065662821%7D; tfstk=gfYo-2m-R3SSJgMADE_SbQRh0emYPa_B8pUdpwBE0tWbe8UJTH0HUdjeyadJm9vchyBrdM3HodvuJgkWpyShHOx74bmPgrYd13-7zbbfcOL343lz4rVVOOvhAb6dL9vpT3hxWVdWNw_U-A3tWcoVSOJhaMzzgX5117lA4G-Jw6QEBA3vsseQZwJdFmNtiIWft6rzzpS43_B4LkJFUiyVs1_F8pSFus5hakyFUgzqi66VLw7eLIlc9tWEKmzFIe8XuxphHlXG1aTcZgXwimaU-xC8B9OPnyzFE6soMQW08y8DxhKYGTo_M9_RFefkdVa5zMx696vorzJH1E9cgdu3WTRX6hIWzDUOjZXlvUJnKkfkXLvCUQyz41blEG8Pc7lDiM-DoaLrdlOviTSGknnjeMQkEh614mMXKIXJLUj4ExBpXILPmdkYopsHfBCHE44yQg-30lPzDy1q9ErQAg5fiOdrh_GHmN2EQjc0f0sPG_HtijqQAg5fiOhmilw54s1-B; ssxmod_itna=YqfxnDu7K7TqzOD2lmGkYD7RQby7prl7xmqTPDsbwDpxB9qidKDBmZQmamakpfxrpbSFcdufbbKmfnhWY2rx0aDbMP+xg0xYYDtxBYDQxAYDGDDPXDj4ibDYf=HDj7I=CgIxy4GrDzqDgD7jFQqDEDG3D0RQqBYqueqG0DDtDAuN3cqDADAfnRDDl97wxfhjQDYPuzL3DkridrB=om0QDjqGgDBd49Pb3gcyQfM6OL=cWDuNVDBQD7L09zriDCo6M+wLWu2GWK0G502n5Y7PemAIbCex5RODviAK1Kxxno+DdbHd3mbl=piKAi6fGDD=; ssxmod_itna2=YqfxnDu7K7TqzOD2lmGkYD7RQby7prl7xmqqikA3DloEW4j4xDte2qOYPjQ2D6CwxLkVjek7rqYO6lyRmDhbW3u+yj08DioBCpxAjbjtKQFF8DXrGCchbS/mEjsku3OLgyPr0W+uEm05ZCO0/K806K0PSUr+QCroVSTUyACLy+qTFALLht4jADdL+ljE74cPUlqaVbuGbmxXxR4jsSb49+LL8H6ykwOQkM4xFj1LdQKA=xUtICUbFmMvqpIRfv9tLL+=A=p8G0/RvuwgLsIRXuqkvSdLjrsgvkVgV70F8QDQ80T8oAMYM0sL8rtqQPq7GEGMRdojh1rhqe7djabiODqhilhaCGG2DbjdWQatQw6fmTjw20+Gq7ZuhWeptlwtCp8CIQjk8eI1gI6bmxT8gh7EjmzQpMCww8ktkDcjasC7uYpVfdwgpnDPD7j5ph2D5a/vnGGMERClP08D2b9diqHGL0Kw24KllIg4Hg49PZaBm9BU9xn95aFdmKK74aSDY6H8aBqs+u+54wmqVY1hdKNOOe4FGGgRGCewntHemX+hDCZONbwZ2DDjKDedq4D=',
}


# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "Nike.middlewares.DemoSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "Nike.middlewares.DemoDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "Demo.pipelines.DemoPipeline": 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
FEED_EXPORT_ENCODING = "utf-8"

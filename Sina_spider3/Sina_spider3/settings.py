# encoding=utf-8
# ------------------------------------------
#   版本：3.0
#   日期：2016-12-01
#   作者：九茶<http://blog.csdn.net/bone_ace>
# ------------------------------------------

BOT_NAME = ['Sina_spider3']

SPIDER_MODULES = ['Sina_spider3.spiders']
NEWSPIDER_MODULE = 'Sina_spider3.spiders'

DOWNLOADER_MIDDLEWARES = {
    "Sina_spider3.middleware.UserAgentLoginMiddleware": 401,     #模拟登录用这个
    # "Sina_spider3.middleware.UserAgentNoLoginMiddleware": 401,   #不登录时用这个
    "Sina_spider3.middleware.CookiesMiddleware": 402,
    # "Sina_spider3.middleware.ProxyMiddleware": 543,
}
ITEM_PIPELINES = {
    "Sina_spider3.pipelines.MongoDBPipeline": 403,
}

SCHEDULER = 'Sina_spider3.scrapy_redis.scheduler.Scheduler'
SCHEDULER_PERSIST = True
SCHEDULER_QUEUE_CLASS = 'Sina_spider3.scrapy_redis.queue.SpiderSimpleQueue'

# 种子队列的信息
REDIS_URL = None
REDIS_HOST = '172.20.10.9'
REDIS_PORT = 6379

# 去重队列的信息
FILTER_URL = None
FILTER_HOST = '172.20.10.9'
FILTER_PORT = 6379
FILTER_DB = 0

#IP代理池
PROXIES=[]

DOWNLOAD_DELAY = 1  # 间隔时间
# LOG_LEVEL = 'INFO'  # 日志级别
CONCURRENT_REQUESTS = 4  # 默认为16
# CONCURRENT_ITEMS = 1
# CONCURRENT_REQUESTS_PER_IP = 1
REDIRECT_ENABLED = False

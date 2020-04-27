# -*- coding: utf-8 -*-

# Scrapy settings for download_cases project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'download_cases'

SPIDER_MODULES = ['download_cases.spiders']
NEWSPIDER_MODULE = 'download_cases.spiders'


# Obey robots.txt rules
ROBOTSTXT_OBEY = True


# Crawlera
DOWNLOADER_MIDDLEWARES = {'scrapy_crawlera.CrawleraMiddleware': 300}
CRAWLERA_ENABLED = True
CRAWLERA_APIKEY = '...'
CONCURRENT_REQUESTS = 32
CONCURRENT_REQUESTS_PER_DOMAIN = 32
AUTOTHROTTLE_ENABLED = False
DOWNLOAD_TIMEOUT = 600


ITEM_PIPELINES = {
    'scrapy.pipelines.files.FilesPipeline': 500
}
FILES_STORE = 'gs://.../'
IMAGES_STORE = 'gs://.../'
GCS_PROJECT_ID = "..."

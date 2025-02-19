from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

BOT_NAME = 'indeed'

SPIDER_MODULES = ['indeed.spiders']
NEWSPIDER_MODULE = 'indeed.spiders'


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

## ScrapeOps API Key
SCRAPEOPS_API_KEY = os.getenv('SCRAPEOPS_API_KEY')

## ScrapeOps Coutnry Code
SCRAPEOPS_PROXY_SETTINGS = {'country': 'us'}

## Enable ScrapeOps Proxy
SCRAPEOPS_PROXY_ENABLED = True

# Add In The ScrapeOps Monitoring Extension
EXTENSIONS = {
'scrapeops_scrapy.extension.ScrapeOpsMonitor': 500, 
}


DOWNLOADER_MIDDLEWARES = {
    'scrapeops_scrapy.middleware.retry.RetryMiddleware': 550,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
}


CONCURRENT_REQUESTS = 1

# Add these settings
DOWNLOAD_DELAY = 2  # 2 seconds delay between requests
RANDOMIZE_DOWNLOAD_DELAY = True
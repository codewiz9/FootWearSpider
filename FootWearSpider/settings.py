
BOT_NAME = "FootWearSpider"
SPIDER_MODULES = ["FootWearSpider.spiders"]
NEWSPIDER_MODULE = "FootWearSpider.spiders"
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

SCRAPEOPS_API_KEY = '82871d8b-d8f0-462a-879d-cef5beed14cb' 
SCRAPEOPS_PROXY_ENABLED = True

DOWNLOADER_MIDDLEWARES = {
    'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
}


# FEEDS = {
#     'test_data.csv': {'format': 'csv'},
# 

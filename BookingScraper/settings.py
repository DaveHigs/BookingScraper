BOT_NAME = "BookingScraper"

SPIDER_MODULES = ["BookingScraper.spiders"]
NEWSPIDER_MODULE = "BookingScraper.spiders"

# Browser-like user agent to avoid detection
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configures a delay for requests
DOWNLOAD_DELAY = 2

# Disables cookies
COOKIES_ENABLED = False

# Enable or disable spider middlewares
SPIDER_MIDDLEWARES = {}

# Enable or disable downloader middlewares
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 100
}

# Configure item pipelines
#ITEM_PIPELINES = {
#    "BookingScraper.pipelines.BookingscraperPipeline": 300,
#}

# Set settings whose default value is deprecated to a future-proof value
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

# Enables Retry middleware
RETRY_ENABLED = True

# Retry on HTTP error codes
RETRY_HTTP_CODES = [403, 429]

# Number of times to retry
RETRY_TIMES = 3
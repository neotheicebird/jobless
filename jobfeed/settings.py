# Scrapy settings for jobfeed project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'jobfeed'

SPIDER_MODULES = ['jobfeed.spiders']
NEWSPIDER_MODULE = 'jobfeed.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'jobfeed (+http://www.yourdomain.com)'

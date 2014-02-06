# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class JobFeedItem(Item):
    # define the fields for your item here like:
    # name = Field()
    title = Field()
    description = Field()
    link = Field()
    posted = Field() # e.g data - posted 33 minutes ago
    ends = Field() # e,g data - Ends 2d 12h 33m
    price = Field() # expected price like Hourly Rate: 15$/h
                    # or Fixed Price: less than 500$

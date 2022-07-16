# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GeeksItem(scrapy.Item):
    # Item key for Title of Quote
    quotetitle = scrapy.Field()
     
    # Item key for Author of Quote
    author = scrapy.Field()
     
    # Item key for Tags of Quote
    tags = scrapy.Field()
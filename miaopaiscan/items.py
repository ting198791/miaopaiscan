# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MiaopaiscanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    videohref = scrapy.Field()
    look=scrapy.Field()
    like=scrapy.Field()
    commen=scrapy.Field()
    suid=scrapy.Field()
    videoabout=scrapy.Field()
    date=scrapy.Field()


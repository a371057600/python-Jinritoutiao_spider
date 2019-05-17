# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JinritoutiaoSpiderItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    article1 = scrapy.Field()
    img = scrapy.Field()


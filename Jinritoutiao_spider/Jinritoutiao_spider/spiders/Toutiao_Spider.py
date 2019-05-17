# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import datetime

import re
import time

class ToutiaoSpiderSpider(CrawlSpider):
    name = 'Toutiao_Spider'
    allowed_domains = ['toutiao.com', '']
    start_urls = ['https://www.toutiao.com/ch/news_tech/']
    rules = (
        Rule(LinkExtractor(allow=r'.*/group/[0-9a-z]{19}/$'), callback='parse_detail', follow=False),
    )

    def parse_detail(self, response):
        article = response.xpath("//div[@class='article-box']")
        article1 = response.xpath("//div[@class='article-box']").get()

        title = article.xpath("//h1//text()").get()
        content = response.xpath("//div[@class='article-box']/div[@class='article-content']").getall()
        image = article.xpath("//div[@class='article-box']/div[@class='article-content']//img/@src").getall()
        pdtime ="2019-3-16"


        item = {
                'title': title,
                'content': content,
                'img': image,
                'pdtime': pdtime,
                'author': 1,
                'type': 2,
            'article1':article1

            }
        yield item




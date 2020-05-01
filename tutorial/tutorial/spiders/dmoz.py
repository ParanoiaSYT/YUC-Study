# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import DmozItem


class DmozSpider(scrapy.Spider):
    name = 'dmoz'
    allowed_domains = ['dmoztools.net']
    start_urls = ['http://dmoztools.net/Computers/Programming/Languages/Python/Books/',
                  'http://dmoztools.net/Computers/Programming/Languages/Python/Resources/']

    def parse(self, response):
        sel=scrapy.selector.Selector(response)
        sites=sel.xpath('//*[@id="site-list-content"]/div')
        items=[]
        for site in sites:
            item=DmozItem()
            item['title']=site.xpath('div/a/div/text()').extract()
            item['link']=site.xpath('div[3]/a/@href').extract()
            item['desc']=site.xpath('div/div/text()').extract()
            items.append(item)

        return items

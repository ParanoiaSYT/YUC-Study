# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from sepics.items import SepicsItem
import time


class ShangseSpider(scrapy.Spider):
    name = 'shangse'
    # allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://mp.weixin.qq.com/s/OxW3GIbwMfrpNZPnrMdFNQ']
    def parse(self, response):
        soup=BeautifulSoup(response.text,"lxml")
        pics_list = soup.find_all('img', class_='')
        # print(pics_list)
        for i in range(len(pics_list)):
            item=SepicsItem()
            try:
                link=pics_list[i]['data-src']
                item['link'] = [link]
                # yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)
                yield item
            except:
                print('出错了')

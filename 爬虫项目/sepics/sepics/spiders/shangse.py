# -*- coding: utf-8 -*-
import scrapy
from sepics.items import SepicsItem
from bs4 import BeautifulSoup

class ShangseSpider(scrapy.Spider):
    name = 'shangse'
    allowed_domains = ['mp.weixin.qq.com']
    start_urls = ['https://mp.weixin.qq.com/s/OxW3GIbwMfrpNZPnrMdFNQ']

    def parse(self, response):
        item=SepicsItem()
        soup=BeautifulSoup(response.text,"lxml")
        url_list = soup.find_all('img', class_='')
        for i in range(len(url_list)):
            try:
                link=url_list[i]['data-src']
                print(link)
                print('=======================')
                item['link'] = [link]
                # 图片要加上中括号
                yield item
            except:
                pass

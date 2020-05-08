# -*- coding: utf-8 -*-
import scrapy
from Finance.items import FinanceItem
from bs4 import BeautifulSoup
import time

class FinanceSpider(scrapy.Spider):
    name = 'finance'
    allowed_domains = ['finance.eastmoney.com']
    start_urls = ['http://finance.eastmoney.com/news/cywjh.html']
    url1='http://finance.eastmoney.com/news/cywjh_'
    url3='.html'
    def start_requests(self):
        for i in range(1,4):
            url=self.url1+str(i)+self.url3
            print("当前页码为：%s"%url)
            yield scrapy.Request(url=url,callback=self.parse)
    def parse(self, response):
        soup=BeautifulSoup(response.text,"lxml")
        title_list=soup.find_all('p',class_='title')
        for i in range(len(title_list)):
            item=FinanceItem()
            item['title']=title_list[i].a.text.strip()
            link=title_list[i].a['href']
            item['link']=link
            yield scrapy.Request(url=link,meta={'item':item},callback=self.parse2)
    def parse2(self,response):
        item=response.meta['item']
        soup=BeautifulSoup(response.text,"lxml")
        content=soup.find('div',id="ContentBody").text.strip().replace('\n','')
        item['content']=content
        time.sleep(2)
        yield item



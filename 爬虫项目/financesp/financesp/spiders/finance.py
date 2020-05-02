# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from financesp.items import FinancespItem
import time

class FinanceSpider(scrapy.Spider):
    name = 'finance'
    allowed_domains = ['finance.eastmoney.com']             #特别注意⚠️：这里不能加http://
    start_urls = ['http://finance.eastmoney.com/news/cywjh_1.html']
    
    link1='http://finance.eastmoney.com/news/cywjh_'
    link3='.html'

    # 实现获取翻页，再调用实现获取各个内容(这个函数为scrapy自带功能）
    def start_requests(self):
        for i in range(1,4):
            url=self.link1+str(i)+self.link3
            print('当前页面地址为：%s'%url)

            #发生request请求,调用parse()
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        soup=BeautifulSoup(response.text,"lxml")

        title_list=soup.find_all('p',class_="title")

        for j in range(len(title_list)):
            item=FinancespItem()

            title=title_list[j].a.text.strip()
            link=title_list[j].a['href']
            item['title']=title
            item['link']=link

            yield scrapy.Request(url=link,meta={'item':item},callback=self.parse2)

    #item传递，进行深一步操作再返回

    def parse2(self,response):
        item=response.meta['item']
        soup=BeautifulSoup(response.text,"lxml")
        content=soup.find('div',id="ContentBody").text.strip().replace('\n','')

        item['content']=content

        yield item


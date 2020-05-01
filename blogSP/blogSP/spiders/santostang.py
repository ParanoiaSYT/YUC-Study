# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from blogSP.items import BlogspItem


class SantostangSpider(scrapy.Spider):
    name = 'santostang'
    allowed_domains = ['www.santostang.com']
    start_urls = ['http://www.santostang.com/']

    def parse(self, response):
        soup=BeautifulSoup(response.text,"lxml")
        first_title=soup.find('h1',class_="post-title").a.text.strip()
        print(first_title)

        title_list=soup.find_all('h1',class_="post-title")
        items=[]
        for i in range(len(title_list)):
            item=BlogspItem()
            title=title_list[i].a.text.strip()
            link=title_list[i].a['href']
            item['title']=title
            item['link']=link

            yield scrapy.Request(url=link,meta={'item':item},callback=self.parse2)

    # 使用meta传递item参数
    # 通过yield生成器+回调函数来并行处理文章内容

        #下面打开的网页是上面每一个得到的link
    def parse2(self,response):
        item=response.meta['item']
        soup=BeautifulSoup(response.text,"lxml")
        content=soup.find('div',class_="view-content").text.strip().replace('\n','')

        item['content']=content

        yield item

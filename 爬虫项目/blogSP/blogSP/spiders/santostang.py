# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from blogSP.items import BlogspItem

class SantostangSpider(scrapy.Spider):
    name = 'santostang'
    allowed_domains = ['www.santostang.com']
    start_urls = ['http://www.santostang.com/']

    def parse(self, response):
        # print(response.text)
        filename="index.html"
        with open(filename,'w')as f:
            f.write(response.text)

        soup=BeautifulSoup(response.text,"lxml")
        first_title=soup.find("h1",class_="post-title").a.text.strip()
        print(first_title)

        title_list=soup.find_all("h1",class_="post-title")
        for i in range(len(title_list)):
            item=BlogspItem()
            title=title_list[i].a.text.strip()
            item["title"]=title
            link=title_list[i].a['href']
            item['link']=link
            print("第%s篇标题为：%s"%(str(i+1),title))

            yield scrapy.Request(url=link,meta={'item':item},callback=self.parse2)

    def parse2(self,response):
            # 接受传过来的item
            item=response.meta['item']
            # 解析子网页link(和上面差不多）
            soup=BeautifulSoup(response.text,"lxml")
            content=soup.find("div",class_="view-content").text.strip().replace('\n','')
            item['content']=content
            yield item


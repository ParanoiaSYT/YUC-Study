# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class FinancePipeline(object):

    file_path='/Users/sunyuting/YuC-Study/爬虫项目/Finance/result.txt'

    def __init__(self):
        self.article=open(self.file_path,'w')

    def process_item(self, item, spider):
        title=item['title']
        link=item['link']
        content=item['content']
        output=title+'\t'+link+'\n'+content+'\n'
        self.article.write(output)

        return item

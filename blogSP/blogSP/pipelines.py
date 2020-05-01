# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class BlogspPipeline(object):
    file_path="/Users/sunyuting/YuC-Study/blogSP/result.txt"
    
    def __init__(self):
        self.article=open(self.file_path,'w',encoding='utf-8')
      
    def process_item(self, item, spider):
        title=item["title"]
        link=item["link"]
        content=item["content"]
        output=title+'\t'+link+'\n'+content+'\n'
        self.article.write(output)
        return item

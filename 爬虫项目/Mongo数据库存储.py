from  pymongo import MongoClient
from bs4 import BeautifulSoup
import requests
import datetime

client=MongoClient('localhost',27017)
db=client.blog_database
collection=db.blog

link="http://www.santostang.com/"
headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
r=requests.get(link,headers=headers)
html=r.text

soup=BeautifulSoup(html,"lxml")
title_list=soup.find_all("h1",class_="post-title")
for each_title in title_list:
    url1=each_title.a["href"]
    title=each_title.a.text
    post={"url":url1,"title":title,"date":datetime.datetime.utcnow()}       #utcnow()：读取的时间一直都是系统的“世界标准时间”，不管系统的本地时区是否设置，读取的时间不会随这些设置变化
    collection.insert_one(post)

print(datetime.datetime.utcnow())       #UTC时间
print(datetime.datetime.utcnow().astimezone())      #返回任何地区时间
print(datetime.datetime.today())        #返回当前时区时间
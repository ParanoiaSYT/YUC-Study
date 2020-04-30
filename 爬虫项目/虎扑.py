# 所有帖子:ul for-list  li
# name:div titlelink box a
# author:div author box a[href]
# 时间:div author box
# .............

import requests
from bs4 import BeautifulSoup
import datetime
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
import time

def get_page(link):
    headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
    r=requests.get(link,headers=headers)
    html=r.content
    html=html.decode('utf-8')
    soup=BeautifulSoup(html,"lxml")
    return soup

def get_data(post_list):
    data_list=[]
    for post in post_list:
        title=post.find('div',class_="titlelink box").a.text.strip()
        author=post.find('div',class_="author box").a.text.strip()
        postlink=post.find('div',class_="author box").a["href"]

        data_list.append([title,author,postlink])
        # time.sleep(3)
    return data_list


link="https://bbs.hupu.com/bxj"
soup=get_page(link)
post_all=soup.find("ul",class_="for-list")
post_list=post_all.find_all('li')           #find()查找第一个匹配结果出现的地方，find_all()找到所有匹配结果出现的地方。
data_list=get_data(post_list)
for each in data_list:
    print(each)

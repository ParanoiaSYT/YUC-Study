import requests
from bs4 import BeautifulSoup
import datetime
import time
from mongoapi import MongoAPI   #自制模块里

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
        title=post.find('div',class_="titlelink box").text.strip()        #class是python的保留关键字，所以无法使用class这个关键字。
        title=title.replace('\xa0','').replace('\n','')                   #strip()只能去除两端的空格，中间的空格用replace去可以

        site = post.find('div', class_="titlelink box").a["href"]
        site='http://bbs.hupu.com'+site
        author=post.find('div',class_="author box").a.text.strip()
        postlink=post.find('div',class_="author box").a["href"]
        posttime=post.find('div',class_="author box").contents[5].text           #contents表示从'div',class_="author box"标签开始，html代码形式标签之间的内容，⚠️回车号也占一个位置，[0]是回车，[1]是作者...[5]是时间

        reply_view=post.find('span',class_="ansour box").text.strip()
        (reply,view)=reply_view.split('/',1)
        reply=reply.strip()
        view=view.strip()

        last_reply=post.find('span',class_="endauthor").text.strip()
        # last_reply=post.find('div',class_="endreply box").span.text.strip()       #这样也可

        last_time=post.find('div',class_="endreply box").a.text.strip()
        if ':'in last_time:
            date_time=str(datetime.date.today())+' '+last_time
            date_time=datetime.datetime.strptime(date_time,'%Y-%m-%d %H:%M')
        elif last_time.find('-')==4:
            date_time=datetime.datetime.strptime(last_time,'%Y-%m-%d').date()
        else:
            date_time=str(datetime.date.today().year)+'-'+last_time
            date_time=datetime.datetime.strptime(date_time,'%Y-%m-%d').date()

        data_list.append([title,site,author,posttime,postlink,reply,view,last_reply,date_time])     #date_time不是str形式
    return data_list


link1="https://bbs.hupu.com/bxj-"
for i in range(1,11):                           #虎扑步行街第十一页就要登陆了
    link=link1+str(i)
    soup=get_page(link)
    post_all=soup.find("ul",class_="for-list")
    post_list=post_all.find_all('li')           #find()查找第一个匹配结果出现的地方，find_all()找到所有匹配结果出现的地方。
    data_list=get_data(post_list)

    hupu_post=MongoAPI("localhost",27017,"hupu","post")
    for each in data_list:
        hupu_post.update({'帖子链接:':each[1]},{'帖子名:':each[0],'帖子链接:':each[1],'作者:':each[2],'发帖时间:':each[3],'作者主页:':each[4],'回复数:':each[5],'浏览量:':each[6],'最新回复:':each[7],'最新回复时间':str(each[8])})
        # print(each)
    time.sleep(3)   #3秒一页
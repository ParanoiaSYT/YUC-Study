import pymysql
import requests
from bs4 import BeautifulSoup

db=pymysql.connect("localhost","root","password","scraping")       #注意⚠️这里的password要改成自己的密码
# 打开数据库连接
cursor =db.cursor()     #cursor()方法获取操作游标（通过游标cur操作execute()来写入SQL语句）

# sql="insert into urls(url,content) values('www.baidu.com','Some content.')" #插入语句
# try:
#     cursor.execute(sql)     #执行语句
#     db.commit()             #提交
# except:
#     db.rollback()           #出错则回滚
# db.close()
# # 关闭数据库连接

link="http://www.santostang.com"
headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}
r=requests.get(link,headers=headers)
html=r.text
soup=BeautifulSoup(html,"lxml")

title_list=soup.find_all("h1",class_="post-title")
for title in title_list:
    content=title.a.text.strip()        # 获取html的a标签的信息(soup.a默认获取第一个a标签，想获取全部就用for循环去遍历)
    print(content.strip())
    url2=title.a["href"].strip()
    print(title.a["href"].strip())      #应该就是获取a标签的href内容

    try:
        cursor.execute("insert into urls(url,content) values(%s,%s)",(url2,content))
    except:
        db.rollback()

db.commit()
db.close()

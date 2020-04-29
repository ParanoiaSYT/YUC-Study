import requests
from bs4 import BeautifulSoup

link="http://www.santostang.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}

r=requests.get(link,headers=headers)
html=r.text

soup=BeautifulSoup(html,"lxml")

# first_title=soup.find("h1",class_="post-title").text
# print(first_title)
# print(type(first_title))

title_list=soup.find_all("h1",class_="post-title")
# print(type(title_list))
# print(title_list)        #这里包含一些html里的乱七八糟字符

for i in range(len(title_list)):
    title=title_list[i].text        #在.text后，乱七八糟的被自动去除了
    print("第%d个标题为：%s"%(i+1,title))
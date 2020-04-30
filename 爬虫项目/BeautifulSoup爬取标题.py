import requests
from bs4 import BeautifulSoup

link="http://www.santostang.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}

r=requests.get(link,headers=headers)
html=r.text

soup=BeautifulSoup(html,"lxml")     #将代码转化为BeautifSoup对象，采用"lxml"解析器

# first_title=soup.find("h1",class_="post-title").text
# print(first_title)
# print(type(first_title))

title_list=soup.find_all("h1",class_="post-title")      #找<h1>元素，class为"post-title"
# print(type(title_list))
# print(title_list)        #这里包含一些html里的乱七八糟字符

for i in range(len(title_list)):
    title=title_list[i].text        #加上.text后，提取元素中的文字
    print("第%d个标题为：%s"%(i+1,title))

#################################################################################

# print(soup)
# print(soup.prettify())    #看起来美化一点，效果不行

# 遍历文档数（不常用）
# print(soup.header.h1)       #获取h1标签
# print(soup.header.div.contents)

# 搜索文档数(可配合正则表达式）
import re
soup=BeautifulSoup(html,"lxml")     #将代码转化为BeautifSoup对象，采用"lxml"解析器
result=re.compile(r"^h")        #以h开头的(这里和正则找内容不一样,这里搜索文档是找位置)
for tag in soup.find_all(result,class_="post-title"):   #soup已经对html解析过了
    # print(tag)
    print(tag.name)
    print(tag.text)

# CSS选择器
# 遍历文档树
print(soup.select("header h1"))     #获得div下所有的h1标签
print(soup.select("header > h1"))   #获得div下所有的h1标签(子标签遍历）
print(soup.select("div>a"))     #获得div 下所有的<a>标签

print("==================================")
# 搜索文档树
print(soup.select('a[href^="http://www.santostang.com/"]'))    #找所有链接以http://www.santostang.com/开始的a标签

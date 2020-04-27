#urllib.requeat
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# SSL证书验证错误，当请求一个https站点，但是证书验证错误时，就会报这样的错误。

import urllib.request
response=urllib.request.urlopen("http://www.fishc.com")
print(response)             #返回的是一个HTTPResponse的实例对象，它属于http.client模块。

print(response.geturl())
print(response.info())
print(response.getcode())       #http的状态码，200表示正常响应，404表示页面不见

html=response.read()
html=html.decode('utf-8')
print(html)
print('===========================================')
#053作业
# 打印网页前300字
# import urllib.request
#
# response=urllib.request.urlopen('http://www.fishc.com')
# html=response.read(300)
# html=html.decode('utf-8')       #没有这句就是乱码
# print(html)

# 敏感内容爬虫协议
# 在网站的根目录下创建并编辑 robots.txt 文件，用于表明您不希望搜索引擎抓取工具访问您网站上的哪些内容。
# 此文件使用的是 Robots 排除标准，该标准是一项协议，所有正规搜索引擎的蜘蛛均会遵循该协议爬取。既然是协议，那就是需要大家自觉尊重，所以该协议一般对非法爬虫无效。

print('===========================================')
# 检测指定 URL 的编码
# import urllib.request
# import chardet
#
# temp=input('请输入URL:')
# response=urllib.request.urlopen(temp)
# html=response.read()
# bm=chardet.detect(html)
# print('该网页使用的编码是：%s'%bm)

print('===========================================')
# 依次访问文件中指定的站点，并将每个站点返回的内容依次存放到不同的文件中
def urlop(temp):
    response = urllib.request.urlopen(temp)
    html = response.read()

def save(content,num):
    with open('/Users/sunyuting/YuC-Study/爬虫项目/url%d.txt'%num,'w')as f:
        f.write(content)

list1=[]
with open('/Users/sunyuting/YuC-Study/爬虫项目/urls.txt')as f:
    for each_line in f:
        list1.append(each_line)

count=0
while count<len(list1):
    temp=list1[count]
    urlop(temp)
    count+=1
    save(html,count)
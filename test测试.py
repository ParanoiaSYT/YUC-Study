import requests
import datetime
from bs4 import BeautifulSoup


link='http://www.santostang.com/'
headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}

r=requests.get(link,headers=headers,timeout=10)

soup=BeautifulSoup(r.text,"lxml")
content = soup.find('div', class_="post-content clearfix").get_text().strip().replace('\n','')
print(type(content))
print(content)



# print('文本编码：',r.encoding)
# print('响应状态码：',r.status_code)
# print('字符串方式的响应体：',r.text)



t=datetime.datetime.utcnow()    #返回UTC时间
print(datetime.datetime.today())
print(t)
print(datetime.datetime.utcnow())
print(t.astimezone())       #把时间返回出来（任何地区）


print(datetime.date.today())
print(datetime.date.today().year)

c=datetime.datetime.today()
print(c)
# c = datetime.datetime.strptime(str(c),'%Y-%m-%d %H:%M')
print(c)
c=datetime.date.today()
c = datetime.datetime.strptime(str(c),'%Y-%m-%d').date()
print(c)



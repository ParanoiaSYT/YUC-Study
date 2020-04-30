import requests
from lxml import etree

link="http://www.santostang.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}

r=requests.get(link,headers=headers)

html=etree.HTML(r.text)     #先要解析成lxml格式

for i in range(1,5):
    title_list=(html.xpath('//*[@id="main"]/div/div[1]/article[%d]/header/h1/a'%i))
# xpth通过Chrome审查的话只能定位到一个标题,还要找到规律加个for循环才行
    print(title_list[0].text)


import requests
import json

link='https://api-zero.livere.com/v1/comments/list?callback=jQuery112408442961859649811_1588002687827&limit=10&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&code=&_=1588002687829'
headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}

r=requests.get(link,headers=headers,timeout=10)
print(r.text)

json_string=r.text
json_string=json_string[json_string.find('{'):-2]       #json格式的内容从第一个大括号开始，结束于最后末尾的大括号（要去掉r.text最后的小括号和分号）

target0=json.loads(json_string)
print('=================================================')
print(target0)
target=target0['results']['parents']
print('=================================================')

for each in target:
    message=each['content']
    print(message)

# 'https://api-zero.livere.com/v1/comments/list?callback=jQuery1124008442833829323093_1588002896757&limit=10&offset=2&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&code=&_=1588002896764'
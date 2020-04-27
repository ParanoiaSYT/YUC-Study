import urllib.request
import urllib.parse
import json

content=input('请输入需要翻译的内容：')

url1="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
data={}
data['i']=content
data['from']= 'AUTO'
data['to']='AUTO'
data['smartresult']='dict'
data['client']='fanyideskweb'
data['salt']='15879572649271'
data['sign']='443ed89d58508ff8cddb7539eada89f4'
data['ts']='1587957264927'
data['bv']='736128d4eb7d527718d5b79ac5369080'
data['doctype']='json'
data['version']='2.1'
data['keyfrom']= 'fanyi.web'
data['action']= 'FY_BY_REALTlME'

data=urllib.parse.urlencode(data).encode('utf-8')       #把Unicode文件格式转化为utf-8编码形式

response=urllib.request.urlopen(url1,data)
html=response.read().decode('utf-8')        #utf-8解码成Unicode格式

# print(html)

#json结构，字符串封装
# import json
target=json.loads(html)
# print(type(target))
# print(target["translateResult"])
print('翻译结果为：%s'%target["translateResult"][0][0]['tgt'])

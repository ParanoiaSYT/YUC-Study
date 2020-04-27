import urllib.request
import urllib.parse
import json
import time

while True:
    content=input('请输入需要翻译的内容(输入q/Q退出程序）：')
    if content == 'Q'or 'q':
        break
    url1="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

    head={}
    head['User-Agent']='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'

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

    #utf-8是Unicode编码的一种
    data=urllib.parse.urlencode(data).encode('utf-8')       #把Unicode文件格式转化为utf-8编码形式
    # urlopen 函数有一个 data 参数，如果给这个参数赋值，那么 HTTP 的请求就是使用 POST 方式；
    # 如果 data 的值是 NULL，也就是默认值，那么 HTTP 的请求就是使用 GET 方式

    req=urllib.request.Request(url1,data,head)
    response=urllib.request.urlopen(req)

    # response=urllib.request.urlopen(url1,data)      #这一句就等于上面两句
    html=response.read().decode('utf-8')        #utf-8解码成Unicode格式
    # print(html)

    print(req.headers)

    #json结构，字符串封装
    # JSON 是一种轻量级的数据交换格式，说白了这里就是用字符串把Python的数据结构封装起来，便与存储和使用。
    # import json
    target=json.loads(html)
    # print(type(target))
    # print(target["translateResult"])
    print('翻译结果为：%s'%target["translateResult"][0][0]['tgt'])
    time.sleep(5)       #等5秒
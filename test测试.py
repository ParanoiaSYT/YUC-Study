import requests

link='http://www.santostang.com/'
headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}

r=requests.get(link,headers=headers,timeout=10)

print('文本编码：',r.encoding)
print('响应状态码：',r.status_code)
print('字符串方式的响应体：',r.text)


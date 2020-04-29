import urllib.request
import urllib.error
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# import requests
# try:
#     r = requests.get('http://www.ooxx-fishc.com',timeout=5)
#     print(r.text)
# except requests.ConnectionError as e:
#     print(e)


req=urllib.request.Request('http://www.fishc.com/ooxx.html')
try:
    urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
    print(e)


# 本节是讲的urllib模块打开页码和检查错误
# 不能换成requests模块的访问网页和错误（两者访问方式和错误不太一样）

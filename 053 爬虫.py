#urllib.requeat
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# SSL证书验证错误，当请求一个https站点，但是证书验证错误时，就会报这样的错误。

import urllib.request
response=urllib.request.urlopen("http://www.fishc.com")
html=response.read()
html=html.decode('utf-8')
print(html)


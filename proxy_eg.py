import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import random


url1='http://www.goubanjia.com/'
iplist=['221.122.91.61:80','182.92.242.11:80','101.231.104.82:80','121,69,70,182:8118']

proxy_support=urllib.request.ProxyHandler({'http':random.choice(iplist)})

opener=urllib.request.build_opener(proxy_support)
opener.addheaders=[('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit Safari/605.1.15')]

urllib.request.install_opener(opener)

response=urllib.request.urlopen(url1)
html=response.read().decode('utf-8')

print(html)


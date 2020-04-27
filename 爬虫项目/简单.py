import urllib.request

url1="http://www.santostang.com/"

response=urllib.request.urlopen(url1)
response.addheaders=[('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit Safari/605.1.15')]

html=response.read().decode('utf-8')
print(html)
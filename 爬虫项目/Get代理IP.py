import requests
import re

def open_url(link):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
    html=requests.get(link,headers=headers,).text
    return html

def get_ip(html):
    # p=r'((?:[01]?\d{0,2}|2[0-4]\d|25[0-5])\.){3}(?:[01]?\d{0,2}|2[0-4]\d|25[0-5])'    #如果不要端口号，只要这句，且不用那么麻烦地打印
    p=r'([01]?\d{0,2}|2[0-4]\d|25[0-5])\.([01]?\d{0,2}|2[0-4]\d|25[0-5])\.([01]?\d{0,2}|2[0-4]\d|25[0-5])\.([01]?\d{0,2}|2[0-4]\d|25[0-5])</td>\s*<td>(\d+)</td>'
    iplist=re.findall(p,html)

    for each_ip in iplist:
        temp =''
        for i in range(5):
            temp+=(each_ip[i]+'.')
        print(temp)

if __name__=='__main__':
    link='http://www.66ip.cn'
    get_ip(open_url(link))

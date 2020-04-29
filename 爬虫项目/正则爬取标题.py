import re
import requests

link="http://www.santostang.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}

r=requests.get(link,headers=headers)
html=r.text

comment=re.compile(r'<h1 class="post-title"><a href=.*?>(.*?)</a>',flags=re.DOTALL)
title_list=comment.findall(html)
for each in title_list:
    print(each)

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random
import time


def url_open(url):
    headers={'User-Agent':UserAgent().random}
    response=requests.get(url,headers=headers,timeout=20)
    html=response.text

    return html

def content_get():
    number=0
    paper=[]
    for i in range(20):
        number+=1
        # %用来转义，%%表示输出%
        url="https://journals.aps.org/prl/recent?toc_section%%5B%%5D=general-physics-statistical-and-quantum-mechanics-quantum-information-etc&page=%d " % number
        html=url_open(url)
        soup=BeautifulSoup(html,"lxml")
        title_list=soup.find_all("h5",class_="title")
        for j in range(10):
            try:
                title=title_list[j].a.text
                if "qubit" in title:
                    paper.append(title)
            except:
                pass
            # time.sleep(2)
    return paper

paper=content_get()
for k in range(len(paper)):
    print(paper[k])
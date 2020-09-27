import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random


def url_open(url):

    headers={'User-Agent':UserAgent().random}
    response=requests.get(url,headers=headers,timeout=20)
    html=response.text

    return html

def content_return():
    url_list=[
        'https://www.nature.com/search?article_type=protocols,research,reviews&subject=physics',
        'https://arxiv.org/list/quant-ph/new',
        
    ]
    url0=url_list[0]
    html0=url_open(url0)
    soup0=BeautifulSoup(html0,"lxml")
    title_list=soup0.find_all("h2",role="heading")
    date_list=soup0.find_all("time",itemprop='datePublished')
    items0=[]
    for i in range(len(title_list)):
        title=title_list[i].a.text.strip()
        link='https://www.nature.com'+title_list[i].a['href']
        date=date_list[i].text.strip().replace('\n','')
        items0.append([title,date,link])

    # url1=url_list[1]
    # html1=url_open(url1)
    # soup1=BeautifulSoup(html1,"lxml")
    # title_list=soup1.find_all("div",class_="list-title mathjax")
    # for i in range(len(title_list)):
    #     title=title_list[i].text.strip()
    #     print(title)


    # print(items0)
    # print(title_list)
    return items0

if __name__=='__main__':
    content_return()
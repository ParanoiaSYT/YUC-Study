import requests
from bs4 import BeautifulSoup
import time
import csv

with open('安居客.csv','w') as csvfile:

    house_info=[]

    for i in range(1,3):        #数据太多csv用excel打开慢
        link1="http://beijing.anjuke.com/sale/p"
        link=link1+str(i)+'/'
        header={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
        r=requests.get(link,headers=header)
        html=r.text
        soup=BeautifulSoup(html,"lxml")

        house_list=soup.find_all('li',class_="list-item")

        for house in house_list:
            price=house.find("div",class_="pro-price").text
            name=house.find("div",class_="house-title").a.text.strip()
            details=soup.find("div",class_="details-item").text.strip()
            address=house.find("span",class_="comm-address").text.strip()

            house_info.append([price,name,details,address])         #每组添加成一个小列表
            w=csv.writer(csvfile)
            w.writerows(house_info)
        print('=====第%d页结束啦==========================='%i)
        time.sleep(3)
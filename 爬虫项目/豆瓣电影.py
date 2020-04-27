import requests
from bs4 import BeautifulSoup

def get_movies():

    headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
    movie_list=[]

    for i in range(10):

        link = 'http://movie.douban.com/top250?'+'start=%d'%(i*25)
        r=requests.get(link,headers=headers,timeout=10)

        print(str(i+1),'页状态响应码：',r.status_code)
        # print(r.text)

        soup=BeautifulSoup(r.text,'lxml')
        div_list=soup.find_all('div',class_='hd')
        for each in div_list:
            movie=each.a.span.text.strip()
            movie_list.append(movie)
    return movie_list

movies=get_movies()
print(movies)


import requests
import os

def url_open(link):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
    r = requests.get(link, headers=headers)

    return r
def get_page(link):
    # 获得页码数
    html=url_open(link).text

    # a=html.find("page-cur")+10     #向右偏移（20+3）个字符
    # b=html.find("<",a)          #从a处找至第一个]
    # return (html[a:b])

def find_imgs(page_url):
    html=url_open(page_url).text
    img_addrs=[]

    a=html.find("img src=")
    while a!=-1:
        b=html.find(".jpg",a,a+255)         #从a位置找到（a+255）位置

        if b!=-1:
            img_addrs.append(html[a+9:b+4])
        else:
            b=a+9
    a = html.find("img src=",b)

    for each in img_addrs:
        print('http:'+each)

def save_imgs(folder,img_addrs):
    for each in img_addrs:
        filename=each.split('/')[-1]
        with open(filename,'wb')as f:
            img=url_open(each)
            f.write(img)

def dl_MM(folder='OOXX',page=10):
    os.mkdir(folder)
    os.chdir(folder)
    link="http://www.meituba.com/dongmantupian/"
    page_num=int(get_page(link))

    for i in range(page):
        page_url=link+'list31'+str(page_num)+'.html'
        page_num += i
        img_addrs=find_imgs(page_url)
        save_imgs(img_addrs)

# MjAyMDA0MjgtMjEw#comments
# MjAyMDA0MjgtMjA5#comments



if __name__=='__main__':
    dl_MM()
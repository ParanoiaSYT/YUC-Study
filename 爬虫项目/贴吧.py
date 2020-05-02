import requests
import re
import os

def open_url(link):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
    html=requests.get(link,headers=headers)
    return html

def get_img(html):
    p=r'img class="BDE_Image" src="([^"]+\.jpg)"'   #加上小括号分组后findall列表里就只单独返回子组里的内容（如果有多个自组，就会组成元组形式）
    imglist=re.findall(p,html.text)
    print(imglist)
    return imglist

def save_img(imglist):
    # os.mkdir("TieBa")
    os.chdir("TieBa")
    for each in imglist:
        filename=each.split("/")[-1]    #取最好一个反斜杠后的作为文件名
        with open(filename,'wb')as f:
            imgs=open_url(each)
            f.write(imgs.content)

if __name__=='__main__':
    link='https://tieba.baidu.com/p/6646751387?red_tag=0896846278'
    save_img(get_img(open_url(link)))

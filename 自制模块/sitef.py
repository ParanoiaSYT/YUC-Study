import urllib.request
import chardet
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def main():
    i=0

    with open('../爬虫项目/urls.txt')as f:          #文件相对位置
        # 读取待访问的网址
        # 由于urls.txt每一行一个URL
        # 所以按换行符'\n'分割
        urls=f.read().splitlines()
        # print(urls)                             #列表存放了每行

    for each_url in urls:
        response=urllib.request.urlopen(each_url)
        html=response.read()

        bm=chardet.detect(html)['encoding']
        if bm =='GB2312':
            bm='GBK'
        i+=1
        filename='../爬虫项目/url%d.txt'%i

        with open(filename,'w')as f:
            f.write(html.decode(bm,'ignore'))       #忽略少部分的乱码，大部分按bm格式解码

if __name__=='__main__':
    main()
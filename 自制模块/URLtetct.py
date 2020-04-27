import urllib.request
import chardet
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def main():
    temp=input('请输入URL:')
    response=urllib.request.urlopen(temp)
    html=response.read()
    bm=chardet.detect(html)['encoding']

    if bm =='GB2312':
        bm='GBK'        #GBK是GB2312的扩展
    print('该网页使用的编码是：%s'%bm)

if __name__=='__main__':
    main()
import requests
import datetime
from bs4 import BeautifulSoup


def url_open(link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}

    r = requests.get(link, headers=headers, timeout=10)
    return r


# link='http://www.santostang.com/'

# soup=BeautifulSoup(r.text,"lxml")
# content = soup.find('div', class_="post-content clearfix").get_text().strip().replace('\n','')
# print(type(content))
# print(content)

# print('==================================')
# link='https://mp.weixin.qq.com/s/OxW3GIbwMfrpNZPnrMdFNQ'
# r=url_open(link)
# soup=BeautifulSoup(r.text,"lxml")
# pics_list = soup.find_all('img',class_='')
# # print(pics_list)
# for i in range(len(pics_list)):
#     try:
#         link = pics_list[i]['data-src']
#     except:
#         pass
#     content=url_open(link).content
#     # filename = '/Users/sunyuting/YuC-Study/爬虫项目/sepics/' + link.split('/')[-2] + '.jpg'
#     # with open(filename, 'wb')as f:
#     #     f.write(content)
#     print(link)
#     print('===========================')


# print('文本编码：',r.encoding)
# print('响应状态码：',r.status_code)
# print('字符串方式的响应体：',r.text)


t = datetime.datetime.utcnow()  # 返回UTC时间
print(datetime.datetime.today())
print(t)
print(datetime.datetime.utcnow())
print(t.astimezone())  # 把时间返回出来（任何地区）

print(datetime.date.today())
print(datetime.date.today().year)

c = datetime.datetime.today()
print(c)
# c = datetime.datetime.strptime(str(c),'%Y-%m-%d %H:%M')
print(c)
c = datetime.date.today()
c = datetime.datetime.strptime(str(c), '%Y-%m-%d').date()
print(c)

# 判断文件有多少行
for count, line in enumerate(open('Burning.txt')):
    pass
count += 1
print(count)

# 字符串分割
string = 'https://mmbiz.qpic.cn/mmbiz_jpg/KAJBcOzuyCeImzECXn27CZNM86avt794kxLr0lgXj' \
         '94pSlszvDrm9wicNJXaJ0zkThbic04CC5VpZSmGTVZFJbCA/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1'

name=string.split('/')      #分成一个列表
print(name)
name=string.split('/')[-1]      #没有指定分割次数，无限次
print(name)
string='https://mmbiz.qpic.cn/mmbiz_jpg/KAJBcOzuyCeImzECXn27CZNM86avt794kxLr0lgXj\n'\
         '94pSlszvDrm9wicNJXaJ0zkThbic04CC5VpZSmGTVZFJbCA/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1'
name=string.splitlines()       #如果有分行符，splitlines将每行内容组成一个列表
print(name)
(a,b)=name=string.split('?',1)        #分割一次
print(name)
print(a,b)      #换行符依然有效


# 整个列表取相反数
list1=[2,4,67,8]
list1=[-i for i in list1]
print(list1)

# 列表中单个元素取相反数
list1[0]=-list1[0]
print(list1)


# 测试ttk
# from tkinter import *
# from tkinter import ttk
# help(ttk.Button)
# root=Tk()
# ttk.Style().configure("TButton",padding=15,relief=FLAT,background="green",foreground="blue")
# # mac上Button似乎仍然无法改bg
# ttk.Button(root,text="撒放放假啊阱n").pack()
#
# Button(root,text="NO.2",relief=SUNKEN,fg="purple").pack()
# # tk的按钮显现不了字还是
# mainloop()


from fake_useragent import UserAgent

headers = {UserAgent().random}
print(headers)
print('==================================')


str1="sasas, sajfqn http:http\n llsaajghttps"
a=str1.rfind("https")
print(a)

print('==================================')
with open("Burning.txt",'a+')as f:
    # f.write("sssak\n")
    f.seek(0,0)
    # print(f.read())
    print(f.readlines())
print('==================================')


with open("078-096pygame/ThunderPlane/record.txt",'a+')as f:
    f.seek(0,0)
    # print(f.read())
    # print(int(f.read()))
    # f.seek(0,0)
    # f.truncate()
    f.write("0")
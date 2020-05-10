from tkinter import *
from tkinter import ttk
from 文献查找.spider import content_return
import webbrowser


# CTFontCreateUIFontForLanguage()

def click(event,link):
    print(link)
    webbrowser.open(link)
def clickAdaptor(fun,link):
    return lambda event,fun=fun,link=link:fun(event,link)

def show_arrow_cursor(event):
    text.config(cursor="arrow")     #如果里面改为cursor="hand2"，放上去鼠标样式变手
def show_xterm_cursor(event):
    text.config(cursor="xterm")


root=Tk()
root.title("量子计算文献查找")

# default_font = tkFont.nametofont("TkDefaultFont")
# default_font.configure(size=48)

group=ttk.LabelFrame(root,text="请添加网址:")
group.grid(row=0,columnspan=21,padx=10,pady=10)

v1=StringVar()
v1.set('http://')
e1=ttk.Entry(group,textvariable=v1,width=100).pack(padx=10,pady=20)


OPTIONS=[
    '----请选择网站----',
    'Nature:https://www.nature.com/search?article_type=protocols,research,reviews&subject=physics',
    'ETH:https://ethz.ch/en/news-and-events/eth-news/news/2020/03.html',
    '4399:www.4300.com'
]
v2=StringVar()
w=ttk.OptionMenu(root,v2,*OPTIONS).grid(row=1,column=5,columnspan=11,pady=20)


text=Text(root,width=100,height=40)
text.grid(row=2,columnspan=21,pady=20)
items=content_return()
lines=1
url_list=[]
for i in range(len(items)):
    content=(items[i][0]+'\t'+items[i][1]+'\t'+items[i][2]+'\n\n')
    link=items[i][2]
    text.insert(END,content)
    a=content.rfind("http")
    text.tag_add("tag%s"%str(i),'%s.%s'%(str(lines),str(a)),INSERT)
    url_list.append([str(lines),str(a)])
    print('%s.%s'%(str(lines),str(a)))
    text.tag_config("tag%s"%str(i),foreground="blue",underline=True)
    text.tag_bind("tag%s"%str(i),'<Button-1>',clickAdaptor(click,link))
    text.tag_bind("tag%s"%str(i),'<Enter>',show_arrow_cursor)
    text.tag_bind("tag%s"%str(i),'<Leave>',show_xterm_cursor)
    lines+=1
    lines+=int(len(content)//100+0.5)


ttk.Style().configure("TButton",relief=SUNKEN,fg="blue",width=15)

button1=ttk.Button(root,text="查找")
button1.grid(row=3,column=5,pady=30)

button2=ttk.Button(root,text="查找所有")
button2.grid(row=3,column=15,pady=30)

mainloop()
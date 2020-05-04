# Tags 改变Text组件中内容的样式和功能
from tkinter import *
import webbrowser
# 这是一个打开网页的成熟模块
import hashlib


root=Tk()

text=Text(root,width=30,height=6)
text.pack()

text.insert(INSERT,"I love FishC.com")
text.tag_add("tag1",1.7,1.12,1.14)
# 表示范围为1.7到1.12 (范围包左不包右)以及1.14
text.tag_config("tag1",background="yellow",foreground="red")
# Tag里bg不等于background，有个顶掉了,fg也被顶掉了

text.tag_add("tag2",1.7,1.16)
text.tag_config("tag2",background="green",foreground="blue",underline=True) #加了下划线
# 后加的标签会覆盖之前的
text.tag_lower("tag2")
# 用tag_raise或tag_lower可以提高或降低标签的优先级

# 事件绑定（tag_band)
def show_arrow_cursor(event):
    text.config(cursor="arrow")     #如果里面改为cursor="hand2"，放上去鼠标样式变手
def show_xterm_cursor(event):
    text.config(cursor="xterm")
def click(event):
    webbrowser.open("https://fishc.com.cn")
text.tag_bind("tag1",'<Enter>',show_arrow_cursor)
text.tag_bind("tag1",'<Leave>',show_xterm_cursor)
text.tag_bind("tag1",'<Button-1>',click)

##########################################
# 检查内容是否发生改变
content=text.get(1.0,END)
# 这个get方法会把结束位置换行符也算进去,如果不需要可以contents[:-1]删去

def getSig(content):
    m=hashlib.md5(content.encode())
    return m.digest()
sig=getSig(content)
# 对比两次的md5值，同一个值只能形成唯一的一个散列，不一样就说明内容发生了改变
def check():
    content = text.get(1.0, END)
    if sig !=getSig(content):
        print('警报，内容发生了变动')
    else:
        print("风平浪静")
# 对比两次content的hash值即可

Button(root,text="检查",command=check).pack()


mainloop()
from tkinter import *

root=Tk()
root.title('点点点')

text=Text(root,width=100,height=50)
text.pack()

text.insert(INSERT,"I love \n")     #INSERT指光标所在位置
text.insert(END,"FishC.com!\n")

photo=PhotoImage(file="/Users/sunyuting/Desktop/18.gif")


def show():
    print("点我干嘛？")
    text.image_create(INSERT,image=photo)

b1=Button(text,text="这是个按钮",fg='blue',height=8,width=15,relief=SUNKEN,command=show)
text.window_create(INSERT,window=b1)

mainloop()


# Text组件Index通过行/列索引来实现（行从1开始，列从0开始）1.0就是第一行第一列
# 2.3这种可以直接当成浮点型或者字符串形式
# 1.END 就是第一行末尾


# Marks 标记位置（自动移动）,只能通过mark_unset()方法来删除
# Tags 改变Text组件中内容的样式和功能

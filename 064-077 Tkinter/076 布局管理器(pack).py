# Tkinter三种布局方法
# pack(添加顺序),grid(行列),place(自定义组件大小和位置）

from tkinter import *

root=Tk()

listbox=Listbox(root)
listbox.pack(fill=BOTH,expand=True)
# expand=1表示拉伸root窗口时,填充也会随之拉伸

for i in range(10):
    listbox.insert(END,str(i))

Message(root,text="red",fg="red").pack(fill=X)
Label(root,text="pink",bg="pink").pack(fill=X)
# 纵向填充
Label(root,text="green",bg="green").pack(side=LEFT)
Label(root,text="blue",fg="blue").pack(side=LEFT)
Label(root,text="yellow",bg="yellow").pack(side=LEFT)
# 横向填充


mainloop()
from tkinter import *
from tkinter import ttk

root=Tk()

photo=PhotoImage(file="/Users/sunyuting/Desktop/18.gif")
Label(root,image=photo).grid(row=0,column=2,rowspan=2,padx=5,pady=5)
# 实现跨行（一行放不下不好看）(上面即0，1两行）

Label(root,text="用户名：").grid(row=0,column=0,sticky=W)
# sticky=罗盘方向,可以都设置为左对齐
Entry(root).grid(row=0,column=1)
Label(root,text="密码：").grid(row=1,column=0,sticky=W)
Entry(root,show="*").grid(row=1,column=1)

ttk.Style().configure("TButton",width=20,relief=SUNKEN)
ttk.Button(root,text="Submit").grid(row=2,columnspan=3,pady=10)
# column不设置默认为0

mainloop()
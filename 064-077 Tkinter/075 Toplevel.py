# 顶级窗口，类似于frame
from tkinter import *
from tkinter import ttk

root=Tk()
def create():
    top=Toplevel()
    top.attributes("-alpha",0.5)
    # 属性设置（-alpha是透明度）
    top.title("Fish C title")

    msg=Message(top,text="小甲鱼")
    msg.pack()

ttk.Style().configure("TButton",relief=SUNKEN)
ttk.Button(root,text="创建顶级窗口",command=create).pack()


mainloop()
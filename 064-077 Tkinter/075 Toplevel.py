# 顶级窗口，类似于frame
from tkinter import *

root=Tk()
def create():
    top=Toplevel()
    top.attributes("-alpha",0.5)
    # 属性设置（-alpha是透明度）
    top.title("Fish C title")

    msg=Message(top,text="小甲鱼")
    msg.pack()

Button(root,text="创建顶级窗口",relief=SUNKEN,command=create).pack()


mainloop()
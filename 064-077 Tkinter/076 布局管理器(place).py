from tkinter import *
from tkinter import ttk

root=Tk()

photo=PhotoImage(file="/Users/sunyuting/Desktop/18.gif")
Label(root,image=photo).pack(fill=BOTH,expand=1)


Label(root,bg="red").place(relx=0.5,rely=0.5,relheight=0.4,relwidth=0.5,anchor=CENTER)
Label(root,bg="yellow").place(relx=0.5,rely=0.5,relheight=0.35,relwidth=0.35,anchor=CENTER)
Label(root,bg="blue").place(relx=0.5,rely=0.5,relheight=0.2,relwidth=0.2,anchor=CENTER)
# relheight和relwidth表示相对于副组件的大小

def callback():
    print("正中靶心！！")
ttk.Button(root,text="葵花点穴手！",command=callback)\
    .place(relx=0.5,rely=0.5,anchor=CENTER)
#  relx,rely范围是0到1，anchor不设置的话是"葵"在中间

# 这样可以在一个组件里(中间)放另一个

mainloop()
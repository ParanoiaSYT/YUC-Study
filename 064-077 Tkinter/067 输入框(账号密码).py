from tkinter import *

root=Tk()

# e=Entry(root)
# e.pack(padx=20,pady=20)

Label(root,text="账号：").grid(row=0,column=0)
Label(root,text="密码：").grid(row=1,column=0)

v1=StringVar()
v2=StringVar()
v1.set('小甲鱼')
v2.set('fishc')
# 这样可以加一个初始默认功能

e1=Entry(root,textvariable=v1)
e1.grid(row=0,column=1,padx=10,pady=5)
e2=Entry(root,textvariable=v2,show='*')
e2.grid(row=1,column=1,padx=10,pady=5)

def show():
    print("账号：《%s》"%e1.get())
    print("密码：%s"%e2.get())


Button(root,text="芝麻开门",width=10,command=show)\
    .grid(row=2,column=0,sticky=W,padx=10,pady=5)
Button(root,text="退出",width=10,command=root.quit)\
    .grid(row=2,column=1,sticky=E,padx=10,pady=5)

# e.delete(0,END)
# e.insert(0,"默认文本")

mainloop()
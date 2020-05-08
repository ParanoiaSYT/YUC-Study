from tkinter import *
from tkinter import ttk

master = Tk()
frame=Frame(master)
# 这里先把整个装进框架，然后定义框架的边距(如果不这样的话，grid模式和边距会有冲突）
frame.pack(padx=10,pady=10)


v1 = StringVar()
v2 = StringVar()
v3 = StringVar()

# v1.set('0')
# v2.set('0')
# v3.set('0')


def test(content):
    if content.isdigit():
        print('是数字啦')
        return True
    else:
        print("非法输入！")
        print(content)
        return False

testCMD = frame.register(test)

e1 = Entry(frame,width=15,textvariable=v1, validate="key",
           validatecommand=(testCMD, '%P'))
# validate的值为key表示当输入框被编辑的时候验证
# width=15表示15个正常大小的字符宽度

e1.grid(row=0,column=0)

Label(frame,text="+").grid(row=0,column=1)

e2 = Entry(frame, width=15,textvariable=v2, validate="key",
           validatecommand=(testCMD, '%P'))
e2.grid(row=0,column=2)

Label(frame,text="=").grid(row=0,column=3)

e3 = Entry(frame,width=15,textvariable=v3,state="readonly")     #输出结果只读、拷贝...
e3.grid(row=0,column=4)


def calc():
    result=int(v1.get())+int(v2.get())
    v3.set(result)
    return v3

ttk.Style().configure("TButton",fg="purple",pady=15)
ttk.Button(frame,text="计算结果",command=calc).grid(row=1,column=2)     #开始计算


mainloop()
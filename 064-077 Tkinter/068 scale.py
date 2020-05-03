from tkinter import *

root=Tk()

s1=Scale(from_=0,to=43,tickinterval=5,length=200)     #默认方向竖直
s1.pack(side=RIGHT)
s2=Scale(from_=0,to=200,orient=HORIZONTAL,
         tickinterval=10,resolution=5,length=600)
# tickinterval表示刻度间隔,resolution表示移动步长,length表示像素大小
s2.pack(side=BOTTOM)




def show():
    print(s1.get(),s2.get())

Button(root,text='获取位置',fg='purple',relief=SUNKEN,command=show).pack(side=BOTTOM)

mainloop()
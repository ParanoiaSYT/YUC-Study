# Label组件的变体，显示多行文本消息(自动换行）
from tkinter import *

root=Tk()

w1=Label(root,text="这是一则消息发扩散的年轻还记",width=100)
w1.pack()
w2=Message(root,text="这啥饭那是\n沙发扩散的年轻还记得那司马光长消息",width=100)
# 也可以自己加强制换行
w2.pack()

##########################################################
# 可按上下来调整数值的Entry组件
w3=Spinbox(root,from_=0,to=10,wrap=True)
# 范围0到10,wrap表示头尾相连循环
w3.pack()

w4=Spinbox(root,values=("小甲鱼","风","ssag","maybe"))
w4.pack()



mainloop()
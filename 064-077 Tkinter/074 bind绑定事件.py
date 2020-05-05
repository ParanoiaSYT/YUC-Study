from tkinter import *


root=Tk()
frame=Frame(root,width=400,height=400)

def callback1(event):
#     绑定事件需要传入一个形参
    print("点击位置",event.x,event.y)
# 打印鼠标点击位置相对应用程序的坐标(event.x,event.y)
frame.bind("<ButtonRelease-1>",callback1)
# Button是事件本身,-1是事件描述(按下鼠标左键）
# ButtonRelease当用户释放鼠标按键的时候触发该事

def callback2(event):
    print(event.char,event.keysym)
#  打印键盘敲击的字符
frame.bind("<Key>",callback2)
# 键盘事件
frame.focus_set()
# 程序一形成就获得焦点

# def callback3(event):
#     print("当前位置",event.x,event.y)
# # 鼠标运动即时打印位置
# frame.bind("<Motion>",callback3)

frame.pack()

mainloop()
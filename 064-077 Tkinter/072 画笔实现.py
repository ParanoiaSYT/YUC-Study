from tkinter import *


root=Tk()

w=Canvas(root,width=800,height=400)

w.pack()

def paint(event):
    x1,y1=(event.x-1),(event.y-1)
    x2,y2=(event.x+1),(event.y+1)
# 设定左上角和右下角的点来制备一个小圆
    w.create_oval(x1,y1,x2,y2,outline="purple",fill="purple")
w.bind("<B1-Motion>",paint)
# B1-Motion事件表示鼠标左键点击下去绑定

Label(root,text="按住鼠标并拖动，实现你的理想吧！").pack()



mainloop()
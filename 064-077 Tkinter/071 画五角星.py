from tkinter import *
import math as m

root=Tk()

w=Canvas(root,width=600,height=300,bg="black")
w.pack()

center_x=300
center_y=150
r=150

points=[
    #左上点
    center_x- int(r*m.sin(2*m.pi/5)),center_y-int(r*m.cos(2*m.pi/5)),
    #右上点
    center_x +int(r*m.sin(2 * m.pi/ 5)), center_y - int(r * m.cos(2 * m.pi / 5)),
    #左下点
    center_x-int(r* m.sin(m.pi / 5)),center_y+int(r*m.cos(m.pi / 5)),
    #最上点
    center_x,center_y-r,
    #右下点
    center_x+int(r* m.sin(m.pi / 5)),center_y+int(r*m.cos(m.pi / 5))
]
# 这里坐标要按画布来，从上到下，从左到右

w.create_polygon(points,outline="green",fill="yellow")
w.create_polygon(points,outline="green",fill="")
# 设置成透明的了

mainloop()
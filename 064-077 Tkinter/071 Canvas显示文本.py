from tkinter import *

root=Tk()

w=Canvas(root,width=200,height=100,bg="black")
w.pack(padx=10,pady=10)

line1=w.create_line(0,0,200,100,fill="yellow",width=3)
line2=w.create_line(200,0,0,100,fill="blue",width=3,dash=(4,4))
rec1=w.create_rectangle(50,25,150,75,fill="pink")
rec2=w.create_rectangle(75,30,125,70,fill="purple")

w.create_oval(75,30,125,70,fill="white")
# 椭圆
w.create_oval(80,30,120,70,fill="green")

text=w.create_text(100,50,text="Python",anchor=SW)
# 这里文字位置和设定的相反...(按100，50为文字的SW方向理解）


mainloop()
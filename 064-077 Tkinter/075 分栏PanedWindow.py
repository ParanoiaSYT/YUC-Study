from tkinter import *


root=Tk()

m1=PanedWindow(orient=VERTICAL,showhandle=True,sashrelief=SUNKEN)
# 默认左右分布，orient=VERTICAL设置成垂直分布
# 打开手柄，分割线样式向下凹
# 手柄位置默认8像素,可以通过handlepad修改
m1.pack(fill=BOTH,expand=1)
top=Label(m1,text="上路")
m1.add(top)

m2=PanedWindow(showhandle=True,sashrelief=SUNKEN,handlepad=30)

m1.add(m2)
left=Label(m2,text="左边")
right=Label(m2,text="右边")
m2.add(left)
m2.add(right)

mainloop()
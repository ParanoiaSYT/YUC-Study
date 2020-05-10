# 右键出菜单
from tkinter import *

root=Tk()
menubar=Menu(root)

def callback():
    print("你好")
menubar.add_command(label="Hello",command=callback)
menubar.add_separator()
menubar.add_command(label="Quit",command=root.quit)

# 搞一个右键框架
frame=Frame(root,width=512,height=512)
frame.pack()
def popup(event):
    menubar.post(event.x_root,event.y_root)

frame.bind("<Button-2>",popup)
# 注意这里windows里2是滚轮3是右键，tkinter对于Mac的话，2就是右键
# 这里注意pygame里button==3对应mac右键
# MouseWheel表示滚轮滚动（mac和win)


mainloop()
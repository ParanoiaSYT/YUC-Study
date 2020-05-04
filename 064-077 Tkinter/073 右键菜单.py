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
# 注意这里windows里2是滚轮3是右键，Mac触控板的话，2就是右键

mainloop()
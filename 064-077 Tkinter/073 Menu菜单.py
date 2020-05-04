from tkinter import *

root=Tk()
menubar=Menu(root)  #创建菜单栏
# 因为Tk试图遵循苹果的Human Interface Guide for menus，所以不会在窗口中显示菜单。

file_menu = Menu(menubar, tearoff=False)
# 创建空菜单，把菜单栏加进去.tearoff默认为True(win上可以单独撕开菜单），Mac上这个参数没用

def callback():
    print("你好")
file_menu.add_command(label="Hello",command=callback)
file_menu.add_command(label="保存",command=callback)
file_menu.add_separator()   #加入菜单分隔线
file_menu.add_command(label="Quit",command=root.quit)
# 空菜单中加入内容和功能

menubar.add_cascade(label="菜单",menu=file_menu)
# 将file_menu菜单添加到菜单栏
# cascade功能是创建多级菜单
# Mac只能这样来创建级联菜单

##########################################
edit_menu=Menu(menubar,tearoff=False)
edit_menu.add_command(label="打印",command=callback)
edit_menu.add_command(label="退出",command=root.quit)
menubar.add_cascade(label="编辑",menu=edit_menu)


root.config(menu=menubar)
# 连接root

mainloop()
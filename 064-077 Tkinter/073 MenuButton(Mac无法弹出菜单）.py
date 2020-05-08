from tkinter import *
from tkinter import ttk


root=Tk()

mb=ttk.Menubutton(root,text="隐藏菜单")
mb.pack()

file_menu = Menu(mb, tearoff=False)
def callback():
    print("你好")
file_menu.add_command(label="Hello",command=callback)
file_menu.add_command(label="保存",command=callback)
file_menu.add_separator()   #加入菜单分隔线
file_menu.add_command(label="Quit",command=root.quit)



root.config(menu=file_menu)



mainloop()
from tkinter import *

root=Tk()
menubar=Menu(root,tearoff=False)  #创建菜单栏

openVar=IntVar()
saveVar=IntVar
quVar=IntVar()

file_menu = Menu(menubar, tearoff=False)
def callback():
    print("你好")
file_menu.add_checkbutton(label="Hello",command=callback,variable=openVar)
file_menu.add_checkbutton(label="保存",command=callback,variable=saveVar)
file_menu.add_separator()   #加入菜单分隔线
file_menu.add_checkbutton(label="Quit",command=root.quit,variable=quVar)

menubar.add_cascade(label="菜单",menu=file_menu)

##########################################
editVar=IntVar()

edit_menu=Menu(menubar,tearoff=False)
edit_menu.add_radiobutton(label="打印",command=callback,variable=editVar,value=1)
edit_menu.add_radiobutton(label="退出",command=root.quit,variable=editVar,value=2)

menubar.add_cascade(label="编辑",menu=edit_menu)


root.config(menu=menubar)



mainloop()
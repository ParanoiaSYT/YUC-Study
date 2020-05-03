from tkinter import *

root=Tk()

sb=Scrollbar(root)
sb.pack(side=RIGHT,fill=Y)

lb=Listbox(root,yscrollcommand=sb.set)
# 这里把sb和Listbox互联互通

for i in range(999):
    lb.insert(END,i)

lb.pack(side=LEFT,fill=BOTH)

sb.config(command=lb.yview)
# config方法来设置某个选项的值

mainloop()
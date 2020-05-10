from tkinter import *
from tkinter import ttk

OPTIONS=[
        '',
        "china",
         "USA",
         "Japan",
         "England",
         "India"
]

root=Tk()

variable=StringVar()
variable.set("one")     #默认值

w=ttk.OptionMenu(root,variable,"one","two","three","four")
w=ttk.OptionMenu(root,variable,*OPTIONS)
# *或**加列表、字典、元组等具有解包的功能
w.pack()

mainloop()
from tkinter import *

# root=Tk()
#
# v=IntVar()      #是否选中的状态
#
# c=Checkbutton(root,text="测试试试",variable=v)
# c.pack()
#
# l=Label(root,textvariable=v)       #未选中v=0，选中后v=1
# l.pack()
#
# mainloop()

#################################
root=Tk()

GIRLS=['西施','貂蝉','王昭君','杨玉环']

v=[]

for girl in GIRLS:
    v.append(IntVar())
    b=Checkbutton(root,text=girl,variable=v[-1])
    b.pack(anchor=SW,fill=BOTH,expand=1)       #这里要大写或者加引号，SW即西南方向
# 加上fill和expand就填充满了

mainloop()
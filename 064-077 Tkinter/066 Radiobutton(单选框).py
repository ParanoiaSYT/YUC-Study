from tkinter import *

# root=Tk()
#
# v=IntVar()
#
# Radiobutton(root,text="One",variable=v,value=1).pack(anchor=W)
# Radiobutton(root,text="Two",variable=v,value=2).pack(anchor=W)
# Radiobutton(root,text="Three",variable=v,value=3).pack(anchor=W)
# # 假如选中2，会把value的值2给variable;v=2时，value不是2的就变为未选中,形成互斥。
#
# mainloop()

######################################
root=Tk()

group=LabelFrame(root,text="最好的脚本语言是？",padx=5,pady=5)
# 标签框架,可以把选项按钮等放进去,看起来好看
group.pack(padx=10,pady=10)

LANGS=[
    ('python',1),
    ('VB',2),
    ('C',3),
    ('Ruby',4),
    ('JAVA',5)
]
v=IntVar()
v.set(1)    #这里默认选中了1,即python。去掉的话默认没有选中

for lang,num in LANGS:
    b=Radiobutton(group,text=lang,variable=v,value=num,indicatoron=False)
    # indicatoron写成False就变为按钮（非圆圈）
    b.pack(anchor=W,fill=X) #fill可以改为横行和纵向填充

mainloop()
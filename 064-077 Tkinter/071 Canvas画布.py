from tkinter import *

root=Tk()

w=Canvas(root,width=200,height=100,bg="black")
w.pack(padx=10,pady=10)

line1=w.create_line(0,50,200,50,fill="yellow")
# 从坐标0.50画到200.50(注意画布坐标x，y都是0开始）
line2=w.create_line(100,0,100,100,fill="red",dash=(4,4))
rec1=w.create_rectangle(50,25,150,75,fill='pink')
# 后画的部分会覆盖前面,通过lift和lower来升降
w.lift(line1)
w.lower(rec1)

# 以下有三种修改方法
w.coords(line1,0,25,200,25)
# 移动到新位置
w.itemconfig(rec1,fill='purple')
# 修改属性
# w.delete(line2)
# 删除

Button(root,text="清空",command=(lambda x=ALL:w.delete(x))).pack()
# 用lambda写函数精简

mainloop()
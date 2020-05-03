from tkinter import *

master=Tk()

theLB=Listbox(master,selectmode=MULTIPLE,height=12)
# Listbox有四种selectmode（单选，多选，滑动，拖拽）
# height可以设置显示行数（默认10行，多的要滚轮）
theLB.pack()

theLB.insert(0,'你是猪')
theLB.insert(END,'小甲鱼是猪')

for item in ['鸡蛋','鸭蛋','鹅蛋','李狗蛋']:
    theLB.insert(END,item)

# theLB.delete(0,END)
# theLB.delete(0)
#如果是两个参数，那就是起始和结尾；如果是一个参数那就是索引号

theButton=Button(master,text='删除谁？说话！',
                 command=lambda x=theLB:x.delete(ACTIVE))
# ACTIVE表示当前选中的值
theButton.pack()

mainloop()
from tkinter import *

def callback():
    var.set("你就吹吧，我才不信呢！！")


root=Tk()
root.title('电影下载？')

frame1=Frame(root)
frame2=Frame(root)
# 两个框架，分别放两张图和一个按钮

var=StringVar()
var.set("您所下载的影片为18禁，\n\n请先成年！！")
textLable=Label(frame1,
                textvariable=var,
                fg="red",
                font=("微软雅黑",25),
                justify=LEFT)
        #justify各行对齐方式

textLable.pack(side=LEFT)


photo=PhotoImage(file='/Users/sunyuting/Desktop/18.gif')
# 注意Tkinter只支持gif图片，就算改后缀也没用!

imageLabel=Label(frame1,image=photo)
imageLabel.pack(side=RIGHT)

theButton=Button(frame2,text='我已满十八周岁！',fg="purple",command=callback)

theButton.config(relief=SUNKEN)
# 按下的时候按钮保持凹下去

theButton.pack()

frame1.pack(padx=10,pady=10)        #可以直接把xy间距放框架里（放Label也可以运行）
frame2.pack(padx=10,pady=10)
#分框架后，也要分位置（当没分frame时，就不用了）

mainloop()
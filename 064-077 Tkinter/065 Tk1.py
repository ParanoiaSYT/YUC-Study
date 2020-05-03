from tkinter import *

root=Tk()
root.title('电影下载？')

textLable=Label(root,
                text="您所下载的影片为18禁，\n\n请先成年！！",
                justify=LEFT,
                padx=10)
        #justify各行对齐方式

textLable.pack(side=LEFT)


photo=PhotoImage(file='/Users/sunyuting/Desktop/18.gif')
# 注意Tkinter只支持gif图片，就算改后缀也没用!

imageLabel=Label(root,image=photo)
imageLabel.pack(side=RIGHT)

mainloop()
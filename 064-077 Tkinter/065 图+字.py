from tkinter import *

root=Tk()
root.title('背景图片上加字')


photo=PhotoImage(file='/Users/sunyuting/Desktop/bg.gif')

theLabel=Label(root,text='这里有一片星空\n星辰大海',image=photo,
               justify=CENTER,
               font=("微软雅黑",30),
               fg='pink',
               compound=CENTER)

theLabel.pack()
mainloop()
import tkinter as tk

#  用类来封装
class App:
    def __init__(self,master):
        frame=tk.Frame(master)      #框架,部件分组作用
        # frame.pack()    #自动调节位置，默认调整到最上面
        frame.pack(side=tk.LEFT,padx=10,pady=10)    #在左边，离墙x间距，y间距

        self.hi_there=tk.Button(frame,text='打招呼',bg="blue",fg="blue",command=self.say_hi)
        # fg表示前景色(font ground) ,Mac上不能修改bg背景色。   放在了frame框架里
        # command表示被按下按钮时,调用 say_hi 函数

        self.hi_there.pack()

    def say_hi(self):
        print('hello everybody! I am fishc!')


root=tk.Tk()
app=App(root)

root.mainloop()

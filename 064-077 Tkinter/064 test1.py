import tkinter as tk

app=tk.Tk()     #生成了顶层窗口实例（top level root窗口）
app.title("FishC Demo")

thelabel=tk.Label(app,text='我的第二个窗口程序!')     #标签组件实例化,放在app下
# 显示文本、图标和图片

thelabel.pack()     #自动调节尺寸和位置

app.mainloop()      #窗口的主事件循环


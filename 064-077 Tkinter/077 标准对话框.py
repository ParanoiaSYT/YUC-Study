from tkinter import *
from tkinter import messagebox,filedialog,colorchooser
# messagebox,filedialog,colorchooser不能通过*引进所有命名空间来导入

#############################################
# 文件对话框
root=Tk()
def callback():
    fileName=filedialog.askopenfilename(defaultextension=".txt",filetypes=[("PNG",".png"),("GIF",".gif"),("Python",".py")])
    # 限定和自动添加文件后缀
    print(fileName)
Button(root,text="点击打开文件",relief=SUNKEN,command=callback).pack()

#############################################
# 对话框
# messagebox.askokcancel("FishC demo","发射核弹")
print(messagebox.askokcancel("FishC demo","发射核弹"))

#############################################
# 颜色对话框
def callback():
    fileName = colorchooser.askcolor()
    print(fileName)
# 打印出RGB值
Button(root, text="选择颜色", command=callback).pack()


mainloop()


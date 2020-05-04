from tkinter import *
import hashlib

root=Tk()

text=Text(root,width=30,height=6,undo=True,autoseparators=False)
#打开undo功能(撤销上一步操作）
# 默认是撤销一整段操作（回车算分隔）.
# 如果要撤销单个字的话，autoseparators修改为False然后自定义分隔方法
text.pack()

text.insert(INSERT,"I love FishC.com")
text.tag_add("tag1",1.7,1.12,1.14)
text.tag_config("tag1",background="yellow",foreground="red")

def callback(event):
    text.edit_separator()
text.bind("<Key>",callback)
# ⚠注意这里要大写Key
# 'key'表示当输入框被编辑的时候验证
# bind callback函数，每当有按键操作，就插入一个分隔符
def show():
    text.edit_undo()
Button(root,text="撤销",relief=SUNKEN,command=show).pack()
# 每按一下按钮，调用show函数，实现撤销功能

###################################
# 实现全文搜索
start=1.0
while True:
    pos=text.search("o",start,stopindex=END)
    if not pos:
        break
    else:
        print("找到了，位置在:",pos)
        start=pos+"+1c"
# "+1c"就是"+ count chars"的简写,将索引往前移动一个字符，可以跨越换行符但不能跨过END

mainloop()
#图形化小游戏
# import easygui as g
# import random
# g.msgbox('嗨，欢迎进入SYT设计的第一个小游戏hhh')
# secret=random.randint(1,10)
# msg="不妨猜一下小甲鱼想的数字"
# title='数字小游戏'
# guess=g.integerbox(msg,title,lowerbound=1,upperbound=10)
# time=0
# while guess != secret :
#     time = time + 1
#     if guess > secret:
#         g.msgbox("哥，大了大了～")
#     else:
#         g.msgbox("嘿，小了小了")
#     msg1=("哎呀猜错了，再来个新数字吧")
#     guess = g.integerbox(msg1, title, lowerbound=1, upperbound=10)
#     if time == 3:
#         g.msgbox("猜错了，没有机会了！")
#         break
# if guess==secret:
#     g.msgbox("卧槽，你是蛔虫吗")
#     g.msgbox("哼，猜中也没有奖励")
# g.msgbox("游戏结束，不玩了^v^")

#登记用户账号信息
# import easygui as g
# # g.msgbox('请填写以下联系方式')
# title='账号中心'
# msg='请填写以下联系方式'
# fieldNames=["*用户名","*真实姓名","固定电话","*手机号码","QQ","E-mail"]
# fieldValues=[]
# fieldValues=g.multenterbox(msg,title,fieldNames)
# while 1:
#     if fieldValues == None:
#         break
#     errmsg=''
#     for i in range(len(fieldNames)):
#         option=fieldNames[i].strip()
#         if fieldValues[i].strip()==''and option[0]=='*':       #判断带*号的是否填了信息
#             errmsg+=('【%s】为必填项。\n\n'%fieldNames[i])
#     if errmsg=='':
#         break
#     fieldValues=g.multenterbox(errmsg,title,fieldNames,fieldValues)

#文件浏览框(mac上有问题，不支持？）
# import easygui as g
# import os
# file_path=g.fileopenbox(default='*.txt')       #*代表任意多个字符
# with open(file_path) as f:
#     title =os.path.basename(file_path)
#     msg='文件【%s】的内容如下：'%title
#     text=f.read()
#     g.textbox(msg,title,text)

#统计代码量
import easygui as g
import os
def show_result(start_dir):
    lines=0
    total=0
    text=''
    for i in source_list:
        lines=source_list[i]
        total+=lines
        text+='【%s】源文件%d个，源代码%d行\n'%(i,file_list[i],lines)
    title='统计结果'
    msg='您目前共累计编写了%d行代码'%total
    g.textbox(msg,title,text)
def calc_code(file_name):
    lines=0
    with open(file_name)as f:
        print('正在分析文件：%s...'%file_name)
        try:
            for each_line in f:
                lines+=1
        except UnicodeDecodeError:
            pass    #万一遇到格式不兼容的文件忽略掉
    return lines
def search_file(start_dir):
    os.chdir(start_dir)
    for each_file in os.listdir(os.curdir):      #此处是当前目录
        ext=os.path.splitext(each_file)[1]
        if ext in target:
            lines=calc_code(each_file)
            try:
                file_list[ext]+=1
            except KeyError:
                file_list[ext]=1
            try:
                source_list[ext]+=lines
            except KeyError:
                source_list[ext]=lines
        if os.path.isdir(each_file):
            search_file(each_file)
            os.chdir(os.pardir)     #返回上一级目录
target=['.c','.cpp','.py','.cc','java','.pas','.asm']
file_list={}
source_list={}
g.msgbox('请打开您存放所有代码的文件夹','统计代码量')
path=g.diropenbox('请选择代码库:')
search_file(path)
show_result(path)


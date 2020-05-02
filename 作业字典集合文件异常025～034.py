#025
dict1={'F':70,'C':67,'h':104,'i':105}
dict2=dict((('F',70),('C',67)))
print(dict1['C'])
print(dict2['C'])

a=dict(one=1,two=2,three=3)
print(a['one'])

date="9999,xss,man"
MyDict={}
(MyDict['id'],MyDict['name'],MyDict['sex'])=date.split(',')     #字符串的分割
print(MyDict)

#通讯录app
# print((('|---欢迎进入通讯录程序---|\n|---1:查询联系人资料---|\n|---2:插入新的联系人---｜\n|---3:删除已有联系人---|\n|---4:退出通讯录程序---｜')))
# CoDict={}
# while True:
#     comm = int(input('请输入相关的指令代码：'))
#     if comm==1:
#         name=input('请输入联系人姓名：')
#         if CoDict.get(name) ==None:
#             print('查无此人')
#         else:
#             print(name+':'+CoDict[name])
#     elif comm==2:
#         name = input('请输入联系人姓名：')
#         if CoDict.get('name')==None:
#             number=input('请输入联系人电话：')
#             temp={name:number}
#             CoDict.update(temp)
#         else:
#             print('您输入的姓名在通讯录已存在-->>'+name+CoDict[name])
#     elif comm==3:
#         name=input('请输入联系人姓名：')
#         if CoDict.get(name) ==None:
#             print('查无此人')
#         else:
#             CoDict.pop(name)
#     elif comm==4:
#         break
#     else:
#         print('指令错误！')
# print('|---感谢使用通讯录程序---|')

#026
dict3={1:('one','first')}
print(dict3[1])
dict3[2]='two'
print(dict3)

#fromkeys直接创建(后面整个对应前面）,会覆盖之前的字典
print(dict1.fromkeys((1,2,3),('one','two','three')))
print(dict1.fromkeys((1,3),'数字'))

dict4=dict1.copy()
dict1[6]='six'
print(dict4,dict1)

#用户登录程序
# dict5={}
# def mFun():
#     while True:
#         print((('|---新建用户：N/n---|\n|---登录账户：E/e---|\n|---推出程序:Q/q---|')))
#         code=input('|---请输入指令代码：')
#         if code in 'Nn':
#             name=input('请输入用户名：')
#             while name in dict5:
#                 name = input('此用户名已经被使用，请重新输入：')
#                 continue
#             else:
#                 mm = input('请输入密码：')
#                 dict5[name] = mm
#                 print('注册成功，赶紧登录试试吧')
#         elif code in 'Ee':
#             name=input('请输入用户名：')
#             while name not in dict5:
#                 name = input('此用户名不存在，请重新输入：')
#                 continue
#             else:
#                 mm = input('请输入密码：')
#                 while mm != dict5[name]:
#                     print('密码错误！')
#                     mm = input('请输入密码：')
#                     continue
#                 else:
#                     print('欢迎进入xx系统，请点击右上角x结束程序!')
#                     break
#         elif code in 'Qq':
#             break
#         else:
#             print('指令错误!')
#     print('感谢使用')
# mFun()

#027
#set集合中元素唯一性(集合是无序的，不能索引）
set1=frozenset([2,34,6])    #不变集合
print(set1)

print(len(set1))
set1=set([1,2,6])

print(set1)
set1.add(9)
print(set1)
set1.remove(6)
print(set1)

#028文件
#windows路径接受斜线/和反斜线\
# 'xb'为可写入二进制模式。x和w都是可写入模式，x模式如果存在相同文件名文件会报错，⚠️w会覆盖.

#list(f)即可将文件数据放入列表

# f= open('我为什么是一个文件.txt')
# for each_line in f:
#     print(each_line,end='')
# f.close()
# f1=open('我为什么是一个文件.txt')
# f2=open('别问为什么.txt','x')
# f2.write(f1.read())
# f2.close()
# f1.close()

#029
# def file_write():
#     name=input('请输入文件名:')
#     print("请输入内容【单独输入':w'保存退出】：")
#     f=open(name,'w')
#     while True:
#         word=input()
#         if word!=':w':
#             f.write(word+'\n')
#         else:
#             f.close()
#             break
# file_write()

#比较文件行不同
# def file_compare():
#     name1=input('请输入需要比较的第一个文件名：')
#     name2=input('请输入需要比较的第二个文件名：')
#     f1=open(name1)
#     f2=open(name2)
#     differ=[]
#     count=0
#     for each_line1 in f1:
#         each_line2=f2.readline()
#         count+=1
#         if each_line1!=each_line2:
#             differ.append(count)
#     f1.close()
#     f2.close()
#     if len(differ)==0:
#         print('all same')
#     else:
#         print('有%d行不同'%len(differ))
#     for i in differ:
#         print('第%d行不同'%i)
# file_compare()

#打印文件指定行
# def filePr(name,n):
#     f=open(name)
#     (s,e)=n.split(':')
#     if s=='':
#         start=0
#     else:
#         start=int(s)
#     if e=='':
#         end=-1
#     else:
#         end=int(e)
#     length=end - start
#     count = start
#     for i in range(start):
#         f.readline()
#     if length<0:
#         print(f.read())
#     else:
#         while count<=end:
#             print(list(f)[count])
#             count+=1
#     f.close()
# name=input('请输入要打开的文件：')    #Burning
# filePr(name,'1:')

list1=[2,35,7,2]    #上面程序有个小bug
print(list1[1:-2])

#全部替换
# def file_replace(name,oldword,newword):
#     f1=open(name)
#     count=0
#     content=[]
#     for eachline in f1:
#         if oldword in eachline:
#             count+=eachline.count(oldword)
#             eachline=eachline.replace(oldword,newword)
#         content.append(eachline)
#     print('文件%s中共有%d个【%s】'%(name,count,oldword))
#     print('您确定要把所有的【%s】替换为【%s】吗？\n【Yes/No】:'%(oldword,newword),end='')
#     answer=input()
#     if answer in 'YES,yes,Yes,y,Y':
#         f2=open(name,'w')
#         f2.writelines(content)
#         f2.close()
#     f1.close()
# name = input('请输入文件名:')
# oldword=input('请输入要替换的单词或字符：')
# newword=input('请输入新的单词或字符：')
# file_replace(name,oldword,newword)

#30 文件系统
#文件类型
import os
all_files=os.listdir(os.curdir)
type_dict=dict()
for each_file in all_files:
    if os.path.isdir(each_file):
        type_dict.setdefault('文件夹',0)       #字典中创建'文件夹'key,默认值为0
        type_dict['文件夹']+=1
    else:
        # ext=os.path.split(each_file)[1]     #把路径分割成 dirname 和 basename，返回一个元组
        # (name,diff)=ext.split('.',1)        #第二个参数表示分割的次数，不填或者是-1即无限分割
        diff=os.path.splitext(each_file)[1]
        type_dict.setdefault(diff,0)
        type_dict[diff]+=1
for each_type in type_dict.keys():
    print('该文件夹下共有类型为【%s】的文件%d个'%(each_type,type_dict[each_type]))

#文件大小
import os
all_files=os.listdir(os.curdir)     #当前目录的文件名
file_dict=dict()
for each_file in all_files:
    if os.path.isfile(each_file):
        file_size=os.path.getsize(each_file)
        file_dict[each_file]=file_size
print(file_dict)
for each in file_dict.items():      #字典里的各项
    print('%s【%dBytes】'%(each[0],each[1]))

#文件搜索
import os
# def getFun(path,name):
#     os.chdir(path)
#     all_files = os.listdir(os.curdir)
#     for each_file in all_files:
#         if os.path.isdir(each_file):
#             getFun(each_file,name)
#         elif name==each_file:
#             print(os.path.abspath(each_file))
# #!!!精彩的自制递归
# path=input('请输入待查找的初始目录：')
# name=input('请输入需要查找的目标文件:')
# getFun(path,name)

#文件关键字(待修改)
import os
def print_pos(key_dict):
    keys=key_dict.keys()
    keys=sorted(keys)
    for each_key in keys:
        print('关键字出现在第%s行，第%s个位置。'%(each_key,key_dict[each_key]))
def pos_in_line(line,key):             #对单行搜索key所在位置
    pos=[]
    begin=line.find(key)
    while begin !=-1:               #find()如果找不到就返回-1，否则返回索引值（从0开始）
        pos.append(begin+1)
        begin=line.find(key,begin+1)
    return pos
def search_in_file(file_name,key):     #对单个文件搜索看是否有key
    with open(file_name)as f:
        count=0
        key_dict=dict()
        for each_line in f:
            count+=1
            if key in each_line:
                pos=pos_in_line(each_line,key)
                key_dict[count]=pos
        return key_dict
def search_files(key,detail):           #查找.txt文件
    all_files=os.walk(os.getcwd())      #os.walk() 方法用于通过在目录树中游走输出在目录中的文件名，向上或者向下。 os.getcwd() 方法用于返回当前工作目录。
    txt_files=[]
    for i in all_files:
        for each_file in i[2]:          #os.walk遍历后i[2]为文件名
            if os.path.splitext(each_file)[1]=='.txt':
                each_file=os.path.join(i[0],each_file)  #os.walk遍历后i[0]为目录 #把目录和文件名合成一个路径
                txt_files.append(each_file)
    for each_txt_file in txt_files:         #所有的.txt文件都在txt_file这个列表中
        key_dict=search_in_file(each_txt_file,key)
        if key_dict:
            print('==================================================================')
            print('在文件【%s】中找到关键词【%s】'%(each_txt_file,key))
            if detail in ['YES','yes','Yes']:
                print_pos(key_dict)
key=input('请输入关键字：')
detail=input('请问是否需要打印关键字【%s】在文件中的具体位置【Yes/No】？'%key)
search_files(key,detail)


#031 (泡菜)
import pickle
def fsave(count):
    filename_boy = 'boy_' + str(count) + '.pkl'
    filename_girl = 'girl_' + str(count) + '.pkl'
    f1 = open(filename_boy, 'wb')
    pickle.dump(boy,f1)
    f2 = open(filename_girl, 'wb')
    pickle.dump(girl,f2)
    f1.close()
    f2.close()

f=open('/Users/sunyuting/Desktop/yuc/record.txt')
count=1
boy=[]
girl=[]
for each_line in f:
    if each_line[:6]!='======':
        (role,spoken) = each_line.split(':',1)
        if role == '小甲鱼':
            boy.append(spoken)
        elif role == '小客服':
            girl.append(spoken)

    else:
        fsave(count)
        count += 1
fsave(count)
f.close()

f1=open('boy_1.pkl','rb')
boy1=list(pickle.load(f1))
print(boy1)     #二进制存储

#032异常处理
try:
    for i in range(3):
        for j in range(3):
            if i==2:
                raise KeyboardInterrupt
        print(i,j)
except KeyboardInterrupt:
    print('退出！')

#提高用户体验
# import random
# secret=random.randint(1,10)
# print('~~~~~~~~~~~~~我爱鱼C工作室~~~~~~~~~~~~~~~~')
# try:
#     temp = input("不妨猜一下小甲鱼想的数字:")
#     guess = int(temp)
# except (EOFError,ValueError,KeyboardInterrupt) as reason:
#     print('错啦，要输入数字哦,错误原因是：%s'%str(reason))
#     guess=secret
# while secret != guess:
#     if guess > secret:
#         print("哥，大了大了～")
#     else:
#         print("嘿，小了小了")
#     temp = input("哎呀猜错了，再来个新数字吧:")
#     guess = int(temp)
#     if guess == secret:
#         print("卧槽，你是蛔虫吗")
#         print("哼，猜中也没有奖励")
# print("游戏结束，不玩了^v^")

#定义新函数
# def int_input():
#     while True:
#         try:
#             int(input('请输入一个整数:'))
#             break
#         except ValueError:
#             print('出错,您输入的不是整数!')
# int_input()

#不存在的文件
try:
    f=open('机密.txt')
    print(f.read())
except OSError as reason:       #该文件不存在
    print('出错了，错误原因是：%s'%str(reason))
finally:
    if 'f' in locals():         #如果文件对象变量存在当前局部变量符号表，则说明打开成功
        f.close()

#034 else with
try:
    print('abc')
except:
    print('def')
else:
    print('ghi')
finally:
    print('jkl')

#不怕文件忘关
try:
    with open('zhutou.txt','w')as f:
        for each_line in f:
            print(each_line)
except OSError as reason:
    print('出错了，错误原因是：%s'%reason)


# with A() as a,B()as b:
#     suite

with open('Burning.txt') as f:
    print(f.read())

#通讯录app 异常实现方法
#KeyError:不在字典里报错
print((('|---欢迎进入通讯录程序---|\n|---1:查询联系人资料---|\n|---2:插入新的联系人---｜\n|---3:删除已有联系人---|\n|---4:退出通讯录程序---｜')))
CoDict={}
while True:
    comm = int(input('请输入相关的指令代码：'))
    if comm==1:
        name=input('请输入联系人姓名：')
        try:
            print(name + ':' + CoDict[name])
        except KeyError:
            print('查无此人')
    elif comm==2:
        name = input('请输入联系人姓名：')
        try:
            print('您输入的姓名在通讯录已存在-->>'+name+CoDict[name])
            if input('是否修改用户资料？【Yes/No】：') in 'Yes,YES,yes':
                CoDict[name]=input('请输入联系人电话：')
        except KeyError:
            number=input('请输入联系人电话：')
            CoDict[name]=number
    elif comm==3:
        name=input('请输入联系人姓名：')
        try:
            del CoDict[name]
            print('已删除。')
        except KeyError:
            print('查无此人')
    elif comm==4:
        break
    else:
        print('指令错误！')
print('|---感谢使用通讯录程序---|')
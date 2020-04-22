# 001
str1 = '人名币是"什么"'
print(str1)
5 + 8  # 结果+类型都有
print(5 + 8)  # 结果，没有类型（NoneType)

# 002
# print(dir(__builtins__))    #查看内置函数有哪些（68个）
# temp=input('请输入您的姓名：')
# print('你好，'+str(temp)+'!')
#
# temp=int(input('请输入1到100之间的数字'))
# if 1<=temp<=100:
#     print('你妹好漂亮！')
# else:
#     print('你大爷好丑啊')

# 003
# Python 中的变量名不能以数字开头。
print("let's go")

HoursPerDay = 24
MinutesPerHour = 60
SecondPerMinute = 60
DaysPerYear = 365
SecondPerYear = HoursPerDay * MinutesPerHour * SecondPerMinute * DaysPerYear
print(SecondPerYear)
string = ((("")))
# 004
# 去除第一段的第二个字符和第二段的第三个字符
# 去重
# str1=input('请输入您的名字：')
# temp=' '
# for each in str1:
#     if each == ' ':
#         (f,l)=str1.split(' ',1)
# for i in f:
#     for j in l:
#         if j == i:
#             f=f.replace(j,' ')
# for k in f:
#     if k == ' ':
#         f=f.replace(k,'')
# final=f+temp+l
# print(final)

str1 = 'cxkks sffj'
str1 = str1[0:1] + str1[2:]
print(str1)

string1 = ((("释放肌肤烦恼,\n是是非非就")))
string2 = ("释放肌肤烦恼,\n""是是非非就")  # 两种方法都可
print(string1)
print(string2)

# 005
m = int(3.1415926)
print(m)  # 向下取整
m = int(3.14 + 0.5)
print(m)
m = int(3.6 + 0.5)
print(m)  # +0.5再取即可四舍五入

isinstance(m, int)  # 这种方法返回类型更直接
print(type(m))

销售奶粉 = '三鹿'  # python3可以使用中文变量名(utf-8编码)
print(销售奶粉)

# year=int(input('请输入一个年份：'))
# if year%4==0 and year%100!=0 or year%400==0:
#     print('%d年是闰年哦'%year)
# else:
#     print('%d年非闰'%year)

# 006
print(3 // 2)  # floor地板除
print(3.0 // 2.0)
# a<b<c 即为 a<b and b<c
print(5 ** -2)

print(not 1 or 0 and 1 or 3 and 4 or 5 and 6 or 7 and 8 and 9)
# 短路逻辑：3 and 4 == 4 ; 3 or 4 == 3
print(0 and 1)  # 0 and 1 == 0
print(4 and 3)

print(800 % 4)  # 整除求余数

# for i in range(100):    #打印出 0~100 所有的奇数
#     if i%2 !=0:
#         print(i)

# 爱因斯坦的难题
a = 7
count = 1
while count < 100:
    if a % 2 == 1 and a % 3 == 2 and a % 5 == 4 and a % 6 == 5:
        print('阶梯数为：', a)
        break
    else:
        a = 7 * (count + 1)
    count += 1
else:
    print('在程序范围内无法找到！')

# 007 and 008
b = 800
assert type(b) == int  # 断言用来测试程序

x = 1
y = 2
z = 3
# temp=x
# x=y
# y=z
# z=temp
# print(x,y,z)
x, y, z = y, z, x
print(x, y, z)  # 快速交换三个变量的值

# 三元操作符
x, y, z = 6, 5, 4
small = x if x < y else y
small = y if y < z else z
print(small)

# 009
for i in range(0, 10, 2):  # 0,2,4,6,8
    print('fishc')

# continue 终止本轮循环并开启下一轮循环

print(list(range(10)))

while True:
    while True:
        break
        print(1)
    print(2)
    break
print(3)  # break 只能跳出一层循环

# while True:循环体可用于游戏或操作系统———消息循环（break跳出）

# i = 0
# string = 'ILoveFishC.com'
# while i < len(string)):       #效率较低，因为每次循环都要用len函数
#     print(string[i])
#     i += 1

i = 0
string = 'ILoveFishC'
length = len(string)
while i < length:
    print(string[i])
    i += 1

# code=input('请输入密码：')
# count=0
# if '*' in code:
#         code = input('密码中不能含有"*"号！您还有3次机会！请输入密码:')
# while count<3 and code !='FishC.com':
#     code = input('密码错误！您还有%d次机会！请输入密码:'%(3-count))
#     if code == '小甲鱼是帅哥':
#         print('呃，鱼C棒！')
#         code = input('密码错误！您还有%d次机会！请输入密码:' %(3-count))
#     count+=1
# if count ==3:
#     print('密码错误！您没有机会啦！')
# if code == 'FishC.com':
#     print('密码正确，进入程序……')

# 下面是下甲鱼参考答案
# count = 3
# password = 'FishC.com'
# while count:
#     passwd = input('请输入密码：')
#     if passwd == password:
#         print('密码正确，进入程序......')
#         break
#     elif '*' in passwd:
#         print('密码中不能含有"*"号！您还有', count, '次机会！', end=' ')
#         continue
#     else:
#         print('密码输入错误！您还有', count-1, '次机会！', end=' ')
#     count -= 1

for i in range(10):
    print(i, end=' ')  # 如果没有end，则为换行输出

for i in range(100, 1000):
    a = i // 100
    b = (i - a * 100) // 10
    c = i % 10
    if i == a ** 3 + b ** 3 + c ** 3:
        print('%d是水仙花数' % i)

print(153 % 10, 153 // 10, 15 % 10, 15 // 10, 1 % 10, 1 // 10)
# %除给余数，//除给整数部分(地板除)

# 有红、黄、蓝三种颜色的求，其中红球 3 个，黄球 3 个，绿球 6 个。先将这 12 个球混合放在一个盒子中，从中任意摸出 8 个球，编程计算摸出球的各种颜色搭配。
print('red\tyello\tgreen')  # \t为空格
for red in range(4):
    for yellow in range(4):
        for green in range(2, 7):  # 注意8个球至少有2个绿
            if red + yellow + green == 8:
                print(red, '\t', yellow, '\t', green)

#010
#列表可以存放任何数据类型
list1=[1,2,3.14,'AME',[99,22]]
list1.append(0)
list1.extend([4,96])    #append只能加一个元素,extend可以加一个列表的元素（升级版）
print(list1)

list1.append(['竹林','死神'])    #等于list1.extend([['竹林','死神']])
list1.extend([1,2])
print(list1)

name=['F','i','h','C']
name.insert(2,'s')      #笨办法name=name[:2]+['s']+name[2:]
print(name)

member = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']
member.insert(1,90)
member.insert(3,88)
member.insert(5,86)
member.insert(7,92)
member.insert(9,94)
print(member)

for each in member:
    print(each)

print(member[0],member[1:3])
#方法一
count=0
length=len(member)
while count<length:
    print(member[count],member[count+1])
    count+=2
#方法二
for i in range(len(member)):
    if i %2==0:
        print(member[i],member[i+1])

#011
list1=[1,3,2,9,7,8]
print(list1[2:5])
print(list1[0],list1[0:1])
list1.insert(0,list1.pop())     #弹出最后一个值
print(list1)

print(list1[-3:-1])     #注意不包括末尾

print(list1[0:5:2])     #设置步长
print(list1[::-2])
print(list1[-1:-6:-2])  #等于list1[-1:-6:-2]

#012
old=[1,2,3,4,5]     #列表1
new=old
old.append(7)       #列表1+了一个元素
old=[6]         #列表2
print(new)

list1 = [1, [1, 2, ['小甲鱼']], 3, 5, 8, 13, 18]
# list1[1][2].pop()
# list1[1][2].append(['小鲫鱼'])
list1[1][2][0]='小鲫鱼'
print(list1)

list2=[4,1,2,7,4,9]
list2.sort()
print(list2)
list2.sort(reverse=True)
print(list2)

# list2.clear()
# print(list2)

list3=list2.copy()      #和切片拷贝一样 list3=list2[:]
print(list3)
list2.append(10)
print(list3,list2)
#列表推到式/列表解析
a=[i * i for i in range(10)]
print(a)

list1=[x**2 for x in range(10)]
print(list1)

list1 = [(x, y) for x in range(10) for y in range(10) if x%2==0 if y%2!=0]
print(list1)

# list2=[(x,y) for x in range(0,10,2)for y in range(1,10,2)]
list2=[]
for x in range(10):
    for y in range(10):
        if x%2==0 and y%2!=0:
            list2.extend([(x,y)])
print(list2)

#列表对应
list1=['4.addidas','2.李宁']
list2=['2.impossible','4.可能']
list3=[brand+':'+slogan[2:]for brand in list1 for slogan in list2 if brand[0]==slogan[0]]
print(list3)

#013
# 列表：一个大仓库，你可以随时往里边添加和删除任何东西。
# 元组：封闭的列表，一旦定义，就不可改变（不能添加、删除或修改）。
list4=[1,2,3,4,4,5,5,8]
print(list4.count(4))   #4出现的次数
print(list4.index(4))   #返回4出现的索引值（第一个)

temp = ('小甲鱼', '黑夜', '迷途', '小布丁')
# 如果我想在“黑夜”和“迷途”之间插入“怡静”，我们应该：
temp = temp[:2] + ('怡静',) + temp[2:]        #注意⚠️逗号
print(temp)

x,y,z=1,2,3
print(type(x))
h=x,y,z
print(type(h))  #tuple类型

tuple1=(x**2 for x in range(10))
print(type(tuple1))
# 生成器
print(tuple1.__next__())
print(tuple1.__next__())
print(tuple1.__next__())
print(tuple1.__next__())

#014
str1 = '''待我长发及腰，将军归来可好？
此身君子意逍遥，怎料山河萧萧。
天光乍破遇，暮雪白头老。
寒剑默听奔雷，长枪独守空壕。
醉卧沙场君莫笑，一夜吹彻画角。
江南晚来客，红绳结发梢。'''
print(str1)
str2 = '待卿长发及腰，我必凯旋回朝。\
昔日纵马任逍遥，俱是少年英豪。\
东都霞色好，西湖烟波渺。\
执枪血战八方，誓守山河多娇。\
应有得胜归来日，与卿共度良宵。\
盼携手终老，愿与子同袍。'
print(str2)
str3 = ('待卿长发及腰，我必凯旋回朝。\n'
'昔日纵马任逍遥，俱是少年英豪。\n'
'东都霞色好，西湖烟波渺。\n'
'执枪血战八方，誓守山河多娇。\n'
'应有得胜归来日，与卿共度良宵。\n'
'盼携手终老，愿与子同袍。\n')
print(str3)

f=open('/Users/sunyuting/Desktop/yuc/未命名1.txt','r')
print(f)        #对于\下需要r'C:\xxx'

str1 = '<a href="http://www.fishc.com/dvd" target="_blank">鱼C资源打包</a>'
print(str1[-52:-32])
print(str1[20:-36])

str1 = 'i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
print(str1[::3])

# # 密码安全性检查代码
# code=input('请输入需要检查的密码组合:')
# special=r'~!@#$%^&*()_=-/,.?<>;:[]{}|\\'
# chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# number='0123456789'
#
# def note():
#     print('''1. 密码必须由数字、字母及特殊字符三种组成
# 2. 密码只能由字母开头
# 3. 密码长度不能低于16位''')
#
# #先判断长度
# length=len(code)
# if length >=16:
#     flag_len=3
# elif 8<=length<16:
#     flag_len=2
# else:
#     flag_len=1
# #判断密码包含类型
# flag_con=0
# for each in code:
#     if each in chars:
#         flag_con+=1
#         break
# for each in code:
#     if each in number:
#         flag_con+=1
#         break
# for each in code:
#     if each in special:
#         flag_con+=1
#         break
#
# if  flag_con==1 and flag_con==1:
#     print('您的密码安全级别为：低')
#     note()
# elif flag_len==3 and flag_con==3 and (code[0] in chars):
#     print('您的密码安全级别为：高')
#     print('请继续保持')
# else:
#     print('您的密码安全级别为：中')
#     note()

#015
# 符号 说明
# % c 格式化字符及其ASCII码
# % s 格式化字符串
# % d 格式化整数
# % o 格式化无符号八进制数
# % x 格式化无符号十六进制数
# % X 格式化无符号十六进制数（大写）
# % f 格式化定点数，可指定小数点后的精度
# % e 用科学计数法格式化定点数
# % E 作用同 % e，用科学计数法格式化定点数
# % g 根据值的大小决定使用 % f或者 % e
# % G 作用同 % g，根据值的大小决定使用 % F或者 % E

print("{{1}}".format("不打印","打印"))
print("{1}+++{0}".format("不打印","打印"))
print("{a} love {b}.{c}".format(a="I", b="FishC", c="com"))

print('{0}={1:.2f}'.format('Pi',3.1415))    #定点数

# temp=input('请输入一个整数（输入Q结束程序）')
# if temp=='Q':
#     exit()
# else:
#     number = int(temp)
#     print('十进制->十六进制:%d->0x%x'%(number,number))
#     print('十进制 -> 八进制 : %d -> 0o%o' % (number, number))
#     print('十进制 -> 二进制 : %d -> ' % number, bin(number))

# q=True
# while q:
#     temp = input('请输入一个整数（输入Q结束程序）')
#     if temp!='Q':
#         number = int(temp)
#         print('十进制->十六进制:%d->0x%x' % (number, number))
#         print('十进制 -> 八进制 : %d -> 0o%o' % (number, number))
#         print('十进制 -> 二进制 : %d -> ' % number, bin(number))
#     else:
#         q=False

#016
print(max('I love FishC.com'))

# name = input('请输入待查找的用户名:')
# score=[['迷途',85],['黑夜',80],['小布丁',90]]
# IsFind=False
# for each in score:
#     if each[0]==name:
#         print(name+'的得分是：',each[1])
#         IsFind=True
#         break
# if IsFind==False:
#     print('查找的数据不存在！')

# min()
list5=[1,34,4,6,3,8]
count=0
while count<len(list5)-1:
    small =list5[0]if list5[0]<list5[count+1] else list5[count+1]
    count+=1
print(small)

def sum1(x):
    temp1 = 0
    for each in x:
        if isinstance(each,int or float)==True:
            temp1+=each
        else:
            continue
    print(temp1)
sum1([2,4,5,'s',True])

print(sum([2,5,8,22]))
#017
def MyFun(x,y):
    return x[0]*x[1]-y[0]*y[1]
print(MyFun((3,4),(1,2)))

def hello():
    print('Hello World!')
    return
    print('Welcome To FishC.com!')
print(hello())      #函数默认到retur停止，即使没有任何返回值

def power(x,y):
    return x**y
print(power(2,3))

#最大公约数
def gcd(x,y):
    while y:
        t=x%y
        x=y
        y=t
    return x
print(gcd(6,8))

print(1%2)

#十进制转二进制
def Dec2Bin(dec):
    temp=[]
    result=''
    while dec:
        q=dec%2
        dec=dec//2
        temp.append(q)
    while temp:
        result+=str(temp.pop())
    print(result)
Dec2Bin(10)

#018
def MyFirstFunction(name):
    '函数文档在函数定义的最开头部分，用不记名字符串表示'
    print('I love FishC.com!')
MyFirstFunction('fs')

print(MyFirstFunction.__doc__)
help(MyFirstFunction)

def mFun(*param,base=3):
    result=0
    for each in param:
        result+=each
    result*=base
    print('输出结果：%d'%result)
mFun(2,3,5,6,base=5)

def water():
    for x in range(100,1000):
        a=x//100
        b=(x%100)//10
        c=x%10
        if x==a**3+b**3+c**3:
            print('%d是水仙花数' % x)
water()

#字符串查重
# def findstr():
#     str1=input('请输入字符串:')
#     str2=input('请输入子字符串：')
#     count=0
#     for i in range(len(str1)-1):
#         if str1[i]==str2[0]and str1[i+1]==str2[1]:
#             count+=1
#     print('子字母串在目标字符串中共出现%d次'%count)
# findstr()

#019
def next():
    print('我在next()函数里...')
    pre()
def pre():
    print('我在pre()函数里...')
next()

def fun(var):
    var=1314
    print(var,end='')
var=520
fun(var)
print(var)

var='Hi'
def fun1():
    global var
    var='Baby'
    return fun2(var)
def fun2(var):
    var+='I Love You'
    fun3(var)
    return var      #这里就返回了
def fun3(var):
    var='fishc'    #这里非全局
print(fun1())

#检测回文联
# def hui():
#     x=input('请输入一句话：')
#     y=x[::-1]           #或者y=''.join(reversed(str))
#     for i in range((len(x))):
#         if x[i]!=y[i]:
#             print('不是回文联')
#             break
#         else:
#             print('是回文联')
#             break
# hui()

def count(*param):
    for i in range(len(param)):
        letters=0
        digits=0
        spaces=0
        others=0
        for each in param[i]:
            if each.isalpha():
                letters+=1
            elif each.isdigit():
                digits+=1
            elif each==' ':
                spaces+=1
            else:
                others+=1
        print('第%d个字符串共有：%d个英文字母,%d个数字,%d个空格,%d'
              '个其它字符。'%((i+1),letters,digits,spaces,others))
count('fishc.com ')

#20闭包
def funOut():
    def funIn():
        print('bingo！')
    return funIn()
funOut()

#021匿名函数
op=lambda x,y=3:x*y
print(op(5,9))

def mufun(x):
    if x%2:                 #奇数返回x,否则返回None
        return x
    else:
        return None
print(mufun(5))

list1=[1,2,0,True]
print(list((filter(None,[1,2,0,True]))))


print(list(filter(lambda x:not (x%3),range(100))))
#filter(不想要的条件,范围）
def ThreeFun():
    list1=[]
    for i in range(100):
        if i%3==0:
            list1.append(i)
    return list1
print(ThreeFun())

print(list(zip([1,3,5,7],[2,4,6,8])))

print(list(map(lambda x,y:[x,y],[1,3,5],[2,4,6])))      #map(函数，all变量)

def make_repeat(n):
    return lambda s:s*n
print(make_repeat(2)(8))
double=make_repeat(2)
print(double('Fishc'))

#022 递归条件（函数调用自身、正确返回值)
def gcd(x,y):
    t=x%y
    if y%t==0:
        return t
    else:
        x=y
        y=t
        return gcd(x,y)
print(gcd(7,49))

def power(x,y):
    if y:
        return x*power(x,y-1)
    else:
        return 1
print(power(2,0))
#下面这种方法不能返回0次幂
# def power(x,y):
#     if y == 1:
#         return x
#     else:
#         return x * power(x,y-1)
# print(power(2,3))

#023 and 024
#递归进制
def Dec2Bin(x):
    result=''
    if x:
        result=Dec2Bin(x//2)        #如果是Dec2Bin，先执行x=1,再x=2,4,8
        return result+str(x%2)
    else:
        return result
print(Dec2Bin(8))

print('5'+str(5%2))

#递归数字
list2=[]
def get_digits(n):
    if n:
        list2.insert(0,n%10)
        get_digits(n // 10)
        return list2
print(get_digits(341))

print(31//10,3%10)
#递归回文
# def Hui(n,start,end):
#     if start>end:
#         return 1
#     else:
#         if n[start]==n[end]:
#             return Hui(n,start+1,end-1)
#         else:
#             return 0
# string=input('请输入一串字符:')
# if Hui(string,0,len(string)-1):
#     print('是回文')
# else:
#     print('不是回文')

#递归年龄
#第一个人是10岁，后面每一个比前一个大2岁，只要知道人数即可！
def old(x):
    if x==1:
        return 10
    else:
        return 2+old(x-1)
print(old(5))



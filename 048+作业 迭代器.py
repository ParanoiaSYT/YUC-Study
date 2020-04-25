#提供迭代方法的容器
# 迭代器就是实现了__next__()方法的对象（用于遍历容器中的数据）。
# 迭代器看做可迭代对象的函数化，不用每次都for循环（不过一般情况下不用将可迭代对象封装为迭代器）

print('shasjangn',
      'ssahhgaga',
      'sjahghadnqf')

#iter()     魔法方法__iter__()
#next()     魔法方法__next__()
string='Fishc'
it = iter(string)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
#如果没有元素了，就会报错StopIteration

#斐波那契数列
class Fibs:
    def __init__(self,n=20):        #加一个迭代器的控制变量
        self.a=0
        self.b=1
        self.n=n
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>self.n:           #进行限制
            raise StopIteration
        return self.a

f=Fibs(100)
for each in f:
#     if each<25:
    print(each)
#     else:
#         break


print('=============================================================')

#####⚠️作业

#for each in range(5):
    # print(each)

#就等于下面
# iter() 函数用来生成迭代器。
#迭代器是一个可以记住遍历的位置的对象。
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。

a=range(5)
it=iter(a)
while True:
    try:
        print(next(it))
    except StopIteration:
        break

#闰年
import datetime         #常用来获得今天的时间

a=datetime.date.today()
print(a,a.year,a.month,a.day,end='\n')

class LeapYear:
    def __init__(self):
        self.now=datetime.date.today().year

    def __iter__(self):
        return self

    def __next__(self):
        while not self.isLeapYear(self.now):     #如果是闰年就跳出循环
            self.now-=1
        temp=self.now
        self.now-=1             #是闰年的话把值给temp，然后-1(如果触发迭代就继续循环）
        return temp

    def isLeapYear(self,year):
        if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
            return True
        else:
            return False

learYears=LeapYear()
for i in learYears:             #for循环触发迭代
    if i >= 2000:
        print(i)
    else:
        break

#序列翻转
class MyRev:
    def __init__(self,name):
        self.name=name
        self.index=len(name)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index==0:
            raise StopIteration
        self.index-=1           #长度和索引值区别
        return self.name[self.index]

myRev = MyRev("FishC")
for i in myRev:
    print(i, end='')

print('\n==============================================\n下面是自己的方案')
class MyRev:
    def __init__(self,name):
        self.name=name
        self.list1=list(x for x in name)
        self.list1.reverse()
        self.y=-1               # 此处-1为了让第一个元素返回
    def __iter__(self):
        return self

    def __next__(self):
        self.y+=1
        if self.y>len(self.name)-1:
            raise StopIteration
        temp = self.list1[self.y]       #这样呼应前面就从第一个元素开始返回
        return temp

myRev = MyRev("FishC")
for i in myRev:
    print(i, end='')
# 036
# 人名类
class Person():
    def setName(self, name='小甲鱼'):
        self.name = name
        print(self.name)

a = Person()
a.setName()
a.setName('王多余')

# 矩形类
# class Rectangle:
#     length = 5
#     width = 4
#
#     def setRect(self):
#         print('请输入矩形的长和宽...')
#         self.length = float(input('长：'))
#         self.width = float(input('宽：'))
#
#     def getRect(self):
#         print('矩形的长和宽分别为:%.2f和%.2f' % (self.length, self.width))
#
#     def getArea(self):
#         S = self.length * self.width
#         print('矩形的面积为：%d' % S)
#
# b = Rectangle()
# b.setRect()
# b.getRect()
# b.getArea()

# 037
class MyClass:
    name = 'FishC'

    def myFun(self):
        print("Hello FishC!")

print(MyClass.name)
a=MyClass()
a.myFun()

#游乐园票价
# class Ticket():
#     def __init__(self,weekend=False):
#         price = float(input('平日票价为：'))
#         if weekend:
#             self.price=price*1.2
#         else:
#             self.price=price
#     def all_price(self,adult=1,child=0):
#         adult=int(input('请输入成年人数量：'))
#         child=int(input('请输入儿童数量：'))
#         cost=adult*self.price+child*self.price/2
#         print('%d个成年人和%d个儿童共需%.2f元'%(adult,child,cost))
# a=Ticket(weekend=1)
# a.all_price()

#乌龟吃鱼
import random as r
legal_x=[0,10]
legal_y=[0,10]

class Gui():            #乌龟的操作有：能量变化，移动，吃鱼
    def __init__(self):
        self.power=100
        self.x=r.randint(legal_x[0],legal_x[1])
        self.y=r.randint(legal_y[0],legal_y[1])
        # speed=int(input('乌龟每次移动的步伐为speed='))
    def move(self,speed=1):
        new_x=self.x+r.choice([speed,-speed])
        new_y=self.y+r.choice([speed,-speed])

        if new_x<legal_x[0]:
            self.x=legal_x[0]-(new_x-legal_x[0])
        elif new_x>legal_x[1]:
            self.x=legal_x[1]+(legal_x[1]-new_x)
        else:
            self.x=new_x

        if new_y<legal_y[0]:
            self.y=legal_y[0]-(new_y-legal_y[0])
        elif new_y>legal_y[1]:
            self.y=legal_y[1]+(legal_y[1]-new_y)
        else:
            self.y=new_y

        self.power-=1
        return (self.x,self.y)

    def eat(self):
        self.power+=20
        if self.power>100:
            self.power=100

class Fish():
    def __init__(self):
        self.x=r.randint(legal_x[0],legal_x[1])
        self.y=r.randint(legal_y[0],legal_y[1])
    def move(self):
        new_x=self.x+r.choice([1,-1])
        new_y=self.y+r.choice([1,-1])

        if new_x < legal_x[0]:
            self.x = legal_x[0] - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            self.x = legal_x[1] + (legal_x[1] - new_x)
        else:
            self.x = new_x

        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            self.y = legal_y[1] + (legal_y[1] - new_y)
        else:
            self.y = new_y

        return (self.x,self.y)

# class Goldfish(Fish):
#     pass
# class Carp(Fish):
#     pass
# class Salmon(Fish):
#     pass
# class Shark(Fish):
#     def __init__(self):       #子类重写了父类的方法就会覆盖
#         # Fish.__init__(self)         #未绑定的父类，给的是子类的实例对象
#         super(Shark, self).__init__()      #或者用super函数方法（不用给出继类名字）
#         self.hungry=True
#     def eat(self):
#         if self.hungry==True:
#             print('吃吃吃吃吃次吃吃吃')
#             self.hungry=False
#         else:
#             print('吃饱了')
# shark=Shark()
# shark.eat()

gui=Gui()
fish=[]     #鱼群列表
for i in range(10):
    new_fish=Fish()
    fish.append(new_fish)

while True:
    if not len(fish):
        print('鱼🐟都被吃完啦！')
        break
    elif not gui.power:
        print('乌龟的能量耗完啦')
        break

    pos=gui.move()

    # 在迭代器中删除列表元素是非常危险的，经常会出现意想不到的问题，因为迭代器是直接引用列表的数据进行引用
    # 这里我们把列表拷贝给迭代器，然后对原列表进行删除操作就不会有问题了^_^
    for each_fish in fish.copy():
        if each_fish.move()==pos:
            gui.eat()
            fish.remove(each_fish)
            print('一条鱼🐟被吃掉啦！')

#038继承
# __init__(self):   #魔法方法init最多只能返回None

#覆盖
class Bird():
    def fly(self):
        print('fly away!')
class Penguin(Bird):
    def fly(self):
        pass
p=Penguin()
p.fly()        #这样就能覆盖父类的fly

#多重继承(导致钻石继承问题等等）
class A():
    def __init__(self):
        print("进入A…")
        print("离开A…")
class B(A):
    def __init__(self):
        print("进入B…")
        A.__init__(self)
        print("离开B…")
class C(A):
    def __init__(self):
        print("进入C…")
        A.__init__(self)
        print("离开C…")
class D(B, C):
    def __init__(self):
        print("进入D…")
        B.__init__(self)
        C.__init__(self)
        print("离开D…")
d=D()
print('==========================')
#修改为：
class A():
    def __init__(self):
        print("进入A…")
        print("离开A…")
class B(A):
    def __init__(self):
        print("进入B…")
        super().__init__()
        print("离开B…")
class C(A):
    def __init__(self):
        print("进入C…")
        super().__init__()
        print("离开C…")
class D(B, C):
    def __init__(self):
        print("进入D…")
        super().__init__()
        print("离开D…")
d=D()

#点和直线
import math as m
class Point():
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
class Line():
    def __init__(self,p1,p2):
        self.l=p1.getX()-p2.getX()
        self.w=p1.getY()-p2.getY()
    def getLen(self):
        L=m.sqrt(self.l**2+self.w**2)
        print('直线的长度为：%s'%L)
p1=Point(1,2)
p2=Point(4,5)
l=Line(p1,p2)
l.getLen()

#039

#继承和组合
# 根据实际应用场景确定。简单的说，组合用于“有一个”的场景中，继承用于“是一个”的场景中。
# 例如，水池里有一个乌龟，天上有一个鸟，地上有一个小甲鱼，这些适合使用组合。
# 青瓜是瓜，女人是人，鲨鱼是鱼，这些就应该使用继承啦。

class BB:
    def printBB(self):         #一定要有这个self
        print("no zuo no die")
bb = BB()
bb.printBB()

#实例化一个+1，删除一个-1
class C:
    count = 0
    def __init__(self):
        C.count += 1
    def __del__(self):
        C.count -= 1
a = C()
b = C()
c = C()
del a
print(C.count)

#栈（Stack）类
class Stack():
    def __init__(self,start=[]):
        self.stack=[]
        for i in start:
            self.push(i)
    def isEmpty(self):
        return not self.stack
    def push(self,x):
        self.stack.append(x)
    def pop(self):
        self.stack.pop()
    def top(self):
        return self.stack[-1]
    def bottom(self):
        return self.stack[0]
s=Stack([2,5,7,4,9])
s.push(5)
print(s.top())
print(s.bottom())

#040
#修饰符,用来对@下的函数进行修饰(给一颗圣诞树添加饰品）
import time
def timeslong(func):
    def call():
        start = time.perf_counter()         #time.perf_counter(),返回计时器的精准时间（系统的运行时间），包含整个系统的睡眠时间。
                                            # 由于返回值的基准点是未定义的，所以，只有连续调用的结果之间的差才是有效的。
        print("It's time starting ! ")
        func()
        print("It's time ending ! ")
        end = time.perf_counter()
        return "It's used : %s ." % (end - start)
    return call
@timeslong
def f():
    y = 0
    for i in range(10):
        y = y + i + 1
        print(y)
    return y
print(f())          #计算数10个数所需的时间，详情见（https://fishc.com.cn/thread-128529-1-1.html）

#‘@’修饰符必须出现在函数定义前一行，不允许和函数定义在同一行。
# 只可以在模块或类定义层内对函数进行修饰，不允许修饰一个类。
# @修饰符更像是装饰器的一个浓缩，一个语法糖

#描述符property()
class D:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
    x = property(getx, setx, delx, "I'm the 'x' property.")
d1=D()
d1.x=20
print(d1.x,d1._x)
#和下面功能一样
class C1:
    def __init__(self):
        self._x = None
    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x
    @x.setter                #名字不是乱取的...
    def x(self, value):
        self._x = value
    @x.deleter              #名字不是乱取的...
    def x(self):
        del self._x
c=C1()
print(c.x)
c.x=32
print(c.x,c._x)
del c.x

#041
#######
class FileObject:
    '''给文件对象进行包装从而确认在删除时文件流关闭'''

    def __init__(self, filename='sample.txt'):
        #读写模式打开一个文件
        self.new_file = open(filename, 'r+')

    def __del__(self):
        self.new_file.close()
        del self.new_file


f=FileObject('boy_1.txt')
print(f.new_file.read())
del f

#C2F
class C2F(float):
    def __new__(cls, arg=0.0):
        return float.__new__(cls,arg*1.8+32,)
print(C2F(30))

#新int
class Aint(int):
    def __new__(cls, arg=0):
        if isinstance(arg,str):
            total=0
            for i in arg:
                total+=ord(i)
            arg= total
        return int.__new__(cls,arg)
a=Aint('sag')
b=Aint(234)
c=Aint('23A')       #A的ASCII码是65，2和3也返回ASCII码加起来了
print(a,b,c)

#042
class Nstr(str):
    def __sub__(self, other):
        for i in self:
            for j in other:
                if i==j:
                    return self.replace(i,'')
a=Nstr('fishfish')
b=Nstr('sssccc')
print(a-b)

class Nstr(str):
    def __lshift__(self, other):
        return self[other:]+self[:other]
    def __rshift__(self, other):
        return self[-other:]+self[:-other]
n=Nstr('abcdefg')
print(n.__lshift__(2))
print(n.__rshift__(2))

#字符串加减乘除
class Nstr(str):
    def __init__(self,arg=''):
        if isinstance(arg,str):
            self.total=0
            for i in arg:
                self.total+=ord(i)
        else:
            print('传入参数非字符串！')
    def __add__(self, other):
        return  self.total+other.total
    def __sub__(self, other):
        return  self.total-other.total
    def __mul__(self, other):
        return  self.total*other.total
    def __truediv__(self, other):
        return  self.total/other.total
a=Nstr('abc')
b=Nstr('ABC')
print((a-b),(a+b),a*b,a/b)
#或者这样实现
class Nstr(int):
    def __new__(cls, arg=0):
        if isinstance(arg, str):
            total = 0
            for each in arg:
                total += ord(each)
            arg = total
        return int.__new__(cls, arg)
a=Nstr('abc')
b=Nstr('ABC')
print((a-b),(a+b),a*b,a/b)

#043

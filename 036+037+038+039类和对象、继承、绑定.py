#对象模拟真实事件,封装
#对象=属性(变量）+方法（函数）
#类class(可以看作图纸，实例化后变为实体）
#类的实例化
class Turtle:
    #属性
    color='green'
    weight=10
    legs=4
    shell=True
    mouth='大嘴巴'
    #方法
    def climb(self):
        print('我正在努力爬')
    def run(self):
        print('飞快跑')
    def bite(self):
        print('咬人啦')
    def eat(self):
        print('吃东西吧')
    def sleep(self):
        print('睡了睡了')

tt=Turtle()
tt.climb()
tt.sleep()
print(tt.color)

#面向对象Object Oriented(OO)
#封装
list1=[2,3,5,1,8,7,0]   #封装了列表的实现，只告诉我们需要的用法
list1.sort()
print(list1)
list1.append(4)
print(list1)
#继承
class Mylist(list):
    pass
list2=Mylist()
list2.append(5)
list2.append(4)
print(list2)
list2.sort()
print(list2)
#多态(不同对象对同一方法响应不同的行动）
class A:
    def fun(self):
        print('我是AAA')
class B:
    def fun(self):
        print('我是BBB')
a=A()
b=B()
a.fun()
b.fun()     #函数名都是fun,但实现不一样


class Ball():
    def setName(self,name):
        self.name=name
    def kick(self):
        print('我叫%s坤,谁黑我？'%self.name)
a=Ball()
a.setName('王多余')
b=Ball()
b.setName('xiaoB')
c=Ball()
c.setName('dongdong')
a.kick()
b.kick()
c.kick()


#构造方法
class Ball:
    def __init__(self,name='优酷'):    #init可视为实例化对象的参数自启动
        self.name=name
    def kick(self):
        print('我叫%s坤,谁黑我？'%self.name)
d=Ball('土豆')
d.kick()
e=Ball()    #默认参数
e.kick()

# 1.在类的方法内使用类的属性变量，需要：self.变量名
# 2.因为py使用普通变量不需定义，在方法内不加self.会被当成普通变量
# 3.这种普通变量不是类共有的，是方法私有的，不可以类外访问，其他方法也不能用

#公有和私有
class Person:
    name='cxk'
p=Person()
print(p.name)   #对象的属性和方法属于公有
#python中定义私有变量只要在变量名或函数名前加双下划线即可
# class Person:
#     __name='cxk'
#     p = Person()
# print(p.name)   #私有无法访问

class Person:
    __name='cxk'
    def getName(self):
        return self.__name
p=Person()
print(p.getName())  #可以通过内部返回
print(p._Person__name)  #也可以通过这样来查看（伪私有）

#继承
class Parent():
    def hello(self):
        print('Hi~')
class Child(Parent):
    pass        #pass就相当于占位符
c=Child()
c.hello()
#子类里如果有和父类相同的函数什么的，之会调用子类自身的
class Child(Parent):
    def hello(self):
        print('这是子类')
c=Child()
c.hello()

#鱼类继承
import random as r
legal_x=[0,10]
legal_y=[0,10]
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

class Goldfish(Fish):
    pass
class Carp(Fish):
    pass
class Salmon(Fish):
    pass
class Shark(Fish):
    def __init__(self):       #子类重写了父类的方法就会覆盖
        # Fish.__init__(self)         #未绑定的父类，给的是子类的实例对象(需要写除父类Fish）
        super().__init__()      #或者用super函数方法（不用给出基类名字），自动找出所有基类和方法
        self.hungry=True
    def eat(self):
        if self.hungry==True:
            print('吃吃吃吃吃次吃吃吃')
            self.hungry=False
        else:
            print('吃饱了')
shark=Shark()
shark.eat()

#多重继承
class Base1:
    def foo1(self):
        print('我fool,sss')
class Base2:
    def foo2(self):
        print('我是foo2...')
class C(Base1,Base2):
    pass
c=C()
c.foo1()
c.foo2()

#039类组合(没有继承关系）
class Turtle:
    def __init__(self,x):
        self.num=x
class Fish:
    def __init__(self,x):
        self.num=x
class Pool:
    def __init__(self,x,y):
        self.turtle=Turtle(x)
        self.fish=Fish(y)
    def print_num(self):
        print('池塘里共有%d条鱼和%d个乌龟'%(self.turtle.num,self.fish.num))

pool=Pool(2,8)
pool.print_num()

#
class C():
    count=0        #静态属性(类定义）
a=C()
b=C()
c=C()               #a,b,c属于实例对象
print(a.count)
a.count+=10
print(a.count,b.count)
C.count+=100    #注意这里是类对象变化
print(a.count,b.count,c.count)

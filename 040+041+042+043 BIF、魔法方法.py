#040
# issubclass(class,classinfo)   class是classinfo的子类则返回True
class A:
    pass
class B(A):
    pass
print(issubclass(B,A))
print(issubclass(B,B))
print(issubclass(B,object))     #object是所有类的继类
class C:
    pass
print(issubclass(A,B))

#isinstance(object,classinfo)   如果第一个参数不是对象,则永远返回False
b=B()
print(isinstance(b,B))
print(isinstance(b,A))      #A是B的父类
print(isinstance(b,(A,B,C)))

#测试对象是否有对应属性
print("=============================")
class C:
    def __init__(self,x=0):
        self.x=x
c1=C()
print(hasattr(c1,'x'))     #hasattr第二个参数属性要用字符串符号扩起来
print(hasattr(c1,'y'))      #True or False

print(getattr(c1,'x'))      #返回x参数值
print(getattr(c1,'y','无此属性'))   #第三个值为不存在时返回值，不设置则会报错
setattr(c1,'y','FISHCCCC')      #设置属性,没有则新建
print(getattr(c1,'y'))
delattr(c1,'y')   #不存在就会异常
print(getattr(c1,'y','无此属性'))

# property
class C:
    def __init__(self,size=10):
        self.size=size
    def getSize(self):
        return self.size
    def setSize(self,value):
        self.size=value
    def delSize(self):
        del self.size
    x=property(getSize,setSize,delSize)
c1=C()
print(c1.getSize())
print(c1.x)
c1.x=18
print(c1.getSize())
del c1.x
# print(c1.size)

# property相当于一个统一端口,对于用户来说，即使改函数名也没有影响
# property(fget=None,fset=None,fdel=None,doc=None)具体函数方法需要程序员自己设计

#构造和析构
class Rectangle():
    def __init__(self,x,y):     #需求传入2个参数
        self.x=x
        self.y=y
    def getPeri(self):
        return 2*(self.x+self.y)
    def getArea(self):
        return self.x*self.y
rect=Rectangle(4,5)
print(rect.getArea())
print(rect.getPeri())

#__new__方法
class CapStr(str):      #str是不可修改的
    def __new__(cls,string):        #__new__用来修改继承父类的参数方法，相当于打开权限
        string=string.upper()
        return str.__new__(cls,string)      #修改完再调用str的__new__
a=CapStr('ansbagKKSJSYMS')
print(a)

#__del__(self)
#垃圾回收机制
class C:
    def __init__(self):
        print('我是__init__方法，我被调用了')
    def __del__(self):
        print('我是__del__方法，我被调用了')
c1=C()
c2=c1
c3=c2
print('========')
del c3
del c2
del c1      #所有标签都被del后，才会出现垃圾回收机制

#042算数运算1
# 工厂函数
print(type(len))
print(type(int))
print(type(list))
class C:
    pass
print(type(C))

a=int('123')    #a就是int的实例对象
b=int('355')
print(a+b)

#算数操作符__add__,__sub__魔法方法
class New_int(int):
    def __add__(self, other):
        return int.__sub__(self,other)
    def __sub__(self, other):
        return int.__add__(self,other)
a=New_int(3)
b=New_int(5)
print(a+b,a-b)

class Try_int(int):
    def __add__(self, other):
        return int(self)+other
    def __sub__(self, other):
        return int(self)-other
a=Try_int(4)
b=Try_int(6)
print(a+b)

print(divmod(5,3))      #divmod(a,b)==(5%2,5//2)

#043算数运算2
# class int(int):
#     def __add__(self, other):
#         return int.__sub__(self,other)
# a=int('5')
# b=int('7')
# print(a,b,a+b)

#__radd__反运算
class Nint(int):
    def __radd__(self, other):
        return int.__sub__(other,self)      #self为实例对象（顺序对应减法顺序不同）
        # return int.__sub__(self,other)
a=Nint(5)
b=Nint(3)
print(a+b)
print(5+b)      #触发了b的__radd__方法

class Oint(int):
    def __rsub__(self, other):
        return int.__sub__(self,other)
a=Oint(5)
print(3-a)        #变成了a-3


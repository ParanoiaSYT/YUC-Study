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
# property(fge=None,fset=None,fdel=None,doc=None)具体函数方法需要程序员自己设计


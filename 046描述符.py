#描述符就是将某种特殊类型的类的实例指派给另一个类的属性
class MyDecriptor:
    def __get__(self,instance,owner):
        print('getting',self,instance,owner)
    def __set__(self,instance,value):
        print('setting',self,instance,value)
    def __delete__(self, instance):
        print('deleting',self,instance)

class Test:
    x=MyDecriptor()

test=Test()
test.x
test.x='x-man'
del test.x

#===================================
class Myproperty:
    def __init__(self,fget=None,fset=None,fdel=None):
        self.fget=fget
        self.fset=fset
        self.fdel=fdel
    def __get__(self,instance,owner):
        return self.fget(instance)
    def __set__(self,instance,value):
        self.fset(instance,value)
    def __delete__(self, instance):
        self.fdel(instance)
class C:
    def __init__(self):
        self._x=None
    def getX(self):
        return self._x
    def setX(self,value):
        self._x=value
    def delX(self):
        del self._x
    x=Myproperty(getX,setX,delX)

c=C()
c.x='x-man'
print(c.x,c._x)

#温度转换
class C2F:
    def __init__(self,tem=26.0):
        self.tem=float(tem)
    def setX(self,value):
        self.tem=float(value)
    def getX(self):
        self.tem=(self.tem*1.8+32)
        print('对应的华氏度为：%d度' %self.tem)
    x=property(getX,setX)
c1=C2F(20)
c1.x

#=====================
class Celsius:              #摄氏度描述符
    def __init__(self,value=26):
        self.value=float(value)
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        self.value=float(value)

class Fahrenheit:           #华氏度描述符
    def __init__(self,value=80):
        self.value=float(value)
    def __get__(self, instance, owner):
        return instance.cel*1.8+32
    def __set__(self, instance, value):
        instance.cel=float((value)-32)/1.8

class Temperature:
    cel=Celsius()
    fah=Fahrenheit()

tem=Temperature()
print(tem.cel)
print(tem.fah)
tem.cel=36
print(tem.fah)
tem.fah=100
print(tem.cel)

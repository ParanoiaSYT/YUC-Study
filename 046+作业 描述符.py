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


print('=========================================')
################################################################################
# 简单说描述符就是一个类，一个至少实现 __get__()、__set__() 或 __delete__() 三个特殊方法中的任意一个的类。

class MyDes:
    def __init__(self, value = None):
        self.val = value

    def __get__(self, instance, owner):
        return self.val - 20

    def __set__(self, instance, value):
        self.val = value + 10
        print(self.val)
class C:
    x = MyDes()

if __name__ == '__main__':  # 该模块被执行的话，执行下边语句。
    c = C()
    c.x = 10
    print(c.x)

print('=========================================')
#访问实例层次上的描述符 x，只会返回描述符本身。为了让描述符能够正常工作，它们必须定义在类的层次上。
# 如果你不这么做，那么 Python 无法自动为你调用 __get__ 和 __set__ 方法。
class MyDes:
    def __init__(self, value = None):
            self.val = value
    def __get__(self, instance, owner):
            return self.val ** 2

class Test:
    def __init__(self):
            self.x = MyDes(3)

    # x=MyDes(3)           #换成这句就可以返回9了

test = Test()
print(test.x)       #不会返回9

print('=========================================')
#描述符不像属性访问，get,set都是自己写的，没有自动过程，不会产生"无限递归"

class MyDes:
    def __init__(self,initval=None,name=None):
        self.val=initval
        self.name=name
    def __get__(self,instance,owner):
        print('做出访问了',self.name)
        return self.val
    def __set__(self, instance, value):
        print('属性修改了',self.name)
        self.val=value
    def __delete__(self, instance):
        print("正在删除变量：", self.name)
        print("噢~这个变量没法删除~")

class Test:
    x=MyDes(10,'x')             #注意这里属性名要加引号

c=Test()
c.x
c.x=33
print(c.x)
del c.x

print('=========================================')
#记录指定变量的读取和写入操作，并将记录以及触发时间保存到文件（record.txt）
import time
print(time.ctime())         #time.ctime()返回以专门格式返回现在的时间
class Record:
    def __init__(self,initval=None,name=None):
        self.val=initval
        self.name=name
        self.filename="record.txt"
    def __get__(self, instance, owner):
        with open('record.txt','a') as f:           #打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。
                                                   # 也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
             f.write('%s变量被读取了:%s=%s，时间为%s\n'%(self.name,self.name,self.val,time.ctime()))
        return self.val
    def __set__(self, instance, value):
        self.val=value
        with open('record.txt', 'a') as f:
            f.write('%s变量被写入了:%s=%s，时间为%s\n' % (self.name, self.name, self.val, time.ctime()))
    def __delete__(self, instance):
        with open('record.txt', 'a') as f:
            f.write('%s变量被删除了:%s=%s，时间为%s\n' % (self.name, self.name, self.val, time.ctime()))
        del self.name

class Test():
    x=Record(66,'y')

test=Test()
print(test.x)   #读取
test.x=999      #写入
test.x          #读取

print('=========================================')
#加上pickle技术
# 编写描述符 MyDes，使用文件来存储属性，属性的值会直接存储到对应的pickle的文件中。如果属性被删除了，文件也会同时被删除，属性的名字也会被注销。
import os
import pickle
print(time.ctime())
class Record:
    saved=[]
    def __init__(self,initval=None,name=None):
        self.val=initval
        self.name=name
        self.filename=self.name+'.pkl'

    def __get__(self, instance, owner):
        if self.name not in Record.saved:
            raise AttributeError('%s 属性未赋值！'%self.name)
        else:
            with open(self.filename,'rb')as f:
                value=pickle.load(f)
        return value

    def __set__(self, instance, value):
        self.val=value
        with open(self.filename,'wb') as f:
            pickle.dump(value,f)
            Record.saved.append(self.name)

    def __delete__(self, instance):
        # with open(self.filename,'wb') as f:       #这样删除只会删掉f中的内容
        #     del f

        os.remove(self.filename)
        Record.saved.remove(self.name)
        del self.name

class Test():
    x=Record(66,'m')

test=Test()
test.x=40
test.x=66
del test.x
# print(test.x)
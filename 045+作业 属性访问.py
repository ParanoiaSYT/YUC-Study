class C:
    def __init__(self):
        self.x='x-Man'
c1=C()
print(c1.x)
print(getattr(c1,'x','没有这个属性!'))
print(getattr(c1,'y','没有这个属性!'))

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

c=C()
print(c.x)
c.x=999
print(c.x)
del c.x

##属性访问魔法方法
class C:
    def __getattribute__(self, item):   #属性被访问时的行为
        print('getattribute')
        # return super().__getattribute__(item)       #此处如果没有return也一样
        super().__getattribute__(item)
    def __getattr__(self, item):        #试图获取一个不存在的属性行为
        print('getattr')
    def __setattr__(self, key, value):
        print('setattr')
        super().__setattr__(key,value)
    def __delattr__(self, item):
        print('delattr')
        super().__delattr__(item)

c=C()
c.y
c.y=1       #设置后属性就存在了
c.y         #不存在
del c.y

#矩形类
class Rectangle:
    def __init__(self,length=5,width=4):
        self.length=length
        self.width=width
    def __setattr__(self, key, value):
        print('正方形')
        if key=='square':
            self.length=self.width=value
        else:
            super().__setattr__(key,value)      #方法一
            # self.__dict__[key]=value          #方法二也可以解决无限递归的问题

    def getArea(self):
        return self.length*self.width
    def __delattr__(self, item):
        print('delattr')
        super().__delattr__(item)
r=Rectangle()
print(r.getArea())
r.square=5
print(r.length,r.width,r.getArea())

print(r.__dict__)
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


def fun1():
    print('fun1()正在被调用...')
    def fun2():
        print('fun2()正在被调用...')
    fun2()
#fun2()为内嵌函数，但只能通过调用fun1()来调用
fun1()

def FunX(x):
    def FunY(y):
        return x*y
    return FunY
#内部函数FunY调用了外部函数FunX的变量x，FunY就称为闭包closure
i=FunX(8)
print(type(i))
print(i(5))
print(FunX(8)(5))

def Fun1():
    x=5
    def Fun2():
        nonlocal x      #内部函数修改外部函数的局部变量
        x *= x
        return x
    return Fun2()
print(Fun1())


#lambda表达式(在不需要专门定义函数、不用考虑起名的时候用）
#创建匿名函数(没有专属名）
def ds(x):
    return 2*x+1
print(ds(5))
g=lambda x:2*x+1   #匿名函数（没有def名字
print(g(5))

def add(x,y):
    return x+y
print(add(3,4))
pp=lambda x,y:x+y
print(pp(3,4))

#filter内置函数
print(list(filter(None,[1,0,False,True])))   #过滤非Ture的内容
#过滤出奇数
def odd(x):
    return x%2
temp=range(10)
show=filter(odd,temp)
print(list(show))

print(list(filter(lambda x:x%2,range(10))))  #通过lambda一步到位

#map内置函数
print(list(map(lambda x:x*2,range(10))))   #将后面可迭代参数都处理形成新序列（映射）



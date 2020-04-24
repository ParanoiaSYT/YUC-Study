#提供迭代方法的容器
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


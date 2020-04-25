#yield表明函数是生成器
# 协同程序调用，函数可以中断
def myGen():
    print('生成器被执行')
    yield 1             #看作不结束的return
    yield 2

myG=myGen()
print(next(myG))
print(next(myG))
# print(next(myG))      #没有元素就会StopIteration

for i in myGen():
    print(i)

def fab():
    a=0
    b=1
    while True:
        a,b=b,a+b
        yield a

f=fab()
for each in f:
    if each>100:
        break
    print(each,end=' ')

print('\n======================')
#列表推导式
a=[i for i in range(100) if not (i%2)and i%3]   #100以内被2整除但不能被3整除的数
print(a)

#字典推导式
b={i:i%2==0 for i in range(10)}     #10以内能否被2整除
print(b)

#集合推导式
c={i for i in[1,2,1,3,4,5,5,6,7,8,3,2]}
print(c)

#生成器推导式
d=(i for i in range(10))    #用一个小括号包起来
print(d)
print(next(d))
print(next(d))
for each in d:
    print(each,end=' ')

print('\n======================')

print(sum(i for i in range(100) if i%2))    #甚至在sum函数里不用括号扩起来也是生成器
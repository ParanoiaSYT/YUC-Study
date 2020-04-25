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

##作业
def myRev(item):
    length=len(item)
    while length>0:
        yield item[length-1]
        length-=1

# def myRev(data):
#     # 这里用 range 生成 data 的倒序索引
#     # 注意，range 的结束位置是不包含的
#     for index in range(len(data)-1, -1, -1):      #这样写更加简洁
#         yield data[index]

for i in myRev('Fishc'):
    print(i,end='')

print('\n==========================================')
#素数和
#我自己写的求素数函数运算太久了(逻辑没问题，速度比不上）
# def is_prime(num):
#     if num==2:return True
#     for i in range(2,num//2+1):
#         if num%i==0:
#             return False
#     return True

import math
def is_prime(num):
    if num > 1:
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(num) + 1), 2):        #两步一跨就快很多了
            if num % current == 0:
                return False
        return True
    return False

def sumPrime(num):
    while True:
        if is_prime(num):
            yield num
        num+=1

def solve():
    sum1=2
    for i in sumPrime(3):
        if i<20000:
            sum1+=i
        else:
            print(sum1)
            break
if __name__ =='__main__':
    solve()


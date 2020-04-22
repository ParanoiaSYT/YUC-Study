def recursion():
    return recursion()

#阶乘
#方式一
def jiechen(x):
    result=x
    while x>1:
        result=result*(x-1)
        x-=1
    return result
print(jiechen(5))
# #方式二
# def factorial1(n):
#     result = n
#     for i in range(1,n):
#         result *= i
#     return result
# number=int(input('请输入一个整数求阶乘:'))
# print(factorial1(number))
#
# #递归函数(1、调用函数自身。2、有正确返回值。)
# def factorial2(n):
#     if n == 1:
#         return 1
#     else:
#         return  n*factorial2(n-1)
# number = int(input('请输入一个整数求阶乘:'))
# print(factorial2(number))

#Fibonacci数列的迭代实现
def Fab(n):
    n1=1
    n2=1
    n3=1
    if n<1:
        print('输入错误！')
        return -1
    while n-2 >0:
        n3=n2+n1
        n1=n2
        n2=n3
        n-=1
    return n3
result=Fab(35)
if result !=-1:
    print('共有%d对小兔诞生！'% result)
#列表表示
def fib(n):
    if n==1:
        return [1]
    if n==2:
        return [1,1]
    fibs=[1,1]
    for i in range(2,n):
        fibs.append(fibs[-1]+fibs[-2])  #fib[-1]即为fib列表中倒数第一个元素。
    return fibs
print(fib(20))

list2=[1,3,4,6]
print(list2[-1])

#Fibonacci数列的递归实现(分治思想）(优雅但效率低）
def Fcc(n):
    if n<1:
        print('输入错误！')
        return -1
    if n==1 or n==2:
        return 1
    else:
        return Fcc(n-1)+Fcc(n-2)
result=Fcc(20)
if result !=-1:
    print('共计诞生%d对'% result)


#汉诺塔
def hanoi(n,x,y,z):
    if n==1:
        print(x,'->',z)
    else:
        hanoi(n-1,x,z,y)    #将前n-1个盘子从x移到y
        print(x,'->',z)     #将最底下一个盘子从x移到z
        hanoi(n-1,y,x,z)    #将y上的n-1移动到z
n=int(input('请输入汉诺塔层数：'))
hanoi(n,'第1根','第2根','第3根')



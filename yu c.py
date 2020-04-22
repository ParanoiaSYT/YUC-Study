# print('~~~~~~~~~~~~~我爱鱼C工作室~~~~~~~~~~~~~~~~')
# temp=input("不妨猜一下小甲鱼想的数字:")
# guess=int(temp)
# if guess == 8:
#     print("卧槽，你是蛔虫吗")
#     print("哼，猜中也没有奖励")
# else:
#     print("猜错了，现在想的是8")
# print("游戏结束，不玩了")

# teacher='小甲鱼'
# print(teacher)
# teacher='老甲鱼'
# print(teacher)
# first=3
# second=8
# third=first+second
# print(third)
#
# myteacher='小甲鱼'
# yourteacher='黑夜'
# ourteacher=myteacher+yourteacher
# print(ourteacher)#字符串拼接
#
# print(first)

print('fishc!=Fishc')

# print('5'+'8')
#
# print('let\'s go!')
# print("let's go!")
#
# str='c:\\now'
# print(str)
#
# str=r'c:\now\users''\\'
# print(str)
#
# str="""师傅家附近，\n看看国家机关叽叽咕咕，\n是开放港口开发全部放假带你飞"""
# print(str)

a=0.485
b=int(a)
c=float(a)
d=str(a)
print(b,c,d)

print(10//6)
print(5%2,11%2)

with open('Burning.txt') as f:
    for each_line in f:
        a=each_line.find('徐')
        print(a)
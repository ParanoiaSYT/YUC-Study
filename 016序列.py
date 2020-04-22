a=list()
print(a)

b='I love fishc'
b=list(b)
print(b)

c=(1,1,2,3,5,8,13,21,34)
c=list(c)
print(c)

#tuple把一个可迭代对象转换为元组
tuple1=c
print(tuple1)

print(max(1,2,3,6,7,24,89,9)) #返回最大值
print(max(b))
print(min(1,3,4,8,9,54,21,-9)) #返回最小值

chars='1234567890'
print(min(chars)) #ascii码中'0'字符对应16进制30，10进制48

print(max(tuple1))

numbers=[0,2,3,566,7544,2224,554,24]
numbers.append('a')
print(numbers) #字符串和数字没法比较（不同类型）

tuple2=(3.1,2.3,3.4)
sum(tuple2)
print(sum(tuple2)) #加起来(同类型）

# tuple3=('21','23','99')
# print(sum(tuple3))   #只有整型可加

print(sorted(b)) #从小到大排序

print(list(reversed(numbers))) #翻转

print(list(enumerate(numbers)))  #列表中元素添加索引值构成元组

a=[1,3,5,7,9]
b=[2,4,6,8,10,12,14]
print(list(zip(a,b)))  #成对匹配

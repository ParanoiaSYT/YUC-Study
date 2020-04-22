num={}
num2={1,2,3,4,5}
print(type(num),type(num2))
#set类型就是集合(没有体现映射关系）

num2={1,2,3,4,5,5,4,3,2,}
print(num2)     #集合的元素唯一，会自动剔除重复的；不支持索引

#通过花括号或者set工厂函数来创建集合
set1=set([1,2,3,4,5,5])
print(set1)

#剔除方法一
num1=[1,2,3,4,5,5,3,1,0]
temp=[]
for each in num1:
    if each not in temp:
        temp.append(each)
print(temp)
temp.sort()
print(temp)
#方法二（集合）
list1=[1,2,3,4,5,5,3,1,0]
list1=list(set(list1))
print(list1)    #set会自动排序

print(num2)
num2.add(6)
print(num2)
num2.remove(2)
print(num2)

#不可变集合(frozen set)
num3=frozenset([1,2,3,4,5])
num3.add(0)
print(num3)     
num3.remove(1)
print(num3)     #不可变集合无法添加、删除元素


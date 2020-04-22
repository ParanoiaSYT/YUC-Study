LGD=['maybe','chalice','fy','old eleven','xnova']
number=[1,2,3,4,5]
mix=[1,2,'maybe',[5,6,7]]
print(mix)

empty=[]
print(empty)

LGD.append('葫芦娃娃') #往列表里+一个元素
print(LGD)
print(len(LGD))
LGD.extend(['ame','一闪']) #extend为拓展一个列表
print(LGD)
print(len(LGD))

LGD.insert(0,'一门')  #从0位置开始
print(LGD)
print(LGD[0])

LGD.remove('一门')   #需要知道具体元素名
print(LGD)

del LGD[7] #直接为命令语句(注意从0开始）
print(LGD)

a=LGD.pop() #括号为空默认弹出最后一个元素
print(a)
print(LGD)
LGD.pop(5)
print(LGD )

#Slice列表分片
print(LGD[1:3])  #取头去尾
print(LGD[:4])

LGD2=LGD[:]   #通过这样可以复制列表，如果直接赋值会随另一个变化而变化。
print(LGD2)   #上一条针对python版本不同，可能会有差异
LGD.append('ame')
print(LGD,LGD2)


#列表操作符
list1=[11]
list2=[32]
print(list1<list2)
list1=[11,99]
list2=[66,10]
print(list1<list2,list1>list2)  #默认比较第零个元素
print(list1<list2 and list1==list1)

list3=list1+list2
print(list3)
list3.extend(['xjy'])
print(list3)

print(list3+['xjy'])  #无法通过+号直接加进列表
print(list3)

list3*=2
print(list3)   #直接print(list3 *=2)会报错（大概括号里只能用list3*2这种写法）

print('maybe' not in list3)
list5=[444,['maybe','小甲鱼'],999]
print('maybe' in list5)  #in 只反应一层成员关系
print('小甲鱼' in list5[1]) #通过指定可以

print(list5[1][1])

print(dir(list))

print(list5.count(999))

list5 *=3
print(list5.index(999,3,7)) #排第几

list5.reverse()  #列表翻转
print(list5)

list6=[3,67,3,4,7,9]
list6.sort()  #小到大排序
print(list6)
# list6.reverse()
# print(list6)
list6.sort(reverse=True)  #反向排序（大到小）
print(list6)

list7=list6[:]
list8=list6
list6.sort()
print(list6,list7,list8)  #分片和标签区别

#元组 tuple
tuple1=(1,3,5,5,5,6,6,7,8,9)
print(tuple1[1],tuple1[2:])
tuple2=tuple1[:]
print(type(tuple2))
temp=2,3,5,7
temp2=()
print(type(temp),type(temp2))
temp3=1,
print(type(temp3))  #通过逗号来创建元组

print(8*(8),8*(8,))

#可切片方法添加和删除元素
LGD=('maybe','chalice','old eleven','xnova')
LGD=LGD[:2]+('ame',)+LGD[2:] #添加ame
print(LGD)
LGD=LGD[:2]+LGD[3:] #删除ame
print(LGD)
del LGD  #删除这个标签（一般不需要）


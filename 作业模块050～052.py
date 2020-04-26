#050
# 如果你不想模块中的某个属性被 from…import * 导入，那么你可以给你不想导入的属性名称的前边加上一个下划线（_）。
# 不过需要注意的是，如果使用 import … 导入整个模块，或者显式地使用 import xx._oo 导入某个属性，那么这个隐藏的方法就不起作用了。

import const
const.NAME = "FishC"
print(const.NAME)

try:
    # 尝试修改常量
    const.NAME = "FishC.com"
except TypeError as Err:
    print(Err)

try:
    # 变量名需要大写
    const.name = "FishC"
except TypeError as Err:
    print(Err)

print('========================================================')
#__dict__可以获得属性值
class MyObj:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myFunc(self):
        pass

mo = MyObj('Boby', 24)
print(mo)
print(mo.__dict__)

print('========================================================')
# if __name__=='__main__':

print('========================================================')
answer=dict.fromkeys(range(16),0)
print(answer)
answer[0]='C'
answer[1]='D'   #错误，选了C    type(1J)是complex
answer[2]='B'
answer[3]='B'
answer[4]='D'
answer[5]='D'   #错误，选了B，需要给参数
answer[6]='D'   #小甲鱼缩进错误！
answer[7]='A'
answer[8]='D'
answer[9]='C'
answer[10]='D'
answer[11]='C'
answer[12]='C'
answer[13]='A'
answer[14]='D'  #错误，选了B（即使是浅拷贝，但是拷贝的列表是变量
answer[15]='B'  #错误，选了D（深拷贝，拷贝下来的是固定值非变量
print(answer)

print(type(1J))
print('========================================================')

values = [1, 1, 2, 3, 5]
nums = set(values)
print(nums)
print('========================================================')

dict1 = {}
dict1[1] = 1
dict1['1'] = 2
dict1[1.0] = 3
print(dict1)
print('========================================================')

def dostuff(param1, *param2):
    print(type(param2))
dostuff('apples', 'bananas', 'cherry', 'dates')

class A:
    def __init__(self, x):
        self.x = x
        x = 666
# a = A()       #这里有问题，需要给入一个参数
a = A(888)
a.x
print('========================================================')

list1 = [1, 2]
list2 = [3, 4]
dict1 = {'1':list1, '2':list2}
dict2 = dict1.copy()            #注意⚠️这里虽然是浅拷贝，但是list1是变量，相当于x，变量发生变化，对应的dict1,2,3都会变
dict3=dict1
dict1['1'][0] = 5
print(dict1,dict2,dict3)
result = dict1['1'][0] + dict2['1'][0]
print(result)
print('========================================================')

import copy
list1 = [1, 2]
list2 = [3, 4]
dict1 = {'1':list1, '2':list2}
dict2 = copy.deepcopy(dict1)    #这里是深拷贝，相当于dict2={'1':[1,2, '2':[3,4},已经突破了变量的束缚(固定了）
dict1['1'][0] = 5
result = dict1['1'][0] + dict2['1'][0]
print(result)
print('========================================================')


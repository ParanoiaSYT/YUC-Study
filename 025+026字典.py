brand = ['李宁', 'nike', 'addidas', 'fishc']
slogan = ['一切皆有可能', 'just do it', 'impossible is nothing', 'change the world']
print('fishc的口号是:', slogan[brand.index('fishc')])

# key,value,键值组合，映射
dict1 = {'李宁': '一切皆有可能', 'nike': 'just do it', 'addidas': 'impossible is nothing',
         'fishc': 'change the world'}  # 大括号表示字典，但注意不是序列类型
print('fishc的口号是:', dict1['fishc'])

dict2 = {1: 'one', 2: 'two', 3: 'three'}
print('1的英文是：', dict2[1])

dict3 = {}  # 空字典

help(dict)
dict4 = dict((('F', 70), ('i', 105), ('C', 67)))  # 元组伪装成一个参数
print(dict4)
print(type(('F', 70)))  # 元组类型

dict5 = dict(小甲鱼='xjy', 苍井空='cjk')  # key=小甲鱼/苍井空
print(dict5)
print(type('xjy'))  # 字符串类型

# 若修改字典里的key，会重新赋值；若字典里不存在，会重新创建
dict5['苍井空'] = '所有从业者都要学编程'
print(dict5)
dict5['爱迪生'] = '天才+汗水+灵感'
print(dict5)
# 工厂函数（类型）

print(dict3.fromkeys((1, 2, 3), 'Number'))
print(dict3.fromkeys((1, 2, 3), ('one', 'two', 'three')))  # 无法各个相对应修改
print(dict3.fromkeys((1, 3), '数字'))  # 创建新字典

# 关键词keys,values,items
dict3 = dict3.fromkeys(range(32), '赞')
print(dict3)
for eachkey in dict3.keys():
    print(eachkey)
for eachValue in dict3.values():
    print(eachValue)
for eachItems in dict3.items():
    print(eachItems)
print(dict3[31])

# get方法(只能get一个值)，逗号后可附加值（如为none）
print(dict3.get(1), dict3.get(32, '木有'))

print(31 in dict3, 32 in dict3)  # 成员关系资格检查(高效),查找的是key

# 清空字典
dict3.clear()
print(dict3)

# 注意clear和直接再赋空值的区别
a = {'姓名：': '小甲鱼'}
b = a
print(a['姓名：'])
a = {}
print(a, b, type(a), type('小甲鱼'))  # 只能清空a

a = b
print(type(a))
a.clear()
print(a, b, type(a))  # 清空的是a、b的整个字典

# copy浅拷贝
a = {1: 'one', 2: 'two', 3: 'three'}
b = a.copy()
c = a
print(a, b, c)
print(id(a), id(b), id(c))  # a和c位置一样是深拷贝（赋值）,b位置不同为浅拷贝(copy)
c[4] = 'four'
print(a, b, c)  # a和c同步变化,b不被干扰

# pop
print(a.pop(2))
print(a)
print(a.popitem())  # 字典里随机弹出一个（本版本似乎和列表一样弹最后一个元素）
print(a)  # 弹出后原来的里面就没有了

a.setdefault('小白')
print(a)
a.setdefault(5, 'five')
a.setdefault('小白',0)        #如果已经存在key了，就没有效果
print(a)

# updata用一个字典来更新另一个
b = {'XB':'狗'}
print(b)
a.update(b)
print(a)


#定制容器

#不可改变
# __len__(self)
#__getitem(self)

#会改变的方法
# __setitem__() 和 __delitem__()
# __reversed__()

#编写一个不可改变的自定义列表，记录列表中每个元素被访问的次数
class Nlist:
    def __init__(self,*args):
        self.values=[x for x in args]
        self.count={}.fromkeys(range(len(self.values)),0)
    def __len__(self):
        return len(self.values)
    def __getitem__(self, item):
        self.count[item]+=1             #self.count是创建的一个字典用来记录每个元素被__getitemd__的次数
        return self.values[item]

n=Nlist(1,2,3,5,8)
print(n[1]+n[2])
print(n[1])
print(len(n))
print(n.count)

print('==============================================')

#作业
#鸭子类型:一个对象有效的语义，不是由继承自特定的类或实现特定的接口，而是由当前方法和属性的集合决定。
class Duck:
    def quack(self):
        print("呱呱呱！")
    def feathers(self):
        print("这个鸭子拥有灰白灰白的羽毛。")

class Person:
    def quack(self):
        print("你才是鸭子你们全家人是鸭子！")
    def feathers(self):
        print("这个人穿着一件鸭绒大衣。")

def in_the_forest(duck):
    duck.quack()
    duck.feathers()

def game():
    donald = Duck()
    john = Person()
    in_the_forest(donald)
    in_the_forest(john)

game()
#in_the_forest() 函数对参数 duck 只有一个要求：就是可以实现 quack() 和 feathers() 方法。然而 Duck 类和 Person 类都实现了 quack() 和 feathers() 方法，
# 因此它们的实例对象 donald 和 john 都可以用作 in_the_forest() 的参数。这就是鸭子类型。

#定制列表
class Countlist(list):
    def __init__(self,*args):
        super().__init__(args)
        self.count=[]
        for i in args:
            self.count.append(0)

    def __getitem__(self, item):
        self.count[item]+=1
        return super().__getitem__(item)       #这里要有return来返回值

    def append(self,key):
        self.count.append(0)
        super().append(key)

    def pop(self,key=-1):
        self.count.pop(key)
        return super().pop(key)

    def extend(self,item):
        self.count.extend(0)
        return super().extend(item)

    def remove(self,item):
        key=super().index(item)
        del self.count[key]
        super().remove(item)

    def reverse(self):
        self.count.reverse()
        super().reverse()

#这里区分一下：定义属于类实例对象的方法,如Countlist.reverse()，即（xxx.+函数名）直接定义不用魔法方法
# 如果是reversed(sth.)则需要定义__reversed__()


c=Countlist(2,5,8)
print(c[1])
print(c.count)
c.append(0)
print(c[3])
print(c.count)
c.reverse()
print(c)
print(c.count)
c.remove(2)
print(c)
print(c.count)
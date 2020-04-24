#定制容器

#不可改变
# __len__(self)
#__getitem(self)

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
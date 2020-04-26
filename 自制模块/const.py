class Const:

    def __setattr__(self, key, value):
        if key in self.__dict__:            #__dict__保存对象的属性和属性值
            raise TypeError('常量无法改变！')
        if not key.isupper():
            raise TypeError('常量名必须由大写字母组成!')
        self.__dict__[key]=value

import sys
sys.modules[__name__] = Const()     #模块名设为类对象名,就可以实现模块与类Const的对象挂钩

if __name__=='__main__':
    test=Const()
    test.NAME=4
    print(test.NAME)

    try:
        test.NAME=6
    except TypeError as reason:
        print(reason)

    try:
        test.name=7
    except TypeError as reason:
        print(reason)
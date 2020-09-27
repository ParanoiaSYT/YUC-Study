#050
#模块封装
# 可以简化代码，也可以实现代码重用

##搜索路径（目录列表）site-packages位置专门存放模块
import sys
print(sys.path)
# sys.path.append('/Users/sunyuting/YuC-Study/自制模块')      #可以导入想要的路径
print(sys.path)

import hello
hello.hi()

#模块导入(三种方法）
##1
import TemperatureConversion
print('32摄氏度=%.2f华氏度' % TemperatureConversion.c2f(32))
print('100华氏度=%.2f摄氏度' % TemperatureConversion.f2c(100))
print('========================================================')
##2
from TemperatureConversion import *         #*表示导入所有命名空间
from TemperatureConversion import c2f,f2c

print('32摄氏度=%.2f华氏度'%c2f(32))
print('100华氏度=%.2f摄氏度'%f2c(100))
print('========================================================')

##3
import TemperatureConversion as tc
print('32摄氏度=%.2f华氏度'%tc.c2f(32))
print('100华氏度=%.2f摄氏度'%tc.f2c(100))
print('========================================================')

########################################################
print(__name__,tc.__name__)
# __main__ TemperatureConversion
# 作为模块导入的时候，这个模块的__name__值就是该模块的名字

########################################################
#051
#package包,需要一个__init__.py的文件（可以为空）
import 自制模块.hello,自制模块.TemperatureConversion as t
hello.hi()
print(t.c2f(36),t.f2c(99))

print('========================================================')
########################################################
#052
import timeit
print(timeit.__doc__)
print('========================================================')
print(dir(timeit))

print(timeit.__all__)       #对外接口函数,如果模块中有all,from timeit import*就只会把这四个接口导入

print(timeit.__file__)      #源代码位置

print('========================================================')
help(timeit)
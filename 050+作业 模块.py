#模块封装
# 可以简化代码，也可以实现代码重用

##搜索路径（目录列表）site-packages位置专门存放模块
import sys
print(sys.path)
sys.path.append('/Users/sunyuting/YuC-Study/自制模块')      #可以导入想要的路径

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

########################################################
#package包,需要一个__init__.py的文件（可以为空）
import 自制模块.hello,自制模块.TemperatureConversion as t
hello.hi()
print(t.c2f(36),t.f2c(99))
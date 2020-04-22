#模块=可用代码段的打包
import random
secret=random.randint(1,10)
print(secret)

#OS模块自动适应各操作系统
import os
print(os.getcwd())  #返回当前工作目录
#os.chdir('some目录') #切换工作目录
print(os.listdir('/Users/sunyuting/yuc study'))     #列举指定文件夹的文件名
os.mkdir('/Users/sunyuting/yuc study/A')    #只能创建单层目录（不能/C/B）
os.makedirs('/Users/sunyuting/yuc study/C/B')   #递归创建多层
os.rmdir('/Users/sunyuting/yuc study/A')   #删除单层文件
os.removedirs('/Users/sunyuting/yuc study/C/B')   #递归删除文件(子到父），遇到目录非空报错
# os.remove('')  #删除文件

# os.system(command)
os.curdir   #指代当前目录(.)
os.pardir   #指代上一级目录(..)
print(os.listdir(os.curdir))    #=os.list(.)

os.sep  #路径分隔符（Linux下为'/'）
os.linesep  #行终止符（'\n')
print(os.name)

print(os.path.basename('/Users/sunyuting/yuc study/boy_1.txt'))     #返回文件名
print(os.path.dirname('/Users/sunyuting/yuc study/boy_1.txt'))      #返回路径
print(os.path.split('/Users/sunyuting/yuc study/boy_1.txt'))     #分离文件名和路径

import time
# getatime最近访问时间
print(time.gmtime(os.path.getatime('/Users/sunyuting/yuc study/boy_1.txt')))    #格林威治时间
print(time.localtime(os.path.getatime('/Users/sunyuting/yuc study/boy_1.txt'))) #本地时间（北京）

all_files=os.walk(os.getcwd())
for i in all_files:
    print(i[1])
    print('===========')
    print(i[0])
    print(i[2])


#丰富的else语句
print(5//2) #除法保留最大整数

try:
    int('123')
except ValueError as reason:
    print('出错了')
else:
    print('No problems')

#简洁的with语句(减少代码量
try:
    f=open('data.txt','r')
    for each_line in f:
        print(each_line)
except OSError as reason:
    print('出错啦'+str(reason))
finally:
    if 'f' in locals():
        f.close()       #查看f是否在局部变量符号表中（如果没有那个文件）

#with方法(不用close）
try:
    with open('data.txt','w') as f:
        for each_line in f:
            print(each_line)
except OSError as reason:
    print('出错啦'+str(reason))

# with open('dongodngdong.txt','w')as f:
#     f.write('with???')


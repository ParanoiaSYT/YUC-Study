str1='I love fishc'
print(str1[:8],str1[5])
print(str1[6:]+'插入字符串'+str1[6:])

print(str1.find('fish'),str1.find('sffg'))  #存在就返回位置，不存在返回-1；对比index不存在就报错。

#format()
zzz="{0} love {1}.{2}".format("I","fishc","com")
zzz="{a} love {b}.{c}".format(a="I",b="fishc",c="com")
print(zzz)

print('\ta','\\')
print("{{0}}".format("不打印"))  #打印花括号(转义）

bbb='{0:.1f}{1}'.format(27.658,'GB') #定点数
print(bbb)

print('%c' % 97)
print('%c %c %c' % (97,98,99))  #ascii码
print('%s' % 'I love fishc') #格式化字符串
print('%d+%d=%d' % (4,5,4+5)) #格式化整数

print('%6.2f' % 27.6583)    #m.n m为总宽度，n为小数点后位数
print('%.2e' % 27.6583)

print('%-10d' % -5)
print('%+10d' % 5)

print('%010d' %5)  #0来取代空格

#\t=TAB , \n=换行


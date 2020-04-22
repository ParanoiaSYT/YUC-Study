# pickle模块(泡菜)
import pickle

my_list = [1, 2, 3, 3.14, '查理斯', ['cxk']]
pickle_file = open('my_list.pkl', 'wb')  # 格式好记就行,wb为写入二进制
pickle.dump(my_list, pickle_file)
pickle_file.close()     #列表保存成二进制

pickle_file = open('my_list.pkl', 'rb')
my_list2=pickle.load(pickle_file)
print(my_list2)     #恢复列表


# #Exception异常处理
# file_name=input('请输入需要打开的文件名：')
# f=open(file_name)
# print('文件的内容如下：')
# for each_line in f:
#     print(each_line)
# #注意要同一目录下


my_list1=['ame']
assert len(my_list1)>0  #assert后面为false则引发异常

my_dict={1:'one',2:'two',3:'three'}
print(my_dict[1])
print(my_dict.get(4))   #get不会异常
my_dict.get(3)      #不会自动打印出来
print(my_dict.get(3))


#try检测异常(一旦发现异常，后面的语句就不会执行）
try:
    sum=1+'1'
    f=open('我为什么是一个文件.txt')
    print(f.read())
    f.close()
# except OSError as reason:         #filenotfoundError并到了OSError里了
#     print('文件出错啦\n错误原因是：'+str(reason))
# except TypeError as reason:
#     print('类型出错啦\n错误原因是：'+str(reason))
# except:
#     print('出错啦！')
except (TypeError,OSError) as reason:
    print('出错啦\n错误原因是：'+str(reason))    #仍然是发现异常不执行后面

try:
    f=open('我为什么是一个文件.txt','w')
    print(f.write('wo存在了!'))
    sum = 1 + '1'                 #这一行与下一行调换顺序竟然可以保存
    # print(f.write('wo存在了!'))    #不用close也能保存？⚠️可能会占用内存空间（养成close好习惯）
    f.close()
except (TypeError, OSError) as reason:
    print('出错啦\n错误原因是：' + str(reason))
finally:    #无论如何都会执行的操作
    f.close()

# f=open('不用close？.txt','w')
# print(f.write('真的吗？'))
# f.close()     #不用close也能保存？⚠️可能会占用内存空间（养成close好习惯）

# raise   ZeroDivisionError('除数为0的异常')   #引发异常



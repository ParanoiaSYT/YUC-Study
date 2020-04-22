#定义函数
def MyFistFunction():
    print('This is my fist function to creat')
    print('I am so excited...')
    print('感谢cctv')

#调用函数
MyFistFunction()

def MySecondFunction(name):
    '函数定义过程中的name叫形参'
    #只有个形式
    print(name+' 我爱你')
MySecondFunction('pikaqiu')      #name为形参，'pikaqiu'为实参

def add(num1,num2):
    result=num1+num2
    return result
    # print(result)
print(add(88,44))

print(MySecondFunction.__doc__)  #双下行线默认属性，doc文档字符串
print(print.__doc__) # =help(print)
help(print)

def SaySome(name,words):
    print(name+ '->'+words)
SaySome('xss','改变世界') #关键字参数SaySome(words='改变世界',name='xss)

#默认参数
def SaySome(name='xss',words='改变世界'):
    print(name+ '->'+words)
SaySome()     #默认参数赋初值防报错
SaySome('teacher cang')

#收集参数(*号)
def test(*params):
    print('参数的长度是：', len(params))
    print('第二个参数是：', params[1])
test(1,'xss',3.14,4,5,78,3)

def test(*params,exp=7):       #收集参数后面还要加参数时，最好加默认参数防报错
    print('参数的长度是：', len(params),exp)
    print('第二个参数是：', params[1])
test(1,'xss',3.14,4,5,78,3,exp=9)

print('猪猪侠','xxs','小甲鱼')   #也是收集参数

def Hello():
    print('Hello World!')
temp=Hello()
print(temp,type(temp))

def back():
    return [1,'xss',3.1415926]
print(back())      #可返回多类型，多个值

def back():
    return 1,'xss',3.1415926
print(back())      #默认元组

# def discounts(price,rate):
#     final_price = price * rate      #final_price为局部变量，仅在定义时有用，函数外无法访问内部局部变量
#     print('尝试打印全局变量',old_price)
#     return final_price
# old_price= float(input('请输入原价：'))
# rate=float(input('请输入折扣率：'))
# new_price=discounts(old_price,rate)
# print('打折后价格为：',new_price)
# # print('无法打印局部变量final_price的值',final_price)
# #old_price和new_price 为函数外全局变量

# def discounts(price,rate):
#     final_price = price * rate      #final_price为局部变量，仅在定义时有用，函数外无法访问内部局部变量
#     # print('尝试打印全局变量',old_price)
#     old_price=50
#     print('修改后值1',old_price)
#     return final_price
# old_price= float(input('请输入原价：'))
# rate=float(input('请输入折扣率：'))
# print('修改后值2',old_price)
# new_price=discounts(old_price,rate)
# print('打折后价格为：',new_price)
# #如果在函数内把全局变量修改成局部变量，那python会在内部和外部建立两个名字一样的变量，注意避免⚠️

count = 5
def Myfun():
    global count         #在定义中加上global就可以修改全局变量
    count=10
    print(count)
Myfun()
print(count)
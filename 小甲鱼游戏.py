import random
secret=random.randint(1,10)
print('~~~~~~~~~~~~~我爱鱼C工作室~~~~~~~~~~~~~~~~')
temp=input("不妨猜一下小甲鱼想的数字:")
while not temp.isdigit():
    print('抱歉，输入不合法')
    temp=input('请输入一个整数啦:')
guess=int(temp)
while guess>10:
    print('要输入0到10的整数哦')
    temp=input('请重新输入：')
    guess=int(temp)
time=0
#     print("猜错了，现在想的是8")
while guess != secret and time<3 :
    time = time + 1
    if guess > secret:
        print("哥，大了大了～")
    else:
        print("嘿，小了小了")
    temp = input("哎呀猜错了，再来个新数字吧:")
    guess = int(temp)
if guess != secret and time == 3:
    print("没有机会了！")
if guess == secret:
    print("卧槽，你是蛔虫吗")
    print("哼，猜中也没有奖励")
print("游戏结束，不玩了^v^")


# s 为字符串
# s.isalnum()  所有字符都是数字或者字母，为真返回 True，否则返回 False。
# s.isalpha()   所有字符都是字母，为真返回 True，否则返回 False。
# s.isdigit()     所有字符都是数字，为真返回 True，否则返回 False。
# s.islower()    所有字符都是小写，为真返回 True，否则返回 False。
# s.isupper()   所有字符都是大写，为真返回 True，否则返回 False。
# s.istitle()      所有单词都是首字母大写，为真返回 True，否则返回 False。
# s.isspace()   所有字符都是空白字符，为真返回 True，否则返回 False。
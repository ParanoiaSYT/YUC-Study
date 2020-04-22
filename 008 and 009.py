# score=int(input("您所输入的分数为："))
# if 90<=score<=100:
#     print("A")
# if 80<=score<90:
#     print("B")
# if 60<=score<80:
#     print("C")
# if 0<=score<60:
#     print("D")
# if score<0 or score>100:
#     print("error")

# score=int(input("您所输入的分数为："))
# if 90<=score<=100:
#     print("A")
# elif 80<=score<90:
#     print("B")
# elif 60<=score<80:
#     print("C")
# elif 0<=score<60:
#     print("D")
# else:
#     print("error")

x=5;y=7
x,y=8,9
small=x if x<y else y
print(small)

assert 5<6 #断言

favourate='DOTA2'
for i in favourate:
    print(i,end=' ')

member =['小甲鱼','小布丁','ori']
for each in member:
    print(each,len(each))

range(5)
print(list(range(5)))

# for i in range(1,10,2):
#     print(i)

# Yesanswer="well done"
# answer=input("请输入正确答案：")
# while True:
#     if answer==Yesanswer:
#         print("nice")
#         break
#     answer=input("错误，请重新输入：")
# print("答对了！")

for i in range(10):
    if i%2 !=0:
        print(i)
        continue #终止本轮循环并开启下一轮循环
    i+=2
    print(i)


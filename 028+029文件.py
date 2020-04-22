# help(open)
f = open('/Users/sunyuting/Desktop/yuc/未命名1.txt')
print(f)
print(f.read())
print(f.tell())
print(f.seek(3, 0))  # 文件指针偏移0位置3个字符
print(list(f))
print(f.readline())
print(list(f))
f.seek(0, 0)
for each_line in f:
    print(each_line)  # 原文档有换行格式，自动逐行打印

f.seek(0,0)
print(f.read(10))

f = open('/Users/sunyuting/Desktop/yuc/未命名2.txt', 'w')
f.write('我爱fishc')
f.close()  # 每次文件写完要关闭，不然仅在内存中





# 对record.txt文件操作(test1)
# f = open('/Users/sunyuting/Desktop/yuc/record.txt')
# boy = []
# girl = []
# count = 1
#
# for each_line in f:
#     if each_line[:4] != '====':
#         # 字符串分割
#         (role, line_spoken) = each_line.split(':', 1)
#         if role == '小甲鱼':
#             boy.append(line_spoken)
#         if role == '小客服':
#             girl.append(line_spoken)
#     else:
#         # 文件保存操作
#         file_name_boy = 'boy_' + str(count) + '.txt'
#         file_name_girl = 'girl_' + str(count) + '.txt'
#
#         boy_file = open(file_name_boy, 'w')
#         girl_file = open(file_name_girl, 'w')
#
#         boy_file.writelines(boy)
#         girl_file.writelines(girl)

#         boy_file.close()
#         girl_file.close()

#         boy = []
#         girl = []
#         count += 1
# file_name_boy = 'boy_' + str(count) + '.txt'
# file_name_girl = 'girl_' + str(count) + '.txt'
#
# boy_file = open(file_name_boy, 'w')
# girl_file = open(file_name_girl, 'w')
#
# boy_file.writelines(boy)
# girl_file.writelines(girl)

# boy_file.close()
# girl_file.close()
# f.close()


#test2(通过定义两个函数来操作）
def save_file(boy,girl,count):
    file_name_boy = 'boy_' + str(count) + '.txt'
    file_name_girl = 'girl_' + str(count) + '.txt'

    boy_file = open(file_name_boy, 'w')
    girl_file = open(file_name_girl, 'w')

    boy_file.writelines(boy)
    girl_file.writelines(girl)

    boy_file.close()
    girl_file.close()
def split_file(file_name):
    f = open(file_name)
    boy = []
    girl = []
    count = 1

    for each_line in f:
        if each_line[:4] != '====':
            (role, line_spoken) = each_line.split(':', 1)
            if role == '小甲鱼':
                boy.append(line_spoken)
            if role == '小客服':
                girl.append(line_spoken)
        else:
            save_file(boy,girl,count)

            boy = []
            girl = []
            count += 1
    save_file(boy,girl,count)
    f.close()
split_file('/Users/sunyuting/Desktop/yuc/record.txt')
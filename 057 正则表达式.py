# AV66771949这里正则表达式讲的很清楚，建议大家去看一下
# 057
import re

position = re.search(r'FishC', 'I love FishC.com!')
print(position)  # (7,12) 7后面开始到第12个

position = re.search(r'.', 'I love FishC.com!')  # 正则表达式中.号表示任意字符
print(position)

position = re.search(r'Fish.', 'I love FishC.com!')
print(position)

position = re.search(r'\.', 'I love FishC.com!')  # 转移\
print(position)

position = re.search(r'\d\d', 'I 9383737 love FishC.com73355')
print(position)  # \d表示任意数字

position = re.search(r'\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d', '192.168.110.111')
print(position)

print('=======================================')
# 字符类(只要匹配到里面任意字符都算匹配成功）
position = re.search(r'[aoeiu]', 'I love FishC.com!')
print(position)  # 大小写敏感区分

position = re.search(r'[a-z,A-Z]', 'I love FishC.com!')
print(position)

print('=======================================')
# 匹配次数
position1 = re.search(r'ab{3}c', 'abbbc')
position2 = re.search(r'ab{3,10}c', 'abbbbbc')  # 3到10次
print(position1, position2)  # 这里是连续两个b

print(re.search(r'[01]\d\d|2[0-4]\d|25[0-5]', '198'))  # 匹配0-255
# |表示or或

position = re.search(r'(([01]?\d{0,2}|2[0-4]\d?|25[0-5])\.){3}([01]?\d{0,2}|2[0-4]\d{0,1}|25[0-5])','1.1.1.1')
print(position)

print('=======================================')
# ################################################
# 058特殊字符
# 元字符
import re

# 脱字符^
position1 = re.search(r"^FishC", 'I love FishC.com')
position2 = re.search(r"^FishC", 'FishC.com')
print(position1)
print(position2)  # 脱字符后的字符在开头才能正常匹配

print('=======================================')
# 结束符$
position1 = re.search(r"FishC$", 'I love FishC.com')
position2 = re.search(r"FishC$", 'com.FishC')
print(position1)
print(position2)

print('=======================================')
position3 = re.search(r"^I|com$", 'I love FishC.com')
print(position3)

position1 = re.search(r"(po)(fishc)\2", 'pofishcfishc')
position2 = re.search(r"(po)(apple)(fishc)\3", 'poapplefishcfishcALKABF')
print(position1)  # (fishc)\1==fishcfishc
print(position2)
# 这里\加对应数字表示匹配第几组,比如(a)(b)\2相当于abb ; (a)(b)(c)\3==abcc
# 且重复一遍

# 反斜杠+0或三位数表示八进制转ascii码匹配

# findall()
list1 = re.findall(r"[a-z]", 'Fishc.com')
print(list1)
# findall+脱字符放在字符类里面==取反，放在外面仍然是开头脱字符功能
list2 = re.findall(r"[^a-z]", 'FishC.com')
print(list2)

# *表示{0,}匹配0次或多次； +表示{1,}匹配1次以上； ?表示{0,1}匹配0次或1次

s="<html><title>I love FishC.com</title></html>"
pos1=re.search(r"<.+>",s)
print(pos1)      #贪婪模式匹配<任意字符+>

pos2=re.search(r"<.+?>",s)   #在元字符后加上?就可以开启非贪婪模式
print(pos2)

# 059特殊字符
# 反斜杠+字母
# \A和脱字符^在开头效果一样；\Z和$在末尾效果一样 (唯一区别在于可以设置包括换行符与否）
import re
# \b单词边界
pos1=re.findall(r"\bFishC\b","FishC.com!FishC_com!(FishC)")     #两个\b表示前后两个边界
print(pos1)     #零宽断言，匹配一个单词边界（比如感叹号，括号，.号），下划线和Unicode 的字母数字都被认为是单词
# \B非单词边界,与\b相反

# \d匹配Unicode任意数字（str类型），如果开启re.ASCII就只匹配[0-9]
# \D与\d相反，匹配非Unicode数字

# \w找Unicode单词字符
pos=re.findall(r"\w",'我爱说话很啊纠结啊 FishC.com!(!!)')
print(pos)
# \W找非Unicode单词字符

print('=======================================')
# 编译成模式对象(如果要重复使用相同的正则表达式）
p=re.compile(r"[A-Z]")
print(type(p))
# 模块化后多了个参数位置(匹配搜索位置) p.search(string,0,50)或者p.search(string[:50],0)
print(p.search("I love FishC.com"))
print(p.findall("I love FishC.com"))

# 编译标志（具体如何使用baidu）
# re.A=re.ASCII
# re.DOTALL=re.S
# re.VERBOSE使得正则表达式书写行落有矩

print('=======================================')
# 060
import re
result=re.search(r" (\w+) (\w+)","I love FishC.com!")
print(result)
print(result.group(),type(result.group()))       #通过group来字符串形式显示结果

print(result.group(1))
print(result.group(2))      #支持子组输出

print(result.start())   #匹配开始位置
print(result.end())     #匹配结束位置
print(result.span())    #匹配范围


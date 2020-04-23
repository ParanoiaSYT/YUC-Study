#044
import time as t
class MyTimer():
    def __init__(self):
        self.prompt='未开始计时！'
        self.lasted=[]
        self.begin=0        #属性名不能和方法名重复
        self.end=0
        self.unit=['年','月','天','小时','分钟','秒']        #添加单位
        self.borrow = [0, 12, 31, 24, 60, 60]

    def __str__(self):  # print()可以显示字符串
        return self.prompt

    # __repr__=__str__  #内容一样直接赋值过去

    # def __repr__(self):  # 实例化对象直接显示字符串
    #     return "总共运行了%d秒"

    def __add__(self, other):
        prompt='两次总共运行了'
        result=[]
        for index in range(6):
            result.append(self.lasted[index]+other.lasted[index])
            if result[index]:
                prompt+=str(self.result[index]+self.unit[index])
        return prompt

    #开始计时
    def start(self):
        self.begin=t.localtime()
        self.prompt='请先停止计时。'
        print('计时开始......')
    #停止计时
    def stop(self):
        if not self.begin:
            self.prompt='请先开始计时'
        else:
            self.end = t.localtime()
            self._calc()
            print('计时结束!')
    #内部方法，计算运行时间
    def _calc(self):
        self.lasted=[]
        self.prompt="总共运行了"
        for index in range(6):
            temp=self.end[index]-self.begin[index]
            if temp<0:
                # 测试高位是否有得“借”，没得借的话向再高位借......
                i = 1
                while self.lasted[index - i] < 1:
                    self.lasted[index - i] += self.borrow[index - i] - 1
                    self.lasted[index - i - 1] -= 1
                    i += 1

                self.lasted.append(self.borrow[index] + temp)
                self.lasted[index - 1] -= 1
            else:
                self.lasted.append(temp)

            # 由于高位随时会被借位，所以打印要放在最后
        for index in range(6):
            if self.lasted[index]:
                self.prompt += str(self.lasted[index]) + self.unit[index]
        #为下一轮初始化
        self.begin=0
        self.end=0

t1=MyTimer()
print(t1)
t1.start()
t1.stop()
print(t1)
t2=MyTimer()
t2.start()
t2.stop()
print(t2)
print(t1+t2)

# =========================================
#可以使用timeit模块来计时
# calendar 月历模块
# time模块

import calendar
cal = calendar.month(2020, 4)
print ("以下输出2020年4月份的日历:")
print (cal)

#########################################
# 统计一个函数运行若干次的时间
import time as t
class MyTimer:
    def __init__(self, func, number=1000000):
        self.prompt = "未开始计时！"
        self.lasted = 0.0
        self.default_timer = t.perf_counter
        self.func = func
        self.number = number
    def __str__(self):
        return self.prompt

    __repr__ = __str__

    def __add__(self, other):
        result = self.lasted + other.lasted
        prompt = "总共运行了 %0.2f 秒" % result
        return prompt

    # 内部方法，计算运行时间
    def timing(self):
        self.begin = self.default_timer()
        for i in range(self.number):
            self.func()
        self.end = self.default_timer()
        self.lasted = self.end - self.begin
        self.prompt = "总共运行了 %0.2f 秒" % self.lasted

    # 设置计时器(time.perf_counter() 或 time.process_time())
    def set_timer(self, timer):
        if timer == 'process_time':
            self.default_timer = t.process_time
        elif timer == 'perf_counter':
            self.default_timer = t.perf_counter
        else:
            print("输入无效，请输入 perf_counter 或 process_time")
def test():
    text = "I love FishC.com!"
    char = 'o'
    if char in text:
        pass

m=MyTimer(test)
m.set_timer('perf_counter')
m.timing()
print(m)


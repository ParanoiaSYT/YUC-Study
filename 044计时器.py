#044
import time as t
class MyTimer():
    def __init__(self):
        self.prompt='未开始计时！'
        self.lasted=[]
        self.begin=0        #属性名不能和方法名重复
        self.end=0
        self.unit=['年','月','天','小时','分钟','秒']        #添加单位

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
            self.lasted.append(self.end[index]-self.begin[index])
            if self.lasted[index]:
                self.prompt+=str(self.lasted[index]+self.unit[index])
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
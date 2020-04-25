def c2f(cel):
    fah=cel*1.8+32
    return fah

def f2c(fah):
    cel=(fah-32)/1.8
    return cel

def test():
    print('0摄氏度=%.2f华氏度' % c2f(0))
    print('90华氏度=%.2f摄氏度' % f2c(90))

if __name__=="__main__":        #相当于仅仅在这个py文件里__name__等于__main__，才会执行test()

    test()
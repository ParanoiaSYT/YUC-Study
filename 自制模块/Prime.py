import math
def is_prime(num):
    if num > 1:
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(num) + 1), 2):        #两步一跨就快很多了
            if num % current == 0:
                return False
        return True
    return False

def sumPrime(num):
    while True:
        if is_prime(num):
            yield num
        num+=1

def solve():
    sum1=2
    for i in sumPrime(3):
        if i<20000:
            sum1+=i
        else:
            print(sum1)
            break
if __name__ =='__main__':
    solve()
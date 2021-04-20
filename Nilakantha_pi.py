#!/usr/bin/python
# -*- encoding: UTF-8 -*-


import timeit
from math import sin, radians, pi
from decimal import Decimal, getcontext
from sympy import Rational, log

PI = Decimal('3.1415926535897932384626433832795028841971693993751058209749445\
923078164062')
math_pi = Decimal(pi)

    
## 以下是浮动运算的两个迭代函数（过程）    
def nilakantha_series():
    '''浮点运算得到Nilakantha序列 {1/n*1/(n+1)*1/(2n+1), n=1,2,3,...}'''

    #getcontext().prec = 100
    n = 1
    while True:
        #yield Decimal(1/n*1/(n+1)*1/(2*n+1))
        yield Decimal(1/(n*(n+1)*(2*n+1)))
        n += 1

def nilakantha_iter(n):
    '''浮点计算Nilakantha级数的交替和差计算π'''

    #getcontext().prec = 100
    s, k = 0, 1
    a = nilakantha_series()
    for _ in range(n):
        s += k * next(a)  # 乘积仍是Decimal
        k = -k
    return 3+s  # 加法也是Decimal


def nilakantha_epson(eps, limit=float("inf")):
    '''
    pi = 3+4/(2*3*4)-4*/(4*5*6)+4/(6*7*8)-4/(8*9*10)-...
       = 3 + sum{(-1)**(i/2+1)*4.0/(i*(i+1)*(i+2))}  # 收敛较快
       = 3 + 1/(1*2*3)-1/(2*3*5)+1/(3*4*7)-1/(4*5*9)+...
       = 3 + sum((-1)**(k+1)*1/(k*(k+1)*(2k+1)))  # 收敛较慢
    Nilakantha series
    '''

    #getcontext().prec = 100
    s, k, i = 3, 1, 1
    a = nilakantha_series()
    while (abs(s - math_pi) > eps) and (i < limit):
        s += k * next(a)
        k = -k
        i += 1
    return (s, i)


def pi_limit_sin(n):
    return radians(n*sin(180.0/n))



## 以下是符号运算的Nilakantha级数法求π
def nilakantha_RSeries():
    '''有理数符号运算的 Nilakantha级数 {1/(n(n+1)(2n+1)), n=1,2,3,...}'''

    n = 1
    while True:
        #yield Rational(1,n) * Rational(1,n+1) * Rational(1,2*n+1)
        yield Rational(1,n*(n+1)*(2*n+1))
        n += 1

def nilakantha_RIter(n):
    '''有理迭代Nilakantha级数的交替和差计算π'''

    s, k = 0, 1
    a = nilakantha_RSeries()
    for _ in range(n):
        s += k * next(a)
        k = -k
    return 3+s

def test_nilakantha_RIter():
    '''测试有理迭代的符号运算结果的收敛性快慢'''

    nList = [24836,50000]
    print("\n**符号运算Nilakantha级数计算π**\n")
    print("|耗时(s)|迭代次数|近似π值|\n |-----|-----|-----|")
    for n in nList:
        start = timeit.default_timer()
        mypi = nilakantha_RIter(n).evalf(50)
        stop = timeit.default_timer()
        print('|{T}| {N}| {Pi}|'.format(T=stop-start, N=n, Pi=mypi))


def test_nilakantha_iter():

    nList = [10000,60000,130000]
    print("\n**Nilakantha级数求和得π**\n")
    print('|Elapsed(s)| Iterations| PI|\n|-----|-----|-----|')
    for n in nList:
        start = timeit.default_timer()
        mypi = nilakantha_iter(n)
        stop = timeit.default_timer()
        print('|{T}|{N}|{Pi}|'.format(T=stop-start, N=n, Pi=mypi))


def test_nilakantha_epson():
    '''The fastest convergence method
    '''
    print("\n**Nilakantha级数求和得π，带误差范围**\n")
    print('|耗时(s)|迭代次数|精度(10^n)|π|\n|-----|-----|-----|-----|')

    #getcontext().prec = 100
    for j in range(15, 24, 2):  # 超过24 就死循环了，精度只能到 10**(-22)吗？
        epson = Decimal(10**(-j))
        start = timeit.default_timer()
        mypi, n_iter = nilakantha_epson(epson,900000)
        stop = timeit.default_timer()
        print('|{T}|{N}|{E}|{Pi}|'.format(T=stop-start, N=n_iter, E=int(log(epson,10).evalf(10)), Pi=mypi))


def Nilakantha_Series(n):
    '''Approximation of the number PI through the Nilakantha's series，Decimal可用来保存具有小数点而且数值确定的数值
    Arbitrary precision
    Language: Python
    Author: Jose Cintra (jose.cintra@html-apps.info)
    '''

    getcontext().prec = 100

    s = Decimal(1)   # Signal for the next operation
    pi = Decimal(3)

    #print("\n用Nilakantha级数逼近π，采用十进制精确小数Decimal\n")
    #n = 190000
    #int(input("Enter the number of iterations: "))
    #print("\nPlease wait. Running...\n")

    for i in range(2, n * 2, 2):
        pi += s*(Decimal(4)/(Decimal(i)*Decimal(i+1)*(Decimal(i+2))))
        s = -s

    #print("耗时(s)={0}, 迭代次数={1}, 近似π={2}".format(stop-start, n, pi))
    return pi


def test_nilakantha_Series():
    nList = [200000,250000,300000]
    print("\n**Nilakantha级数求和得π，Decimal判断**\n")
    print('|Elapsed(s)| Iterations| PI|\n|-----|-----|-----|')
    for n in nList:
        start = timeit.default_timer()
        mypi = Nilakantha_Series(n)
        stop = timeit.default_timer()
        print('|{T}|{N}|{Pi}|'.format(T=stop-start, N=n, Pi=mypi))

if __name__ == '__main__':
    #test_nilakantha_RIter()
    test_nilakantha_iter()
    test_nilakantha_epson()
    test_nilakantha_Series()

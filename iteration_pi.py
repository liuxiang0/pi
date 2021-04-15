#!/usr/bin/python
# -*- encoding: UTF-8 -*-
"""
代数几何迭代算法, 迭代逼近单位圆的半周长 $\pi$, 从而得到圆周率 π 
初始状态：取单位圆的内接正六边形，其变成为 1.
从正六边形得到正十二边形的半周长，以此类推，迭代以此，边数增加一倍。
求边长的迭代函数为 f(x)=sqrt(2-sqrt(4-x**2))
迭代次数：n
对应半周长：6*2**(n-1)*f(x)

采取：迭代生成器方法，和符号运算法则，得到迭代序列。需要时再计算某个迭代值。
讨论：如何通过相邻几个迭代值，计算出迭代误差值，或结果的精度。
    好像只能字符判断，不能用浮点数判断。
"""

# from math import sqrt
from sympy import sqrt
import timeit

def HalfCircumference():
    '''迭代生成器: 生成单位圆上的正 6*2**n 边形的半周长'''

    L =  1  # 初始值，正六边形的边长为 L6 = 1
    n = 0
    while True:
        L = sqrt(2-sqrt(4-L*L))  # 迭代公式 
        n = n + 1                # 迭代次数
        yield 6*2**(n-1)*L       # 迭代产生的半周长，符号运算结果


def iterate_HalfCircumference(n):
    '''不用迭代生成器，直接生成指定迭代次数的正多边形的半周长'''

    L = 1  # 初始值，正六边形的边长为 L6 = 1
    k = 0
    while k < n:
        L = sqrt(2-sqrt(4-L*L))
        k += 1

    return 6*2**(n-1)*L

def Compare(a,b):
    '''通过判断字符串的差异，得到两数之间的误差，获取精度，输出小数点后第几位开始不同 '''
    k = 0
    sup = min(len(a),len(b))
    for i in range(sup):
        if a[i]==b[i]:
            k += 1
        else:
            break
    return k-2  # 剔除首两位的 3.

def Fibo():
    '''Fibonacci数列，斐波那契数列的迭代生成法 F_n = F_{n-1} + F_{n-2}'''

    a,b = 0,1
    while True:
        a, b = b, a+b
        yield a



if __name__=='__main__':
    print("开始计算了......")
    cir = HalfCircumference()   # 几乎不花时间1.7999999999407379e-06

    start = timeit.default_timer()

    for i in range(100):            # 150次迭代耗时最多，为77.1517524s
        next(cir)                   # 舍弃前面的精度不高的值
    #stop = timeit.default_timer()
    #print('next Elapsed(s)={T}'.format(T=stop-start))  

    # TODO 如何得到精度值，通过相邻几个迭代值获取精度值？
    Prev = next(cir).evalf(100)
    #start = timeit.default_timer()
    for i in range(30):             # 计算在此花了 18.6607882秒
        Next = next(cir).evalf(100)
        print(Next)                 # 保留后面的精度较高的π值
        print("精确到小数点后{0}位".format(Compare(str(Prev),str(Next))))
        Prev = Next
    
    stop = timeit.default_timer()
    print('结束总耗时(s)={T}'.format(T=stop-start))  
    
    """
    fib = Fibo()                    # 测试迭代生成器的工作原理
    for i in range(5):
        print(next(fib))
    """
    """
    nmin, valid = 12, 40
    nmax = nmin + 10                # 每次迭代10个
    print("min={0},max={1},valid={2}".format(nmin,nmax,valid))
    for i in range(nmin, nmax):
        pi = iterate_HalfCircumference(i).evalf(valid)
        print(pi, end=',')
    """

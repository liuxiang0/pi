#!/usr/bin/python
# -*- encoding: UTF-8 -*-


import timeit
from math import sin, radians, pi
from decimal import Decimal, getcontext

PI = Decimal('3.1415926535897932384626433832795028841971693993751058209749445\
923078164062')
math_pi = pi


def nilakantha_series():
    n = 1
    while True:
        yield 1/n*1/(n+1)*1/(2*n+1)
        n += 1


def nilakantha_iter(n):
    s, k = 0, 1
    a = nilakantha_series()
    for _ in range(n):
        s += k * next(a)
        k = -k
    return 3+s


def nilakantha_epson(eps, limit=float("inf")):
    '''
    pi = 3+4/(2*3*4)-4*/(4*5*6)+4/(6*7*8)-4/(8*9*10)-...
       = 3 + sum{(-1)**(i/2+1)*4.0/(i*(i+1)*(i+2))}    # 收敛较快
       = 3 + 1/(1*2*3)-1/(2*3*5)+1/(3*4*7)-1/(4*5*9)+...
       = 3 + sum((-1)**(k+1)*1/(k*(k+1)*(2k+1)))       # 收敛较慢
    Nilakantha series
    '''
    s, k, i = 3, 1, 1
    a = nilakantha_series()
    while (abs(s - math_pi) > eps) and (i < limit):
        s += k * next(a)
        k = -k
        i += 1
    return (s, i)


def pi_limit_sin(n):
    return radians(n*sin(180.0/n))


def test_nilakantha_iter():
    nList = [20, 50, 100, 180, 450, 800, 1500]
    print("==Nilakantha series with iterations for PI==")
    for n in nList:
        start = timeit.default_timer()
        mypi = nilakantha_iter(n)
        stop = timeit.default_timer()
        print('Elapsed(s)={T}, Iterations={N}, PI={Pi}'.format(
            T=stop-start, N=n, Pi=mypi))


def test_nilakantha_epson():
    '''The fastest convergence method
    '''
    print("===Nilakantha series sum with epson for PI===")
    for j in range(7, 15):
        epson = 10**(-j)
        start = timeit.default_timer()
        mypi, n_iter = nilakantha_epson(epson)
        stop = timeit.default_timer()
        print('Elapsed(s)={T}, Iterations={N}, Epson={E}, PI={Pi}'.format(
            T=stop-start, N=n_iter, E=epson, Pi=mypi))


def Nilakantha_series():
    # Approximation of the number PI through the Nilakantha's series
    # Arbitrary precision
    # Language: Python
    # Author: Jose Cintra (jose.cintra@html-apps.info)

    getcontext().prec = 100

    s = Decimal(1)   # Signal for the next operation
    pi = Decimal(3)

    print("Approximation of the number PI through the Nilakantha's series\n")
    n = int(input("Enter the number of iterations: "))

    print("\nPlease wait. Running...\n")

    for i in range(2, n * 2, 2):
        pi += s*(Decimal(4)/(Decimal(i)*Decimal(i+1)*(Decimal(i+2))))
        s = -s

    print("Aproximated value of PI :", pi)


if __name__ == '__main__':
    test_nilakantha_iter()
    test_nilakantha_epson()

#!/usr/bin/python
# -*- encoding: UTF-8 -*-
"""
Algorithms of Gregory-Leibniz series sum for calculating PI
PI/4=1-1/3+1/5-1/7+...
1. Iterations: Leibniz_iter(n)
2. Epson     : Leibniz_epson(eps)
"""


import timeit
import math

math_pi = math.pi


def reciprocal_of_odd(n):
    # series for reciprocal of an odd number: 1, -1/3,1/5,-1/7,...
    return (-1)**n/(2*n+1)


def series_for_reciprocal_of_odd():
    # generate series for reciprocal of odd number
    n = 0
    while True:
        yield 1.0/(2*n+1)
        n += 1


def sum_recipodd_series(n):
    # sum for Gregory-Leibniz series 1-1/3+1/5-1/7+...
    a = series_for_reciprocal_of_odd()
    s, k = 0, 1
    for _ in range(n):
        s += k * next(a)
        k = -k
    return s


def Leibniz_iter(n):
    # get PI from 4*(1-1/3+1/5-1/7+...)
    return 4*sum_recipodd_series(n)


def test_Leibniz_iter():
    nList = [1e4, 1e6, 1e8]
    print("==Gregory Leibniz Series Generator with Iterations for PI==")
    for n in nList:
        n = int(n)
        print("Iterations={N}, PI={Pi}".format(N=n, pi=Leibniz_iter(n)))


def Leibniz_epson(eps):
    '''
    π = 4*(1-1/3+1/5-1/7+1/9-1/11+...)
    Gregory-Leibniz Series sum
    Input: deviation 'eps'
    Output: PI and iterations
    '''
    s, k, i = 0, 1, 1
    ''' given iteration upper number 'up':
    for i in range(1, up):
        s += k*1/(2*i-1.0)
        k = -k
    #for i in range(1, up, 4): # odd number, period is 4.
    #    s += 1.0/i - 1.0/(i+2)
    '''
    a = series_for_reciprocal_of_odd()
    while (abs(4*s-math_pi) > eps) and (i < 1e9):
        s += k * next(a)
        k = -k
        i += 1

    return (4*s, i)


def test_Leibniz_epson():
    print("===Gregory Leibniz series sum for PI with epson===")
    for j in range(7, 9):
        epson = 10**(-j)
        start = timeit.default_timer()
        mypi, n_iter = Leibniz_epson(epson)
        stop = timeit.default_timer()
        print('Elapsed(s)={T}, Iterations={N}, Epson={Eps}, PI={Pi}'.format(
            T=stop-start, N=n_iter, Eps=epson, Pi=mypi))


if __name__ == '__main__':
    test_Leibniz_iter()
    test_Leibniz_epson()

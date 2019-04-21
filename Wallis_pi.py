#!/usr/bin/python
# -*- coding: UTF-8 -*-


import timeit
import math
# from math import sin,radians,pi

EPSON = 1e-4  # default 4 precision
math_pi = math.pi


def wallis_series():
    k = 1
    while True:
        a = 1+1/(4*k*k-1)
        yield a
        k += 1


def wallis_iter(n):
    '''
    suppose sin(x) = c*(1-x/(kπ))(1+x/(kπ))x (k=-1,+1, -2,+2, ...)
    c=1
    so sinx = \\prod_{k=1} ^{\\infty} x*(1-x^2/(k*π)^2) (k=1,2,3,...)
    let x = π/2, we get
    π/2 = \\prod_{k=1}^{\\infty} (4k^2)/(4k^2-1) = 1/(1-1/(4k^2))  k=1,2,3,...
    from Wallis Product for pi
    '''
    k = 1
    a = wallis_series()
    for _ in range(n):
        k *= next(a)
    return 2*k


def wallis_epson(eps):
    k, i = 1, 1
    a = wallis_series()
    while (abs(2*k-math_pi) > eps) and (i < 1e9):
        k *= next(a)
        i += 1
    return (2*k, i)


def test_wallis_iter():
    nList = [500, 1500, 5000, 10000, 1000000]
    print("==John Wallis' Product with iterations for π==")
    for max in nList:
        start = timeit.default_timer()
        mypi = wallis_iter(max)
        stop = timeit.default_timer()
        print('Elapsed(s)={T}, Iterations={N}, PI={Pi}'.format(
            T=stop-start, N=max, Pi=mypi))


def test_wallis_epson():
    my_epson = EPSON*1e-4  # 8 decimal place precision is ok, 9 cannot work.
    print("===John Wallis' Product with epson for π===")
    for i in range(7, 9):
        my_epson = 10**(-i)
        start = timeit.default_timer()
        my_pi, n_iter = wallis_epson(my_epson)
        stop = timeit.default_timer()
        print('Elapsed(s)={T}, Iterations={N}, Epson={E}, PI={Pi}'.format(
            T=stop-start, N=n_iter, E=my_epson, Pi=my_pi))


if __name__ == '__main__':
    test_wallis_iter()
    test_wallis_epson()

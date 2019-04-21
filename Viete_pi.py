#!/usr/bin/python
# -*- coding: UTF-8 -*-


import timeit
import math
from math import sqrt, pi

# PI = Decimal('3.141592653589793238462643383279502884197169399375105820974944
# 5923078164062')
math_pi = pi


def sqrt2_series():
    '''
    generator for viete series
    return: series sqrt(2), sqrt(2+sqrt(2)),....
    '''
    _a = sqrt(2)
    while True:
        yield _a
        _a = sqrt(2+_a)


def viete_iter(n):
    '''
    sin(x)/x = \\prod_{k=1} ^{\\infty} cos(x/2^k)
    let x = π/2, we get
    2/π = \\sqrt(2)/2 * \\sqrt(2+sqrt(2))/2 *...
    from viete formula for 2/pi
    '''
    K = 1
    a = sqrt2_series()
    for _ in range(n):
        K = K * next(a)/2
    return 2/K


def viete_epson(eps):
    '''The most fastest algorithm for pi
    This Viete's formula with very good ratio of convergent.
    Return: (PI, Iterations)
    '''
    s, i = 1, 1
    a = sqrt2_series()
    while (abs(2/s-math_pi) > eps) and (i < 1e9):
        s *= next(a)/2
        i += 1
    return (2/s, i)


def test_viete_iter():
    nList = [20, 30, 40, 50, 100]
    print("==Viete Formula with iterations for 2/PI==")
    for max in nList:
        start = timeit.default_timer()
        my_pi = viete_iter(max)
        stop = timeit.default_timer()
        print('Elapsed(s)={T}, Iterations={N}, PI={Pi}'.format(
            T=stop-start, N=max, Pi=my_pi))


def test_viete_epson():
    print("===Viete Formula with epson for 2/PI===")
    for i in range(14, 17):
        my_epson = 10**(-i)
        start = timeit.default_timer()
        my_pi, n_iter = viete_epson(my_epson)
        stop = timeit.default_timer()
        print('Elapsed(s)={T}, Iterations={N}, Epson={E}, PI={Pi}'.format(
            T=stop-start, N=n_iter, E=my_epson, Pi=my_pi))
    # 'Deviations%%=', abs(my_pi-math_pi)*1e4,


if __name__ == '__main__':
    test_viete_iter()
    test_viete_epson()

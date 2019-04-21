#!/usr/bin/python
#-*-encoding: utf-8 -*-


from decimal import Decimal, getcontext
import itertools as it

Decimal = float
# from decimal import Decimal  # To use arbitrary precision decimal type
getcontext().prec = 60


def nilakantha_series():
    yield Decimal(3)
    c = it.cycle([1, -1])
    for d in it.count(2, 2):
        yield Decimal(next(c)*4)/Decimal(d*(d+1)*(d+2))


def term_count(series, error, exact):
    for N, value in enumerate(it.accumulate(series)):
        if abs(value - exact) <= error:
            return N, value


PI = Decimal('3.14159265358979323846264338327950288419716939937510582'+
                '09749445923078164062')
M = 25
N, PAI=term_count(nilakantha_series(), 10**-M, PI)
print('Iterations={n}, PI={Pi}'.format(n=N, Pi=Decimal(PAI)))
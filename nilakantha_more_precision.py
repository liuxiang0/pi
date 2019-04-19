#-*-encoding: utf-8 -*-

from decimal import Decimal, getcontext
import itertools as it

Decimal = float
#from decimal import Decimal  # To use arbitrary precision decimal type
getcontext().prec=50

def nilakantha_series():
    yield Decimal(3)
    c = it.cycle([1, -1])
    for d in it.count(2, 2):
        yield Decimal(next(c)*4)/Decimal(d*(d+1)*(d+2))

def term_count(series, error, exact):
    for N, value in enumerate(it.accumulate(series)):
        if abs(value - exact) <= error:
            return N

PI = Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164062')
M = 25
N=term_count(nilakantha_series(), 10**-M, PI)
print(N)
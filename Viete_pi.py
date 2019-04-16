# -*- coding: UTF-8 -*-


import timeit
import math
from math import sqrt
#from math import sin,radians,pi

EPSON = 1e-4 # default 4 precision
math_pi = math.pi

def viete_pi_max(upper):
    '''
    sin(x)/x = \\prod_{k=1} ^{\\infty} cos(x/2^k)
    let x = π/2, we get 
    2/π = (\\sqrt(2)/2 * \\sqrt(2+sqrt(2))/2 *...
    from viete formula for 2/pi
    '''

    k = 1 
    a = sqrt(2)/2
    for _ in range(1,upper):
        k = k*a
        a = sqrt((1+a)/2)
    return 2.0/k

def viete_pi(eps=EPSON):
    """The most fastest algorithm for pi
    Very good ratio of convergence
    """
    s, i = 1, 1
    a = sqrt(2)/2
    while (abs(2.0/s-math_pi) > eps) and (i<1e9):
        s = s*a
        a = sqrt((1+a)/2)
        i += 1
    return (2.0/s, i)

def viete_pi2(eps=EPSON):
    """The most fastest algorithm for pi
    Very good ratio of convergence
    """
    s, i = 1, 1
    a = sqrt(2)
    while (abs(2.0/s-math_pi) > eps) and (i<1e9):
        s = s*a/2
        a = sqrt(2+a)
        i += 1
    return (2.0/s, i)

def test_viete_pi_max():
    upper=[500,1000,1500,2000,2500,3000,3500,4000,5000,10000,1000000]
    #upper = []
    for max in upper:
        start = timeit.default_timer()
        mypi = viete_pi_max(max)
        stop = timeit.default_timer()
        print('elapsed time=', stop-start, 'n=', max, 'deviations%%=', abs(mypi-math.pi)*1e4, 'π=', mypi)

def test_viete_pi():
    """
    =====Viete Formula for 2/π=====
    elapsed time= 2.261100007672212e-05 iteration number= 13 epson= 1e-07 deviations%%= 0.0007700492110629398 π= 3.141592576584872
    elapsed time= 1.4524999642162584e-05 iteration number= 15 epson= 1e-08 deviations%%= 4.8128079299658566e-05 π= 3.141592648776985
    elapsed time= 1.4885999917169102e-05 iteration number= 17 epson= 1e-09 deviations%%= 3.008002735782611e-06 π= 3.141592653288993
    elapsed time= 1.4447000012296485e-05 iteration number= 18 epson= 1e-10 deviations%%= 7.519984634996035e-07 π= 3.1415926535145933
    elapsed time= 1.9718000203283736e-05 iteration number= 20 epson= 1e-11 deviations%%= 4.6997961078432127e-08 π= 3.1415926535850933
    elapsed time= 1.7522000234748702e-05 iteration number= 22 epson= 1e-12 deviations%%= 2.9309887850104133e-09 π= 3.1415926535895
    elapsed time= 1.7984999885811703e-05 iteration number= 23 epson= 1e-13 deviations%%= 7.283063041541027e-10 π= 3.1415926535897203
    elapsed time= 2.0431999928405276e-05 iteration number= 25 epson= 1e-14 deviations%%= 3.9968028886505635e-11 π= 3.141592653589789
    """
    print("=====Viete Formula for 2/π=====")
    for i in range(7,15):
        my_epson = 10**(-i)
        start = timeit.default_timer()
        my_pi, n_iter = viete_pi2(my_epson)
        stop = timeit.default_timer()
        print('elapsed time=', stop-start, 'iteration number=', n_iter,
            'epson=', my_epson, 'deviations%%=', abs(my_pi-math.pi)*1e4, 
            'π=', my_pi)

if __name__ == '__main__':
    test_viete_pi()
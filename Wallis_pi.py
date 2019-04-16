# -*- coding: UTF-8 -*-


import timeit
import math
#from math import sin,radians,pi

EPSON = 1e-4 # default 4 precision

def wallis_pi_max(upper):
    '''
    suppose sin(x) = c*(1-x/(kπ))(1+x/(kπ))x (k=-1,+1, -2,+2, ...)
    c=1
    so sinx = \\prod_{k=1} ^{\\infty} x*(1-x^2/(k*π)^2) (k=1,2,3,...)
    let x = π/2, we get 
    π/2 = \\prod_{k=1}^{\\infty} (4k^2)/(4k^2-1) = 1/(1-1/(4k^2))  k=1,2,3,...
    from Wallis Product for pi
    results-1:
        elapsed time= 8.497300041199196e-05 n= 500 π= 3.1400206785767715
        elapsed time= 0.0002362970008107368 n= 1000 π= 3.1408069608284497
        elapsed time= 0.0003733440007636091 n= 1500 π= 3.141068923892681
        elapsed time= 0.00042554899846436456 n= 2000 π= 3.141199880867808
        elapsed time= 0.0007371089996013325 n= 2500 π= 3.141278447195831
        elapsed time= 0.0005745939997723326 n= 3000 π= 3.1413308214743445
        elapsed time= 0.0007816679990355624 n= 3500 π= 3.141368230070024
        elapsed time= 0.0007163280006352579 n= 4000 π= 3.141396285640022
        elapsed time= 0.0009940180007106392 n= 5000 π= 3.1414355621755488
        elapsed time= 0.0018275210004503606 n= 10000 π= 3.1415141108281306
        elapsed time= 0.1809437590000016 n= 1000000 π= 3.1415918681912465
    '''

    k = 1
    for i in range(1,upper):
        k = k*1.0/(1.0-1.0/(4.0*i*i))
    return 2.0*k
    #print("upper= ", upper, "π/2= ", k)
    #print("upper= ", upper, "π= ", 2.0*k)

def wallis_pi(eps=EPSON):
    """
    elapsed time= 3.283482266000192 epson= 1e-07 π= 3.1415925 535897995
    elapsed time= 23.4369514670002 epson= 1e-08 π= 3.1415926 43589793
    """
    k, i = 1, 1
    while (abs(2.0*k-math.pi) > eps) and (i<1e9):
        k = k*1/(1.0-1.0/(4*i*i))
        i += 1
    return (2.0*k, i)

def test_wallis_pi_max():
    upper=[500,1000,1500,2000,2500,3000,3500,4000,5000,10000,1000000]
    #upper = []
    for max in upper:
        start = timeit.default_timer()
        mypi = wallis_pi_max(max)
        stop = timeit.default_timer()
        print('elapsed time=', stop-start, 'n=', max, 'deviations%%=', abs(mypi-math.pi)*1e4, 'π=', mypi)

def test_wallis_pi():
    my_epson = EPSON*1e-4 # 4+4=8 decimal place precision is ok, but 9 cannot work.
    print("=====John Wallis' Product for π=====")
    for i in range(7,9):
        my_epson = 10**(-i)
        start = timeit.default_timer()
        my_pi, n_iter = wallis_pi(my_epson)
        stop = timeit.default_timer()
        print('elapsed time=', stop-start, 'iteration number=', n_iter,
            'epson=', my_epson, 'deviations%%=', abs(my_pi-math.pi)*1e4, 
            'π=', my_pi)

if __name__ == '__main__':
    #test_wallis_pi()
    test_wallis_pi()
# -*- coding: UTF-8 -*-


import timeit
from math import sin,radians

def half_pi(upper):
    """
    sinx=c*(k*π-x)(k*π+x)x (k=-1,+1, -2,+2, ...)
    c=1/π^2*1/k^2 (k=1,2,3,...)
    so sinx = x*(1-x^2/(k*π)^2) (k=1,2,3,...)
    let x = π/2, we get 
    π/2 = (4k^2)/(4k^2-1) = 1/(1-1/(4k^2))  k=1,2,3,...

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
    """

    k = 1
    for i in range(1,upper):
        k = k*1.0/(1.0-1.0/(4.0*i*i))
    return 2*k
    #print("upper=", upper, "half_π=",k)
    #print("upper=", upper, "π=", 2.0*k)

if __name__ == '__main__':
    upper=[500,1000,1500,2000,2500,3000,3500,4000,5000,10000,1000000]
    #upper = []
    for max in upper:
        start = timeit.default_timer()
        pi = half_pi(max)
        stop = timeit.default_timer()
        print('elapsed time=', stop-start, 'n=', max, 'π=', pi)
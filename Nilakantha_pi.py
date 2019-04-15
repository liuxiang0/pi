# -*- encoding: UTF-8 -*-


import timeit
from math import sin, radians, pi
from decimal import Decimal, getcontext

def GregoryLeibniz(up):
    """
    π = 4*(1-1/3+1/5-1/7+1/9-1/11+...)
    Gregory-Leibniz Series
    Result-1:
        time= 0.01116342400018766 n= 10000 pi= 3.1414926535900345
        time= 0.05287647299883247 n= 100000 pi= 3.1415826535897198
        time= 0.5135733970000729 n= 1000000 pi= 3.1415916535897743
        time= 5.146407479000118 n= 10000000 pi= 3.1415925535897915
    Result-2:
        elapsed time= 0.0003674100007629022 n= 10000 pi= 3.1413926535917893
        elapsed time= 0.004349148000983405 n= 100000 pi= 3.141572653589808
        elapsed time= 0.05806082999879436 n= 1000000 pi= 3.1415906535898936
        elapsed time= 0.38916986000003817 n= 10000000 pi= 3.14159245358981
        elapsed time= 4.1743483019999985 n= 100000000 pi= 3.1415926335405047
    """

    s = 0
    #k = 1
    #for i in range(1, up):
    #    s += k*1/(2*i-1.0)
    #    k = -k

    for i in range(1, up, 4):
        s += 1.0/i - 1.0/(i+2)
    return 4*s

def Nilakantha(n):
    """
    pi = 3+4/(2*3*4)-4*/(4*5*6)+4/(6*7*8)-4/(8*9*10)-...
       = 3 + sum{(-1)**(i/2+1)*4.0/(i*(i+1)*(i+2))}    # 收敛较快     
       = 3 + 1/(1*2*3)-1/(2*3*5)+1/(3*4*7)-1/(4*5*9)+...
       = 3 + sum((-1)**(k+1)*1/(k*(k+1)*(2k+1)))       # 收敛较慢
    Nilakantha series
    Result:
        elapsed time= 0.002012544000535854 n= 10000 pi= 3.14159265359 1801
        elapsed time= 0.03268574599860585 n= 100000 pi= 3.14159265358978 9
        elapsed time= 0.22780541599968274 n= 1000000 pi= 3.141592653589787
        elapsed time= 2.1424825150006654 n= 10000000 pi= 3.141592653589787
        elapsed time= 21.897401184000046 n= 100000000 pi= 3.141592653589787
        elapsed time= 211.97589817000153 n= 1000000000 pi= 3.141592653589787

        elapsed time= 0.011356643999533844 n= 10000 pi= 3.1415926535900383
        elapsed time= 0.07902656999976898 n= 100000 pi= 3.141592653589787
        elapsed time= 0.7144408519998251 n= 1000000 pi= 3.141592653589787
        elapsed time= 6.582710100999975 n= 10000000 pi= 3.141592653589787
        elapsed time= 67.80659229699995 n= 100000000 pi= 3.141592653589787
    """
    s = 3.0
    for i in range(2,n,2):
        #s += 4.0/(2*i*(2*i-1.0)*(2*i-2.0))-4.0/(2*i*(2*i+1.0)*(2*i+2.0))
        s += 1.0/(i*(2*i-1)*(i-1)) - 1.0/(i*(2*i+1.0)*(i+1))
    
    # k=1
    #for i in range(1,n):
    #    s += k*1.0/(i*(i+1.0)*(2*i+1.0))
    #    k = -k
    return s

def pi_limit_sin(n):
    """
    elapsed time= 9.774999853107147e-06 n= 10000 pi= 3.141423010334743
    elapsed time= 1.223700019181706e-05 n= 100000 pi= 3.14159 0957130035
    elapsed time= 1.011999756883597e-06 n= 1000000 pi= 3.1415926 366251 93
    elapsed time= 1.621000137674855e-06 n= 10000000 pi= 3.141592653 420147
    elapsed time= 1.7880001905723475e-06 n= 100000000 pi= 3.14159265358 80967
    elapsed time= 1.3888000012229895e-05 n= 10000000000 pi= 3.141592653589793
    elapsed time= 2.5710000954859424e-06 n= 100000000000 pi= 3.141592653589793
    elapsed time= 2.0530001165752765e-06 n= 1000000000000 pi= 3.141592653589793
    """
    return radians(n*sin(180.0/n))

def test_GregoryLeibniz():
    """
    =====Gregory Leibniz series=====
    elapsed time= 0.00011285099935776088 n= 1000 deviations%%= 19.999980000107165 π= 3.1395926555897824
    elapsed time= 0.0010005920012190472 n= 10000 deviations%%= 1.9999999800379697 π= 3.1413926535917893
    elapsed time= 0.006130163999841898 n= 100000 deviations%%= 0.1999999998503199 π= 3.141572653589808
    elapsed time= 0.05090512599963404 n= 1000000 deviations%%= 0.019999998994713053 π= 3.1415906535898936
    elapsed time= 0.46311455800059775 n= 10000000 deviations%%= 0.0019999998324138346 π= 3.14159245358981
    elapsed time= 4.588323792000665 n= 100000000 deviations%%= 0.0002004928845167342 π= 3.1415926335405047
    """
    print("=====Gregory Leibniz series=====")
    math_pi = pi # pi_limit_sin(100000000000)
    for j in range(3,9):
        n = 10**j
        start = timeit.default_timer()
        mypi = GregoryLeibniz(n)
        stop = timeit.default_timer()
        print('elapsed time=', stop-start, 'n=', n, 'deviations%%=', abs(mypi-math_pi)*1e4, 'π=', mypi)
    
def test_Nilakantha():
    """The fastest convergence method
    =====Nilakantha series=====
    elapsed time= 0.0003047879999940051 n= 1000 deviations%%= 2.5075319598499846e-06 π= 3.14159265333904
    elapsed time= 0.0033252370012633037 n= 10000 deviations%%= 2.6778579353958776e-09 π= 3.1415926535895253
    elapsed time= 0.03417829800127947 n= 100000 deviations%%= 2.6778579353958776e-09 π= 3.1415926535895253
    elapsed time= 0.33687384800032305 n= 1000000 deviations%%= 2.6778579353958776e-09 π= 3.1415926535895253
    elapsed time= 3.3668270830003166 n= 10000000 deviations%%= 2.6778579353958776e-09 π= 3.1415926535895253
    elapsed time= 31.370165743999678 n= 100000000 deviations%%= 2.6778579353958776e-09 π= 3.1415926535895253
    """
    print("=====Nilakantha series=====")
    math_pi = pi # pi_limit_sin(100000000000)
    for j in range(3,9):
        n = 10**j
        start = timeit.default_timer()
        mypi = Nilakantha(n)
        stop = timeit.default_timer()
        print('elapsed time=', stop-start, 'n=', n, 'deviations%%=', abs(mypi-math_pi)*1e4, 'π=', mypi)

def Nilakantha_series():
    # Approximation of the number PI through the Nilakantha's series
    # Arbitrary precision
    # Language: Python
    # Author: Jose Cintra (jose.cintra@html-apps.info)

    getcontext().prec = 100

    s = Decimal(1)   #Signal for the next operation
    pi = Decimal(3)

    print ("Approximation of the number PI through the Nilakantha's series\n")
    n = int(input("Enter the number of iterations: "))

    print("\nPlease wait. Running...\n")

    for i in range (2, n * 2, 2):
        pi = pi + s * (Decimal(4) / (Decimal(i) * (Decimal(i) + Decimal(1)) * (Decimal(i) + Decimal(2))))
        s = -1 * s

    print ("Aproximated value of PI :")
    print (pi)


if __name__ == '__main__':
    #test_GregoryLeibniz()
    #test_Nilakantha()
    Nilakantha_series()
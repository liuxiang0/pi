# -*- encoding: UTF-8 -*-


import timeit
from math import sin,radians

def pi_GregoryLeibniz_series(up):
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
    for i in range(1, up, 4):
        #s += (-1)**i*4.0/(2.0*i+1.0)
        s += 1.0/i - 1.0/(i+2.0)
    return 4*s

def pi_nilakantha_series(n):
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
        s += (-1)**(i/2+1)*4.0/(i*(i+1.0)*(i+2.0))
    #for i in range(1,n):
    #    s += (-1)**(i+1)/(i*(i+1.0)*(2*i+1.0))
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
    for j in range(4,8):
        n = 10**j
        start = timeit.default_timer()
        pi = pi_gleibniz_series(n)
        stop = timeit.default_timer()
        print('elapsed time=', stop-start, 'n=', n, 'pi=', pi)
    
    for j in range(4,9):
        n = 10**j
        start = timeit.default_timer()
        pi = pi_nilakantha_series(n)
        stop = timeit.default_timer()
        print('elapsed time=', stop-start, 'n=', n, 'pi=', pi)

if __name__ == '__main__':

    for j in range(4,9):
        n = 10**j
        start = timeit.default_timer()
        mypi = pi_GregoryLeibniz_series(n)
        #pi = pi_limit_sin(n)
        stop = timeit.default_timer()
        print('elapsed time=', stop-start, 'n=', n, 'pi=', mypi)
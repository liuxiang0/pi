# -*- encoding: UTF-8 -*-


import timeit
import math

math_pi = math.pi

def GregoryLeibniz_pi(eps):
    """
    π = 4*(1-1/3+1/5-1/7+1/9-1/11+...)
    Gregory-Leibniz Series sum
    Input: deviation 'eps'
    Output: pi and iteration_number

    Test Result:
        elapsed time= 0.0003674100007629022 n= 10000 pi= 3.1413926535917893
        elapsed time= 0.004349148000983405 n= 100000 pi= 3.141572653589808
        elapsed time= 0.05806082999879436 n= 1000000 pi= 3.1415906535898936
        elapsed time= 0.38916986000003817 n= 10000000 pi= 3.14159245358981
        elapsed time= 4.1743483019999985 n= 100000000 pi= 3.1415926335405047
    """

    s, k, i = 0, 1, 1
    ''' given iteration upper number 'up':
    for i in range(1, up):
        s += k*1/(2*i-1.0)
        k = -k
    #for i in range(1, up, 4): # odd number, period is 4.
    #    s += 1.0/i - 1.0/(i+2)
    '''
    while (abs(4*s-math_pi)>eps) and (i<1e9):
        s += k*1/(2*i-1.0)
        k = -k
        i += 1

    return (4*s,i)

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
    print("=====Gregory Leibniz series sum=====")
    for j in range(7,9):
        epson = 10**(-j)
        start = timeit.default_timer()
        mypi, n_iter = GregoryLeibniz_pi(epson)
        stop = timeit.default_timer()
        print('elapsed time=', stop-start, 'iteration number=', n_iter,
            'epson=', epson, 'deviations%%=', abs(mypi-math_pi)*1e4,
            'π=', mypi)
    

if __name__ == '__main__':
    test_GregoryLeibniz()
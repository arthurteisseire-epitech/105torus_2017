from bisection import *

def newton(a0, a1, a2, a3, a4, n):
    x_n = 0.5
    x = x_n - (f4(x_n, a0, a1, a2, a3, a4)) / derived(x_n, a0, a1, a2, a3, a4)
    print('x = %s' %(str(round(x_n, n)).rstrip('0')[:n + 2]))
    while (True):
        x = x_n - (f4(x_n, a0, a1, a2, a3, a4) / derived(x_n, a0, a1, a2, a3, a4))
        if (round(x_n * pow(10, n)) == round(x * pow(10, n))):
            break
        x_n = x
        print('x = %s' %(str(round(x_n, n)).rstrip('0')[:n + 2]))

def derived(x, a0, a1, a2, a3, a4):
    return (4 * (a4 * pow(x, 3)) + 3 * (a3 * pow(x, 2)) + 2 * (a2 * pow(x, 1)) + a1)

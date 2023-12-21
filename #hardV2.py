#hard
import math 
def f(x):
    return 3*math.cos(x) - math.exp(x)
def g(x):
    return -3*math.sin(x) - math.exp(x)

def newtonLaGlr(x0,r,N):
    print('\n\n*** méthode newton raphson ***')
    step = 1
    flag = 1
    obligation = True
    while obligation:
        if g(x0) == 0.0:
            print('la division par 0 arrive!')
            obligation = False
        x1 = x0 - f(x0)/g(x0)
        print('iteration-%d, x1 = %0.6f, f(x1) = %0.6f and g(x1) = %0.6f' % (step, x1, f(x1), g(x1)) ) 
        x0 = x1
        step = step + 1

        if step > N:
            flag = 0
            obligation = False

        obligation = abs(f(x1)) > e

    if flag==1:
        print('\nLa racine cubique requise est: %0.8f' % x1)
    else:
        print('\nNan coïncident.')

x0 = input('Entre une valeur la!!:')
e = input('On tolère un peux tout de même:')
N = input('Max Step:')

x0 = float(x0)
e = float(e)


N = int(N)

newtonLaGlr(x0,e,N)
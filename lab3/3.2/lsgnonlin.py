from numpy import linalg as la
from math import sqrt

eps = 0.00001
M   = 100
n   = 2

def f( x ):
    x1 = x[0]
    x2 = x[1]

    return 4 * ( x1 - 5 )**2 + 2 * ( x2 - 6 )**4

def H( x ):
    return [[8, 0],[0, 24 * x[1]**2 - 288 * x[1] + 864]]

def grad( x ):
    return [ 8 * x[0] - 40, 8 * x[1]**3 - 144 * x[1]**2 + 864 * x[1] - 1728 ]

def E(n):
    e = [[0]*n for i in range(n)]

    for i in range(n):
        e[i][i] = 1

    return e

def norm( x ):
    return sqrt( sum([ a**2 for a in x ]) )
    
def addM( M1, M2 ):
    return [ [ x1 + x2 for x1, x2 in zip( Mi1, Mi2 ) ] for Mi1, Mi2 in zip( M1, M2 ) ]

def subX( xs1, xs2 ):
    return [ x1 - x2 for x1, x2 in zip( xs1, xs2 ) ]

def mulM( M, k ):
    return [[ x * k for x in xs ] for xs in M ]

def mulMx( M, x ):
    return [ sum([ M[i][j] * x[j] for j in range(n) ]) for i in range(n) ]

def lsgnonlin( f, grad, H, x, g, k ):
    gx = grad( x )
    
    if norm( gx ) < eps or k >= M:
        return x, f( x )

    d  = mulMx( la.inv( addM( H( x ), mulM( E(n), g ))), gx )
    xk = subX( x, d )

    if f( xk ) < f( x ):
        return lsgnonlin( f, grad, H, xk, g / 2, k + 1 )
    else:
        return lsgnonlin( f, grad, H, xk, 2 * g, k + 1 )

def main():
    x = [1, 1]
    g = 10**4

    print lsgnonlin( f, grad, H, x, g, 0 )

if __name__ == '__main__':
    main()
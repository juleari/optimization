import math

def trythis( x, coefs ):
    s, r = 1, 0

    while len( coefs ):
        r += coefs.pop() * s
        s *= x

    return r

def calcUr( a, b, c, d, e, eps=0.1, i=0.000001 ):
    
    arr = [ ( abs( trythis( x / (1 / i), [a, b, c, d, e] )), x / (1 / i)) for x in range( -3 * int(1 / i), -1 * int(1 / i) ) ]

    x1 = min(arr)[1]
    x21 = 2 + math.sqrt( x1**2 - 6 * x1 + 4 )
    x22 = 2 - math.sqrt( x1**2 - 6 * x1 + 4 )

    f1 = (x1 - 2)**2 + (x21 - 3)**2 + x1*x21
    f2 = (x1 - 2)**2 + (x22 - 3)**2 + x1*x22
   
    return [(x1, x21, f1), (x1, x22, f2)]

if __name__ == '__main__':
    print calcUr(1, -6, -37, 144, 476)
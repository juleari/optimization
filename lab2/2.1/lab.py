from math import sqrt

a = 1
b = 0.5
g = 2

n = 2
p = 0.01
eps = 0.01

def f( x ):

    x1 = x[0]
    x2 = x[1]

    return 4 * ( x1 - 5 )**2 + 2 * ( x2 - 6 )**4

def calcD( d1, d2 ):

    D = [ [ d2 ] * n for i in range( n + 1 ) ]

    for i in range( n ):
        D[ i ][ i ] = d1

    return D

def calcds():
    return  p * ( sqrt( n + 1 ) + n - 1 ) / ( n * sqrt(2) ),\
            p * ( sqrt( n + 1 ) - 1 ) / ( n * sqrt(2) )

def getMinMaxSmax( x ):

    fx = [ ( f( x[i] ), i ) for i in range( len(x) ) ]
    fx.sort()

    return  fx[0][1],\
            fx[-1][1],\
            fx[-2][1]

def getMiddle( x, h ):
    return [ sum([ x[i][j] for i in range( n + 1 ) if i != h ]) / n for j in range( n ) ]

def addX( xs1, xs2 ):
    return [ x1 + x2 for x1, x2 in zip( xs1, xs2 ) ]

def subX( xs1, xs2 ):
    return [ x1 - x2 for x1, x2 in zip( xs1, xs2 ) ]

def mulX( xs, k ):
    return [ x * k for x in xs ]

def calcDiff( xs, x2 ):
    fx2 = f( x2 )
    return sqrt( sum([ f( x ) - fx2 for x in xs ]) / ( n + 1 ) )

def NedlerMid( x ):
    l, h, s = getMinMaxSmax( x )

    x2 = getMiddle( x, h )

    if calcDiff( x, x2 ) <= eps:
        return x[l], f( x[l] )

    x3 = reverse( x[h], x2 )

    if f( x3 ) <= f( x[l] ):
        x4   = tension( x2, x3 )
        x[h] = x4 if f( x4 ) < f( x[l] ) else x3

    elif f( x[s] ) < f( x3 ) and f( x3 ) <= f( x[h] ):
        x[h] = compress( x[h], x2 )

    elif f( x[l] ) < f( x3 ) and f( x3 ) <= f( x[s] ):
        x[h] = x3

    else:
        x = [ addX( x[l], mulX( subX( xj, x[l] ), 0.5 ) ) for xj in x ]

    return NedlerMid( x )

def reverse( xh, x2 ):
    return addX( x2, mulX( subX( x2, xh ), a ) )

def tension( x2, x3 ):
    return addX( x2, mulX( subX( x3, x2 ), g ) )

def compress( xh, x2 ):
    return addX( x2, mulX( subX( xh, x2 ), b ) )

def init():
    d1, d2 = calcds()
    return calcD( d1, d2 )

def main():
    x = init()

    print NedlerMid( x )

if __name__ == '__main__':
    main()
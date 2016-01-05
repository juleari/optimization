from lsgnonlin import lsgnonlin

r = 0.01
eps = 0
C = 4
    
def f( x ):
    return x[0]**2 + x[1]**2

def F( x ):
    return f( x ) + P( x )

def P( x ):
    return r * ( max(0, -x[0] + 1)**2 + max(0, x[0] + x[1] - 2)**2 ) / 2

def gradF( x ):
    g1  = 0 if x[0] >= 1 else r * x[0] - r
    g21 = 0 if x[0] + x[1] <= 2 else r * ( x[0] - 2 + x[1] )
    g22 = 0 if x[0] + x[1] <= 2 else r * ( x[1] - 2 + x[0] )
    
    return [ 2 * x[0] + g1 + g21, 2 * x[1] + g22 ]

def H( x ):
    g1 = 0 if x[0] >= 1 else 2 * r
    g2 = 0 if x[0] + x[1] <= 2 else r
    
    return [[2 + g1, g2], [g2, 2 + g2]]

def penalty( x ):
    global r

    xk, Fxk = lsgnonlin( F, gradF, H, x, 10**4, 0 )
    
    if P( xk ) <= eps:
        return xk, f( xk )

    r *= C
    return penalty( xk )

def main():
    x = [1, 1]

    print penalty( x )

if __name__ == '__main__':
    main()
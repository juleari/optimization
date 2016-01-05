from lsgnonlin import lsgnonlin

r = 0.01
eps = 0
C = 4
mu = [0, 0]
n = 2

def g1( x ):
    return -x[0] + 1

def g2( x ):
    return x[0] + x[1] - 2

g = [ g1, g2 ]
    
def f( x ):
    return x[0]**2 + x[1]**2

def L( x ):
    return f( x ) + P( x )

def P( x ):
    return sum([ max( 0, mi + r * gi(x) )**2 - mi**2 for mi, gi in zip( mu, g ) ]) / ( 2 * r )

def gradL( x ):
    xg1  = 0 if mu[0] + r * g[0](x) <= 0 else - mu[0] + r * x[0] - r
    xg21 = 0 if mu[1] + r * g[1](x) <= 0 else mu[1] + r * x[0] + r * x[1] / 2 - 2 * r
    xg22 = 0 if mu[1] + r * g[1](x) <= 0 else mu[1] + r * x[0] / 2 + r * x[1] - 2 * r
    
    return [ 2 * x[0] + xg1 + xg21, 2 * x[1] + xg22 ]

def H( x ):
    xg1 = 0 if mu[0] + r * g[0](x) <= 0 else r
    xg21 = 0 if mu[1] + r * g[1](x) <= 0 else r / 2
    xg22 = 0 if mu[1] + r * g[1](x) <= 0 else r
    
    return [[2 + xg1 + xg22, xg21], [xg21, 2 + xg22]]

def penalty( x ):
    global r, mu

    xk, Lxk = lsgnonlin( L, gradL, H, x, 10**4, 0 )

    if abs( P( xk ) ) <= eps:
        return xk, f( xk )

    r *= C
    mu = [ max( 0, mi + r * gi( xk ) ) for mi, gi in zip( mu, g ) ]
    return penalty( xk )

def main():
    x = [1, 1]

    print penalty( x )

if __name__ == '__main__':
    main()
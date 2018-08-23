# Enter your code here. Read input from STDIN. Print output to STDOUT.

import math

def normal(x, mu, sigma):
    ans = 0.5 * ( 1 + math.erf( (x - mu) / ( sigma * math.sqrt(2) ) ) )
    return ans

mu = 20
sigma = 2

x = 19.5
y = 20
z = 22

pA = normal(x, mu, sigma)
print "%.3f" % pA

pB = normal(z, mu, sigma) - normal(y, mu, sigma)
print "%.3f" % pB

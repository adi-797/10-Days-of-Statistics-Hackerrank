# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def phi(x, mu, sigma):
    ans = 0.5 * ( 1 + math.erf( (x - mu) / ( sigma * math.sqrt(2) ) ) )
    return ans

maxweight = 250
mu = 2.4
sigma = 2.0
n = 100

muprime = mu * n
sigmaprime = sigma * math.sqrt(n)

print "%.4f" % phi(maxweight, muprime, sigmaprime)


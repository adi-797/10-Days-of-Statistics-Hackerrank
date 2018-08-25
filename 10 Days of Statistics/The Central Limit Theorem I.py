# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def phi(x, mu, sigma):
    ans = 0.5 * ( 1 + math.erf( (x - mu) / ( sigma * math.sqrt(2) ) ) )
    return ans

maxweight = 9800
mu = 205
sigma = 15
n = 49

muprime = mu * n
sigmaprime = sigma * math.sqrt(n)

print "%.4f" % phi(maxweight, muprime, sigmaprime)


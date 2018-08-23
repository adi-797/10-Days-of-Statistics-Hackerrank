# Enter your code here. Read input from STDIN. Print output to STDOUT.

import math

def normal(x, mu, sigma):
    return 0.500 * ( 1 + math.erf( (x - mu) / ( sigma * math.sqrt(2) ) ) )

mu = 70.000
sigma = 10.000

x = 80.000
y = 60.000

pB = normal(100, mu, sigma) - normal(x, mu, sigma)
print "%.3f" % (pB*100)

pB = normal(100, mu, sigma) - normal(y, mu, sigma)
print "%.3f" % (pB*100)

pA = normal(y, mu, sigma)
print "%.3f" % (pA*100)

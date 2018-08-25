import math

mu_p = 500.0    #population_mean
sigma_p = 80.0  #population sd
n = 100          
z = 1.96        #z value or no of sds from mean
ci = 0.95       #confidence interval
mu=mu_p
sigma = sigma_p/math.sqrt(n) 
interval = z*sigma
hi = mu+interval
lo = mu-interval

print('{number:.{digits}f}'.format(number=lo,digits=2))
print('{number:.{digits}f}'.format(number=hi,digits=2))

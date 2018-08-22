# Enter your code here. Read input from STDIN. Print output to STDOUT
def fact(n):
    if n==0:
        fact = 1;
    else:
        i = 1;
        fact = 1;
        while i<=n:
            fact = fact * i;
            i = i+1;
    return fact;

import sys

arr = (sys.stdin.readlines());
list = list((map(float, arr[0].split())));

p = float(list[0])/100;
n = float(list[1])

q = 1-p;
r=0;
prob = 0;
while r<=2:
    prob = prob + (fact(n)/(fact(r)*fact(n-r)))*(p**r)*(q**(n-r));
    r+=1;
    
print round(prob, 3)

r = 2;
prob =0;
while r<=n:
    prob = prob + (fact(n)/(fact(r)*fact(n-r)))*(p**r)*(q**(n-r));
    r+=1;
    
print round(prob, 3)

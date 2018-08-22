# Enter your code here. Read input from STDIN. Print output to STDOUT
def fact(n):
    i = 1;
    fact = 1;
    while i<=n:
        fact = fact * i;
        i = i+1;
    return fact;

import sys

arr = (sys.stdin.readlines());
list = list((map(float, arr[0].split())));

boys = float(list[0])
girls = float(list[1])

p = boys/(boys+girls);
q = 1-p;
n = 6;
r=3;
prob = 0;
while r<=n:
    prob = prob + (fact(n)/(fact(r)*fact(n-r)))*(p**r)*(q**(n-r));
    r+=1;
    
print round(prob, 3)

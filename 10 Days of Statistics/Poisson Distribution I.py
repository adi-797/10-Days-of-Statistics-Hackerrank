# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def fact(n):
    i = 1;
    fact = 1;
    if n>0:
        while i<=n:
            fact = fact * i;
            i = i+1;
    return fact;

arr = (sys.stdin.readlines());
l = list((map(float, arr[0].split())));
l = float(l[0])
k = list((map(float, arr[1].split())));
k = int(k[0])
e = 2.71828
prob = ((l**k)*(e**(-l)))/fact(k);
print round(prob, 3)

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

arr = (sys.stdin.readlines());
list1 = list((map(float, arr[0].split())));
list2 = list((map(float, arr[1].split())));

p = float(list1[0]/list1[1])
n = int(list2[0])
q = 1-p
prob = (q**(n-1))*(p)
print round(prob, 3)

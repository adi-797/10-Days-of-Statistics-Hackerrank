# Enter your code here. Read input from STDIN. Print output to STDOUTfrom math import factorial,exp
import sys

arr = (sys.stdin.readlines());
arr = list((map(float, arr[0].split())));
A = float(arr[0])
B = float(arr[1])

C_A = 160+40*(A**2+A)
C_B = 128+40*(B**2+B)

print(round(C_A,3))
print(round(C_B,3))

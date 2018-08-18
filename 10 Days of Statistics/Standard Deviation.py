# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import math

N = (sys.stdin.readlines());
arr = list(map(int, N[1].split()));

mean = sum(arr)/len(arr);

for i in range(len(arr)):
    arr[i] = (arr[i]-mean)**2;

print round(math.sqrt(sum(arr)/len(arr)), 1);

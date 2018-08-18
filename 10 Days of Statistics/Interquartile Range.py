import sys
arr = (sys.stdin.readlines());

nums = list((map(int, arr[1].split())));
f = list((map(int, arr[2].split())));

arr = [];
for i in range(len(nums)):
    for j in range(f[i]):
        arr.append(nums[i])

length = len(arr);
list = sorted(arr, key=int, reverse = True);
former = [];
later = [];

if length%2==0:
    Q1 = (list[int(length/2)] + list[int(length/2) - 1])/2;
    Q1 = int(Q1);
    for i in range(length/2):
        former.append(list[i]);
        later.append(list[i+length/2]);
else:
    Q1 = list[int(length/2)];
    Q1 = int(Q1);
    for i in range(int(length/2)):
        former.append(list[i]);
        later.append(list[i+int(length/2)+1]);
         
length = len(former);
                
if length%2==0:
    Q2 = ((former[int(length/2)] + former[int(length/2) - 1])/2);
    Q2 = round(Q2,1);
else:
    Q2 = former[int(length/2)];
    Q2 = round(Q2,1);

length = len(later);
                
if length%2==0:
    Q3 = ((later[int(length/2)] + later[int(length/2) - 1])/2);
    Q3 = round(Q3,1);
else:
    Q3 = later[int(length/2)];
    Q3 = round(Q3,1);

print abs(Q3-Q2)

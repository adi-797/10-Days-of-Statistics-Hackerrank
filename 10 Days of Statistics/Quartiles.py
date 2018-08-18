import sys

arr = (sys.stdin.readlines());

arr = arr[1];
list = [];
temp = "";

for i in range(len(arr)):
    temp += str(arr[i]);
    if arr[i] == " " or i==len(arr)-1:
        list.append(int(temp));
        temp = "";
        continue;

length = len(list);
list = sorted(list, key=int, reverse = True);
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
    Q2 = int(Q2);
else:
    Q2 = former[int(length/2)];
    Q2 = int(Q2);

length = len(later);
                
if length%2==0:
    Q3 = ((later[int(length/2)] + later[int(length/2) - 1])/2);
    Q3 = int(Q3);
else:
    Q3 = later[int(length/2)];
    Q3 = int(Q3);
    
print Q3;
print Q1;
print Q2;

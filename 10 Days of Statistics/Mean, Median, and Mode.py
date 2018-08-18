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
        
arr = list;
length = len(arr);

#mean
mean = sum(arr)/length;
mean = round(mean, 1);

#median
sorte = sorted(arr, key=int, reverse = True);

if length%2==0:
    median = ((sorte[int(length/2)] + sorte[int(length/2) - 1])/2);
    median = round(median, 1);
else:
    median = sorte[int(length/2)];
    median = round(median, 1);
    
#mode
n = length;
counter = {}
for i in range(n):
    try:
        counter[arr[i]] += 1
    except KeyError:
        counter[arr[i]] = 1
mode = None
best_count = 0
for key in counter:
    if counter[key] > best_count:
        mode = key
        best_count = counter[key]
    elif counter[key] == best_count and int(mode) > int(key):
        mode = key


print (mean);
print (median);
print (mode);

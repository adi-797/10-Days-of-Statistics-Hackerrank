N = int(input())
arr = list(map(int, input().split()))
w = list(map(int, input().split()))

for i in range(len(w)):
    arr[i] = arr[i]*w[i];
    
print (round((sum(arr)/sum(w)), 1));

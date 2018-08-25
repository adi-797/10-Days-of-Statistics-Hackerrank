import sys, math

arr = (sys.stdin.readlines());
x = list((map(float, arr[1].split())));
y = list((map(float, arr[2].split())));

ux = sum(x)/len(x)
uy = sum(y)/len(y)

xl = []
yl = []

for i in range(len(x)):
    xl.append((x[i]-ux)**2)

sdx = math.sqrt(sum(xl)/len(x))

for i in range(len(y)):
    yl.append((y[i]-uy)**2)

sdy = math.sqrt(sum(yl)/len(y))

num = x
for i in range(len(x)):
    num[i] = ((x[i]-ux)*(y[i]-uy))

pc = round(sum(num)/(len(x)*sdx*sdy), 3)
print pc

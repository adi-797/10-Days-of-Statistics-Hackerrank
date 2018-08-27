# Enter your code here. Read input from STDIN. Print output to STDOUT
from sklearn import linear_model
input_line = str(raw_input()).split()
m,n = int(input_line[0]),int(input_line[1])
x_train=[]
y_train=[]
for i in range(n):
    input_line = map(float,str(raw_input()).split())
    x_train.append(input_line[:m])
    y_train.append(input_line[m])
input_line = str(raw_input()).split()
k = int(input_line[0])
x_test =[]
for i in range(k):
    input_line = map(float,str(raw_input()).split())
    x_test.append(input_line)

lm = linear_model.LinearRegression()
lm.fit(x_train, y_train)
a = lm.intercept_
b = lm.coef_

y_pred = lm.predict(x_test)
for item in y_pred:
    print round(item,2)

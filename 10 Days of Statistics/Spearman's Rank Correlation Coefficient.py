from __future__ import division
# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
X = map(float, raw_input().strip().split(' '))
Y = map(float, raw_input().strip().split(' '))

def rank(Arr):
    sortedArr = sorted(Arr)
    ranks = [sortedArr.index(x)+1 for x in Arr]
    return ranks

rankX = rank(X)
rankY = rank(Y)

di = [(rX - rY) ** 2 for rX, rY in zip(rankX, rankY)]
ans = 1 - (6 * sum(di)) / (N * ((N ** 2) -1))
print round(ans, 3)

import sys
from bisect import bisect_left
input = sys.stdin.readline
a = int(input())
b = list(map(int, input().split()))
tails = []
pos = []
parent = [-1] * a
for i, val in enumerate(b):
    j = bisect_left(tails, val)
    if j == len(tails):
        tails.append(val)
        pos.append(i)
    else:
        tails[j] = val
        pos[j] = i
    if j > 0:
        parent[i] = pos[j-1]
length = len(tails)
res = []
k = pos[-1]
while k != -1:
    res.append(b[k])
    k = parent[k]
res.reverse()
print(length)
print(' '.join(map(str, res)))
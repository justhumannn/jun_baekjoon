import sys
input = sys.stdin.readline
a = int(input())
c = [0] * 10001
for _ in range(a):
    n = int(input())
    c[n] += 1
for i in range(1,10001):
    if c[i] != 0:
        for _ in range(c[i]):
            print(i)
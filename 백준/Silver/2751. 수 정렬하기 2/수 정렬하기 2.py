import sys
input = sys.stdin.readline
a = int(input())
b = []
b = set(b)
for _ in range(a):
    b.add(int(input()))
b = list(b)
b = sorted(b)
for i in range(0,a):
    print(b[i])
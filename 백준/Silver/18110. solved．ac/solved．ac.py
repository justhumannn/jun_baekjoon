import sys
input = sys.stdin.readline
a = int(input())
if a == 0:
    print(0)
else:
    b = int(a * 0.15 + 0.5)
    c = []
    for i in range(a):
        c.append(int(input()))
    c.sort()
    c = c[b:a - b]
    print(int(sum(c) / len(c) + 0.5))
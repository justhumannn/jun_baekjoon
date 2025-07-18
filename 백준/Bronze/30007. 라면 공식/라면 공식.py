import sys
input = sys.stdin.readline
a = int(input())
for _ in range(a):
    b, c, d = map(int, input().split())
    e = b * (d - 1) + c
    print(e)

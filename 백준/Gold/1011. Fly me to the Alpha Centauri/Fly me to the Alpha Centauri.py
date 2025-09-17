import sys
input = sys.stdin.readline

a = int(input())
for i in range(a):
    b, c = map(int, input().split())
    d = c - b
    e = int(d**0.5)
    if e * e == d:
        print(2 * e - 1)
    elif d <= e * e + e:
        print(2 * e)
    else:
        print(2 * e + 1)
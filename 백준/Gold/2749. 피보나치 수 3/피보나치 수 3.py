import sys
input = sys.stdin.readline
n = int(input())
n %= 1500000
a, b = 0, 1
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    for _ in range(2, n + 1):
        a, b = b, (a + b) % 1000000
    print(b)
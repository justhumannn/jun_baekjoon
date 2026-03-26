import sys

n, m = map(int, sys.stdin.readline().split())
if n % 3 == 0 or m % 3 == 0:
    print("YES")
else:
    print("NO")
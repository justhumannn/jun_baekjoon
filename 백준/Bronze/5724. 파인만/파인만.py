import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    ans = n * (n + 1) * (2 * n + 1) // 6
    print(ans)
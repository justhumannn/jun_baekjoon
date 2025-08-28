import sys
input = sys.stdin.readline

a = int(input())
numbers = [0] + list(map(int, input().split()))
dp = [[False] * (a + 1) for _ in range(a + 1)]
for i in range(1, a + 1):
    dp[i][i] = True
for i in range(1, a):
    if numbers[i] == numbers[i + 1]:
        dp[i][i + 1] = True
for i in range(a - 2, 0, -1):
    for j in range(i + 2, a + 1):
        if numbers[i] == numbers[j] and dp[i + 1][j - 1]:
            dp[i][j] = True
b = int(input())
result = []
for _ in range(b):
    start, end = map(int, input().split())
    result.append('1' if dp[start][end] else '0')

print('\n'.join(result))
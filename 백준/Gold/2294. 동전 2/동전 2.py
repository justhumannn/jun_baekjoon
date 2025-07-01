import sys
input = sys.stdin.readline
n,k = map(int, input().split())
a = set()
for i in range(n):
    a.add(int(input()))
a = list(a)
dp = [float('inf')] * (k+1)
for i in a:
    if i > k:
        continue
    dp[i] = 1
for i in range(1, k+1):
    for j in a:
        if i-j <= 0:
            continue
        dp[i] = min(dp[i], dp[i-j]+1)
if dp[k] == float('inf'):
    print(-1)
else:
    print(dp[k])
import sys
input = sys.stdin.readline
a = int(input())
b = []
for i in range(a):
    b.append(int(input()))
dp = [[1,0],[0,1]]
for i in range(2,41):
    dp.append([dp[i-1][0]+dp[i-2][0],dp[i-1][1]+dp[i-2][1]])
for i in b:
    print(*dp[i])
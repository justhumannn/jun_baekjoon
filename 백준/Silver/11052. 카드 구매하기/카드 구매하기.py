a = int(input())
b = list(map(int, input().split()))
b.insert(0,0)
dp = [0 for _ in range(a+1)]
for i in range(1,a+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i],b[j]+dp[i-j])
print(dp[a])
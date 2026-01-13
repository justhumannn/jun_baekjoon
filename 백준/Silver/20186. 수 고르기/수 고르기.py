import sys
input = sys.stdin.readline
N, K = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort(reverse=True)
ans = sum(nums[:K]) - (K * (K - 1) // 2)
print(ans)
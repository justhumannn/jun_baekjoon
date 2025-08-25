import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = set(map(int, input().split()))
nums = sorted(nums)
result = []
def backtrack(start):
    if len(result) == m:
        print(*result)
        return
    for i in range(start, len(nums)):
        result.append(nums[i])
        backtrack(i)
        result.pop()
    
backtrack(0)
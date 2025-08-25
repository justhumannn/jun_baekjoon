import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
visited = [False] * n
result = []
def backtrack():
    if len(result) == m:
        print(*result)
        return
    prev = None
    for i in range(n):
        if not visited[i] and nums[i] != prev:
            visited[i] = True
            result.append(nums[i])
            prev = nums[i]
            backtrack()
            result.pop()
            visited[i] = False
backtrack()
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
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            result.append(nums[i])
            backtrack()
            result.pop()
            visited[i] = False
backtrack()
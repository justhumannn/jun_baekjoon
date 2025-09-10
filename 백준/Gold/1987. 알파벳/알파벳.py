import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
a, b = map(int, input().split())
board = [input().strip() for _ in range(a)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cache = {}
ans = 1
start = 1 << (ord(board[0][0]) - ord('A'))
def dfs(x, y, visited):
    if (x, y, visited) in cache:
        return cache[(x, y, visited)]
    max_len = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < a and 0 <= ny < b:
            bit = 1 << (ord(board[nx][ny]) - ord('A'))
            if not visited & bit:
                max_len = max(max_len, 1 + dfs(nx, ny, visited | bit))
    cache[(x, y, visited)] = max_len
    return max_len

print(dfs(0, 0, start))
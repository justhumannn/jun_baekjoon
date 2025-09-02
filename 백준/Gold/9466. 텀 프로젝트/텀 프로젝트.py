import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x):
    global cycle_count
    visited[x] = 1
    next_node = student[x]

    if visited[next_node] == 0:
        dfs(next_node)
    elif visited[next_node] == 1:
        cur = next_node
        while True:
            cycle_count += 1
            cur = student[cur]
            if cur == next_node:
                break
    visited[x] = 2
t = int(input())
for _ in range(t):
    n = int(input())
    student = [0] + list(map(int, input().split()))
    visited = [0] * (n + 1)
    cycle_count = 0
    for i in range(1, n + 1):
        if visited[i] == 0:
            dfs(i)
    print(n - cycle_count)
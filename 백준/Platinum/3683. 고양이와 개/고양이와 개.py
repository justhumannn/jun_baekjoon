import sys

sys.setrecursionlimit(2000)
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    c, d, v = map(int, input().split())
    
    cat_lovers = []
    dog_lovers = []
    
    for _ in range(v):
        stay, leave = input().split()
        if stay.startswith('C'):
            cat_lovers.append((stay, leave))
        else:
            dog_lovers.append((stay, leave))
            
    n = len(cat_lovers)
    m = len(dog_lovers)
    
    adj = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if cat_lovers[i][0] == dog_lovers[j][1] or cat_lovers[i][1] == dog_lovers[j][0]:
                adj[i].append(j)
                
    match = [-1] * m
    
    def dfs(node, visited):
        for nxt in adj[node]:
            if visited[nxt]:
                continue
            visited[nxt] = True
            if match[nxt] == -1 or dfs(match[nxt], visited):
                match[nxt] = node
                return True
        return False
        
    match_count = 0
    for i in range(n):
        visited = [False] * m
        if dfs(i, visited):
            match_count += 1
            
    print(v - match_count)
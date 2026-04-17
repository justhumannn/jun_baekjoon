import sys

tokens = sys.stdin.read().split()
k = int(tokens[0])
n = int(tokens[1])
graph = [[] for _ in range(2 * k + 2)]
rev_graph = [[] for _ in range(2 * k + 2)]
idx = 2
for _ in range(n):
    l1 = int(tokens[idx])
    c1 = tokens[idx + 1]
    l2 = int(tokens[idx + 2])
    c2 = tokens[idx + 3]
    l3 = int(tokens[idx + 4])
    c3 = tokens[idx + 5]
    idx += 6
    u = l1 * 2 if c1 == 'R' else l1 * 2 + 1
    v = l2 * 2 if c2 == 'R' else l2 * 2 + 1
    w = l3 * 2 if c3 == 'R' else l3 * 2 + 1
    graph[u ^ 1].append(v)
    graph[v ^ 1].append(u)
    rev_graph[v].append(u ^ 1)
    rev_graph[u].append(v ^ 1)
    graph[v ^ 1].append(w)
    graph[w ^ 1].append(v)
    rev_graph[w].append(v ^ 1)
    rev_graph[v].append(w ^ 1)
    graph[w ^ 1].append(u)
    graph[u ^ 1].append(w)
    rev_graph[u].append(w ^ 1)
    rev_graph[w].append(u ^ 1)
visited = [False] * (2 * k + 2)
stack = []
edge_ptr = [0] * (2 * k + 2)
for i in range(2, 2 * k + 2):
    if not visited[i]:
        dfs_stack = [i]
        visited[i] = True
        while dfs_stack:
            curr = dfs_stack[-1]
            if edge_ptr[curr] < len(graph[curr]):
                nxt = graph[curr][edge_ptr[curr]]
                edge_ptr[curr] += 1
                if not visited[nxt]:
                    visited[nxt] = True
                    dfs_stack.append(nxt)
            else:
                stack.append(dfs_stack.pop())
visited = [False] * (2 * k + 2)
scc_id = [0] * (2 * k + 2)
scc_cnt = 0
while stack:
    node = stack.pop()
    if not visited[node]:
        scc_cnt += 1
        dfs_stack = [node]
        visited[node] = True
        while dfs_stack:
            curr = dfs_stack.pop()
            scc_id[curr] = scc_cnt
            for nxt in rev_graph[curr]:
                if not visited[nxt]:
                    visited[nxt] = True
                    dfs_stack.append(nxt)
ans = []
possible = True
for i in range(1, k + 1):
    if scc_id[2 * i] == scc_id[2 * i + 1]:
        possible = False
        break
    if scc_id[2 * i] > scc_id[2 * i + 1]:
        ans.append('R')
    else:
        ans.append('B')
if possible:
    sys.stdout.write("".join(ans) + "\n")
else:
    sys.stdout.write("-1\n")
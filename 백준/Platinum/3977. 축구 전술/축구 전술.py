import sys
input = sys.stdin.readline
T = int(input())
for t_case in range(T):
    if t_case > 0:
        input() 
    try:
        line = input().split()
        if not line:
            break
        n, m = map(int, line)
    except EOFError:
        break
    except Exception:
        continue
    adj = [[] for _ in range(n)]
    radj = [[] for _ in range(n)]
    for _ in range(m):
        v, w = map(int, input().split())
        adj[v].append(w)
        radj[w].append(v)
    visited = [False] * n
    order = []

    for i in range(n):
        if not visited[i]:
            stack = [(i, 0)]
            visited[i] = True
            while stack:
                v, idx = stack[-1]
                if idx < len(adj[v]):
                    stack[-1] = (v, idx + 1)
                    u = adj[v][idx]
                    if not visited[u]:
                        visited[u] = True
                        stack.append((u, 0))
                else:
                    stack.pop()
                    order.append(v)
    
    visited2 = [False] * n
    scc_count = 0
    scc = [[] for _ in range(n)]
    scc_num = [-1] * n 
    i = 0

    for v in reversed(order):
        if not visited2[v]:
            scc_count += 1 
            stack = [v]
            visited2[v] = True
            while stack:
                x = stack.pop()
                scc[i].append(x)
                scc_num[x] = i
                for y in radj[x]:
                    if not visited2[y]:
                        visited2[y] = True
                        stack.append(y)
            i += 1
    scc_count = i
    if scc_count == 0 and n > 0:
        print("Confused")
        print()
        continue
    if n == 0:
        print()
        continue

    scc_indegree = [0] * scc_count
    for u in range(n):
        for v in adj[u]:
            if scc_num[u] != scc_num[v]:
                scc_indegree[scc_num[v]] += 1

    source_scc_id = -1
    source_scc_count = 0
    for k in range(scc_count):
        if scc_indegree[k] == 0:
            source_scc_count += 1
            source_scc_id = k

    if source_scc_count == 1:
        result_nodes = scc[source_scc_id]
        result_nodes.sort()
        for node in result_nodes:
            print(node)
    else:
        print("Confused")
    print()
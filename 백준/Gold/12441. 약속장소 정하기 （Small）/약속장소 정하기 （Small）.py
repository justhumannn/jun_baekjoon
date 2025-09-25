import sys
import heapq

input = sys.stdin.readline
INF = 10**18

def dijkstra(a, adj, start):
    dist = [INF] * (a + 1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist

t = int(input())
for case in range(1, t + 1):
    a, b, c = map(int, input().split())
    x = []
    v = []
    for _ in range(b):
        xi, vi = map(int, input().split())
        x.append(xi)
        v.append(vi)

    adj = [[] for _ in range(a + 1)]
    for _ in range(c):
        data = list(map(int, input().split()))
        d, l = data[0], data[1]
        cj = data[2:]
        while len(cj) < l:
            cj += list(map(int, input().split()))
        for i in range(l - 1):
            u_city, v_city = cj[i], cj[i + 1]
            adj[u_city].append((v_city, d))
            adj[v_city].append((u_city, d))

    dist_list = [None] * b
    for i in range(b):
        dist_list[i] = dijkstra(a, adj, x[i])

    ans = INF
    for city in range(1, a + 1):
        max_time = 0
        ok = True
        for i in range(b):
            dist = dist_list[i][city]
            if dist == INF:
                ok = False
                break
            arrival = dist * v[i]
            if arrival > max_time:
                max_time = arrival
            if max_time >= ans:
                ok = False
                break
        if ok and max_time < ans:
            ans = max_time

    if ans == INF:
        print(f"Case #{case}: -1")
    else:
        print(f"Case #{case}: {ans}")
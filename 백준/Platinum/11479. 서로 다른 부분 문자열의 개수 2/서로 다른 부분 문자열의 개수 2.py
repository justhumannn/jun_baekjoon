import sys
s = sys.stdin.readline().strip()

n = len(s)
max_states = max(2 * n + 5, 20)
max_edges = max(3 * n + 5, 20)
head = [-1] * max_states
edge_to = [0] * max_edges
edge_char = [0] * max_edges
edge_nxt = [-1] * max_edges
edge_cnt = 0
length = [0] * max_states
link = [-1] * max_states
last = 0
sz = 1
for char in s:
    c = ord(char) - 97
    cur = sz
    sz += 1
    length[cur] = length[last] + 1
    p = last
    while p != -1:
        e = head[p]
        q = -1
        while e != -1:
            if edge_char[e] == c:
                q = edge_to[e]
                break
            e = edge_nxt[e]
        if q != -1:
            break
        edge_to[edge_cnt] = cur
        edge_char[edge_cnt] = c
        edge_nxt[edge_cnt] = head[p]
        head[p] = edge_cnt
        edge_cnt += 1
        p = link[p]
    if p == -1:
        link[cur] = 0
    else:
        if length[p] + 1 == length[q]:
            link[cur] = q
        else:
            clone = sz
            sz += 1
            length[clone] = length[p] + 1
            e = head[q]
            while e != -1:
                edge_to[edge_cnt] = edge_to[e]
                edge_char[edge_cnt] = edge_char[e]
                edge_nxt[edge_cnt] = head[clone]
                head[clone] = edge_cnt
                edge_cnt += 1
                e = edge_nxt[e]
            link[clone] = link[q]
            while p != -1:
                e = head[p]
                found_q = False
                while e != -1:
                    if edge_char[e] == c:
                        if edge_to[e] == q:
                            edge_to[e] = clone
                            found_q = True
                        break
                    e = edge_nxt[e]
                if not found_q:
                    break
                p = link[p]
            link[q] = link[cur] = clone
    last = cur
ans = 0
for i in range(1, sz):
    ans += length[i] - length[link[i]]
sys.stdout.write(str(ans) + '\n')
import sys
data = sys.stdin.read().split()

n = int(data[0])
S = [n] * (n + 1)
for i in range(1, n + 1):
    S[i] = S[i - 1] + (1 if data[i] == '1' else -1)
m = int(data[n + 1])
queries = []
B = 316
idx = n + 2
for q_id in range(m):
    l = int(data[idx]) - 1
    r = int(data[idx + 1])
    idx += 2
    queries.append((l // B, r, l, q_id))
queries.sort()
ans = [0] * m
first = [1000000] * (2 * n + 1)
last = [-1000000] * (2 * n + 1)
first_naive = [1000000] * (2 * n + 1)
blocks = {}
for q in queries:
    b, r, l, q_id = q
    if b not in blocks: blocks[b] = []
    blocks[b].append((r, l, q_id))
for b, b_queries in blocks.items():
    start_L = (b + 1) * B
    cur_R = start_L - 1
    max_ans = 0
    for r, l, q_id in b_queries:
        if r < start_L:
            res = 0
            for i in range(l, r + 1):
                v = S[i]
                if first_naive[v] == 1000000:
                    first_naive[v] = i
                elif i - first_naive[v] > res:
                    res = i - first_naive[v]
            ans[q_id] = res
            for i in range(l, r + 1):
                first_naive[S[i]] = 1000000
        else:
            while cur_R < r:
                cur_R += 1
                v = S[cur_R]
                if first[v] == 1000000:
                    first[v] = cur_R
                last[v] = cur_R
                if last[v] - first[v] > max_ans:
                    max_ans = last[v] - first[v]
            temp_ans = max_ans
            history = []
            for i in range(start_L - 1, l - 1, -1):
                v = S[i]
                history.append((v, first[v], last[v]))
                if last[v] == -1000000:
                    last[v] = i
                first[v] = i
                if last[v] - first[v] > temp_ans:
                    temp_ans = last[v] - first[v]
            ans[q_id] = temp_ans
            while history:
                v, old_f, old_l = history.pop()
                first[v] = old_f
                last[v] = old_l
    for i in range(start_L, cur_R + 1):
        v = S[i]
        first[v] = 1000000
        last[v] = -1000000
sys.stdout.write('\n'.join(map(str, ans)) + '\n')
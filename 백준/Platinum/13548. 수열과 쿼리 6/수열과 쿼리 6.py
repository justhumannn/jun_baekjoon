import sys

input_data = sys.stdin.read().split()
n = int(input_data[0])
a = [0] * (n + 1)
for i in range(1, n + 1):
    a[i] = int(input_data[i])
m = int(input_data[n + 1])
queries = []
idx = n + 2
for i in range(m):
    u = int(input_data[idx])
    v = int(input_data[idx + 1])
    queries.append((u, v, i))
    idx += 2
B = int(n ** 0.5)
queries.sort(key=lambda x: (x[0] // B, x[1] if (x[0] // B) % 2 == 0 else -x[1]))
ans = [0] * m
cnt = [0] * 100001
freq_cnt = [0] * 100001
max_f = 0
L = queries[0][0]
R = L - 1
for u, v, q_idx in queries:
    while R < v:
        R += 1
        x = a[R]
        freq_cnt[cnt[x]] -= 1
        cnt[x] += 1
        freq_cnt[cnt[x]] += 1
        if cnt[x] > max_f:
            max_f = cnt[x]
    while L > u:
        L -= 1
        x = a[L]
        freq_cnt[cnt[x]] -= 1
        cnt[x] += 1
        freq_cnt[cnt[x]] += 1
        if cnt[x] > max_f:
            max_f = cnt[x]
    while R > v:
        x = a[R]
        freq_cnt[cnt[x]] -= 1
        if cnt[x] == max_f and freq_cnt[cnt[x]] == 0:
            max_f -= 1
        cnt[x] -= 1
        freq_cnt[cnt[x]] += 1
        R -= 1
    while L < u:
        x = a[L]
        freq_cnt[cnt[x]] -= 1
        if cnt[x] == max_f and freq_cnt[cnt[x]] == 0:
            max_f -= 1
        cnt[x] -= 1
        freq_cnt[cnt[x]] += 1
        L += 1
    ans[q_idx] = max_f
print('\n'.join(map(str, ans)))
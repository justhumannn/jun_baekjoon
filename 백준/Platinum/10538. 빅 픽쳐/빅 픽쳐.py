import sys

input_data = sys.stdin.read().split()
hp = int(input_data[0])
wp = int(input_data[1])
hm = int(input_data[2])
wm = int(input_data[3])
P = input_data[4 : 4 + hp]
M = input_data[4 + hp : 4 + hp + hm]
MOD = 10**18 + 9
BASE1 = 5381
BASE2 = 313
B2_pw = pow(BASE2, wp, MOD)
B1_pw = pow(BASE1, hp, MOD)
P_bytes = [s.encode('ascii') for s in P]
M_bytes = [s.encode('ascii') for s in M]
target_hash = 0
for r in range(hp):
    row_hash = 0
    row = P_bytes[r]
    for c in range(wp):
        row_hash = (row_hash * BASE2 + row[c]) % MOD
    target_hash = (target_hash * BASE1 + row_hash) % MOD
H_row = []
cols = wm - wp + 1
for r in range(hm):
    curr = 0
    row = M_bytes[r]
    for c in range(wp):
        curr = (curr * BASE2 + row[c]) % MOD
    row_hashes = [curr]
    for c in range(wp, wm):
        curr = (curr * BASE2 - row[c - wp] * B2_pw + row[c]) % MOD
        row_hashes.append(curr)
    H_row.append(row_hashes)
ans = 0
col_hashes = [0] * cols
for r in range(hp):
    h_r = H_row[r]
    for c in range(cols):
        col_hashes[c] = (col_hashes[c] * BASE1 + h_r[c]) % MOD
for c in range(cols):
    if col_hashes[c] == target_hash:
        ans += 1
for r in range(hp, hm):
    h_r = H_row[r]
    h_r_rem = H_row[r - hp]
    for c in range(cols):
        col_hashes[c] = (col_hashes[c] * BASE1 - h_r_rem[c] * B1_pw + h_r[c]) % MOD
        if col_hashes[c] == target_hash:
            ans += 1
print(ans)
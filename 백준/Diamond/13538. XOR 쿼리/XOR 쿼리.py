import sys

input_data = sys.stdin.read().split()
M = int(input_data[0])

MAX_NODES = M * 20 + 10

lc = [0] * MAX_NODES
rc = [0] * MAX_NODES
cnt = [0] * MAX_NODES
roots = [0] * (M + 5)

node_cnt = 0
sz = 0

out = []
idx = 1

while idx < len(input_data):
    q_type = int(input_data[idx])
    
    if q_type == 1:
        x = int(input_data[idx+1])
        idx += 2
        
        sz += 1
        node_cnt += 1
        curr = node_cnt
        roots[sz] = curr
        prev = roots[sz - 1]
        
        for i in range(18, -1, -1):
            bit = (x >> i) & 1
            cnt[curr] = cnt[prev] + 1
            
            node_cnt += 1
            if bit == 0:
                lc[curr] = node_cnt
                rc[curr] = rc[prev]
                curr = lc[curr]
                prev = lc[prev]
            else:
                lc[curr] = lc[prev]
                rc[curr] = node_cnt
                curr = rc[curr]
                prev = rc[prev]
                
        cnt[curr] = cnt[prev] + 1
        
    elif q_type == 2:
        L = int(input_data[idx+1])
        R = int(input_data[idx+2])
        x = int(input_data[idx+3])
        idx += 4
        
        curr_L = roots[L - 1]
        curr_R = roots[R]
        ans = 0
        
        for i in range(18, -1, -1):
            bit = (x >> i) & 1
            pref_bit = 1 - bit
            
            if pref_bit == 0:
                count_R = cnt[lc[curr_R]]
                count_L = cnt[lc[curr_L]]
            else:
                count_R = cnt[rc[curr_R]]
                count_L = cnt[rc[curr_L]]
                
            if count_R - count_L > 0:
                ans |= (pref_bit << i)
                if pref_bit == 0:
                    curr_R = lc[curr_R]
                    curr_L = lc[curr_L]
                else:
                    curr_R = rc[curr_R]
                    curr_L = rc[curr_L]
            else:
                ans |= ((1 - pref_bit) << i)
                if pref_bit == 1:
                    curr_R = lc[curr_R]
                    curr_L = lc[curr_L]
                else:
                    curr_R = rc[curr_R]
                    curr_L = rc[curr_L]
                    
        out.append(str(ans))
        
    elif q_type == 3:
        k = int(input_data[idx+1])
        idx += 2
        sz -= k
        
    elif q_type == 4:
        L = int(input_data[idx+1])
        R = int(input_data[idx+2])
        x = int(input_data[idx+3])
        idx += 4
        
        curr_L = roots[L - 1]
        curr_R = roots[R]
        ans = 0
        
        for i in range(18, -1, -1):
            if curr_R == 0 and curr_L == 0:
                break
            bit = (x >> i) & 1
            if bit == 1:
                ans += cnt[lc[curr_R]] - cnt[lc[curr_L]]
                curr_R = rc[curr_R]
                curr_L = rc[curr_L]
            else:
                curr_R = lc[curr_R]
                curr_L = lc[curr_L]
                
        ans += cnt[curr_R] - cnt[curr_L]
        out.append(str(ans))
        
    elif q_type == 5:
        L = int(input_data[idx+1])
        R = int(input_data[idx+2])
        k = int(input_data[idx+3])
        idx += 4
        
        curr_L = roots[L - 1]
        curr_R = roots[R]
        ans = 0
        
        for i in range(18, -1, -1):
            count_left = cnt[lc[curr_R]] - cnt[lc[curr_L]]
            
            if k <= count_left:
                curr_R = lc[curr_R]
                curr_L = lc[curr_L]
            else:
                k -= count_left
                ans |= (1 << i)
                curr_R = rc[curr_R]
                curr_L = rc[curr_L]
                
        out.append(str(ans))

print('\n'.join(out))
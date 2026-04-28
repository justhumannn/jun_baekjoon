import sys

input_data = sys.stdin.read().split()

N = int(input_data[0])
ptr = 1

pts = []
x_set = set()
for _ in range(N):
    x = int(input_data[ptr])
    y = int(input_data[ptr+1])
    w = int(input_data[ptr+2])
    ptr += 3
    pts.append((x, y, w))
    x_set.add(x)

x_list = sorted(list(x_set))
x_map = {x: i for i, x in enumerate(x_list)}

y_dict = {}
for x, y, w in pts:
    if y not in y_dict:
        y_dict[y] = []
    y_dict[y].append((x_map[x], w))

y_list = sorted(y_dict.keys())
points_by_y = [y_dict[y] for y in y_list]

M = len(x_list)
sz = 1
while sz < M:
    sz <<= 1

max_ans = 0

for i in range(len(points_by_y)):
    tot_sum = [0] * (sz << 1)
    l_max = [0] * (sz << 1)
    r_max = [0] * (sz << 1)
    m_max = [0] * (sz << 1)
    
    for j in range(i, len(points_by_y)):
        for cx, cw in points_by_y[j]:
            idx = cx + sz
            
            tot_sum[idx] += cw
            v = tot_sum[idx]
            
            if v > 0:
                l_max[idx] = r_max[idx] = m_max[idx] = v
            else:
                l_max[idx] = r_max[idx] = m_max[idx] = 0
                
            p = idx >> 1
            while p:
                left = p << 1
                right = left | 1
                
                ts_l = tot_sum[left]
                ts_r = tot_sum[right]
                tot_sum[p] = ts_l + ts_r
                
                lm_l = l_max[left]
                lm_r = l_max[right]
                r_max_l = r_max[left]
                r_max_r = r_max[right]
                
                cand1 = ts_l + lm_r
                l_max[p] = lm_l if lm_l > cand1 else cand1
                
                cand2 = ts_r + r_max_l
                r_max[p] = r_max_r if r_max_r > cand2 else cand2
                
                m1 = m_max[left]
                m2 = m_max[right]
                m3 = r_max_l + lm_r
                
                mx = m1
                if m2 > mx: mx = m2
                if m3 > mx: mx = m3
                m_max[p] = mx
                
                p >>= 1
        
        if m_max[1] > max_ans:
            max_ans = m_max[1]

print(max_ans)
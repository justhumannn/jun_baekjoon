import sys

data = sys.stdin.read().split()
R, C, N = map(int, data[:3])

artifacts = {}
for i in range(3, len(data), 3):
    a = int(data[i])
    v = int(data[i+1])
    h = int(data[i+2])
    
    if a not in artifacts:
        artifacts[a] = [v, v, h, h]
    else:
        info = artifacts[a]
        if v < info[0]: info[0] = v
        if v > info[1]: info[1] = v
        if h < info[2]: info[2] = h
        if h > info[3]: info[3] = h

max_area = -1
best_id = 0

for a_id in sorted(artifacts.keys()):
    v_min, v_max, h_min, h_max = artifacts[a_id]
    area = (v_max - v_min + 1) * (h_max - h_min + 1)
    
    if area > max_area:
        max_area = area
        best_id = a_id

print(best_id, max_area)
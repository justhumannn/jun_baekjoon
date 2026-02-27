import sys

input_data = sys.stdin.read().split()
Q = int(input_data[0])
total_pass_mark = {1: 100, 2: 90, 3: 95, 4: 90, 5: 80}

idx = 1
for _ in range(Q):
    level = int(input_data[idx])
    lang = int(input_data[idx+1])
    read = int(input_data[idx+2])
    listen = int(input_data[idx+3])
    idx += 4
    
    if level not in [1, 2] or listen < 50:
        print("NO")
        continue
        
    c3_1 = 0
    c3_2 = 0
    
    for score in [lang, read]:
        if score * 3 < total_pass_mark[level]:
            c3_1 += 1
        if score < 22:
            c3_2 += 1
            
    if c3_1 >= 2 or c3_2 >= 1:
        print("YES")
    else:
        print("NO")
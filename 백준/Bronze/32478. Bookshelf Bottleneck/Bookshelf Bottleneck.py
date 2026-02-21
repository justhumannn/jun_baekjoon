data = []
try:
    while True:
        line = input().split()
        if not line: break
        data.extend(line)
except EOFError:
    pass

n = int(data[0])
H = int(data[1])
total_width = 0
possible = True
pointer = 2

for _ in range(n):
    l = int(data[pointer])
    w = int(data[pointer + 1])
    h = int(data[pointer + 2])
    pointer += 3
    
    current_min = float('inf')
    found = False
    
    if l <= H:
        found = True
        if w < current_min: current_min = w
        if h < current_min: current_min = h
    if w <= H:
        found = True
        if l < current_min: current_min = l
        if h < current_min: current_min = h
    if h <= H:
        found = True
        if l < current_min: current_min = l
        if w < current_min: current_min = w
        
    if not found:
        possible = False
        break
    total_width += current_min

if possible:
    print(total_width)
else:
    print("impossible")
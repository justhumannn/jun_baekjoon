import sys
input_data = sys.stdin.read().split()
x1, y1, x2, y2, x3, y3 = map(int, input_data[:6])
q = int(input_data[6])
ptr = 7
results = []
for _ in range(q):
    x, y = int(input_data[ptr]), int(input_data[ptr+1])
    t1, t2, t3 = int(input_data[ptr+2]), int(input_data[ptr+3]), int(input_data[ptr+4])
    ptr += 5
    
    d1 = abs(x - x1) + abs(y - y1)
    d2 = abs(x - x2) + abs(y - y2)
    d3 = abs(x - x3) + abs(y - y3)
    
    w1 = ((d1 + t1 - 1) // t1) * t1
    w2 = ((d2 + t2 - 1) // t2) * t2
    w3 = ((d3 + t3 - 1) // t3) * t3
    
    results.append(str(min(w1, w2, w3)))
sys.stdout.write('\n'.join(results) + '\n')
import sys

tokens = sys.stdin.read().split()

if tokens:
    T = int(tokens[0])
    idx = 1
    
    for t in range(1, T + 1):
        N = int(tokens[idx])
        idx += 1
        
        wires = []
        for _ in range(N):
            wires.append((int(tokens[idx]), int(tokens[idx+1])))
            idx += 2
            
        wires.sort()
        
        intersections = 0
        for i in range(N):
            for j in range(i + 1, N):
                if wires[i][1] > wires[j][1]:
                    intersections += 1
                    
        print(f"Case #{t}: {intersections}")
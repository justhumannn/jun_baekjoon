import sys

T = int(sys.stdin.readline())

for t in range(1, T + 1):
    N = int(sys.stdin.readline())
    
    cost = 0
    current_max = ""
    
    for _ in range(N):
        name = sys.stdin.readline().rstrip('\n')
        
        if name < current_max:
            cost += 1
        else:
            current_max = name
            
    print(f"Case #{t}: {cost}")
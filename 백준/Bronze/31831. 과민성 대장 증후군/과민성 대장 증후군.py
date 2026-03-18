import sys
tokens = sys.stdin.read().split()
if tokens:
    n = int(tokens[0])
    m = int(tokens[1])
    
    current_stress = 0
    sick_days = 0
    
    for i in range(2, n + 2):
        current_stress += int(tokens[i])
        
        if current_stress < 0:
            current_stress = 0
            
        if current_stress >= m:
            sick_days += 1
            
    print(sick_days)
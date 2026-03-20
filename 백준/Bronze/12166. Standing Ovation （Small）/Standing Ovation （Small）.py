import sys

T = int(sys.stdin.readline())

for t in range(1, T + 1):
    line = sys.stdin.readline().split()
    s_max = int(line[0])
    audience_str = line[1]
    
    total_standing = 0
    added_friends = 0
    
    for shyness_level in range(s_max + 1):
        count = int(audience_str[shyness_level])
        
        if count > 0:
            if total_standing < shyness_level:
                needed = shyness_level - total_standing
                added_friends += needed
                total_standing += needed
            
        total_standing += count
    
    print(f"Case #{t}: {added_friends}")
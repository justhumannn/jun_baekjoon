while True:
    n = int(input())
    if n == 0:
        break
    
    names = []
    heights = []
    
    for _ in range(n):
        name, h = input().split()
        names.append(name)
        heights.append(float(h))
        
    max_height = max(heights)
    
    result = []
    for i in range(n):
        if heights[i] == max_height:
            result.append(names[i])
            
    print(" ".join(result))
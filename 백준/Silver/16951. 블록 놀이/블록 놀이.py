n, k = map(int, input().split())
a = list(map(int, input().split()))
min_changes = n
for first_height in range(1, 1001):
    current_changes = 0
    possible = True
    for i in range(n):
        target_height = first_height + (i * k)
        
        if target_height < 1:
            possible = False
            break
        if a[i] != target_height:
            current_changes += 1
    if possible:
        if current_changes < min_changes:
            min_changes = current_changes
print(min_changes)
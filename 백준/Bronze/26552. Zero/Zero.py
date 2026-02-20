n = int(input())
for _ in range(n):
    k = int(input())
    next_val = k + 1
    while '0' in str(next_val):
        next_val += 1
    print(next_val)
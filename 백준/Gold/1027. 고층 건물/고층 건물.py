import sys

input = sys.stdin.read

data = input().split()
a = int(data[0])
if a == 1:
    print(0)
else:
    h = list(map(int, data[1:]))
    max_visible_count = 0
    for i in range(a):
        current_visible_count = 0
        for j in range(a):
            if i == j:
                continue
            is_visible = True   
            start_k = min(i, j) + 1
            end_k = max(i, j)
            for k in range(start_k, end_k):
                lhs = (h[k] - h[i]) * (j - i)
                rhs = (h[j] - h[i]) * (k - i)
                if i < j:
                    if lhs >= rhs:
                        is_visible = False
                        break
                else: 
                    if lhs <= rhs:
                        is_visible = False
                        break
            if is_visible:
                current_visible_count += 1
        max_visible_count = max(max_visible_count, current_visible_count)
    print(max_visible_count)
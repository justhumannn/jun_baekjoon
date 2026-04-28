import sys

sys.setrecursionlimit(300000)

input_data = sys.stdin.read().split()

T = int(input_data[0])
idx = 1
out = []

for _ in range(T):
    n = int(input_data[idx])
    idx += 1
    A = input_data[idx : idx+n]
    idx += n
    
    prev_occ = [-1] * n
    next_occ = [n] * n
    last_seen = {}
    
    for i in range(n):
        val = A[i]
        if val in last_seen:
            prev_occ[i] = last_seen[val]
            next_occ[last_seen[val]] = i
        last_seen[val] = i
        
    def check(L, R):
        if L >= R:
            return True
        left = L
        right = R
        while left <= right:
            if prev_occ[left] < L and next_occ[left] > R:
                return check(L, left - 1) and check(left + 1, R)
            if prev_occ[right] < L and next_occ[right] > R:
                return check(L, right - 1) and check(right + 1, R)
            left += 1
            right -= 1
        return False

    if check(0, n - 1):
        out.append("non-boring")
    else:
        out.append("boring")

print('\n'.join(out))
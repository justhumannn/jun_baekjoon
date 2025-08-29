a = int(input())
b = list(map(int, input().split()))
l, r = 0, a - 1
ans1, ans2 = b[l], b[r]
min_sum = abs(b[l] + b[r])
while l < r:
    s = b[l] + b[r]
    if abs(s) < min_sum:
        min_sum = abs(s)
        ans1, ans2 = b[l], b[r]
    if s > 0:
        r -= 1
    else:
        l += 1
print(ans1, ans2)
import sys
input = sys.stdin.readline
a = int(input())
left = 0
right = 2**32
while left < right:
    mid = (left + right) // 2
    if mid * mid >= a:
        right = mid
    else:
        left = mid + 1
print(left)
import sys
input = sys.stdin.readline

def bisect_left(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left
def bisect_right(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left
def count_by_binary_search(arr, target):
    return bisect_right(arr, target) - bisect_left(arr, target)
a = int(input())
b = list(map(int, input().split()))
c = int(input())
d = list(map(int, input().split()))

b.sort()

# 출력
result = [str(count_by_binary_search(b, i)) for i in d]
print(*result)

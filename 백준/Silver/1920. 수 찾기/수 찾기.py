import sys
input = sys.stdin.readline
a = int(input())
b = list(map(int, input().split()))
c = int(input())
d = list(map(int, input().split()))
b.sort()
def binary_search(x,n):
    left = 0
    right = len(x)-1
    while left <= right:
        mid = (left + right) // 2
        if x[mid] == n:
            return 1
        if x[mid] > n:
            right = mid-1
        else:
            left = mid + 1
    return 0
for i in d:
    print(binary_search(b,i))
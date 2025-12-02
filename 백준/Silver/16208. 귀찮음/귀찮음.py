import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
total_sum = sum(arr)
sum_of_squares = sum(x * x for x in arr)
result = (total_sum**2 - sum_of_squares) // 2
print(result)
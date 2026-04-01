import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
pow2 = [1] * n
for i in range(1, n):
    pow2[i] = (pow2[i-1] * 2) % 1000000007
total_sum = 0
for i in range(n):
    max_term = arr[i] * pow2[i]
    min_term = arr[i] * pow2[n - 1 - i]
    total_sum = (total_sum + max_term - min_term) % 1000000007
print(total_sum)
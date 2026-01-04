import sys
input = sys.stdin.readline

def sum_mul(n, k):
    m = n // k
    return k * m * (m + 1) // 2
T = int(input())
Ns = list(map(int, input().split()))
for N in Ns:
    ans = sum_mul(N, 3) + sum_mul(N, 7) - sum_mul(N, 21)
    print(ans)
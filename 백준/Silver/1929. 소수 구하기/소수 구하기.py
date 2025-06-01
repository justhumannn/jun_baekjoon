import sys
input = sys.stdin.readline

a, d = map(int, input().split())

# 0과 1은 소수가 아니므로 제외
is_prime = [False, False] + [True] * (d - 1)

# 에라토스테네스의 체
for i in range(2, int(d ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, d + 1, i):
            is_prime[j] = False

# a 이상 d 이하의 소수 출력
for i in range(a, d + 1):
    if is_prime[i]:
        print(i)

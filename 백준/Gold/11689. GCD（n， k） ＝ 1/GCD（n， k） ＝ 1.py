import sys
input = sys.stdin.readline

def phi(n: int) -> int:
    if n == 1:
        return 1
    result = n
    m = n
    if m % 2 == 0:
        result -= result // 2
        while m % 2 == 0:
            m //= 2
    if m % 3 == 0:
        result -= result // 3
        while m % 3 == 0:
            m //= 3
    i = 5
    while i * i <= m:
        if m % i == 0:
            result -= result // i
            while m % i == 0:
                m //= i
        j = i + 2
        if j * j <= m and m % j == 0:
            result -= result // j
            while m % j == 0:
                m //= j
        i += 6
    if m > 1:
        result -= result // m
    return result

n = int(input())
print(phi(n))
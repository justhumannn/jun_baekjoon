import sys
input = sys.stdin.readline

value = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
n = int(input())

for _ in range(n):
    s = input().strip()
    max_right = 0
    total = 0

    for ch in reversed(s):
        v = value[ch]
        if v < max_right:
            total -= v
        else:
            total += v
            max_right = v

    print(total)
import sys
input = sys.stdin.readline

t = int(input().strip())
for i in range(1, t + 1):
    first = input().strip()
    last = input().strip()
    print(f"Case {i}: {last}, {first}")
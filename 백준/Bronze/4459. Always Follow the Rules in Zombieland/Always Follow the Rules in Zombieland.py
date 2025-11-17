import sys
input = sys.stdin.readline

q = int(input())
quotes = [input().rstrip() for _ in range(q)]

r = int(input())
for _ in range(r):
    rule = int(input())
    if 1 <= rule <= q:
        print(f"Rule {rule}: {quotes[rule-1]}")
    else:
        print(f"Rule {rule}: No such rule")
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    s = input().strip()
    if 6 <= len(s) <= 9:
        sys.stdout.write("yes\n")
    else:
        sys.stdout.write("no\n")
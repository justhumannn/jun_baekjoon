import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    X = input().strip()
    print(len(set(X)))
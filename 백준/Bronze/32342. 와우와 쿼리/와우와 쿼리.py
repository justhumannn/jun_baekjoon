import sys
input = sys.stdin.readline

q = int(input())

for _ in range(q):
    s = input()
    count = 0
    for i in range(len(s) - 2):
        if s[i:i+3] == "WOW":
            count += 1
    print(count)
import sys
input = sys.stdin.readline
a = int(input())
b = list(map(int, input().split()))
c = int(input())
for _ in range(c):
    d = list(map(int, input().split()))
    if d[0] == 1:
        i = d[1] - 1
        noise = d[2]
        while i >= 0 and noise > 0:
            add_noise = min(b[i],noise)
            b[i] += add_noise
            noise -= add_noise
            i -= 1
        i = d[1]
        noise = d[2]
        while i < a and noise > 0:
            add_noise = min(b[i],noise)
            b[i] += add_noise
            noise -= add_noise
            i += 1
    else:
        print(b[d[1]-1])
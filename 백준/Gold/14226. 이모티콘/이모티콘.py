from collections import deque
import sys
input = sys.stdin.readline

a = int(input())
time = [[False] * (a * 2 + 1) for _ in range(a * 2 + 1)]
sequence = deque()
sequence.append((1, 0, 0))
time[1][0] = True
while sequence:
    node, clip, t = sequence.popleft()
    if node == a:
        print(t)
        break
    if not time[node][node]:
        time[node][node] = True
        sequence.append((node, node, t + 1))
    if clip > 0 and node + clip <= a * 2 and not time[node + clip][clip]:
        time[node + clip][clip] = True
        sequence.append((node + clip, clip, t + 1))
    if node - 1 >= 0 and not time[node - 1][clip]:
        time[node - 1][clip] = True
        sequence.append((node - 1, clip, t + 1))
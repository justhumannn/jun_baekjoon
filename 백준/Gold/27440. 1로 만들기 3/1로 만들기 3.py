from collections import deque
import sys
input = sys.stdin.readline
a = int(input())
visited = set()
sequence = deque([(a,0)])
visited.add(a)
while sequence:
    node,weight = sequence.popleft()
    if node == 1:
        print(weight)
        break
    if node % 3 == 0:
        v = node//3
        if v not in visited:
            visited.add(v)
            sequence.append((v,weight+1))
    if node % 2 == 0:
        v = node//2
        if v not in visited:
            visited.add(v)
            sequence.append((v,weight+1))
    v = node - 1
    if v not in visited:
        visited.add(v)
        sequence.append((v,weight+1))
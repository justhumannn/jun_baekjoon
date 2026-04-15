import sys

tokens = sys.stdin.read().split()
n = int(tokens[0])
k = int(tokens[1])
d = int(tokens[2])
students = []
idx = 3
for _ in range(n):
    m = int(tokens[idx])
    skill = int(tokens[idx+1])
    idx += 2
    algos = []
    for _ in range(m):
        algos.append(int(tokens[idx]))
        idx += 1
    students.append((skill, algos))
students.sort(key=lambda x: x[0])
counts = [0] * (k + 1)
left = 0
max_e = 0
for right in range(n):
    for algo in students[right][1]:
        counts[algo] += 1
    while students[right][0] - students[left][0] > d:
        for algo in students[left][1]:
            counts[algo] -= 1
        left += 1
    size = right - left + 1
    or_c = 0
    and_c = 0
    for i in range(1, k + 1):
        c = counts[i]
        if c > 0:
            or_c += 1
            if c == size:
                and_c += 1
    e = (or_c - and_c) * size
    if e > max_e:
        max_e = e
print(max_e)
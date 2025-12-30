import sys
input = sys.stdin.readline

N = int(input())
students = []
for _ in range(N):
    x, a, b, c, d = map(int, input().split())
    students.append((x, a, b, c, d))
kor = sorted(students, key=lambda x: (-x[1], x[0]))
eng = sorted(students, key=lambda x: (-x[2], x[0]))
math = sorted(students, key=lambda x: (-x[3], x[0]))
sci = sorted(students, key=lambda x: (-x[4], x[0]))
used = [False] * (N + 1)
ans = []
for arr in (kor, eng, math, sci):
    for s in arr:
        if not used[s[0]]:
            used[s[0]] = True
            ans.append(s[0])
            break
print(*ans)
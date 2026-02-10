import sys
input = sys.stdin.readline

n = int(input())
students = []
for _ in range(n):
    data = input().split()
    name = data[0]
    day = data[1].zfill(2)
    month = data[2].zfill(2)
    year = data[3]
    students.append((year + month + day, name))
students.sort()
print(students[-1][1])
print(students[0][1])
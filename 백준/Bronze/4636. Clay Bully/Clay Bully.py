while True:
    n = int(input())
    if n == -1:
        break
    students = []
    for _ in range(n):
        a, b, c, name = input().split()
        volume = int(a) * int(b) * int(c)
        students.append((volume, name))

    bully = max(students)[1]
    victim = min(students)[1]

    print(f"{bully} took clay from {victim}.")
import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break

    events = []
    for _ in range(n):
        s, e = input().split('-')
        sh, sm = map(int, s.split(':'))
        eh, em = map(int, e.split(':'))
        start = sh * 60 + sm
        end = eh * 60 + em
        events.append((start, end))

    events.sort()

    conflict = False
    for i in range(1, n):
        if events[i-1][1] > events[i][0]:
            conflict = True
            break

    print("conflict" if conflict else "no conflict")
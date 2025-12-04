T = int(input().strip())

for _ in range(T):
    s = input()
    print(min(s.count('a'), s.count('b')))
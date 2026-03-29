import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    
    sums = set()
    diffs = set()
    
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            a = n // i
            b = i
            sums.add(a + b)
            diffs.add(a - b)
            
    if sums & diffs:
        print(f"{n} is nasty")
    else:
        print(f"{n} is not nasty")
import sys
for i in sys.stdin:
    if i.strip() == "":
        continue
    a, b = map(int, i.split())
    print(b // (a + 1))
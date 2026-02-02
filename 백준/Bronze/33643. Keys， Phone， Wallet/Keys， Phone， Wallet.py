n = int(input())
items = [input() for _ in range(n)]
target = ['keys', 'phone', 'wallet']
missing = False
for t in target:
    if t not in items:
        print(t)
        missing = True
if not missing:
    print("ready")
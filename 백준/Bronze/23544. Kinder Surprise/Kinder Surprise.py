n = int(input())
collected = set()
for _ in range(n):
    collected.add(input())
print(n - len(collected))
import sys

input = sys.stdin.read

data = input().split()
n = int(data[0])
q = int(data[1])
queries = data[2:]

pattern = "SciComLove"
is_upper = [False] * (n + 1)
current_upper_count = 0

for i in range(1, n + 1):
    char = pattern[(i - 1) % 10]
    if 'A' <= char <= 'Z':
        is_upper[i] = True
        current_upper_count += 1

results = []
for i in range(q):
    x = int(queries[i])
    if is_upper[x]:
        current_upper_count -= 1
        is_upper[x] = False
    else:
        current_upper_count += 1
        is_upper[x] = True
    results.append(str(current_upper_count))

sys.stdout.write('\n'.join(results) + '\n')
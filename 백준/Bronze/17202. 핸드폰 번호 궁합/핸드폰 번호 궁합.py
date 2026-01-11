a = input().strip()
b = input().strip()
arr = []
for x, y in zip(a, b):
    arr.append(int(x))
    arr.append(int(y))
while len(arr) > 2:
    arr = [(arr[i] + arr[i + 1]) % 10 for i in range(len(arr) - 1)]
print(f"{arr[0]}{arr[1]}")
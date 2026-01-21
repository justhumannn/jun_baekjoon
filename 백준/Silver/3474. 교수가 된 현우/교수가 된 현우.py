import sys

input_data = sys.stdin.read().split()
t = int(input_data[0])
cases = input_data[1:]
for i in range(t):
    n = int(cases[i])
    count = 0
    while n >= 5:
        count += n // 5
        n //= 5
    print(count)
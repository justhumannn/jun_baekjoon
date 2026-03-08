import math
n = int(input())
min_perimeter = float('inf')
limit = int(math.sqrt(n)) + 1

for x in range(2, limit + 2):
    y = (n + x - 1) // x
    if y < 2:
        y = 2
    current_perimeter = 2 * (x - 1 + y - 1)
    if current_perimeter < min_perimeter:
        min_perimeter = current_perimeter
print(min_perimeter)
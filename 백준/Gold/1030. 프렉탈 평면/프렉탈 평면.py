import sys

sys.setrecursionlimit(2000)
input = sys.stdin.readline

s, n, k, r1, r2, c1, c2 = map(int, input().split())
start_boundary = (n - k) // 2
end_boundary = (n + k) // 2 - 1
powers = [1] * (s + 1)
for i in range(1, s + 1):
    powers[i] = powers[i - 1] * n
def get_color(time, r, c):
    if time == 0:
        return 0
    parent_size = powers[time - 1]
    super_r = r // parent_size
    super_c = c // parent_size
    if (start_boundary <= super_r <= end_boundary and
        start_boundary <= super_c <= end_boundary):
        return 1
    inner_r = r % parent_size
    inner_c = c % parent_size
    return get_color(time - 1, inner_r, inner_c)
for r in range(r1, r2 + 1):
    row_output = []
    for c in range(c1, c2 + 1):
        row_output.append(str(get_color(s, r, c)))
    print("".join(row_output))
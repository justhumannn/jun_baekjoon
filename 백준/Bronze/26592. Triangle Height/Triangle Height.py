a = int(input())
for _ in range(a):
    b, c = map(float, input().split())
    d = (2 * b) / c
    print(f"The height of the triangle is {d:.2f} units")
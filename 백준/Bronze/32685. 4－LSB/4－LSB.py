a = int(input())
b = int(input())
c = int(input())
x = a & 15
y = b & 15
z = c & 15
binary_str = f"{x:04b}{y:04b}{z:04b}"
ans = int(binary_str, 2)
print(f"{ans:04d}")
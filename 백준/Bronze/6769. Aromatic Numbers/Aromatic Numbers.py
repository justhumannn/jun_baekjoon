roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

s = input().strip()
n = len(s)
result = 0

for i in range(0, n, 2):
    A = int(s[i])
    R = s[i + 1]
    value = A * roman[R]

    if i + 2 < n:
        next_R = s[i + 3]
        if roman[next_R] > roman[R]:
            result -= value
        else:
            result += value
    else:
        result += value

print(result)
def fact(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
a = int(input())
print(fact(a))

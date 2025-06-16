N = int(input())

# 1부터 N까지의 합
sum_n = N * (N + 1) // 2

# 합의 제곱
square_of_sum = sum_n ** 2

# 1부터 N까지의 세제곱의 합
sum_of_cubes = sum(i ** 3 for i in range(1, N + 1))

# 결과 출력
print(sum_n)
print(square_of_sum)
print(sum_of_cubes)

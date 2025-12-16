N, M, S = map(int, input().split())
price_time_discount = (M + 1) * S * (100 - N) // 100
price_m_plus_1 = M * S
print(min(price_time_discount, price_m_plus_1))
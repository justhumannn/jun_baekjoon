# 부품 가격 상수
prices = [350.34, 230.90, 190.55, 125.30, 180.90]

# 테스트 케이스 수 입력
T = int(input())

# 각 테스트 케이스 처리
for _ in range(T):
    A, B, C, D, E = map(int, input().split())
    counts = [A, B, C, D, E]
    
    # 총 가격 계산
    total_cost = sum(p * c for p, c in zip(prices, counts))
    
    # 출력: $기호 + 소수 둘째 자리까지
    print(f"${total_cost:.2f}")

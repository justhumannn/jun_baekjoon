a = int(input())  # 참가자 수
b = list(map(int, input().split()))  # 티셔츠 신청 수
c, d = map(int, input().split())  # T: 티셔츠 묶음, P: 펜 묶음

# 티셔츠 최소 묶음 계산
t = sum((x + c - 1) // c for x in b)  # 각 신청 수를 c장 단위로 올림 나누기

# 펜 묶음 및 개별 펜 개수 계산
pen_bundle = a // d
pen_single = a % d

print(t)
print(pen_bundle, pen_single)

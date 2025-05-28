T = int(input())  # 테스트 케이스 수 입력

for _ in range(T):
    s = input()  # 문자열 입력
    print(s[0] + s[-1])  # 첫 글자와 마지막 글자 이어서 출력

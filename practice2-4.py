# 사용자로부터 1에서 100 사이의 자연수 n 입력받기
n = int(input("1에서 100 사이의 자연수를 입력하세요: "))

# 배수 판별 (3과 5의 공배수를 가장 먼저 조건 검사)
if n % 3 == 0 and n % 5 == 0:
    print(f"{n}은 3과 5의 배수입니다")
elif n % 3 == 0:
    print(f"{n}은 3의 배수입니다")
elif n % 5 == 0:
    print(f"{n}은 5의 배수입니다")

    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:
            print(f"{n}은 3과 5의 배수입니다")
        elif n % 3 == 0:
            print(f"{n}은 3의 배수입니다")
        elif n % 5 == 0:
            print(f"{n}은 5의 배수입니다")
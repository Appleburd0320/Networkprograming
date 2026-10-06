# 사용자로부터 1에서 100 사이의 자연수 n 입력받기
n = int(input("1에서 100 사이의 자연수를 입력하세요: "))

# 홀수/짝수 판별
if n % 2 != 0:
    print(f"{n}은 홀수입니다")
else:
    print(f"{n}은 짝수입니다")

    for n in range(1, 101):
        if n % 2 != 0:
            print(f"{n}은 홀수입니다")
        else:
            print(f"{n}은 짝수입니다")
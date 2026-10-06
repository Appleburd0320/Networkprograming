# 연도 입력받기
year = int(input("연도를 입력하세요: "))

# 윤년 조건 판별
# 1. 4로 나누어 떨어지고 100으로 나누어 떨어지지 않거나
# 2. 400으로 나누어 떨어지는 해
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year}년은 윤년입니다")
else:
    print(f"{year}년은 평년입니다")
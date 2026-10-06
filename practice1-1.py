# 정수 두 개를 각각 입력받기
num1 = int(input("첫 번째 정수를 입력하세요: "))
num2 = int(input("두 번째 정수를 입력하세요: "))

# f-string을 이용한 출력
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")
# 공백으로 구분하여 정수 두 개를 한 번에 입력받기
num1, num2 = map(int, input("두 정수를 공백으로 구분하여 입력하세요: ").split())

# format() 메서드를 이용한 출력
print("{} + {} = {}".format(num1, num2, num1 + num2))
print("{} - {} = {}".format(num1, num2, num1 - num2))
print("{} * {} = {}".format(num1, num2, num1 * num2))
print("{} / {} = {}".format(num1, num2, num1 / num2))
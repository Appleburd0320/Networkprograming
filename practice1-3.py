import math

# 1) a = 3, b = 4, c = 5 일 때 1 / (1 + a/b + c) 의 값
a, b, c = 3, 4, 5
result1 = 1 / (1 + (a / b) + c)
print(f"1번 결과: {result1}")

# 2) 2차 방정식의 계수가 a = 1, b = 1, c = -6 일 때 두 근 (근의 공식 사용)
a, b, c = 1, 1, -6
root1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
root2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
print(f"2번 결과 (두 근): {root1}, {root2}")

# 3) 반지름 r = 5 일 때 원의 면적 (π * r^2)
r = 5
area = math.pi * (r ** 2)
print(f"3번 결과 (원의 면적): {area}")

# 4) beta = 2.0, g = 3.2 일 때 beta * e^(-g) 의 값
beta = 2.0
g = 3.2
result4 = beta * math.exp(-g)
print(f"4번 결과: {result4}")

# 5) x = 0, mu = 1.5, rho = 2.0 일 때 정규분포 확률밀도함수 식 계산
# 식: (1 / sqrt(2 * pi * rho)) * exp( - (x - mu)^2 / (2 * rho^2) )
x = 0
mu = 1.5
rho = 2.0
result5 = (1 / math.sqrt(2 * math.pi * rho)) * math.exp(- ((x - mu)**2) / (2 * (rho**2)))
print(f"5번 결과: {result5}")
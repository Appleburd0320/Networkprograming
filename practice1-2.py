##1번 문제
x = 10
def test():
    print(x)
test()
print(x)
## 결과 10
#      10
## 2번문제
x = 10
def test():
    x = 20
    print(x)
test()
print(x)
## 결과 20
#      10
## 3번째 문제
x = 10
def outer():
    x = 20
    def inner():
        x = 30
        print("A:", x)
    inner()
    print("B:", x)
outer()
print("C:", x)
## 결과 A: 30
#      B: 20
#      C: 10
## 4번째 문제
x = 10

def test():
    global x         # 전역 변수 x를 수정하겠다고 선언
    print(x)         # 이 시점의 x는 전역 변수 x (값: 10)
    x = 20           # 전역 변수 x의 값을 20으로 변경

test()
print(x)             # 변경된 전역 변수 x (값: 20) 출력
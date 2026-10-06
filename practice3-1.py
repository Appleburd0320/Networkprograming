def calc(*args, op='+'):
    if op == '+':
        result = 0
        for num in args:
            result += num
        return result
    elif op == '*':
        result = 1
        for num in args:
            result *= num
        return result
    else:
        raise ValueError("지원하지 않는 연산자입니다. ('+' 또는 '*')")

# --- 실행 예 테스트 ---
print(calc(1, 1, 4, op='+'))  # 결과: 6
print(calc(1, 2, op='*'))      # 결과: 2
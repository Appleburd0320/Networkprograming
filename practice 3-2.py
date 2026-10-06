def min_max(lst):
    """원소가 정수로 구성된 리스트를 받아 최소값과 최대값을 튜플로 반환하는 함수"""
    if not lst:
        return None  # 빈 리스트인 경우 예외 처리
    return (min(lst), max(lst))


# --- 사용자로부터 정수들을 입력 받아 min 값과 max 값을 출력하는 프로그램 ---
if __name__ == "__main__":
    # 사용자 입력 받기 (예: 공백으로 구분하여 정수 입력)
    user_input = input("정수들을 공백으로 구분하여 입력하세요: ")

    # 입력받은 문자열을 정수 리스트로 변환
    numbers = [int(x) for x in user_input.split()]

    # min_max 함수 호출
    result = min_max(numbers)

    if result:
        print(f"입력한 정수: {numbers}")
        print(f"최소값(min)과 최대값(max) 튜플 반환 결과: {result}")
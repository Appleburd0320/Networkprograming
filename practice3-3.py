def count_vowel(text):
    """문자열을 인수로 받아 모음(a, e, i, o, u, 대소문자 포함)의 개수를 정수로 반환하는 함수"""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


# --- 사용자로부터 문자열을 입력 받아 모음의 개수를 출력하는 프로그램 ---
if __name__ == "__main__":
    # 사용자 입력 받기
    user_input = input("문자열을 입력하세요: ")

    # count_vowel 함수 이용
    result = count_vowel(user_input)

    # 결과 출력
    print(f"입력한 문자열: {user_input}")
    print(f"모음의 개수: {result}개")
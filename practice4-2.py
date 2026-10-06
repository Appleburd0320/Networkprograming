def analyze_file():
    while True:
        # 사용자가 요청한 파일 이름 입력 받기
        file_name = input("파일 이름을 입력하세요 (종료하려면 'quit' 입력): ")

        if file_name.lower() == 'quit':
            print("프로그램을 종료합니다.")
            break

        try:
            # 파일 읽기 시도 (FileNotFoundError 예외 처리)
            with open(file_name, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            # 라인의 수 (라인은 \n으로 분리된 문자열)
            num_lines = len(lines)

            # 전체 텍스트 합치기
            full_text = "".join(lines)

            # 단어의 수 (단어는 공백으로 분리된 문자열)
            # split()을 사용하면 공백(스페이스, 탭, 줄바꿈 등)을 기준으로 단어를 분리합니다.
            words = full_text.split()
            num_words = len(words)

            # 공백을 제외한 글자수
            # 공백 문자(' ', '\t', '\n', '\r')를 모두 제외하고 카운트합니다.
            num_chars = sum(len(word) for word in words)
            # 또는 아래와 같이 공백을 제거할 수도 있습니다:
            # num_chars = len("".join(full_text.split()))

            # 출력 형식
            print(f"characters : {num_chars}")
            print(f"words      : {num_words}")
            print(f"lines      : {num_lines}")
            break

        except FileNotFoundError:
            print(f"[오류] '{file_name}' 파일을 찾을 수 없습니다. 다시 시도해 주세요.\n")
        except Exception as e:
            print(f"[오류 발생] {e}\n")


if __name__ == "__main__":
    analyze_file()
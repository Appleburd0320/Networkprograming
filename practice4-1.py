def process_file():
    while True:
        # 사용자가 요청한 파일 이름 입력 받기
        file_name = input("읽을 파일명을 입력하세요 (종료하려면 'quit' 입력): ")

        if file_name.lower() == 'quit':
            print("프로그램을 종료합니다.")
            break

        try:
            # 1. 파일 읽기 시도 (FileNotFoundError 예외 처리)
            with open(file_name, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            # 출력용 리스트 및 저장용 리스트 준비
            numbered_lines = []
            print("\n--- [라인 번호가 붙은 출력 결과] ---")
            for idx, line in enumerate(lines, start=1):
                # 줄바꿈 문자 제거 후 번호 부여
                formatted_line = f"{idx} {line.strip()}"
                numbered_lines.append(formatted_line + '\n')
                print(formatted_line)
            print("-" * 35)

            # 2. '***.sav' 형식의 이름으로 저장하기
            # 확장자를 제외한 파일명 추출 (예: test.txt -> test)
            base_name = file_name.rsplit('.', 1)[0] if '.' in file_name else file_name
            sav_file_name = f"{base_name}.sav"

            with open(sav_file_name, 'w', encoding='utf-8') as sf:
                sf.writelines(numbered_lines)

            print(f"성공적으로 '{sav_file_name}' 파일로 저장되었습니다.\n")
            break  # 성공적으로 처리 후 종료

        except FileNotFoundError:
            print(f"[오류] '{file_name}' 파일을 찾을 수 없습니다. 다시 시도해 주세요.\n")
        except Exception as e:
            print(f"[오류 발생] {e}\n")


if __name__ == "__main__":
    process_file()
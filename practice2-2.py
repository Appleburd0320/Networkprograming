students = {}

print("--- 1. 명단 작성 ---")
while True:
    nameid = input("학번(id)을 입력하세요 (종료하려면 'fin' 입력): ")
    if nameid == 'fin':
        break
    name = input("이름을 입력하세요: ")
    if name == 'fin':
        break
    students[nameid] = name

print("\n [생성된 딕셔너리]")
print(students)

print("\n--- 2. 학번으로 이름 검색 ---")
while True:
    search_id = input("조회할 학번을 입력하세요 (종료하려면 'Quit!'): ")

    # "Quit!" 입력 시 프로그램 종료
    if search_id == "Quit!":
        print("프로그램을 종료합니다.")
        break

    # 학번 존재 여부 확인 및 출력
    if search_id in students:
        print(f"이름: {students[search_id]}")
    else:
        print("not found!")
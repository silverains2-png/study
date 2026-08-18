# 반복문 + 함수 + 딕셔너리를 모두 쓰는 종합 문제입니다.

# 할 일 목록(To-do) 프로그램을 만드세요.

#   add_task(tasks, name)      : 할 일 추가 (완료 여부는 False로)

#   done_task(tasks, name)     : 완료 처리 (없으면 안내 메시지)

#   show_tasks(tasks)          : 전체 목록 출력 (완료는 [v], 미완료는 [ ])

#   count_done(tasks)          : 완료한 개수

# 아래 순서로 실행하세요.

#   "보고서 작성" 추가 -> "회의 준비" 추가 -> "메일 확인" 추가

#   -> "회의 준비" 완료 -> "없는일" 완료 시도 -> 목록 출력

# [기대 결과]

#   '없는일' 은(는) 목록에 없습니다

#   [할 일 목록]

#     [ ] 보고서 작성

#     [v] 회의 준비

#     [ ] 메일 확인

#   완료: 1 / 3

# while True + input() 으로 실제 메뉴를 만들어 보세요.

#     1. 추가  2. 완료  3. 목록  4. 종료

# -------------------------------------------------------------
tasks = {}


def add_task(tasks, name):
    tasks[name] = False


def done_task(tasks, name):
    if name in tasks:
        tasks[name] = True
    else:
        print(f"'{name}'은(는) 목록에 없습니다")


def show_tasks(tasks):
    print("[할 일 목록]")
    for i, j in tasks.items():
        if j:
            print(f"[v] {i}")
        else:
            print(f"[ ] {i}")
    print(f"완료 : {count_done(tasks)} / {len(tasks)}")


def count_done(tasks):
    count = 0
    for i in tasks.values():
        if i:
            count += 1
    return count


while True:
    print("1. 추가")
    print("2. 완료")
    print("3. 목록")
    print("4. 종료")

    choice = input("메뉴를 선택하세요: ")

    if choice == "1":
        name = input("추가할 할 일을 입력하세요: ")
        add_task(tasks, name)
        print(f"'{name}' 이(가) 추가되었습니다.")

    elif choice == "2":
        name = input("완료할 할 일을 입력하세요: ")
        done_task(tasks, name)

    elif choice == "3":
        show_tasks(tasks)

    elif choice == "4":
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못된 메뉴입니다. 1~4 중에서 선택하세요.")

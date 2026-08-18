# 학생 3명의 이름과 점수를 입력받아 성적표를 출력하시오.

# [입력 형식]
#   학생 1명당
#     input("이름 : ")
#     input("점수 : ")
#   3명 반복

# [조건]
#   - 이름이 비어 있으면 다시 입력받기
#   - 점수는 0~100 정수만 허용, 잘못 넣으면 다시 입력받기
#   - 평균을 구하고, 최고점 학생의 이름을 찾아 출력 (반복문으로 직접 찾기)
#   - 어떤 값을 넣어도 프로그램이 멈추면 안 됨

# [출력 형식]
#   오류 : "이름을 입력하세요"
#          "숫자를 입력하세요"
#          "0~100 사이만 가능합니다"
#   마지막 :
#     "철수 : 90점"
#     "영희 : 75점"
#     "민수 : 85점"
#     "평균 : 83.33"
#     "1등 : 철수"

# [필요한 함수 : 2개]
#   (1) 점수 하나를 올바르게 받아내는 함수 (재입력 포함)
#   (2) 이름과 점수를 받아 성적표를 출력하는 함수

# [실행 예시]
#   이름 : 철수
#   점수 : 백점
#   숫자를 입력하세요
#   점수 : 90
#   이름 : 영희
#   점수 : 75

students = []


def get_score():
    while True:
        try:
            score = int(input("점수 : "))

            if not 0 <= score <= 100:
                print("0~100 사이만 가능합니다")
            else:
                return score
        except ValueError:
            print("숫자를 입력하세요")


def print_report(students):
    total = 0

    for i, j in students:
        print(f"{i} : {j}점")
        total += j

    avg = round(total / len(students), 2)
    print(f"평균 : {avg}")

    first_name = ""
    first_score = 0

    for i, j in students:
        if j > first_score:
            first_name = i
            first_score = j

    print(f"1등 : {first_name}")


for i in range(3):
    while True:
        name = input("이름 : ")

        if name.strip() != "":
            break
        print("이름을 입력하세요")

    score = get_score()
    students.append((name, score))

print_report(students)

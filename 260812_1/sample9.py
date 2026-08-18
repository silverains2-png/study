# "이름,점수" 형식의 문자열을 3번 입력받아 정리하시오.

# [입력 형식]
#   input("이름,점수 : ")  -> 3번 반복
#   예) 철수,90

# [조건]
#   - 쉼표로 나눈 개수가 2개가 아니면
#     raise Exception("이름,점수 형태로 입력하세요") 으로 발생시킬 것
#   - 점수가 숫자가 아니면 예외 처리
#   - except 는 ValueError 를 먼저, Exception 을 나중에 쓸 것
#   - 정상 데이터만 딕셔너리에 저장
#   - 마지막에 저장된 내용을 반복문으로 출력

# [출력 형식]
#   오류 : "이름,점수 형태로 입력하세요"
#          "점수는 숫자여야 합니다"
#   마지막 :
#     "철수 : 90점"
#     "민수 : 80점"

# [필요한 함수 : 1개]
#   (1) 한 줄을 받아 (이름, 점수) 로 나눠서 반환

# [실행 예시]
#   이름,점수 : 철수,90
#   이름,점수 : 영희 80
#   이름,점수 형태로 입력하세요
#   이름,점수 : 민수,팔십
#   점수는 숫자여야 합니다
#   철수 : 90점

student = {}


def get_student():
    data = input("이름,점수 : ").split(",")
    if len(data) != 2:
        raise Exception("이름,점수 형태로 입력하세요")

    name = data[0]
    score = int(data[1])
    return name, score


for i in range(3):
    try:
        name, score = get_student()
        student[name] = score
    except ValueError:
        print("점수는 숫자여야 합니다")
    except Exception as e:
        print(e)

for i, j in student.items():
    print(f"{i} : {j}점")

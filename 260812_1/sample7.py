# 학생 3명의 점수를 입력받아 학점을 출력하시오.

# [입력 형식]
#   input("점수 : ")  -> 3번 반복

# [조건]
#   - 0~100 을 벗어나면 raise Exception("0~100 사이만 가능합니다") 으로 발생시킬 것
#   - 숫자가 아니어도 예외 처리
#   - except 는 ValueError 를 먼저 쓰고, Exception 을 나중에 쓸 것
#     ※ Exception 은 모든 예외를 다 잡기 때문에 먼저 쓰면 ValueError 가 안 잡힌다
#   - 오류가 나도 멈추지 말고 다음 학생으로 넘어갈 것
#   - 학점 : 90 이상 A / 80 이상 B / 70 이상 C / 나머지 F

# [출력 형식]
#   성공 : "학점 : A"
#   오류 : "0~100 사이만 가능합니다"
#          "숫자를 입력하세요"

# [필요한 함수 : 1개]
#   (1) 점수를 받아 학점을 반환 (범위를 벗어나면 raise)

# [실행 예시]
#   점수 : 95
#   학점 : A
#   점수 : 150
#   0~100 사이만 가능합니다
#   점수 : 75
#   학점 : C


def get_grade():
    score = int(input("점수 : "))

    if not 0 <= score <= 100:
        raise Exception("0~100 사이만 가능합니다")

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"


for i in range(3):
    try:
        grade = get_grade()
        print(f"학점 : {grade}")

    except ValueError:
        print("숫자를 입력하세요")
    except Exception as e:
        print(e)

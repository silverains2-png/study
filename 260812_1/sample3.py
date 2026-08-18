# 나이를 3번 입력받아 성인인지 판별하시오.

# [입력 형식]
#   input("나이 : ")  -> 3번 반복

# [조건]
#   - 숫자가 아니면 예외 처리
#   - 19세 이상이면 성인, 아니면 미성년자
#   - 음수면 조건문으로 걸러서 오류 메시지 출력

# [출력 형식]
#   "성인입니다"
#   "미성년자입니다"
#   "숫자를 입력하세요"
#   "나이는 0보다 작을 수 없습니다"

# [필요한 함수 : 1개]
#   (1) 나이를 받아 "성인" 또는 "미성년자" 를 반환

# [실행 예시]
#   나이 : 20
#   성인입니다
#   나이 : 열살
#   숫자를 입력하세요
#   나이 : -3
#   나이는 0보다 작을 수 없습니다


def age_check(num):
    if num >= 19:
        return "성인"
    else:
        return "미성년자"


for i in range(3):
    age = input("나이 : ")

    try:
        age = int(age)

        if age < 0:
            print("나이는 0보다 작을 수 없습니다")
            continue

        adult = age_check(age)

        if adult == "성인":
            print("성인입니다")
        else:
            print("미성년자입니다")

    except ValueError:
        print("숫자를 입력하세요")

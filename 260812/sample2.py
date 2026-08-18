# 여러 값을 한 줄로 입력받아, 유효한 숫자만 골라 통계를 내시오.

# [입력 형식]
#   input("값 입력(공백 구분) : ")   -> 한 줄에 여러 값, 공백으로 구분
#   입력은 1회만 받는다
#   예) 10 20 abc 9999 30 -5

# [조건]
#   - 반복문으로 값을 하나씩 정수 변환
#   - 변환 실패 → "무시된 값" 목록에 저장
#   - 변환은 됐지만 0 미만 또는 1000 초과 → raise 로 처리해 "범위 초과" 목록에 저장
#   - 최댓값·최솟값은 max/min 없이 반복문으로 직접 구할 것
#   - 유효 값이 하나도 없으면 평균 계산에서 나는 예외를 처리

# [출력 형식]
#   "무시된 값 : abc"            (여러 개면 쉼표로 이어서, 없으면 이 줄 생략)
#   "범위 초과 값 : 9999, -5"     (없으면 이 줄 생략)
#   "합계 : 60"
#   "평균 : 20.00"
#   "최대 : 30 / 최소 : 10"
#   유효 값이 없으면 "유효한 숫자가 없습니다" 만 출력

# [필요한 함수 : 3개]
#   (1) 값 하나를 검사해 정수로 반환 (문제가 있으면 예외 발생)
#   (2) 숫자 리스트를 받아 (합계, 평균, 최댓값, 최솟값) 반환
#   (3) 결과를 출력

# [실행 예시]
#   값 입력(공백 구분) : 10 20 abc 9999 30 -5
#   무시된 값 : abc
#   범위 초과 값 : 9999, -5
#   합계 : 60
#   평균 : 20.00
#   최대 : 30 / 최소 : 10


def to_int(num):
    try:
        number = int(num)
    except ValueError:
        raise ValueError("숫자를 입력하세요")

    if num < 0 or num > 1000:
        raise OverflowError("범위 초과")

    return number


def cal_1234(list):
    cal_sum = sum(list)
    cal_avg = sum(list) / len(list)
    cal_max = 0
    cal_min = list[0]
    for i in list:
        if i >= cal_max:
            cal_max = i
        if i <= cal_min:
            cal_min = i
    return cal_sum, cal_avg, cal_max, cal_min


def print_result(list, ValueErr, OverflowErr):
    if not list:
        print("유효한 숫자가 없습니다")
        return
    if ValueErr:
        print("무시된 값 : ")

#  조건 : import / 모듈 사용 금지
#   모든 문제는 try-except 를 반드시 사용할 것
#   함수 / 조건문 / 반복문 / 입출력 모두 포함
#   except 는 예외 종류별로 나눠서 처리할 것
#   입력 안내문(프롬프트)은 아래 명시된 문구를 그대로 사용할 것
#   한 작업에 입력이 여러 개면 → 입력을 모두 받은 뒤에 검사할 것
#   (중간에 오류가 나도 남은 입력은 받고 나서 메시지를 출력)
#    메뉴가 있는 문제에서 메뉴가 잘못되면 → "메뉴는 1~5 중에 고르세요"

# ======================================================

# 두 정수를 입력받아 나눗셈 결과를 출력하되, 모든 시도를 기록으로 남기시오.
# [입력 형식]

#   input("숫자1(종료: q) : ")   -> 값 하나 (q 입력 시 즉시 종료)
#   input("숫자2 : ")            -> 값 하나
#   위 두 입력을 한 쌍으로, q 가 나올 때까지 반복

# [조건]
#   - 0으로 나누기 / 숫자 아님 을 서로 다른 except 로 처리
#   - 성공 기록과 실패 기록을 각각 다른 리스트에 저장
#   - 종료 시 성공률(%)을 출력. 시도가 0번이면 0으로 나누는 상황을 처리할 것

# [출력 형식]
#   성공 : "10 / 3 = 3.33"        (소수점 둘째 자리)
#   실패 : "실패 - 0으로 나눌 수 없습니다"
#          "실패 - 숫자를 입력하세요"
#   종료 시 : 성공 기록을 한 줄씩 출력 후 "성공률 : 50.0%"

# [필요한 함수 : 3개]
#   (1) 두 값을 받아 나눗셈 결과를 반환 (예외는 호출한 쪽에서 처리)
#   (2) 성공/실패 기록을 받아 성공률을 반환
#   (3) 최종 기록을 출력

# [실행 예시]
#   숫자1(종료: q) : 10
#   숫자2 : 3
#   10 / 3 = 3.33
#   숫자1(종료: q) : 7
#   숫자2 : 0
#   실패 - 0으로 나눌 수 없습니다
#   숫자1(종료: q) : q
#   [성공 기록]
#   10 / 3 = 3.33
#   성공률 : 50.0%


def divide_num(num1, num2):
    return num1 / num2


def success_rate(success, fail):
    if len(success) + len(fail) == 0:
        return 0
    return (len(success) / (len(success) + len(fail))) * 100


def final_result(success, rate):
    print("[성공 기록]")

    for i in success:
        print(i)

    print(f"성공률 : {rate:.1f}%")


success = []
fail = []

while True:
    num1 = input("숫자1(종료: q) : ")

    if num1 == "q":
        break

    num2 = input("숫자2 : ")

    try:
        result = divide_num(int(num1), int(num2))
        success.append(f"{num1} / {num2} = {result:.2f}")
        print(f"{num1} / {num2} = {result:.2f}")

    except ZeroDivisionError:
        fail.append("실패 - 0으로 나눌 수 없습니다")
        print("0으로 나눌 수 없습니다")
    except ValueError:
        fail.append("실패 - 숫자를 입력하세요")
        print("숫자를 입력하세요")

rate = success_rate(success, fail)
final_result(success, rate)

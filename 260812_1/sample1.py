# 두 숫자를 입력받아 나눈 결과를 출력하는 것을 3번 반복하시오.

# [입력 형식]
#   input("숫자1 : ")
#   input("숫자2 : ")
#   두 입력을 한 쌍으로 3번 반복 (for 문 사용)

# [조건]
#   - 0으로 나누면 예외 처리
#   - 숫자가 아닌 값을 넣어도 예외 처리
#   - 두 경우의 메시지가 서로 달라야 함

# [출력 형식]
#   성공 : "결과 : 3.33"      (소수점 둘째 자리)
#   오류 : "0으로 나눌 수 없습니다"
#          "숫자를 입력하세요"

# [필요한 함수 : 1개]
#   (1) 두 값을 받아 나눗셈 결과를 반환

# [실행 예시]
#   숫자1 : 10
#   숫자2 : 3
#   결과 : 3.33
#   숫자1 : 5
#   숫자2 : 0
#   0으로 나눌 수 없습니다
#   숫자1 : abc
#   숫자2 : 2
#   숫자를 입력하세요


def divide_num(num1, num2):
    return num1 / num2


for i in range(3):
    num1 = input("숫자1 : ")
    num2 = input("숫자2 : ")

    try:
        result = divide_num(int(num1), int(num2))
        print(f"결과 : {result:.2f}")

    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다")

    except ValueError:
        print("숫자를 입력하세요")

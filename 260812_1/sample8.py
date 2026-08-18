# 숫자, 연산자, 숫자를 입력받아 계산하는 것을 3번 반복하시오.

# [입력 형식]
#   input("숫자1 : ")
#   input("연산자(+ - * /) : ")
#   input("숫자2 : ")
#   세 입력을 한 세트로 3번 반복

# [조건]
#   - + - * / 가 아닌 연산자면 raise Exception("모르는 연산자입니다") 으로 발생시킬 것
#   - 0으로 나누기 예외 처리
#   - 숫자가 아닌 입력 예외 처리
#   - except 순서 : ZeroDivisionError → ValueError → Exception

# [출력 형식]
#   성공 : "결과 : 12"
#   오류 : "모르는 연산자입니다"
#          "0으로 나눌 수 없습니다"
#          "숫자를 입력하세요"

# [필요한 함수 : 1개]
#   (1) 숫자, 연산자, 숫자를 받아 결과를 반환

# [실행 예시]
#   숫자1 : 4
#   연산자(+ - * /) : *
#   숫자2 : 3
#   결과 : 12
#   숫자1 : 5
#   연산자(+ - * /) : ^
#   숫자2 : 2
#   모르는 연산자입니다


def calculater():
    num1 = int(input("숫자1 : "))
    operator = input("연산자(+ - * /) : ")
    num2 = int(input("숫자2 : "))

    if operator not in ["+", "-", "*", "/"]:
        raise Exception("모르는 연산자입니다")

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    else:
        return num1 / num2


for i in range(3):
    try:
        print(f"결과 : {calculater()}")
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다")
    except ValueError:
        print("숫자를 입력하세요")
    except Exception as e:
        print(e)

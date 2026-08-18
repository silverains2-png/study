# 번호를 3번 입력받아 해당 위치의 값을 출력하시오.

# [입력 형식]
#   input("번호(0~4) : ")  -> 3번 반복

# [조건]
#   - 리스트 범위를 벗어나면 예외 처리
#   - 숫자가 아니면 예외 처리
#   - 음수 번호는 이 문제에서 다루지 않는다 (0 이상만 들어온다고 보면 됨)
#   - 조회에 성공한 횟수를 세어 마지막에 출력

# [출력 형식]
#   성공 : "값 : 30"
#   오류 : "그 번호는 없습니다"
#          "숫자를 입력하세요"
#   마지막 : "성공 : 2번"

# [필요한 함수 : 1개]
#   (1) 리스트와 번호를 받아 값을 반환

# [실행 예시]
#   번호(0~4) : 2
#   값 : 30
#   번호(0~4) : 9
#   그 번호는 없습니다
#   번호(0~4) : 0
#   값 : 10
#   성공 : 2번

data = [10, 20, 30, 40, 50]


def get_value(data, num):
    return data[num]


success_count = 0

for i in range(3):
    num = input("번호(0~4) : ")

    try:
        num = int(num)
        value = get_value(data, num)

        print(f"값 : {value}")
        success_count += 1
    except IndexError:
        print("그 번호는 없습니다")
    except ValueError:
        print("숫자를 입력하세요")

print(f"성공 : {success_count}번")

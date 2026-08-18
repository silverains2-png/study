# 과일 이름을 3번 입력받아 가격을 출력하시오.

# [입력 형식]
#   input("과일 이름 : ")  -> 3번 반복

# [조건]
#   - 없는 과일이면 예외 처리
#   - 아무것도 입력 안 하면 조건문으로 걸러서 메시지 출력
#   - 찾은 가격들을 모두 더해 마지막에 출력

# [출력 형식]
#   성공 : "사과 : 1000원"
#   오류 : "그런 과일은 없습니다"
#          "이름을 입력하세요"
#   마지막 : "총 가격 : 4000원"

# [필요한 함수 : 1개]
#   (1) 과일 이름을 받아 가격을 반환

# [실행 예시]
#   과일 이름 : 사과
#   사과 : 1000원
#   과일 이름 : 수박
#   그런 과일은 없습니다
#   과일 이름 : 포도
#   포도 : 3000원
#   총 가격 : 4000원

price = {"사과": 1000, "바나나": 1500, "포도": 3000}


def get_price(fruit):
    return price[fruit]


total = 0

for i in range(3):
    fruit = input("과일 이름 : ")

    if fruit == "":
        print("과일 이름을 입력하세요")
        continue

    try:
        fruit_price = get_price(fruit)

        total += fruit_price
        print(f"{fruit} : {fruit_price}원")
    except KeyError:
        print("그런 과일은 없습니다")

print(f"총 가격 : {total}원")

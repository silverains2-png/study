# 값을 5번 입력받아, 숫자인 것만 골라 합계를 구하시오.

# [입력 형식]
#   input("값 : ")  -> 5번 반복 (for 문 사용)

# [조건]
#   - 정수로 바꿀 수 없는 값은 건너뛴다
#   - 건너뛴 값은 그때그때 메시지 출력
#   - 몇 개가 유효했는지도 함께 세기

# [출력 형식]
#   건너뛸 때 : "abc 은(는) 숫자가 아닙니다"
#   마지막 :
#     "유효한 값 : 3개"
#     "합계 : 60"

# [필요한 함수 : 1개]
#   (1) 값 하나를 받아 정수로 반환

# [실행 예시]
#   값 : 10
#   값 : abc
#   abc 은(는) 숫자가 아닙니다
#   값 : 20
#   값 : 30
#   값 : x
#   x 은(는) 숫자가 아닙니다
#   유효한 값 : 3개
#   합계 : 60


def to_int(num):
    return int(num)


total = 0
valid_num = 0

for i in range(5):
    num = input("값 : ")

    try:
        answer = to_int(num)
        total += answer
        valid_num += 1
    except ValueError:
        print(f"{num} 은(는) 숫자가 아닙니다")

print(f"유효한 값 : {valid_num}")
print(f"합계 : {total}")

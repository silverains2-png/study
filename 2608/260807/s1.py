# ----------------------------------------
# for 문
# ----------------------------------------
# 반복문이 왜 필요한가?

fruits = ["사과", "바나나", "포도"]

print(fruits[0])  # 하나씩 쓰면
print(fruits[1])  # 개수가 늘 때마다 추가해야 하고
print(fruits[2])  # 개수를 잘못 세면 Error

for fruit in fruits:  # 반복문이면 개수와 상관없이 두 줄로 만들어버림!
    print(fruit)

# 기본 구조
# for i in fruits:
#  |  |  |    |  |
#  |  |  |    |  |
#  |  |  |    | 콜론(:) 필수!
#  |  |  |  꺼낼 대상  <- 꺼낼 대상의 길이만큼 반복
#  |  | in 키워드
#  | 꺼낸 값을 담을 변수(이름은 자유)  <-  fruit라는 변수는 for문 안에서만 사용됨! : x, i, a, ... 등 아무거나 가능
# for 키워드

# 동작 : 값을 하나 꺼내 fruit에 넣고 -> 안쪽 실행 ->
#        다음값 꺼내기 -> ... -> 더 없으면 종료

for fruit in fruits:
    print(f"과일 : {fruit}")

print("반복 끝")  # 들여쓰기 밖 : 다 끝난 뒤 한번만 실행

# 과일 : 사과
# 과일 : 바나나
# 과일 : 포도
# 반복 끝

# 조건문과 마찬가지로 들여쓰기가 곧 문법입니다!

# ----------------------------------------
# 다른 자료형도 반복합니다.
# ----------------------------------------

for char in "파이썬":
    print(char)

scores = {"국어": 90, "영어": 85}

for i in scores:  # 딕셔너리 : 기본은 '키'
    print(i)  # 국어 / 영어

for i in scores.values():  # value 만 가져옴
    print(i)  # 90 / 85

for i, j in scores.items():
    print(f"{i}:{j}점")


# ---- 예시 ----

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for i in nums:
#     print("지금은", i)

# for i in range(1, 101):  # range(a,b) = a에서 b-1까지
#     print(i)

# di = [1, 2, 3, 4, "사과", "바나나", [1, 2]]

# for i in di:
#     print(i)

# name_list = {"name": "철수", "age": 25}

# for i in name_list:
#     # name은 철수
#     print(f"{i}은 {name_list[i]}")

# name_list = [
#     {"name": "김덕배", "age": 21, "city": "서울"},
#     {"name": "김춘봉", "age": 25, "city": "인천"},
#     {"name": "김춘식", "age": 23, "city": "경기"},
#     {"name": "김춘삼", "age": 22, "city": "충남"},
# ]

# for i in name_list:
#     print(i)
#     for x in i:
#         print(i[x])


# ----------------------------------------
# range() - 숫자를 순서대로 만들기
# ----------------------------------------

for i in range(5):  # 0 1 2 3 4 : 0부터 5미만까지
    print(i)

# range(끝) 0부터 끝미만까지
# range(시작,끝) 시작부터 끝미만까지
# range(시작,끝,간격) 시박부터 끝 미만까지 간격만큼 건너뛰며

print(list(range(5)))  # [0, 1, 2, 3, 4]
print(list(range(1, 6)))  # [1, 2, 3, 4, 5]
print(list(range(1, 10, 2)))  # [1, 3, 5, 7, 9]

# 최다 실수 : 끝값이 포함되지 않음!! (끝값 미만!)

for i in range(1, 5):
    print(i)  # 1 2 3 4 <- 5 '미만'

for i in range(1, 6):
    print(i)  # 1 2 3 4 5

for i in range(3):
    print("안녕")  # 안녕 안녕 안녕

# ----------------------------------------
# 누적하기 (가장 중요한 패턴)
# ----------------------------------------
# 반복하면서 결과를 쌓아나가는 방식입니다
# 시그마 : 이런 패턴의 한 종류 -> 확실히 익혀두자!

numbers = [10, 20, 30, 40]

total = 0  # 담을 그릇을 먼저 만든다 (0으로 시작)

for i in numbers:
    total += i  # total = total + i

print(total)  # 100

sum = 0
for i in range(1, 101):
    sum += i

print(sum, "1부터 100까지 더한 값")


# 동작 과정
# 시작 total = 0
# 1회차 total = 0 + 10 = 10
# 2회차 total = 10 + 20 = 30
# 3회차 total = 30 + 30 = 60
# 4회차 total = 60 + 40 = 100

# total = 0 을 반복문 안에 두면 매번 리셋되어 결과가 틀립니다
# for i in numbers:  # 절대 이렇게 하지 마세요
#     total = 0
#     total += i

# ---- 곱셈 누적 : 시작할 때 1로시작! ----

result = 1  # 0으로 시작하면 계속 0

for i in range(1, 6):
    result *= i  # 1 2 6 24 120

print(result)

# ---- 개수 세기 ----

count = 0  # 1 1 2 2 3
scores = [90, 55, 77, 40, 88]

for i in scores:
    if i >= 60:
        count += 1

print(f"합격자는 총 {count}명 입니다.")

# ---- 리스트에 모으기 ----

events = []

for i in range(1, 11):
    if i % 2 == 0:
        events.append(i)

print(events)

# ---- 최대값 직접 찾기 : max() ----

scores = [90, 85, 77, 92, 60]

biggest = scores[0]  # 첫값을 일단 최대값으로 두고

for i in scores:
    if i > biggest:
        biggest = i

numbers = [44, 22, 66, 32, 11, 677, 22]

mini = numbers[0]

for i in numbers:
    if i < mini:
        mini = i

print(mini, "가장작은값")

# ----------------------------------------
# break, continue
# ----------------------------------------

for i in range(1, 10):
    if i == 5:
        break  # 반복을 즉시 중단
    print(i)  # 1 2 3 4

for i in range(1, 6):
    if i == 3:
        continue  # 이번 회차만 건너뛰고 계속
    print(i)  # 1 2 4 5

# break 반복문 전체 종료
# continue 이번 회차만 건너뛰고 계속

# ----------------------------------------
# 중첩 반복문
# ----------------------------------------

# for i in range(2, 10):
#     for x in range(1, 10):
#         print(f"{i}x{x}={i * x}")
#     print()  # 구구단 출력!


# *로 정삼각형 찍기
n = 5

# for i in range(1, n + 1):
#     print(" " * (n - i), "*" * (2 * i - 1))


# *로 역삼각형 찍기
for i in range(1, n + 1):
    print(" " * (i - 1), "*" * (2 * n + 1 - 2 * i))

# 구구단
for i in range(9, 1, -1):
    for x in range(9, 0, -1):
        print(f"{i}x{x}={i * x}")
    print()

# * 로 다이아몬드 찍기
n = 9
for i in range(1, n + 1):
    if i <= 5:
        print(" " * (5 - i), "*" * (2 * i - 1))
    else:
        print(" " * (i - 5), "*" * (2 * n + 1 - 2 * i))

# ----------------------------------------
# 알아두면 좋은 기능
# ----------------------------------------

fruits = ["사과", "바나나", "포도"]

for idx, i in enumerate(fruits):  # 번호와 값을 함께 나타냄!
    print(f"{idx}번 : {i}")

for idx, i in enumerate(fruits, 1):  # 1번 부터 출력!
    print(f"{idx}번 : {i}")

names = ["철수", "영희"]
ages = [25, 22]

for i, j in zip(names, ages):
    print(f"{i}:{j}살")

# ----------------------------------------
# 시그마(∑) - 수학 기호 처음 배우기
# ----------------------------------------

# ∑는 그냥 "다 더해라"라는 뜻입니다.

#       10    <- 끝값 : 어디까지
#       ∑ i   <- 더할 것 : 무엇을
#       i=1   <- 어디서 부터
#
# 아래쪽 : i=1 'i를 1부터 시작해서'
# 위쪽 : 10 '10까지'
# i : 'i를 하나씩 늘려가며'
# ∑ : 'i를 전부 더해라'


# 1.
total = 0
for i in range(2, 6):
    total += i
print(total)
# 2.
total = 0
for i in range(1, 16):
    total += i**3
print(total)
# 3.
total = 0
for i in range(1, 26):
    total += i * 3
print(total)
# 4.
total = 0
for i in range(2, 21):
    total += 3
print(total)
# 5.
total = 0
for i in range(3, 13):
    total += i**2
print(total)

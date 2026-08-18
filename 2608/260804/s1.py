# ----------------------------------------
# 1. 산술 연산자
# ----------------------------------------

print(7 + 3)  # 10 더하기
print(7 - 3)  # 4 빼기
print(7 * 3)  # 21 곱하기
print(7 / 3)  # 2.3333... 나누기 -> 나누기 결과는 항상 float
print(7 // 3)  # 2 나누고 몫만
print(7 % 3)  # 1 나누고 나머지만
print(7**3)  # 343 거듭제곱

# ---- // 와 % 는 생각보다 자주 씁니다 ----

print(10 % 2 == 0)  # True -> 짝수 판별기로 사용 (나머지가 0)

print(130 // 60, 130 % 60)  # 2 10 -> 130초를 2분10초로

# ---- 문자열에서 쓸 수 있는 연산자 ----

print("파이" + "썬")  # 파이썬 이어붙이기
print("-" * 20)  # ------------------- 구분선 만들때 유리함

# ----------------------------------------
# 2. 대입 연산자
# ----------------------------------------

x = 10  # 기본 대입 : 오른쪽 값을 왼쪽에 넣기

# 자기 자신을 이용해 값을 바꾸는 축약형
x += 5  # x = x + 5 -> 15
x -= 3  # 12
x *= 2  # 24
x /= 4  # 6.0 -> 나누기는 float
x //= 2  # 3.0
x **= 2  # 9.0
print(x)  # 9.0

# 문자열에서도 됩니다
message = "안녕"
message += "하세요"
print(message)  # 안녕하세요

# ----------------------------------------
# 3. 비교 연산자 - 조건문의 핵심
# ----------------------------------------
# 두 값을 비교해서 결과로 True 또는 False를 돌려줍니다.

print(10 > 5)  # True
print(10 < 5)  # False
print(10 >= 10)  # True 크거나 같다
print(10 <= 9)  # False 작거나 같다
print(10 == 10)  # True 같은 값이다
print(10 != 10)  # False 다르다

# ---- = 와 == 는 완전히 다릅니다. (최다 실수)

age = 20  # = : 값을 넣는다 (대입)
print(age == 20)  # == : 같은 값인지 묻는다 (비교) -> True

# ---- 비교의 결과는 bool 입니다 (무조건) ----

result = 10 > 5  # True
print(result)  # True 라고 출력됨
print(type(result))  # bool

# ---- 문자열도 비교 가능 ----

print("abc" == "abc")  # True
print("abc" == "ABC")  # False -> 대소문자를 구분하니까!
print("apple" < "banana")  # True -> 사전순서로 비교함 (a가 b앞에)

# ---- 자료형이 다르면 비교가 안되는 경우가 있다 ----

print(10 == "10")  # False -> 숫자와 문자열은 절대 같지 않다 (무조건 False)
# print(10 > "5")  # TypeError -> 크기 비교는 아예 불가능

# ---- 파이썬만의 편한 문법 : 범위를 한번에 ----

score = 85
print(60 <= score <= 100)  # True : 60 이상이고 100 이하
# 다른 언어에선 (60 <= score) && (score <= 100) 처럼 써야 합니다.

# ----------------------------------------
# 4. 논리 연산자 - 조건문의 핵심
# ----------------------------------------
# 여러 조건을 묶을때 사용합니다.

# ---- and : 둘 다 참이어야 함 ----

print(True and True)  # True
print(True and False)  # False
print(False and False)  # False

# ---- or : 하나라도 참이면 참 ----

print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

# ---- not : 결과물 뒤집기 ----

print(not True)  # False
print(not False)  # True
print(not (10 > 5))  # False

# ---- 실제로는 이렇게 씁니다 ----

age = 25
has_ticket = True

print(age >= 20 and has_ticket)  # True : 성인이고 티켓도 있음
print(age < 20 or age > 80)  # False : 미성년자이거나 노인
print(not has_ticket)  # 티켓이 없다!

# 외우는법 : and는 '전부 만족', or는 '하나만 만족해도됨'

# ---- 자주하는 실수 ----

day = "토"
# print(day == "토" or "일") : 항상 True -> 의도한대로 동작하지 않음 / day가 정해진 값이니깐

# ---- 짧은 회로 평가 ----
# and는 앞이 False면 뒤를 아예 안봅니다.
# or는 앞이 True면 뒤를 아예 안봅니다.
# 그래서 이런 순서가 안전합니다.

value = ""
age = 25
print(
    value != "" and int(value) > 0
)  # False : and 뒤는 error이지만 이미 앞에서 False라 뒤쪽 error 가 안남 -> 뒤쪽으로 넘어가지않음

# ----------------------------------------
# 5. 멤버십 연산자 - (in / not in)
# ----------------------------------------
# 어떤 값이 안에 들어있는지 확인합니다.

# ---- 문자열에서 ----

text = "python programing"
print("python" in text)  # True : 포함되어 있나?

print("java" in text)  # False
print("java" not in text)  # True

# ---- 리스트에서 (리스트는 다음 챕터에서 자세히) ----

fruits = ["사과", "바나나", "포도"]
print("사과" in fruits)  # True
print("딸기" in fruits)  # False

# ---- 실제 활용 예 ----

answer = "y"
print(answer in ["y", "Y", "yes"])  # True
# 여러가지 값 중 하나인지 한번에 확인
# 이렇게 안써도 됨 : answer =="y" or answer == "Y" or answer == "yes"

# ----------------------------------------
# 6. 식별 연산자 ( is / is not )
# ----------------------------------------
# '같은 값' 이 아니라 '완전히 같은 것' 인지를 확인합니다.

# ---- 주 용도는 None 확인 ----

result = None
print(result is None)  # True O 권자오디는 방식
print(result is not None)  # False
print(result == None)  # True : 동작은 하지만 is를 쓰는게 관례

# ---- 주의사항 : 값 비교에는 is 를 쓰지 마세요 ----

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True : 내용이 같다
print(a is b)  # False : 서로 다른 리스트 두개 이므로
# 정리 : 값 비교는 == / None 확인은 is

a = [1, 2, 3]
b = a
print(a is b)  # True : b에 a를 대입한 같은 리스트

# ---- 연산자 우선순위 ----
# 위에 있을수록 먼저 계산됩니다.
# 1. () 괄호
# 2. ** 거듭제곱
# 3. * / // % 곱하기 나누기 계열
# 4. + - 더하기 뺴기
# 5. > < >= <= != in is 비교 계열
# 6. not
# 7. and
# 8. or

print(2 + 3 * 4)  # 14 곱하기 먼저
print((2 + 3) * 4)  # 20 괄호안이 최우선
print(10 > 5 + 3)  # True

# ---- 비교가 논리보다 먼저입니다 ----

print(3 > 1 and 5 > 2)  # True

# ---- and가 or보다 먼저입니다 ----

print(
    True or False and False
)  # True : False and False 에서 먼저 False 가 나오고 이후 True or False
print((True or False) and False)  # False : 괄호부터 계산 이후 True and False
# 그냥 괄호를 쓰면 우선순위를 정할 수 있다!

# ---- 조건문 맛보기 ----

age = 25
if age >= 20:
    print("성인입니다")
else:
    print("미성년자입니다")  # 'True' 일때 까지 내려감
# 연산자를 알아야 조건문을 쓸 수 있습니다.

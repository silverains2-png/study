# ------------------------
# 1. 형 변환이 왜 필요한가?
# ------------------------
# 파이썬은 종류가 다른 값끼리는 계산을 거부합니다

age = "20"  # 문자열 20
# print(age + 1) # TypeError : can only concatenate str 문자열+숫자열이라서

# 에러 메세지 해석 :
# "str + int"는 안된다 -> 둘중 하나의 종류를 바꿔야 함

print(int(age) + 1)  # 21   O 문자열을 정수로 바꾼 뒤에 계산

age = 20
print(float(age))  # 실수형으로 바뀜
print(bool(age))
# print(None(age)) # NoneType object is not callable

# ------------------------
# 2. 두 가지 형변환
# ------------------------

# ---- (1) 자동 형변환 : 파이썬이 알아서 맞춰주는 것 ----

result = 3 + 0.5  # int + float
print(result)  # 3.5
print(type(result))  # float -> 더 정밀한 쪽으로 자동 변환
print(True + 1)  # 2 -> True == 1 / bool은 숫자로 자동변환
print(10 / 2)  # 5.0 -> 나누기는 항상 float

# ---- (2) 수동 형변환 : 내가 직접 바꾸는 것 ----

print(int("10"))  # 문자열 "10"을 숫자열 10으로
print(str(10))  # 숫자 10을 문자열 "10"으로
print(float("3.14"))

# ------------------------
# 3. int() - 정수로 바꾸기
# ------------------------

# ---- 문자열 -> 정수 -----

print(int("100"))  # 100
print(int("-50"))  # -50
print(int(" 42 "))  # 42  -> 앞뒤 공백은 알아서 무시해줌

# ---- 실수 -> 정수 ----

print(int(3.9))  # 3 -> '버림' 입니다
print(int(3.1))  # 3
print(int(-3.9))  # -3 -> 음수는 0쪽으로 버립니다;;

# 반올림이 필요하면 round()를 쓰세요!

print(round(3.9))  # 4
print(round(3.1))  # 3

# ---- bool -> 정수 ----

print(int(True))  # 1
print(int(False))  # 0

# ---- int()가 실패하는 경우 ----

# print(int("3.14")) # ValueError : 소수점이 든 문자열은 바로 안됨
# print(int(float("3.14"))) # 3 -> float을 거쳐서 두 번 변환해야함
# print(int("열")) # 한글 숫자는 불가
# print(int("abc")) # 숫자가 아닌 문자열은 불가
# print(int("")) # 빈 문자열도 불가
# print(int(None)) # 답이 없는걸 정수로 만들수 없으므로 불가

# ---- (참고) 2진수 16진수 문자열 변환 ----

print(int("1010", 2))  # 10 2진수로 해석
print(int("ff", 16))  # 255 16진수로 해석

# ------------------------
# 4. float() - 실수로 바꾸기
# ------------------------

print(
    float("3.14")
)  # 3.14 -> int(float("3.14"))) 얘랑 다름 int 는 정수라서 소수점 버림
print(float("10"))  # 10.0 -> 정수처럼 생겨서 .0 이 붙는다!
print(float(10))  # 10.0
print(float(True))  # 1.0

# 실패하는 경우는 int()와 같다

# print(float("삼점일사"))

# ---- float -> int로 되돌릴때 소수점이 사라지는 것에 주의 ----

price = 3.00
print(int(price))  # 3

# ------------------------
# 5. str() - 문자열로 바꾸기
# ------------------------
# str()은 거의 실패하지 않습니다 (뭐든 문자열로 만들 수 있음)

print(str(100))  # 100
print(str(3.14))  # 3.14
print(str(True))  # True
print(str(None))
print(str([1, 2, 3]))


# ---- 언제 쓰낭? 숫자와 문자를 이어붙일 때 ----

score = 95
# print("점수 :" + score) X

# f-string을 쓰면 str()이 필요 없습니다 (더 편함)
# print("점수 : " + str(score))
print(f"점수 : {score}")  # 점수 : 95

# ---- 문자열이 된 숫자는 더 이상 계산이 안됩니다 ----
num = str(10)
print(num * 3)  # 101010 -> 곱하기 X 문자열이라 반복

# ------------------------
# 6. bool() - 참/거짓으로 바꾸기
# ------------------------
# 비어 있거나 0이면 False, 나머지는 전부 True
# 내용과 상관없이 빈 문자열이 아님이 기준이다 str 일떈!

print(bool(0))  # False
print(bool("0"))  # True -> 문자열이니깐 (빈 문자열도 아님)
print(bool(""))  # False
print(bool(-5))  # True

print(bool([]))  # False
print(bool(0))  # False

print(bool([]) == bool(""))  # True

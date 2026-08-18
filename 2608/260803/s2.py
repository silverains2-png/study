# ------------------------
# 1. 자료형이란?
# ------------------------
# 변수 = 값에 붙이는 '이름표'
# 자료형 = 그 값이 '어떤 종류'인지

# 왜 종류를 나눌까? -> 종류마다 할 수 있는 일이 다르기 때문
print(10 + 5)  # 15 <- 숫자끼리 더하면 '계산'
print("10" + "5")  # 105 <- 문자열끼리 더하면 '이어 붙이기'
# print("10" + 5) X TypeError : 종류가 다르면 더할 수 없음
# 겉보기엔 똑같은 10인데 결과가 다름 -> 그래서 자료형을 알아야 합니다.

# ------------------------
# 2. 자료형을 확인하는 방법
# ------------------------
# type() <- 타입 안에 넣으면 어떤 자료형인지 확인 가능

print(type(10))  # type 이 int 로 나옴 (정수)
print(type(3.14))  # float -> 실수
print(type("안녕"))  # str -> 문자열
print(type(True))  # bool -> 불리언
print(type(None))  # None -> None

# 특정 자료형이 맞는지 확인할 때
print(isinstance(10, int))  # True
# print(isinstance(10, str))  # False

# ------------------------
# 3. int - 정수
# ------------------------

age = 25  # 양수
temparature = -10  # 음수
zero = 0  # 0

# 자릿수 제한이 없습니다 (아주 큰 수도 그대로 계산됩니다)

big = 123456789123456789 * 999999
# print(big)

# 읽기 어려운 큰 숫자는 언더바로 구분 가능 (실행엔 영향이 없음)

population = 51_000_000  # 5100만 과 완전히 같음

# --------- 정수 연산 ---------
print(7 + 3)  # 10 더하기
print(7 - 3)  # 4 빼기
print(7 / 3)  # 2.33333.... 나누기 > 결과값이 무조건 float으로 바뀜
print(7 // 3)  # 2 몫 만 나옴 (소수점 버림)
print(7 % 3)  # 1 나머지 (짝수/홀수 판별에 자주 씀)
print(7**3)  # 343 거듭제곱 7을 3번 곱함

# 짝수 판별 예시

number = 10
print(number % 2)  # True -> 2로 나눈 나머지가 0이면 짝수

# ------------------------
# 4. float - 실수 (소수점이 있는 숫자)
# ------------------------

height = 175.5
pi = 3.141592
minus = -0.5
exp = 1.5e3  # 지수표기 = 1.5 X 10^3 = 1500.0
print(exp)  # 1500.0

# float의 가장 유명한 함정 : 소수 계산에 오차가 생김

print(0.1 + 0.2)  # 우리가 생각하면 0.3  -> 실제로 프린트 하면 0.30000000
print(0.1 + 0.2 == 0.3)  # False -> 그래서 ==로 비교하면 안됨

# 이유 : 컴퓨터는 2진수로 저장하는데 0.1을 2진수로 정확히 표현할 수 없음
# (10진수로 1/3을 0.3333333..) 으로 밖에 못쓰는 것과 같은 원리

# 해결법 1. 반올림해서 비교

print(round(0.1 + 0.2, 2) == 0.3)  # True -> round(값, 소수점자리)

# 해결법 2. 돈 계산처럼 정확해야 하는 decimal 모듈 사용

from decimal import Decimal

print(Decimal("0.1") + Decimal("0.2"))  # 0.3 (정확함)

# -------- int 와 float 을 섞으면? --------

print(3 + 0.5)  # 3.5 -> 더 정밀한 float으로 맞춰짐
print(type(3 + 0.5))  # float 으로 나옴
print(type(10 / 2))  # float <- 나누기는 딱 떨어져도 float 으로 나옴

# ------------------------
# 5. str - 문자열
# ------------------------
# 따옴표로 감싸면 전부 문자열(작은 따옴표 / 큰 따옴표 차이 없음)

name = "김철수"
city = "서울"
number_string = "123"  # 따옴표로 감쌌으니 숫자가 아니라 문자열
# number_string + 1 # X 문자열 + 숫자열 불가능!

# ---- 따옴표를 골라 쓰는 이유 ----

say1 = "그는 '안녕'이라고 말했다"  # 큰 따옴표 안에 작은 따옴표 OK
say2 = "It's a book"  # 같은 따옴표를 사용하면 \' 로 탈출 가능

# ---- 여러줄 문자열 ----

long_text = """ 첫번째 줄 
두번째 줄
세번쨰 줄 """  # 따옴표 3개로 감싸면 줄바꿈이 그대로 저장된다
print(long_text)

# ---- 자주쓰는 이스케이프 문자 ----

print("줄바꿈\n다음줄")  # \n = 줄바꿈
print("이름\t나이")  # \t = 탭(간격)
print("역슬래시 \\ 출력")  # \\ = 역슬래시 자체를 표현
print(r"C:\new\folder")  # 앞에 r을 붙이면 \을 그대로 쓸 수 있음 (경로 쓸 때)

# ---- 문자열 연산 ----

print("파이" + "썬")  # 파이썬 이어붙이기
print("하하" * 3)  # 하하하하하하 반복
print(len("파이썬"))  # 3 길이 세기

# ---- 문자열 연산 심화 ----

word = "PYTHON"

#  P  Y  T  H  O  N
#  0  1  2  3  4  5  <- 번호는 0 부터 시작!
# -6 -5 -4 -3 -2 -1  <- 뒤에서 부터 셀 땐 음수

print(word[0])  # P
print(word[-1])  # N

# ---- 잘라내기 (슬라이싱) ---- word(시작 : 끝) -> 끝 번호는 포함 안됨

print(word[0:3])  # PYT 0, 1, 2번만 나옴
print(word[2:])  # THON 2번부터 끝까지 나옴
print(word[:3])  # PYT 처음부터 3번전까지

# ---- 자주쓰는 문자열 기능 ----

text = "    Hello Python    "
print(text.strip())  # "Hello Python" 앞 뒤 공백을 제거
print(text.upper())  # "    HELLO PYTHON    " 모든 글자가 대문자로 나옴
print(text.lower())  # "    hello python    " 모든 글자가 소문자로 나옴
print(text.replace("o", "0"))  # "    Hell0 Pyth0n    " "a" 를 "b" 로 대체
print("사과, 배,김".split(","))  # [사과, 배, 김] 구분자로 나뉨

# 문자열은 한번 만들면 수정할 수 없습니다.
# word(0) = "J" # TypeError

word = "JYTHON"  # O 통째로 새로 대입하는건 가능

# ------------------------
# 6. bool- 불리언 (참/거짓)
# ------------------------

is_student = True  # 참 첫글자 대문자 (true) 라고 쓰면 에러
is_adult = False  # 거짓

# 비교 연산자의 결과가 bool입니다.

print(10 > 5)  # True
print(10 == 5)  # False '=='는 같다 라는 뜻
print(10 != 5)  # True  '!='는 다르다 라는 뜻

# ---- bool은 사실 숫자입니다 ----
# True == 1  /  False == 0

print(True + True)  # 2
print(int(True))  # 1

# ---- 논리 연산 ----
print(True and False)  # False -> and 는 둘다 참 이어야함
print(True or False)  # True -> or 는 하나만 참이면 됨
print(not True)  # False -> not : 반대로 뒤집기

# ---- 다른 자료형을 참/거짓으로 볼때(매우 자주쓰임) ----
# 아래 값들은 전부 '거짓' 으로 취급됩니다

print(bool(0))  # False 숫자0
print(bool(0.0))  # False
print(bool(""))  # False
print(bool(None))  # False
print(bool([]))  # False 빈 리스트

# ---- 그외 모든 값은 '참' ----

print(bool(1))  # True
print(bool(-5))  # True 0이 아니면 음수도 참
print(bool("0"))  # True 내용이 "0"이어도 빈 문자열이 아니라 참!

# ------------------------
# None - 값이 없음
# ------------------------

result = None  # 첫 글자 대문자
print(type(None))  # NoneType

# "아직 값이 정해지지 않았다"를 표현할 때 사용
# 0, "", False 와 다름
# 0 -> 숫자 0 이라는 값이 '있음'
# "" -> 빈 문자열 이라는 값이 '있음'
# False -> 거짓 이라는 값이 '있음'
# None -> 값 자체가 '없음'

# None 인지 확인할 때 == 대신에 is를 쓰는게 관례

# print(result == None)
print(result is None)  # True
print(result is not None)  # False

# ==========================================================
# 8. 정리
# ==========================================================
# 자료형     설명      예시           특징
# ----------------------------------------------------------
# int       정수       10, -3, 0      자리수 제한 없음
# float     실수       3.14, -0.5     미세한 오차 주의
# str       문자열     "안녕", "1"    따옴표로 감쌈, 수정불가
# bool      참/거짓    True, False    사실상 1과 0
# None      값 없음    None           비어 있음을 표시

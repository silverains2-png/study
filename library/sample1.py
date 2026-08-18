# -------------------------------------------------------------
# [문제 1] 무작위 추천 도서 뽑기
# -------------------------------------------------------------
print("--- 문제 1 ---")

books = ["사피엔스", "코스모스", "총균쇠", "이기적 유전자", "데미안", "토지"]

import random

print(f"오늘의 추천 도서: {random.choice(books)}")

# -------------------------------------------------------------
# [문제 2] 도서 번호 만들기
# -------------------------------------------------------------
print("\n--- 문제 2 ---")

import random as rd

print(f"발급된 도서번호: {rd.sample(range(1000, 10000), 5)}")

# -------------------------------------------------------------
# [문제 3] 반납 예정일 계산하기
# -------------------------------------------------------------
print("\n--- 문제 3 ---")

import datetime

today = datetime.date.today()
two_week = today + datetime.timedelta(days=14)
print(f"대출일      : {today}")
print(f"반납 예정일  : {two_week}")

# -------------------------------------------------------------
# [문제 4] 책 나르기 - 몇 번 왕복해야 하나
# -------------------------------------------------------------
print("\n--- 문제 4 ---")

book_counts = [8, 10, 3, 17]

from math import ceil


def run(num):
    return f"{num:>4}권 -> {ceil(num / 4)}번"


print(run(8))
print(run(10))
print(run(3))

# -------------------------------------------------------------
# [문제 5] 여러 모듈 함께 쓰기
# -------------------------------------------------------------
print("\n--- 문제 5 ---")

import random
import datetime

for i in range(3):
    print(
        f"[{i}] {random.choice(books)} (번호 {random.sample(range(1000, 10000), 1)})\n    {datetime.date.today()} ~ {today + datetime.timedelta(days=14)}"
    )

# -------------------------------------------------------------
# [문제 6] 모듈에 함수 넣고 불러오기
# -------------------------------------------------------------
print("\n--- 문제 6 ---")

import library_tools

due_date = library_tools.get_due_date()
late_fee = library_tools.get_late_fee(5)

print(f"반납 예정일 : {due_date}")
print(f"5일 연체료  : {late_fee}원")

# -------------------------------------------------------------
# [문제 7] 모듈에 상수 넣기
# -------------------------------------------------------------
print("\n--- 문제 7 ---")

import library_tools

print("[대출 규정]")
print(f"  대출 기간   : {library_tools.LOAN_DAYS}일")
print(f"  연체료      : 하루 {library_tools.FEE_PER_DAY}원")
print(f"  최대 대출   : {library_tools.MAX_BOOKS}권")


# -------------------------------------------------------------
# [문제 8] 별칭 붙이고 함수만 골라오기
# -------------------------------------------------------------
print("\n--- 문제 8 ---")

import library_tools as It
from library_tools import get_late_fee

print(f"별칭으로   : {It.get_late_fee(3)}원")
print(f"골라오기로 : {get_late_fee(3)}원")

# -------------------------------------------------------------
# [문제 9] 자체 테스트 블록 만들기
# -------------------------------------------------------------
print("\n--- 문제 9 ---")

import library_tools

print(f"이 파일의 __name__        : {__name__}")
print(f"library_tools 의 __name__ : {library_tools.__name__}")


# -------------------------------------------------------------
# [문제 10] 모듈 탐색하기
# -------------------------------------------------------------
print("\n--- 문제 10 ---")

import library_tools

tools = []

for tool in dir(library_tools):
    if not tool.startswith("_"):
        tools.append(tool)

print("사용 가능한 것들 : ")
print(tools)
print("\nget_due_date 설명 : ")
print(" ", library_tools.get_due_date.__doc__)

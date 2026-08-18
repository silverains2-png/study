# -------------------------------------
# import 란 무엇인가?
# -------------------------------------

# 한마디로 "이미 누군가 만들어 놓은 코드를 가져다 쓰겟다"는 뜻입니다.

# [왜 필요 하나?]

# 프로그래밍에는 이런 원칙이 있습니다.
# "바퀴를 다시 발명하지 마라"

# 제곱근 계산, 날짜 처리, 무작위 숫자 뽑기
# 이미 전 세계 개발자들이 만들어 둔게 있습니다.
# 우리는 그걸 가져다 쓰면 됩니다

# [가져올 수 있는 코드는 세 종류]

# 1) 표준 라이브러리
#    파이썬을 설치하면 자동으로 딸려 옵니다.
#    예) math, random, csv, datetime, os, pathlib 등
#    import 만 하면 바로 씁니다.

# 2) 외부 패키지
#    따로 설치를해야 합니다.
#    pandas, numpy, matplotlib, requests 등
#    pip install 로 설치한 뒤 import 합니다.

# 3) 내가 만들 파일
#    같은 폴더에 있는 내 .py 파일.
#    my_tools.py 같은 것.
#    파일 이름으로 import 합니다.

# 세가지 모두 import 하는 방법은 똑같습니다.

# math 없이 제곱근을 직접 구하려면 복잡한 계산이 필요합니다
# 하지만 import 한줄이면 끝납니다

# 방법 1) 통째로 가져오기
# import 모듈이름
# 쓸 때는 항상 '모듈이름.함수이름' 으로 씁니다.

import math

print("18의 제곱근 : ", math.sqrt(16))
print("원주율 : ", round(math.pi, 4))
print("2의 10제곱 : ", math.pow(2, 10))
print("올림 : ", math.ceil(3.2))
print("내림 : ", math.floor(3.8))

# 방법 2) 별칭 붙이기
# import 모듈이름 as 짧은이름
# 모듈 이름이 길때 짧게 줄여쓸 수 있습니다.

import math as m

print(m.sqrt(16))

# 방법 3) 특정 함수만 꼭 집어 오기
# from 모듈이름 import 함수이름
# 모듈 이름 없이 바로 쓸 수 있습니다.

from math import sqrt, pi

print(sqrt(36))
print(round(pi, 4))

# -------------------------------------
# 세 방법 중 뭘 써야 하나
# -------------------------------------

# import math           -> math.sqrt() 안전하고 명확. 기본
# import pandas as pd   -> pd.read_csv 이름이 길 때
# from math import sqrt -> sqrt() 짧지만 위험할 수 있음

# [from ... import 가 왜 위험한가]


# from math import pow
# pow = 100  <- 실수로 같은 이름의 변수를 만듦
# pow(2, 3)  <- 에러! 숫자를 함수처럼 부르게 됨

# 모듈 이름을 붙여쓰면 (math.pow) 이런 충돌이 생기지 않습니다.

# 코드를 읽을 때도 차이가 납니다
# sqrt(16)  <- 이게 어디서 온 함수지?
# math.sqrt(16)  <- 아 math 에서 왔구나

# [별칭(as)는 언제 쓰나]
# 데이터 분석에서는 별칭이 사실상 표준입니다.

# import pandas as pd
# import munpy as np
# import matplotlib.pyplot as plt

# 전 세계가 쓰는 관례입니다. 다르게 쓰지 마세요.
# 남이 짠 코드를 읽을 때 pd가 pandas 인걸
# 모두가 알고 있어야 소통이 되기 때문입니다.

import random as rd

print("주사위 굴리기 : ", rd.randint(1, 6))
print("무작위 선택 : ", rd.choice(["김밥", "라면", "돈까스"]))

my_list = [1, 2, 3, 4, 5]
# rd.suffle(my_list)  # 리스트의 순서를 섞음
print("섞은 리스트 : ", my_list)  # 섞여서 나옵니다
print("중복없이 3개 : ", rd.sample(range(1, 46), 3))

# -------------------------------------
# import 하면 정확히 무슨 일이 일어나나?
# -------------------------------------

# import my_tools 를 실행하면 파이썬은 이렇게 합니다.
# 1) my_tools.py 파일을 찾는다
#    찾는 순서 : 현재폴더 -> 파이썬 설치 폴더 -> 패키지 폴더
#
# 2) 그 파일을 위에서 아래로 한 번 실행한다
#    def 문들이 실행되면서 함수가 메모리에 등록됩니다
#
# 3) my_tools 라는 이름으로 사용할 수 있게 한다

# 여기서 중요한건 2번 입니다.
# 파일을 실행한다
# 그래서 my_tools.py 안에 print문이 있으면 그게 실행됩니다.
# 좀 있다가 이 문제를 어덯게 막는지 배울겁니다


# -------------------------------------
# 설치 없이 바로 쓰는 것들
# -------------------------------------

import datetime
import os

today = datetime.date.today()
now = datetime.datetime.now()

print("날짜와 시간")
print("오늘 날짜 : ", today)
print("현재 시각 : ", now)
print("현재 시각 : ", now.strftime("%H시 %M분"))

# 요일 구하기 (0 = 월요일, 6 = 일요일)

week = ["월", "화", "수", "목", "금", "토", "일"]
print("요일 : ", week[today.weekday()] + "요일")

# 날짜 계산

tomorrow = today + datetime.timedelta(days=1)
next_week = today + datetime.timedelta(days=7)

print("내일 : ", tomorrow)
print("다음주 : ", next_week)

# 간단 실습
# datetime import 후 timedelta 없이 내일 다음주 다다음주 계산 할 수 있는 함수

# [자주 쓰는 표준 라이브러리]

# math : 수학계산 (제곱근, 올림, 내림)
# random : 무작위 (뽑기, 섞기, 난수)
# datetime : 날짜와 시간
# csv : CSV 파일 읽고 쓰기
# pathlib : 경로 다루기
# os : 운영체제 기능
# json : JSON 데이터 (웹에서 많이 쓰는 형식)
# re : 문자열 패턴 찾기

# 이것들은 설치가 필요 없습니다. import만 하면 바로 됩니다

# -------------------------------------------------------------

# 정리

# -------------------------------------------------------------

#

#   [import 문법]

#

#     import math                 표준 라이브러리

#     import my_tools             내가 만든 파일 (.py 는 뺀다)

#     import pandas as pd         외부 패키지 + 별칭

#     from math import sqrt       함수만 골라오기

#

#

#   [모듈 만들 때 규칙]

#

#     - 관련 있는 함수끼리 한 파일에 모은다

#     - 각 함수에 docstring 으로 설명을 단다

#     - 실행 코드는 if __name__ == "__main__": 안에 넣는다

#

#

#   [pip 명령어]

#

#     pip install 패키지명         설치

#     pip list                    목록 확인

#     python -m pip install ...   안 될 때 이렇게

#

#

#   [기억할 것 5가지]

#     1. import 는 남이 만든 코드 가져오기. 내 파일도 똑같이 가져온다

#     2. import 하면 그 파일이 한 번 실행된다

#     3. 그래서 테스트 코드는 if __name__ == "__main__": 로 감싼다

#     4. 외부 패키지는 터미널에서 pip install 로 설치한다

#     5. import 가 안 되면 5-1 의 5번(파이썬이 여러 개)부터 의심하라

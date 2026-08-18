# -------------------------------------------------
# import 란 무엇인가?
# -------------------------------------------------

# 한마디로 "이미 누군가 만들어 놓은 코드를 가져다 쓰겠다"는 뜻입니다.

# [왜 필요하나]

# 프로그래밍에는 이런 원칙이 있습니다.
# "바퀴를 다시 발명하지 마라"

# 제곱근 계산, 날짜 처리, 무작위 숫자 뽑기
# 이미 전 세계 개발자들이 만들어 둔게 있습니다.
# 우리는 그걸 가져다 쓰면 됩니다

# [가져올 수 있는 코드는 세 종류]

# 1) 표준 라이브러르
#    파이썬을 설치하면 자동으로 딸려 옵니다.
#    예) math, random, csv, datetime, os, pathlib 등
#    import 만 하면 바로 씁니다.

# 2) 외부 패키지
#    따로 설치를 해야 합니다,.
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

print("16의 제곱근 : ", math.sqrt(16))
print("원주율      : ", round(math.pi, 4))
print("2의 10제곱  : ", math.pow(2, 10))
print("올림        : ", math.ceil(3.2))
print("내림        : ", math.floor(3.8))

# 방법 2) 별칭 붙이기
# import 모듈이름 as 짧은이름
# 모듈 이름이 길때 짧게 줄여쓸 수 있습니다.

import math as m

print(m.sqrt(16))

# 방법 3) 특정 함수만 콕 집어 오기
# from 모듈이름 import 함수이름
# 모듈 이름 없이 바로 쓸 수 있습니다.

from math import pi, sqrt

print(sqrt(36))
print(round(pi, 4))

# -------------------------------------------------
# 세 방법 중 뭘 써야 하나
# -------------------------------------------------

# import math           -> math.sqrt() 안정하고 명확. 기본
# import pandas as pd   -> pd.read_csv 이름이 길 때
# from math import sqrt -> sqrt() 짧지만 위험할 수 있음

# [from ... import 가 왜 위험한가]

# from math import pow
# pow = 100  <- 실수로 같은 이름의 변수를 만듬
# pow(2, 3)  <- 에러! 숫자를 함수처럼 부르게 됨

# 모듈 이름을 붙여쓰면 (math.pow) 이런 충돌이 생기지 않습니다.

# 코드를 읽을 때도 차이가 납니다
# sqrt(16)        <- 이게 어디서 온 함수지?
# math.sqrt(16)   <- 아 math 에서 왔구나

# [별칭(as)는 언제 쓰나]
# 데이터 분석에서는 별칭이 사실상 표준입니다.

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

import random as rd

print("주사위 굴리기 : ", rd.randint(1, 6))
print("무작위 선택   : ", rd.choice(["김밥", "라면", "돈까스"]))

my_list = [1, 2, 3, 4, 5]
rd.shuffle(my_list)  # 리스트의 순서를 섞음
print("섞은 리스트   : ", my_list)  # 섞여서 나옵니다
print("중복없이 3개  : ", rd.sample(range(1, 46), 3))

# -------------------------------------------------
# import 하면 정확히 무슨 일이 일어나냐?
# -------------------------------------------------

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
# 그래서 my_tools.py 안에 print문이 잇으면 그게 실행됩니다.
# 좀 있다가 이 문제를 어떻게 막는지 배울겁니다.


# -------------------------------------------------
# 설치 없이 바로 쓰는 것들
# -------------------------------------------------

import datetime

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

tomorrow = today + datetime.timedelta(day=1)
next_week = today + datetime.timedelta(day=7)

print("내일    : ", tomorrow)
print("다음주  : ", next_week)

# 간단 실습
# datetime import 후 timedelta 없이 내일 다음주 다다음주 계산 할 수 있는 함수

# [자주 쓰는 표준 라이브러리]

# math       : 수학계산 (제곱근, 올림, 내림)
# random     : 무작위 (뽑기, 섞기, 난수)
# datetime   : 날짜와 시간
# csv        : CSV 파일 읽고 쓰기
# pathlib    : 경로 다루기
# os         : 운영체제 기능
# json       : JSON 데이터 (웹에서 많이 쓰는 형식)
# re         : 문자열 패턴 찾기

# 이것들은 설치가 필요 없습니다. import만 하면 바로 됩니다.

# -------------------------------------------------
# 같은 폴더의 내 파일 불러오기
# -------------------------------------------------

# 같은 폴더에 있는 my_tools.py 를 가져와 봅시다.
# 중요 : .py 는 빼고 파일 이름만 씁니다.
# import my_tools (O)
# import my_tools.py (X)

import my_tools

# 모듈 안의 변수도 가져다 쓸 수 있습니다.

print("모듈 버전 : ", my_tools.VERSION)
print("작성자 : ", my_tools.AUTHOR)

print("\n[숫자 변환 함수들]")
print("to_int(' 4500 ') = ", my_tools.to_int(" 4500 "))
print("to_int('사천오백') = ", my_tools.to_int("사천오백"), "<- 실패하면 기본값 8")
print("to_int('사천오백', -1)", my_tools.to_int("사천오백", -1))
print("clean_number('4,500원') = ", my_tools.clean_number("4,500원"))

print("\n [통계 함수들]")
print("get_average([90, 85, 100]) = ", my_tools.get_average([90, 85, 100]))
print("find_max([3, 9, 1]) = ", my_tools.find_max([3, 9, 1]))
print("find_min([3, 9, 1]) = ", my_tools.find_min([3, 9, 1]))

# pandas 를 쓰는 것과 똑같은 일입니다.
# 다른 파일에 있는 함수를 가져와서 쓴 것 뿐
# pandas 도 결국 누군가 만들어 둔 .py 파일 묶음입니다.

# ---------------------------------------------
# 내 모듈에도 별칭과 골라오기 됩니다
# ---------------------------------------------

import my_tools as mt

print("[별칭] import my_tools as mt")
print("mt.get_average([1, 2, 3, 4]) = ", mt.get_average([1, 2, 3, 4]))

from my_tools import format_money, make_bar

print("\n[골라오기] from my_tools import make_bar, format_money")
print("make_bar(5000) = ", make_bar(5000))
print("format_moeny = ", format_money(12345))

# ---------------------------------------------
# __name__ 의 정체
# ---------------------------------------------

# import하면 그 파일이 한 번 실행된다 고 했습니다.
# 그런데 my_tools.py 맨 아래에는 테스트 코드가 잔뜩 있습니다.
# 그게 다 실행되면 곤란하겠죠?
# 그걸 막는게 이 블록입니다.
# if __name__ == "__main__":
#      테스트 코드

# [원리]
# 파이썬 파일마다 __name__ 이라는 변수를 자동으로 만듭니다.
# 직접 실행한 파일 -> __name__은 '__main__'
# import 된 파일  -> __name__은 파일이름 ('my_tools')
# 그래서 __name__ == '__main__' 인지 확인하면
# '지금 내가 직접 실행된건가?' 를 알 수 있습니다.

# 앞 뒤 밑줄 두 개는 무슨 뜻인가요?
# 파이썬이 특별하게 다루는 이름이라는 표시입니다.
# __name__, __file__ 처럼요.
# 우리가 직접 만들 일은 거의 없고, 있는 걸 읽기만 하면 됩니다.

print("이 파일의 __name__ : ", __name__)
print("my_tools 의 __name__", my_tools.__name__)

# 지금 실행 중인 파일은 이 파일입니다 -> '__main__'
# my_tools 는 import 된 것입니다.    -> 'my_tools'

# 그래서 my_tools.py 안의
# if __name__ == '__main__':
#     print("자체 테스트")

# 이 블록은 지금 실행되지 않았습니다.

# 터미널에서 my_tools.py를 실행하면
# 테스트 출력이 나옵니다.

# ---------------------------------------------
# 모듈을 만들 때의 규칙
# ---------------------------------------------

"""
  1) 관련있는 함수끼리 모아둔다
     숫자 변환끼리, 통계끼리, 파일 처리끼리

  2) 각 함수에 설명을 단다
     def 바로 아래에 설명을 쓰면 됩니다
     이걸 docstring 이라고 합니다

  3) 실행 코드는 if __name__ == "__main__": 안에 넣는다

  4) 파일 맨 위에는 이 파일이 뭔지 적는다

  [docstring 이 좋은 이유]
    - help() 로 설명을 볼 수 있고.
    - VS Code에서 함수 이름에 마우스를 올리면 설명이 뜹니다.
"""

# ---------------------------------------------
# pip
# ---------------------------------------------

# pandas, numpy 는 파이썬에 딸려오지 않습니다. 직접 설치해야 합니다.
# 설치는 파이썬 코드가 아니라 터미널에서 합니다.

# [자주 쓰는 pip 명령어]
#
# pip install pandas            -> 설치
# pip install pandas numpy      -> 여러개 한번에
# pip install pandas==2.0.0     -> 특정 버전 설치
# pip list                      -> 설치된 목록 보기
# pip show pandas               -> 정보 보기
# pip install --upgrade pandas  -> 최신으로 업데이트
# pip uninstall pandas          -> 삭제

# [윈도우에서 pip 가 안 먹힐 때]
# python -m pip install pandas
# 이렇게 쓰면 대부분 해결됩니다.
# "지금 실행 중인 파이썬의 pip를 쓰겠다" 는 뜻입니다.
# 파이썬이 여러 개 깔려 있을 때 특히 중요합니다.

# [회사 컴퓨터에서 설치가 안 될 때]
# 사내망 방화벽 떄문일 수 있습니다.
# IT팀에 문의하거나 프록시 설정이 필요합니다.

# ---------------------------------------------
# 가상환경 - 개념만 알아두기
# ---------------------------------------------

# [문제 실행]
# A 프로젝트는 pandas 1.5 버전이 필요하고
# B 프로젝트는 pandas 2.0 버전이 필요하다면 ?
#
# 컴퓨터 한 대에 하나만 깔 수 있으니 충돌합니다.
#
# [해결책 : 가상환경]
#
# 프로젝트마다 별도의 작은 파이썬 환경을 만듭니다.
# 각 환경은 서로 완전히 독립적입니다.
#
# python -m venv venv      -> 가상환경 만들기
#
# venv\Scripts\activate    -> 켜기 (윈도우)
# source venv/bin/activate -> 켜기 (맥, 리눅스)
#
# 켜지면 터미널 앞에 (venv) 가 붙습니다.
# 그 상태에서 pip install 하면 이 프로젝트에만 설치됩니다.
#
# 지금 당장은 몰라도 됩니다.
# 혼자 배우는 단계에서는 그냥 pip install 해도 문제 없습니다.
#
# 다만 이런게 있다는 것만 기억해 두세요.
# 나중에 회사에서 프로젝트를 받으면 반드시 만나게 됩니다.
# README 파일에 "가상환경을 만들고 ... " 라고 적혀 있을 겁니다.

# ---------------------------------------------
# import 가 안 될 때 체크리스트
# ---------------------------------------------
#
# ModuleNotFoundError : No Module named 'pandas'
#
# 이 에러를 만나면 위에서 부터 순서대로 확인하세요
# 대부분 5번이 원인

# 1) 설치를 했는가?
#    터미널에서 pip list 로 목록을 확인하세요

# 2) 이름을 정확히 썼는가?
#    대소문자를 구분합니다.
#    Pandas (X) pandas (O)
#    NumPy (X) numpy (O)

# 3) 내 파일 이름이 패키지 이름과 같지 않은가?
#    자주 발생하는 실수입니다.
#    내 파일을 random.py로 저장해놓고 import random 하면
#    파이썬이 내 파일을 가져옵니다.
#    csv.py json.py math.py 등도 마찬가지입니다.
#    해결 : 파일 이름을 바꾸세요 (my_random.py 처럼)

# 4) 같은 폴더에 있는가?
#    내가 만든 모듈일 때 해당합니다.
#    my_tools.py 가 이 파일과 같은 폴더에 있어야 합니다.

# 5) 파이썬이 여러 개 깔려 있지 않은가?
#    가장 흔한 원입입니다.
#    A 파이썬에 설치했는데 B 파이썬으로 실행하는 경우

# 해결방법
# VS Code 오른쪽 아래에서 파이썬 버전 확인
# Ctrl + Shift + P -> "Python Select Interpreter" -> 선택
# 또는 설치할 때 이렇게 쓰기
# python -m pip install pandas

# ---------------------------------------------
# 파이썬은 모듈을 어디서 찾나
# ---------------------------------------------

# import를 하면 파이썬은 정해진 순서대로 폴더를 뒤집니다
# 그 목록이 sys.path 에 들어있습니다
#
# 맨 앞이 현재 폴더입니다.
# 그래서 내가 만든 my_tools.py 를 가장 먼저 찾는 겁니다.
#
# 반대로 말하면, 내 파일 이름이 random.py 면
# 진짜 random 모듈보다 내 파일이 먼저 발견됩니다
# 위의 3번이 이래서 생기는 문제입니다.


# ---------------------------------------------
# 정리
# ---------------------------------------------

# [import 문법]
#
# import math            표준 라이브러리
# import my_tools        내가 만든 파일 (.py는 뺀다)
# import pandas as pd    외부패키지 + 별칭
# from math import sqrt  함수만 골라오기

# [모듈 만들 때 규칙]

# - 관련 있는 함수끼리 한 파일에 모은다
# - 각 함수에 docstring 으로 설명을 단다
# - 실행 코드는 if __name__ == "__name__": 안에 넣는다

# [pip 명령어]

# pip install 패키지명     설치
# pip list                목록 확인
# python -m pip install   안될 때 이렇게

# [기억할 것 5가지]

# 1. import 는 남이 만든 코드 가져오기. 내 파일도 똑같이 가져온다
# 2. import 하면 그 파일이 한 번 실행된다.
# 3. 그래서 테스트 코드는 if __name__ == "__main__": 로 감싼다
# 4. 외부 패키지는 터미널에서 pip install 로 설치한다
# 5. import 가 안되면 5-1 의 5번(파이썬이 여러 개)부터 의심해라

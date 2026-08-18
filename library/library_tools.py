# -------------------------------------------------------------
# [문제 6] 모듈에 함수 넣고 불러오기
# -------------------------------------------------------------
# library_tools.py 에 아래 함수 두 개를 만드세요.
#
#   get_due_date(days=14)
#     오늘부터 days 일 뒤의 날짜를 돌려준다
#
#   get_late_fee(late_days, per_day=100)
#     연체료를 계산해서 돌려준다 (연체일 x 하루 요금)
#
#   library_tools.py 안에도 datetime 을 import 해야 합니다.
#   모듈마다 필요한 것은 각자 가져와야 합니다.
#   이 파일에서 import 했다고 저 파일에서 쓸 수 있는 게 아닙니다.
#
# 그리고 이 파일에서 import 해서 사용하세요.
#
# [출력 예시]
#   반납 예정일: 2026-03-24
#   5일 연체료 : 500원
# -------------------------------------------------------------

import datetime

LOAN_DAYS = 14  # 기본 대출 기간
FEE_PER_DAY = 100  # 연체료 (하루당)
MAX_BOOKS = 5  # 1인당 최대 대출 권수


def get_due_date(days=LOAN_DAYS):
    """오늘 날짜로 부터 days 뒤의 날짜를 돌려준다"""
    today = datetime.datetime.today()
    due_date = today + datetime.timedelta(days=days)
    return due_date.strftime("%Y-%m-%d")


def get_late_fee(late_days, per_day=FEE_PER_DAY):
    """연체료를 계산해서 돌려준다 (연체일 x 하루요금)"""
    return late_days * per_day


# -------------------------------------------------------------
# 테스트 블럭
# -------------------------------------------------------------

if __name__ == "__main__":
    print("library_tools 자체 테스트")
    print(f"반납 예정일: {get_due_date()}")
    print(f"5일 연체료 : {get_late_fee(5)}원")

# 함수 세 개를 만들어 조립하세요.

#   get_overtime_pay(hours) : 초과근무수당 (시간당 20000원)

#   get_tax(amount)         : 세금 (총액의 10%, 정수)

#   get_final_pay(base, hours) : 실수령액

#                             = (기본급 + 초과수당) - 세금

#

# [기대 결과]

#   김철수: 기본급 3000000, 초과 5시간 -> 실수령 2790000

#   이영희: 기본급 3500000, 초과 0시간 -> 실수령 3150000

# -------------------------------------------------------------
workers = [
    {"이름": "김철수", "기본급": 3000000, "초과시간": 5},
    {"이름": "이영희", "기본급": 3500000, "초과시간": 0},
]


def get_overtime_pay(hours):
    return hours * 20000


def get_tax(amount):
    return int(amount * 0.1)


def get_final_pay(base, hours):
    overtime_pay = get_overtime_pay(hours)
    total = base + overtime_pay
    tax = get_tax(total)
    return total - tax


for i in workers:
    name = i["이름"]
    base = i["기본급"]
    overtime = i["초과시간"]

    print(
        f"{name}: 기본급 {base}, 초과 {overtime}시간 -> 실수령 {get_final_pay(base, overtime)}"
    )

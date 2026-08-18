# 한 달 지출 내역을 분석하는 프로그램입니다. 함수로 나눠 만드세요.

#   total_spent(records)         : 총 지출액

#   spent_by_category(records)   : 카테고리별 합계 딕셔너리

#   biggest_category(records)    : 가장 많이 쓴 카테고리

#   over_budget(records, budget) : 예산 초과 여부(True/False)와 차액을 함께 반환

#                                  (return 초과여부, 차액)

#   make_bar(amount, unit)       : 막대그래프 문자열

#                                  (1만원당 ■ 하나. unit 기본값 10000)

# [기대 결과]

#   총 지출: 285000원

#   [카테고리별]

#     식비    120000  ■■■■■■■■■■■■

#     교통     45000  ■■■■

#     쇼핑     90000  ■■■■■■■■■

#     문화     30000  ■■■

#   가장 많이 쓴 곳: 식비

#   예산 250000원 -> 35000원 초과!

# -------------------------------------------------------------
records = [
    {"항목": "점심", "분류": "식비", "금액": 45000},
    {"항목": "지하철", "분류": "교통", "금액": 45000},
    {"항목": "저녁", "분류": "식비", "금액": 75000},
    {"항목": "옷", "분류": "쇼핑", "금액": 90000},
    {"항목": "영화", "분류": "문화", "금액": 30000},
]
BUDGET = 250000


def total_spent(records):
    total = 0

    for i in records:
        total += i["금액"]

    return total


def spent_by_category(records):
    result = {}

    for i in records:
        category = i["분류"]
        amount = i["금액"]

        if category in result:
            result[category] += amount
        else:
            result[category] = amount

    return result


def biggest_category(records):
    category_total = spent_by_category(records)

    biggest = ""
    biggest_amount = 0

    for i, j in category_total.items():
        if j > biggest_amount:
            biggest = i
            biggest_amount = j

    return biggest


def over_budget(records, budget):
    total = total_spent(records)

    if total > budget:
        return True, total - budget
    else:
        return False, budget - total


def make_bar(amount, unit=10000):
    count = amount // unit
    return "■" * count


total = total_spent(records)
print(f"총 지출: {total}원")

print("[카테고리별]")

category_total = spent_by_category(records)

for i, j in category_total.items():
    bar = make_bar(j)
    print(f"{i}  {j}  {bar}")

print(f"가장 많이 쓴 곳: {biggest_category(records)}")

is_over_budget, change = over_budget(records, BUDGET)

if is_over_budget:
    print(f"예산 {BUDGET}원 -> {change}원 초과!")
else:
    print(f"예산 {BUDGET}원 -> {change}원 남음!")

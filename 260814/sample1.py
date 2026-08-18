#  [출제 범위]
#    경로(pathlib) / 파일 읽기와 쓰기 / CSV / 집계

#  [푸는 방법]
#    - 각 문제 아래의 빈 줄에 코드를 작성하세요.
#    - 각 문제의 [출력 예시] 와 비슷하게 나오면 성공입니다.
#    - 숫자를 0 으로 가려둔 곳은 직접 구해야 하는 값입니다.
#      자릿수는 실제 답과 같으니 참고하세요.
#    - input() 은 쓰지 않습니다. 코드에 값을 직접 적어서 호출하세요.
#    - 함수로 만들라고 한 것은 반드시 함수로 만드세요.

#  [실행하면]
#    data 폴더에 orders.csv 가 자동으로 만들어집니다.
#    이 데이터에는 일부러 이상한 값이 섞여 있습니다.
#    코드를 짜기 전에 파일을 직접 열어서 먼저 찾아보세요.
# ============================================================

import csv
from pathlib import Path

BASE = Path(__file__).parent
DATA = BASE / "data"
DATA.mkdir(exist_ok=True)

orders_file = DATA / "orders.csv"

with open(orders_file, "w", encoding="utf-8", newline="") as f:
    f.write("주문일,시간대,매장,메뉴,분류,수량,단가,포장\n")
    f.write("2026-03-02,오전,강남점,아메리카노,커피,3,4500,N\n")
    f.write("2026-03-02,오후,강남점,카페라떼,커피, 2 ,5000,Y\n")  # strip()
    f.write("2026-03-02,오전,홍대점,녹차라떼,논커피,1,5500,N\n")
    f.write("2026-03-03,오후,강남점,치즈케이크,디저트,2,6500,Y\n")
    f.write("2026-03-03,오전,부산점,아메리카노,커피,5,4500,N\n")
    f.write("2026-03-03,오후,홍대점,아메리카노,커피,,4500,N\n")  # 수량x
    f.write("2026-03-04,오전,강남점,크로플,디저트,3,6000,Y\n")
    f.write("2026-03-04,오후,부산점,카페라떼,커피,4,5000,N\n")
    f.write("2026-03-05,오전,홍대점,아메리카노,커피,2,4500,Y\n")
    f.write("2026-03-05,오후,강남점,녹차라떼,논커피,3,사천,N\n")  # 단가 숫자아님
    f.write("2026-03-06,오전,부산점,치즈케이크,디저트,1,6500,N\n")
    f.write("2026-03-06,오후,홍대점,카페라떼,커피,6,5000,Y\n")

print("orders.csv 준비 완료")
print("data 폴더에서 직접 열어보고, 이상한 값이 몇 개인지 세어 보세요.\n")

# -------------------------------------------------------------
# [문제 1] 파일 읽어서 그대로 출력하기
# -------------------------------------------------------------

# orders.csv 를 csv.DictReader 로 읽어 모든 줄을 화면에 출력하세요.
# [힌트] encoding="utf-8", newline="" 을 잊지 마세요.

# [출력 예시]
#   {'주문일': '2026-03-02', '시간대': '오전', '매장': '강남점', ...}
#   {'주문일': '2026-03-02', '시간대': '오후', '매장': '강남점', ...}
# -------------------------------------------------------------
print("--- 문제 1 ---")

with open(orders_file, "r", encoding="utf-8", newline="") as f:
    for i in csv.DictReader(f):
        print(i)


# -------------------------------------------------------------
# [문제 2] 값을 정리하는 함수 만들기
# -------------------------------------------------------------
# 문자열의 앞뒤 공백을 없애고 숫자로 바꾸는 함수를 만드세요.
# 바꿀 수 없으면 None 을 돌려줍니다.

#   함수 이름 : clean_number(value)

# [확인]
#   clean_number(" 3 ")    ->  3
#   clean_number("4500")   ->  4500
#   clean_number("")       ->  None
#   clean_number("사천")    ->  None
# -------------------------------------------------------------
print("\n--- 문제 2 ---")


def clean_number(value):
    # 앞뒤공백없애기
    value = value.strip()
    # 공백 None
    if value == "":
        return None
    # 숫자로 바꿔보고 안되면 None
    try:
        return int(value)
    except ValueError:
        return None


print(clean_number(" 3 "))
print(clean_number("4500"))
print(clean_number(""))
print(clean_number("사천"))

# -------------------------------------------------------------
# [문제 3] 데이터를 읽고 금액을 계산하는 함수
# -------------------------------------------------------------
# 함수 이름 : load_orders(path)

# 하는 일
#   1) CSV 를 읽는다
#   2) 수량과 단가를 숫자로 바꾼다 (문제 2의 함수 사용)
#   3) 둘 중 하나라도 변환에 실패하면 문제 목록에 담고 건너뛴다
#   4) 성공한 줄에는 금액을 계산해 새 항목으로 추가한다
#        금액 = 수량 x 단가
#   5) (정상리스트, 문제목록) 두 개를 돌려준다

# 문제 목록에는 (줄번호, 메뉴, 사유) 를 담으세요.

# [힌트] 줄번호는 enumerate(csv.DictReader(f), start=2) 로 셉니다.
#        1번 줄은 헤더이므로 데이터는 2번 줄부터입니다.

# 함수를 만든 뒤 아래 내용을 출력하세요.
#   - 정상 건수와 문제 건수
#   - 문제 목록 전체
#   - 전체 매출 합계

# [출력 예시]
#   정상 00건 / 문제 0건
#     0번째 줄 아메리카노: 수량 이상 ''
#     00번째 줄 녹차라떼: 단가 이상 '사천'
#   전체 매출: 000,000원
# -------------------------------------------------------------
print("\n--- 문제 3 ---")


def load_orders(path):
    clean_rows = []
    problem_rows = []

    with open(path, "r", encoding="utf-8", newline="") as f:
        for line_no, row in enumerate(csv.DictReader(f), start=2):
            qty = clean_number(row["수량"])
            price = clean_number(row["단가"])

            # 수량 이상함
            if qty is None:
                problem_rows.append(
                    (line_no, row["메뉴"], f"수량 이상 '{row['수량']}'")
                )
                continue

            # 단가 이상함
            if price is None:
                problem_rows.append(
                    (line_no, row["메뉴"], f"단가 이상 '{row['단가']}'")
                )
                continue

            sales = qty * price

            row["수량"] = qty
            row["단가"] = price
            row["금액"] = sales

            clean_rows.append(row)

    return clean_rows, problem_rows


clean, problem = load_orders(orders_file)

print(f"\n정상 {len(clean)}건 / 문제 {len(problem)}건")

for line_no, menu, reason in problem:
    print(f"\n{line_no}번째 줄 {menu}: {reason}")

total_sales = 0

for row in clean:
    total_sales += row["금액"]

print(f"\n전체 매출: {total_sales:,}원")

# -------------------------------------------------------------
# [문제 4] 집계 함수 두 개 만들기
# -------------------------------------------------------------
# 앞으로 계속 쓸 함수 두 개를 만드세요.

#   sum_by(rows, group_key, value_key)
#     group_key 별로 value_key 를 합산한 딕셔너리를 돌려준다
#   count_by(rows, group_key)
#     group_key 별 건수를 센 딕셔너리를 돌려준다

# [확인] 아래처럼 쓸 수 있어야 합니다
#   sum_by(orders, "매장", "금액")   ->  {'강남점': 00000, ...}
#   count_by(orders, "매장")         ->  {'강남점': 0, ...}

# [힌트] 딕셔너리의 .get(키, 0) 을 쓰면 짧아집니다.
# -------------------------------------------------------------
print("\n--- 문제 4 ---")


def sum_by(rows, group_key, value_key):
    # group_key 별로 value_key 를 합산한 딕셔너리를 돌려준다
    result = {}

    for row in rows:
        group = row[group_key]
        value = row[value_key]
        result[group] = result.get(group, 0) + value

    return result


def count_by(rows, group_key):
    # group_key 별 건수를 센 딕셔너리를 돌려준다
    result = {}

    for row in rows:
        group = row[group_key]
        result[group] = result.get(group, 0) + 1

    return result


print(sum_by(clean, "매장", "금액"))
print(count_by(clean, "매장"))

# -------------------------------------------------------------
# [문제 5] 매장별 매출과 막대그래프
# -------------------------------------------------------------
# 문제 4의 sum_by 를 써서 매장별 매출을 구하고, 옆에 막대그래프를 그려 출력하세요.

# 막대는 1만원당 ■ 하나로 그리세요.

# [출력 예시]
#   강남점    00,000원  ■■■■■
#   홍대점    00,000원  ■■■■
#   부산점    00,000원  ■■■■

# [힌트] "■" * (금액 // 10000)
#        f"{금액:,}" 로 쓰면 천 단위 쉼표가 붙습니다.
# -------------------------------------------------------------
print("\n--- 문제 5 ---")

for branch, sales in sum_by(clean, "매장", "금액").items():
    bar = "■" * (sales // 10000)
    print(f"\n{branch}  {sales:,}원 {bar}")

# -------------------------------------------------------------
# [문제 6] 분류별 집계표
# -------------------------------------------------------------
# 분류(커피/논커피/디저트)별로 아래 세 가지를 구해 표로 출력하세요.
#   - 주문 건수
#   - 매출 합계
#   - 건당 평균 (소수 첫째 자리까지)

# [출력 예시]
#   분류      건수      합계      평균

#   ------------------------------------

#   커피         0   000,000   00000.0

#   논커피       0     0,000    0000.0

#   디저트       0    00,000   00000.0

# [힌트] 문제 4에서 만든 함수 두 개를 모두 씁니다.
#        칸 맞추기: f"{값:<6}" 왼쪽 정렬, f"{값:>8}" 오른쪽 정렬
# -------------------------------------------------------------

print("\n--- 문제 6 ---")
print("분류         건수        합계       평균")
print("\n----------------------------------------")

category_sum = sum_by(clean, "분류", "금액")
category_count = count_by(clean, "분류")
for category in category_sum:
    count = category_count[category]
    total = category_sum[category]
    avg = round(total / count, 1)
    width = 10 - len(category)
    print(f"\n{category:<{width}}{count:>6}{total:>13}{avg:>10}")

# -------------------------------------------------------------
# [문제 7] 조건으로 걸러내기
# -------------------------------------------------------------
# 아래 두 가지를 각각 구해 출력하세요.
#   1) 포장 주문(포장 열이 "Y")의 건수와 매출 합계
#   2) 오전 매출 합계와 오후 매출 합계

# [출력 예시]
#   포장 주문: 0건, 00,000원

#   오전 매출: 00,000원

#   오후 매출: 00,000원

# -------------------------------------------------------------

print("\n--- 문제 7 ---")
takeout_count = 0
takeout_total = 0

for row in clean:
    if row["포장"] == "Y":
        takeout_count += 1
        takeout_total += row["금액"]

morning_total = 0
afternoon_total = 0

for row in clean:
    if row["시간대"] == "오전":
        morning_total += row["금액"]
    elif row["시간대"] == "오후":
        afternoon_total += row["금액"]

print(f"포장 주문 : {takeout_count}건, {takeout_total:,}원")
print(f"\n오전 매출 : {morning_total:,}원")
print(f"\n오후 매출 : {afternoon_total:,}원")

# -------------------------------------------------------------
# [문제 8] 가장 많이 팔린 메뉴 찾기
# -------------------------------------------------------------
# 메뉴별 판매 수량을 합산하고, 가장 많이 팔린 메뉴와 그 수량을 찾는 함수를 만드세요.

#   함수 이름 : best_menu(rows)
#   반환      : (메뉴이름, 수량) 두 개를 함께 돌려줄 것

# 만든 뒤 메뉴별 수량 전체와 1등을 출력하세요.

# [출력 예시]

#   메뉴별 판매 수량

#     아메리카노  00개

#     카페라떼    00개

#     ...

#   가장 많이 팔린 메뉴: OOO (00개)

# [힌트] 현재 1등을 변수에 담아두고 하나씩 비교하며 갱신합니다.
#        수량 합산은 문제 4의 sum_by 를 재사용하세요.
# -------------------------------------------------------------

print("\n--- 문제 8 ---")


def best_menu(rows):
    # (메뉴이름,수량) 형태로 반환
    menu_count = sum_by(rows, "메뉴", "수량")
    best_menuname = ""
    best_count = 0

    for menu, count in menu_count.items():
        if count > best_count:
            best_menuname = menu
            best_count = count

    return best_menuname, best_count


best_menuname, best_count = best_menu(clean)
print("메뉴별 판매 수량")

# for menu, count in sum_by(clean, "메뉴", "수량").items():
#     print(f"\n{menu:<6}{count:>6}개")

for menu, count in sum_by(clean, "메뉴", "수량").items():
    width = 10 - len(menu)
    print(f"\n{menu:<{width}}{count:>6}개")


print(f"\n가장 많이 팔린 메뉴 : {best_menuname} ({best_count}개)")

# -------------------------------------------------------------
# [문제 9] 결과를 CSV 로 저장하기
# -------------------------------------------------------------
# 아래 두 파일을 만드세요.
#   1) data/매장별_매출.csv
#      열 구성 : 매장, 주문건수, 매출합계
#   2) data/오류목록.csv
#      열 구성 : 줄번호, 메뉴, 사유
#      (문제 3에서 걸러낸 이상한 데이터)

# 조건 : 엑셀로 열었을 때 한글이 깨지지 않아야 합니다.
# 저장한 뒤 두 파일을 다시 읽어서 내용을 출력해 확인하세요.
# [힌트] encoding 을 뭘로 해야 할까요? 그냥 utf-8 이 아닙니다.
# -------------------------------------------------------------

print("\n--- 문제 9 ---")

store_count = count_by(clean, "매장")
store_total = sum_by(clean, "매장", "금액")

store_file = DATA / "매장별_매출.csv"
with open(store_file, "w", encoding="utf-8-sig", newline="") as f:
    csv.writer(f).writerow(["매장", "주문건수", "매출합계"])

    for store in store_count:
        csv.writer(f).writerow([store, store_count[store], store_total[store]])

error_file = DATA / "오류목록.csv"
with open(error_file, "w", encoding="utf-8-sig", newline="") as f:
    csv.writer(f).writerow(["줄번호", "메뉴", "사유"])

    for line_no, menu, reason in problem:
        csv.writer(f).writerow([line_no, menu, reason])


print("--- 매장별_매출.csv ---")
with open(store_file, "r", encoding="utf-8-sig", newline="") as f:
    for row in csv.reader(f):
        print(row)

print("\n--- 오류목록.csv ---")
with open(error_file, "r", encoding="utf-8-sig", newline="") as f:
    for row in csv.reader(f):
        print(row)

# -------------------------------------------------------------
# [문제 10] 보고서 만들기
# -------------------------------------------------------------
# 지금까지 구한 내용을 모아 data/일일보고서.txt 로 저장하세요.
# CSV 가 아니라 그냥 텍스트 파일입니다.

# [파일에 들어갈 내용 예시]
#   ========================================

#    카페 매출 보고서

#   ========================================

#   총 주문: 00건

#   총 매출: 000,000원

#   [매장별]

#     강남점  00,000원

#     홍대점  00,000원

#     부산점  00,000원

#   [분류별]

#     커피    000,000원

#     논커피    0,000원

#     디저트   00,000원

#   가장 많이 팔린 메뉴: OOO

#   ----------------------------------------

#   처리 실패: 0건 (오류목록.csv 참고)

# [힌트] 여러 줄을 쓸 때는 f.write() 를 여러 번 부르면 됩니다.
#        줄 끝에 \n 을 꼭 붙이세요.
# 저장한 뒤 파일을 다시 읽어서 화면에도 출력해 보세요.
# -------------------------------------------------------------

print("\n--- 문제 10 ---")

# 총주문, 총매출 - 3번 / 매장별 -  4번 / 분류별 - 6번 / 가장많이 - 8번

report_file = DATA / "일일보고서.txt"
with open(report_file, "w", encoding="utf-8") as f:
    f.write("========================================\n\n")
    f.write("            카페 매출 보고서\n\n")
    f.write("========================================\n\n")

    f.write(f"총 주문 : {len(clean)}건\n\n")
    f.write(f"총 매출 : {total_sales:,}원\n\n")

    f.write("[매장별]\n\n")
    for store in store_total:
        f.write(f"{store}  {store_total[store]:,}원\n\n")

    f.write("[분류별]\n\n")
    for category in category_sum:
        width = 6 - len(category)
        f.write(f"{category:<{width}}{(category_sum[category]):>10,}원\n\n")

    f.write(f"\n가장 많이 팔린 메뉴 : {best_menuname}\n\n")
    f.write("----------------------------------------\n\n")
    f.write(f"처리 실패: {len(problem)}건 (오류목록.csv 참고)\n")

with open(report_file, "r", encoding="utf-8") as f:
    print(f.read())

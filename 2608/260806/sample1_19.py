age = int(input("나이를 입력하세요 : "))
student = input("신분을 입력하세요 ('학생' 또는 '일반'): ")

a = ""

if age >= 20:
    a = "성인"
elif age >= 13:
    a = "청소년"
else:
    a = "어린이"

ticket = {
    "성인": {"price": 12000, "학생할인": 2000},
    "청소년": {"price": 9000, "학생할인": 1000},
    "어린이": {"price": 6000, "학생할인": 0},
}

discount = 0

if student == "학생" and ticket[a]["학생할인"] > 0:
    discount = ticket[a]["학생할인"]
    print(f"학생 할인 : {ticket[a]['학생할인']}원 적용")
    print(f"구분 : {a} / 최종 요금 : {ticket[a]['price'] - ticket[a]['학생할인']}원")
else:
    discount = 0
    print(f"구분 : {a} / 최종 요금 : {ticket[a]['price']}원")

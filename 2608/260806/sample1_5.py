money = int(input("금액을 입력하세요 : "))

bills = {"오만원권": 50000, "만원권": 10000, "천원권": 1000}

a = 0
b = 0
c = 0
d = 0

if money >= 50000:
    a = money // bills["오만원권"]
    b = (money % bills["오만원권"]) // bills["만원권"]
    c = ((money % bills["오만원권"]) % bills["만원권"]) // bills["천원권"]
    d = money - (a * bills["오만원권"] + b * bills["만원권"] + c * bills["천원권"])
elif money >= 10000:
    b = money // bills["만원권"]
    c = (money % bills["만원권"]) // bills["천원권"]
    d = money - (b * bills["만원권"] + c * bills["천원권"])
elif money >= 1000:
    c = money // bills["천원권"]
    d = money - (c * bills["천원권"])
else:
    d = money

print(f"오만원권 : {a}장\n만원권 : {b}장\n천원권 : {c}장\n남는돈 : {d}원")

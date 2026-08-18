name = input("상품 이름을 입력하세요 : ")
money = int(input("투입 금액을 입력하세요 : "))

vending = {
    "콜라": {"price": 1500, "stock": 2},
    "사이다": {"price": 1400, "stock": 0},
    "물": {"price": 800, "stock": 5},
}

pay = ""

if name in vending:
    if vending[name]["stock"] == 0:
        print("재고가 없습니다")
    else:
        if money < vending[name]["price"]:
            print(f"잔액이 부족합니다 (부족 금액 : {vending[name]['price'] - money}원)")
        else:
            pay = "구매 완료"
            print(f"{name} {pay} / 거스름돈 {money - vending[name]['price']}원")
            print(f"{name} 남은 재고 : {vending[name]['stock'] - 1}개")
else:
    print("없는 상품입니다")

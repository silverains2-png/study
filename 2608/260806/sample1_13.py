name = input("상품 이름을 입력하세요 : ")
num = int(input("주문 수량을 입력하세요 : "))

stock = {
    "사과": {"qty": 10, "price": 1500},
    "바나나": {"qty": 0, "price": 3000},
    "포도": {"qty": 5, "price": 8000},
}

if name in stock:
    if stock[name]["qty"] != 0:
        if num > stock[name]["qty"]:
            print(f"재고가 부족합니다 (남은 재고 : {stock[name]['qty']})")
        else:
            print(f"{name} {num}개 주문 / 결제금액 {stock[name]['price'] * num}원\n")
            print(f"{name} 남은 재고: {stock[name]['qty'] - num}개")
    else:
        print("재고가 없습니다")
else:
    print("취급하지 않는 상품입니다")

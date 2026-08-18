coffee = input("메뉴를 입력하세요 : ")
cups = int(input("몇 잔 주문하시겠습니까 : "))

menu = {
    "아메리카노": {"price": 3000, "kcal": 10},
    "라떼": {"price": 4000, "kcal": 180},
    "케이크": {"price": 5500, "kcal": 420},
}

if coffee in menu:
    price = menu[coffee]["price"] * cups
    cal = menu[coffee]["kcal"] * cups
    print(f"{coffee} x {cups} = {price}원 / {cal}kcal")
    if price >= 10000:
        print("무료 배송 대상입니다")
    else:
        need = 10000 - price
        print(f"배송까지 {need}원이 더 필요합니다")
else:
    print("없는 메뉴입니다")

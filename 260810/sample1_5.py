# [문제 5] 자판기 프로그램

# 소지금 5000원에서 시작. 반복하면서 메뉴와 현재 소지금을 보여주고

# 음료 이름을 입력받으세요.

#   - 메뉴에 없는 이름 → "그런 음료는 없습니다"

#   - 돈이 부족하면    → "잔액이 부족합니다"

#   - 성공하면 소지금 차감 후 구매 목록 리스트에 추가

#   - "종료"를 입력하거나, 소지금이 가장 싼 음료보다 적어지면 자동 종료

#     → 산 음료 목록과 남은 돈 출력

menu = {"콜라": 1500, "사이다": 1300, "물": 800}

money = 5000

bought = []

while True:
    print(f"현재 소지금 : {money}원")
    print(f"메뉴 : {menu}")
    name = input("메뉴를 입력하세요 (종료 : 종료): ")

    if name == "종료":
        break
    if name not in menu:
        print("그런음료는 없습니다")
        continue
    if money < menu[name]:
        print("잔액이 부족합니다")
        continue

    money -= menu[name]
    bought.append(name)
    if money < menu["물"]:
        print("소지금이 부족해 종료합니다.")
        break

if len(bought) == 0:
    print(f"아무것도 구매하지 않았습니다 / 소지금 : {money}원")
else:
    print(f"구매 음료 목록 : {bought} / 남은돈 : {money}원")

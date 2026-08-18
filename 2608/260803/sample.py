print("--- 스마트 무인 카페에 오신것을 환영합니다 ---")
print("-" * 45)

coffee = int(input("아메리카노 한잔의 가격을 입력하세요 : (예 : 4000) "))
cup = int(input("주문할 잔수를 입력하세요 : (예 : 3) "))
discount = float(input("오늘의 할인율을 입력하세요 : (예 : 10.5) "))
cash = int(input("지갑에 가진 현금의 총액의 입력하세요 : (예 : 16000) "))

print("=" * 45)
print("        [ 영 수 증  및  결 제 내 역]           ")
print("=" * 45)

total = coffee * cup
total_discount = total / 100 * discount
price = int(total - total_discount)

print(f"* 메뉴 가격 : {coffee}원")
print(f"* 주문 수량 : {cup}잔")
print(f"* 총 주문액 : {total}원")
print(f"* 할인 적용 : -{total_discount}원 ({discount}%)")

print("-" * 45)
print(f"* 최종 결제 : {price}원")
print(f"* 보유 현금 : {cash}원")
print("-" * 45)


print("* 결제 가능 여부 : ", bool(cash - price > 0))
print(f"* 남은 잔돈      : {cash - price}원")
print("=" * 45)
print("이용해 주셔서 감사합니다 좋은 하루 보내세요! :)")
print("asdfasdf@asdfasdf.asdf 20260803 %")

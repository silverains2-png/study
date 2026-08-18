print("------ V I P 통합 무인 키오스크 시스템 ------")
print("-" * 45)

movie = int(input("영화 1인의 관람료를 입력하세요 : (예 : 14000) "))
ticket = int(input("예매할 총 인원수를 입력하세요 : (예 : 3) "))
pop_price = int(input("팝콘 세트 1개의 가격을 입력하세요 : (예 : 9000) "))
popcorn = int(input("구매할 팝콘 세트의 수를 입력하세요 : (예 : 2) "))
vip = input("VIP 회원입니까? : (y/n) ")
cash = int(input("보유 현금의 총액의 입력하세요 : (예 : 60000) "))

print("=" * 45)
print("       [ 최 종 정 산  및  결 제 내 역]         ")
print("=" * 45)

movie_total = movie * ticket
popcorn_total = pop_price * popcorn
total = movie_total + popcorn_total

is_vip_bool = vip == "y"
is_vipdiscount = int(vip == "y")
discount = int(-total * 0.2 * is_vipdiscount)

price = total + discount

cut = price // 10
cut_total = cut * 10
change = cash - cut_total

print(f"* 영화 관람료 합계 : {movie_total}원")
print(f"* 팝콘세트 합계    : {popcorn_total}원")
print(f"* 총 주문금액      : {total}원")
print(f"* VIP 할인적용     : {discount}원 (회원여부 : {is_vip_bool}) ")
print(f"* 10원 단위 절사   : 적용 완료 ")

print("-" * 45)
print(f"* 최종 결제 금액 : {cut_total}원")
print(f"* 보유 현금 총액 : {cash}원")
print(f"* 거스름돈       : {change}원")
print("-" * 45)


print("* 정상 예매 승인 : ", bool(change >= 0 and ticket != 0))
print("=" * 45)
print("이용해 주셔서 감사합니다 좋은 하루 보내세요! :)")
print("asdfasdf@asdfasdf.asdf 20260803 %")

my_bag = ["낡은 검", "빨간 포션", "시민의 옷"]
user = ""

new_item = input("새로운 아이템의 이름을 입력하세요 : ")
new_pay = int(input("새로운 아이템의 가격을 입력하세요 : "))

my_bag.append(new_item)

if new_pay >= 10000 or len(my_bag) >= 4:
    user = "상급 모험가"
else:
    user = "초보 모험가"

print(
    f"모험가 등급: {user}\n가방의 최종상태: {my_bag}\n가방의 첫번째 아이템: {my_bag[0]}\n가방의 마지막 아이템: {my_bag[len(my_bag) - 1]}"
)

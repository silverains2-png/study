# items = [12000, 8500, 30000, 4500]
# grade = "GOLD"
# coupon = 5000
# items = [9000, 6000]
# grade = "GOLD"
# coupon = 8000
# items = [9000, 6000]
# grade = "SILVER"
# coupon = 0
items = [12000, 8500, 30000, 4500]
grade = "NONE"
coupon = 0

items_sum = sum(items)

vip = 0

if grade == "GOLD":
    vip = int(items_sum * 0.1)
elif grade == "SILVER":
    vip = int(items_sum * 0.05)
else:
    vip = 0

discount = 0

if items_sum * 0.3 <= vip + coupon:
    discount = int(items_sum * 0.3)
else:
    discount = vip + coupon

final = 0
ship = 0

if items_sum - discount < 30000:
    ship = 3000
    final = items_sum - discount + ship
else:
    ship = 0
    final = items_sum - discount + ship

print(
    f"상품 합계 : {items_sum}\n총 할인 : {discount}\n배송비 : {ship}\n최종 결제 금액 : {final}"
)

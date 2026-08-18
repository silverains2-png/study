#   전역 상수 : BASE_FEE = 3000 (기본 배달료)

#              FREE_LIMIT = 20000 (무료배달 기준액)

#              EXTRA_PER_KM = 500 (1km당 추가요금)

#   함수 : get_delivery_fee(order_price, distance_km)

#         - 주문액이 FREE_LIMIT 이상이면 배달료 0원

#         - 아니면 BASE_FEE + (거리 × EXTRA_PER_KM)

# [기대 결과]

#   주문 15000원, 3km -> 배달료 4500원, 총 19500원

#   주문 25000원, 5km -> 배달료 0원, 총 25000원

#   주문  8000원, 1km -> 배달료 3500원, 총 11500원

# -------------------------------------------------------------
# 아래 주문 목록을 모두 처리하세요. [주문금액, 거리km]

orders = [[15000, 3], [25000, 5], [8000, 1]]

BASE_FEE = 3000
FREE_LIMIT = 20000
EXTRA_PER_KM = 500


def get_delivery_fee(order_price, distance_km):
    if order_price >= FREE_LIMIT:
        return 0
    else:
        return BASE_FEE + (distance_km * EXTRA_PER_KM)


for i in orders:
    order_price = i[0]
    distance_km = i[1]

    delivery_fee = get_delivery_fee(order_price, distance_km)
    total = order_price + delivery_fee

    print(
        f"주문 {order_price}원, {distance_km}km -> 배달료 {delivery_fee}원, 총 {total}원"
    )

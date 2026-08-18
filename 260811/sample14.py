# 함수 두 개를 만드세요.

#   add_item(cart, name)    : 상품을 추가한 새 리스트를 돌려준다

#   remove_item(cart, name) : 상품을 뺀 새 리스트를 돌려준다

#                             (없는 상품이면 "없는 상품입니다" 출력)

# ★ 두 함수 모두 원본 리스트를 바꾸면 안 됩니다.

# [기대 결과]

#   장바구니1: ['사과']

#   장바구니2: ['사과', '우유']

#   장바구니3: ['사과', '우유', '빵']

#   없는 상품입니다: 라면

#   장바구니4: ['사과', '빵']

#   원본 확인 - 장바구니1: ['사과']

# -------------------------------------------------------------

cart1 = ["사과"]


def add_item(cart, name):
    new_cart = []
    for i in cart:
        new_cart.append(i)
    new_cart.append(name)
    return new_cart


def remove_item(cart, name):
    if name not in cart:
        print(f"없는 상품입니다 : {name}")
        return cart

    new_cart = []
    for i in cart:
        if i != name:
            new_cart.append(i)
    return new_cart


print("장바구니1:", cart1)

cart2 = add_item(cart1, "우유")
print("장바구니2:", cart2)

cart3 = add_item(cart2, "빵")
print("장바구니3:", cart3)

cart4 = remove_item(cart3, "라면")
cart4 = remove_item(cart3, "우유")
print("장바구니4:", cart4)

print("원본 확인 - 장바구니1:", cart1)

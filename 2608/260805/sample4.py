cart = ["사과", "우유", "빵"]

item = "우유"

print(cart)

if item in cart:
    print("이미 담겨있습니다")
else:
    cart.append(item)
    print(cart)

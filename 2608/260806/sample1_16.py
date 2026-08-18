num = int(input("상품 번호를 입력하세요 : "))

cart = {
    "items": ["티셔츠", "양말", "모자"],
    "prices": [15000, 3000, 12000],
}

if num > len(cart["items"]) or num < 0:
    print("범위를 벗어난 번호입니다.")
else:
    print(f"{num}번 상품 : {cart['items'][num - 1]} / {cart['prices'][num - 1]}")
    print(f"전체 합계 : {sum(cart['prices'])}원")

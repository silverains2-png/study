# 함수 두 개를 만드세요.

#   make_star(score)     : 점수(0~5)를 별 문자열로. 예) 3 -> "★★★☆☆"

#   show_review(name, score) : "상품명  ★★★☆☆ (3)" 형태로 출력

#                              (make_star 를 불러서 쓸 것)

# [기대 결과]

#   노트북      ★★★★☆ (4)

#   마우스      ★★★★★ (5)

#   키보드      ★★☆☆☆ (2)

# ★ show_review 는 return 없이 print 만 합니다. 이건 괜찮습니다.

# -------------------------------------------------------------
reviews = {"노트북": 4, "마우스": 5, "키보드": 2}


def make_star(score):
    return "★" * score + "☆" * (5 - score)


def show_review(name, score):
    print(f"{name}    {make_star(score)}")


for i, j in reviews.items():
    show_review(i, j)

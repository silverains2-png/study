# 창고의 재고를 관리하는 함수 세 개를 만드세요.
#
#   add_stock(stock, name, count)
#     - stock 딕셔너리에 상품을 count 개 넣는다
#     - 이미 있는 상품이면 기존 개수에 더한다
#     - 없는 상품이면 새로 만든다
#     - 바뀐 stock 을 return 한다
#
#   remove_stock(stock, name, count)
#     - stock 에서 상품을 count 개 뺀다
#     - 보유량보다 많이 빼려고 하면
#       "재고 부족: 상품명 (요청 N, 보유 M)" 을 출력하고 아무것도 빼지 않는다
#     - 바뀐 stock 을 return 한다
#
#   show_stock(stock)
#     - 전체 재고를 보기 좋게 출력한다 (return 없음)
#
# ※ input() 은 쓰지 않습니다. 아래처럼 코드에 직접 값을 적어서 호출하세요.
#
#   [호출 예시]  이런 식으로 쓰게 됩니다
#       stock = add_stock(stock, "마우스", 10)
#       stock = remove_stock(stock, "마우스", 3)
#       show_stock(stock)
#
# 아래 6가지를 순서대로 실행하는 코드를 작성하세요.
#   1) 마우스 10개 입고
#   2) 키보드 5개 입고
#   3) 마우스 3개 출고
#   4) 키보드 10개 출고   <- 5개밖에 없으므로 실패해야 함
#   5) 모니터 2개 입고    <- 처음 보는 상품
#   6) 전체 재고 출력
#
# [기대 결과]
#   재고 부족: 키보드 (요청 10, 보유 5)
#   [재고 현황]
#     마우스: 7개
#     키보드: 5개
#     모니터: 2개
# -------------------------------------------------------------
stock = {}


def add_stock(stock, name, count):
    if name not in stock:
        stock[name] = count
    else:
        stock[name] += count
    return stock


def remove_stock(stock, name, count):
    if stock[name] < count:
        print(f"재고부족: {name} (요청 {count}, 보유 {stock[name]})")
    else:
        stock[name] -= count

    return stock


def show_stock(stock):
    print("[재고 현황]")

    for i, j in stock.items():
        print(f"{i}: {j}개")


add_stock(stock, "마우스", 10)
add_stock(stock, "키보드", 5)
remove_stock(stock, "마우스", 3)
remove_stock(stock, "키보드", 10)
add_stock(stock, "모니터", 2)
show_stock(stock)

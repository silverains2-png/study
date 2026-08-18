# 함수 세 개를 만드세요.

#   visit(count)        : 방문자 수를 1 늘려서 돌려준다

#   reset()             : 0 을 돌려준다

#   show_count(count)    : "현재 방문자: N명" 형태로 출력

# 아래 순서대로 실행하세요.

#   방문 -> 방문 -> 방문 -> 현황 출력 -> 초기화 -> 현황 출력

# [기대 결과]

#   현재 방문자: 3명

#   현재 방문자: 0명

# -------------------------------------------------------------
count = 0


def visit(count):
    count += 1
    return count


def reset():
    return 0


def show_count(count):
    print(f"현재 방문자: {count}명")


count = visit(count)
count = visit(count)
count = visit(count)

show_count(count)

count = reset()

show_count(count)

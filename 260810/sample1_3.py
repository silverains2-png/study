# [문제 3] 점수 입력받아 통계 내기

# 점수를 계속 입력받되 -1을 입력하면 종료.

# 단, 0~100 범위를 벗어난 점수는 리스트에 넣지 말고

# "잘못된 점수입니다" 출력 후 다시 입력받기.

# 종료 시 평균 / 최고점 / 최저점 출력.

# 실행 예시)

#   점수 입력(-1: 종료): 90

#   점수 입력(-1: 종료): 150

#   잘못된 점수입니다

#   점수 입력(-1: 종료): 80

#   점수 입력(-1: 종료): -1

#   평균: 85.0 / 최고: 90 / 최저: 80

scores = []

while True:
    score = int(input("점수 입력(-1: 종료) : "))
    if score == -1:
        break

    if 0 <= score <= 100:
        scores.append(score)
    else:
        print("잘못된 점수입니다")

if scores:
    maxscore = max(scores)
    minscore = min(scores)
    avg = sum(scores) / len(scores)
    print(f"평균 : {avg} / 최고 : {maxscore} / 최저 : {minscore}")
else:
    print("입력된 점수가 없습니다")

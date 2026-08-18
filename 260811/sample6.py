# 함수 두 개를 만드세요.

#   get_average(scores) : 리스트의 평균 (소수 첫째 자리 반올림)

#   get_grade(score)    : 점수 -> 등급 (90이상 A, 80이상 B, 70이상 C, 나머지 D)

# 그리고 아래 학생들의 평균과 등급을 출력하세요.

# [기대 결과]

#   김철수  평균 91.7  등급 A

#   이영희  평균 78.3  등급 C

#   박민수  평균 85.0  등급 B

# --------------------------------------------------------------------------

students = {
    "김철수": [90, 85, 100],
    "이영희": [70, 95, 70],
    "박민수": [80, 85, 90],
}


def get_average(scores):
    total = 0
    for i in scores:
        total += i

    avg = total / len(scores)
    return round(avg, 1)


def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "D"


for i in students:
    print(
        f"{i} 평균 : {get_average(students[i])} 등급 {get_grade(get_average(students[i]))}"
    )

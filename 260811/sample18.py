# 아래 함수들을 조립해서 성적표를 출력하세요.

#   get_average(scores)       : 평균 (소수 첫째 자리)   ← 6번에서 만든 것 재사용!

#   get_grade(avg)            : 등급 (90 A / 80 B / 70 C / 그 외 D) ← 6번 재사용!

#   get_best(students)        : 평균이 가장 높은 학생 이름

#   print_report(students)    : 성적표 전체 출력

# [기대 결과]

#   ===== 성적표 =====

#   김철수   91.7  A

#   이영희   78.3  C

#   박민수   85.0  B

#   최지은   62.7  D

#   ------------------

#   전체 평균: 79.4

#   최고 득점: 김철수

#   6번에서 만든 함수를 다시 만들지 말고 그대로 쓰세요.

# -------------------------------------------------------------
class_scores = {
    "김철수": [90, 85, 100],
    "이영희": [70, 95, 70],
    "박민수": [80, 85, 90],
    "최지은": [55, 70, 63],
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


def get_best(students):
    best_student = ""
    best_avg = 0

    for i, j in students.items():
        avg = get_average(j)

        if avg > best_avg:
            best_avg = avg
            best_student = i

    return best_student


def print_report(students):
    print("===== 성적표 =====")
    total = 0
    count = 0

    for i, j in students.items():
        avg = get_average(j)
        grade = get_grade(avg)

        print(f"{i}   {avg:.1f}  {grade}")

        total += avg
        count += 1

    print("------------------")

    total_avg = total / count
    print(f"전체 평균: {total_avg:.1f}")
    print(f"최고 득점: {get_best(students)}")


print_report(class_scores)

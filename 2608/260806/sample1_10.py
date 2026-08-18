name = input("이름을 입력하세요 : ")

scores = {"김철수": [90, 85, 100], "이영희": [70, 65, 80]}
final = ""
if round(sum(scores[name]) / len(scores[name]), 1) >= 80:
    final = "합격"
else:
    final = "불합격"


print(
    f"{name} 점수: {scores[name]}\n1과목 점수 : {scores[name][0]}\n총점 : {sum(scores[name])} / 평균 : {round(sum(scores[name]) / len(scores[name]), 1)}\n최고점 : {max(scores[name])} / 최저점 : {min(scores[name])}\n{final}"
)

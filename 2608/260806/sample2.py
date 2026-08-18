student = [
    {"name": "민수", "국어": 95, "영어": 100},
    {"name": "철수", "국어": 75, "영어": 50},
]

winner_avg = 0
winner = ""
total = 0

print("# 1. 각 사람의 평균")
for i in student:
    avg = (i["국어"] + i["영어"]) / 2
    total += avg
    print(f"{i['name']} 평균 : {avg}")

    if avg > winner_avg:
        winner_avg = avg
        winner = i["name"]

print("# 2. 두 사람의 평균")
total_avg = total / len(student)
print(f"두 사람의 평균은 {total_avg}입니다")

print("# 3. 누가더 우수한 사람인가?")
print(f"{winner}가(이) 더 우수한 사람입니다")

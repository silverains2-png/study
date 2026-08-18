a = input("반 이름을 입력하세요 (1반) : ")
b = int(input("번호를 입력하세요 : "))

school = {
    "3학년": {
        "1반": {"teacher": "박선생", "students": ["김철수", "이영희", "박민수"]},
        "2반": {"teacher": "최선생", "students": ["정수진", "한동훈"]},
    }
}

if a in school["3학년"]:
    if b > len(school["3학년"][a]["students"]):
        print("학생 수 범위를 벗어났습니다.")
    else:
        print(f"3학년 {a} 담임 : {school['3학년'][a]['teacher']}")
        print(f"학생 수 : {len(school['3학년'][a]['students'])}")
        print(f"{b}번 학생 : {(school['3학년'][a]['students'][b - 1])}")
else:
    print("없는 반입니다")

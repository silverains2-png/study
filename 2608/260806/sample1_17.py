name = input("요즘제 이름을 입력하세요 : ")
usage = int(input("이번 달 사용량을 입력하세요(분) : "))

plans = {
    "basic": {"기본요금": 12000, "무료통화": 100, "초과요금": 50},
    "premium": {"기본요금": 25000, "무료통화": 300, "초과요금": 30},
}

if name in plans:
    if plans[name]["무료통화"] < usage:
        print(
            f"요금제 : {name} / 사용량 {usage}분 / 초과 {usage - plans[name]['무료통화']}분"
        )
        print(
            f"이번 달 요금 : {plans[name]['기본요금'] + (usage - plans[name]['무료통화']) * plans[name]['초과요금']}"
        )
    else:
        print(f"요금제 : {name} / 사용량 {usage}분 / 초과 0분")
        print(f"이번 달 요금 : {plans[name]['기본요금']}")
else:
    print("없는 요금제 입니다")

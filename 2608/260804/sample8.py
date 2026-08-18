code_name = input("요원코드명 (예: Falcon) : ")
code_number = int(input("보안코드 (예: 84269) : "))
code_rank = input("마스터키 등급 ('S'/'A'/'N' 중 하나) : ")
body_temp = float(input("현재 체온 (예: 36.5) : "))
remain_time = int(input("남은 시간(초) (예:200) : "))

num10000 = code_number // 10000
num1000 = (code_number // 1000) % 10
num100 = (code_number // 100) % 10
num10 = (code_number // 10) % 10
num1 = code_number % 10

if num10000 == num1 and num1000 == num10:
    print("복제된 코드 감지! 즉시 폐쇄합니다.")
else:
    cond_a = (num10000 + num1000) >= (num10 + num1)
    cond_b = code_number % 2 == 0 or code_number % 3 == 0
    cond_c = num100 % 2 != 0

    if not (
        code_rank == "S"
        and cond_a
        or code_rank == "A"
        and (cond_a and (cond_b or cond_c))
        or code_rank == "N"
        and (cond_a and cond_b and cond_c)
    ):
        print("보안 시스템 작동! 침입자를 체포하라!")
    else:
        body_cond = ""
        if 36.0 <= body_temp <= 37.5:
            body_cond = "정상"
        elif 35.0 <= body_temp <= 38.5:
            body_cond = "주의"
        else:
            body_cond = "위독"

        risk = (num10000 * num1000) / (num10 + 1)
        risk_level = 0

        if body_cond == "위독":
            risk = None
            print("생체 신호 위독! 의무실로 강제 이송합니다. (위험도: 측정 불가)")
        else:
            if body_cond == "주의":
                risk_level = risk * 1.5
            else:
                risk_level = risk

            required_time = 0

            if risk >= 50:
                required_time = 180
            elif risk <= 50:
                required_time = 60

            limit_time = required_time - remain_time
            time = remain_time - required_time

            if limit_time > 0:
                minute = limit_time // 60
                second = limit_time % 60
                print(
                    f"시간 초과! 문이 다시 잠겼습니다. (부족한 시간: {minute}분 {second:02d}초)"
                )
            else:
                minute = time // 60
                second = time % 60
                print(
                    f"[{code_name}] 서버실 개방! 상태: {body_cond} / 위험도: {risk_level:.2f} / 잔여 {minute}분 {second:02d}초"
                )

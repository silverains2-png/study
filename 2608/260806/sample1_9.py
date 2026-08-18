num = int(input("숫자를 입력하세요 : "))


week = {
    1: {"name": "월요일", "weekend": False},
    2: {"name": "화요일", "weekend": False},
    3: {"name": "수요일", "weekend": False},
    4: {"name": "목요일", "weekend": False},
    5: {"name": "금요일", "weekend": False},
    6: {"name": "토요일", "weekend": True},
    7: {"name": "일요일", "weekend": True},
}

if num in week:
    print(f"{num}번째 요일: {week[num]['name']}")
    if week[num]["weekend"]:
        print("주말입니다")
    else:
        print("주말이 아닙니다")
else:
    print("범위를 벗어났습니다")

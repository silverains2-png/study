time = int(input("시간을 입력하세요 (초) : "))


hour = time // 3600
minite = (time % 3600) // 60
second = ((time % 3600) % 60) % 60

dic = {"시간": hour, "분": minite, "초": second}

print(f"{time}초 = {dic['시간']}시간 {dic['분']}분 {dic['초']}초")

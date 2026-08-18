name = input("모험가의 이름을 입력하세요 : ")
level = int(input("모험가의 레벨을 입력하세요 : "))
ad = int(input("모험가의 공격력을 입력하세요 : "))
shield = input("방패 소지 여부 (y/n) : ")

if level >= 10 and ad >= 50:
    print("던전 입장이 가능합니다")
    if level >= 30 or shield == "y":
        ad *= 1.5
        print("전설의 버프가 발동하여 공격력이 상승합니다!")
        print(f"모험가명 : {name}\n최종레벨 : {level}\n최종전투력 : {ad}")
    else:
        pass
else:
    print("입장 자격 미달입니다. 더 수련하고 오세요!")

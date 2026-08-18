a = input("이름,나이,도시를 입력하세요 : ")

b = a.split(",")

dic = {"name": b[0], "age": int(b[1]), "city": b[2]}

print(dic)
print(f"10년뒤 나이 : {dic['age'] + 10}")
if dic["city"] == "서울":
    print("수도권 거주자입니다.")
else:
    print("지방 거주자입니다.")

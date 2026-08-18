n = input("이름을 입력하세요 : ")
a = int(input("나이를 입력하세요 : "))

ad = True

if a >= 19:
    ad = True
else:
    ad = False

dic = {"name": n, "age": a, "adult": ad}

print(dic)
print(f"{dic['name']}님 / {dic['age']}세 / 성인 여부 : {ad}")

weight = float(input("몸무게를 입력하세요 (kg) : "))
height = float(input("키를 입력하세요 (m) : "))

bmi = round(weight / (height**2), 2)
rating = ""

if bmi < 18.5:
    rating = "저체중"
elif bmi <= 23:
    rating = "정상"
elif bmi <= 25:
    rating = "과체중"
else:
    rating = "비만"

dic = {"bmi": bmi, "판정": rating}

print(dic)
print(f"BMI {dic['bmi']} -> {dic['판정']}")

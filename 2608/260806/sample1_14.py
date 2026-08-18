num = int(input("점수를 입력하세요 : "))

grade = ""

num_str = str(num) + "점"
num_float = float(num)

if num >= 90:
    grade = "A"
elif num >= 80:
    grade = "B"
else:
    grade = "C"

print(f"입력값 타입 : {type(num)}\n")
print(f"문자열로 변환 : {num_str}\n")
print(f"실수로 변환 : {num_float}\n")
print(f"등급 : {grade}")

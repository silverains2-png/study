number = int(input("숫자를 입력하세요 : "))

even = number % 2 == 0
a = number // 2
b = number % 2

dic = {"number": number, "짝수": even, "몫": a, "나머지": b}

c = ""

if even:
    c = "짝수"
else:
    c = "홀수"

print(dic)
print(f"{number}은(는) {c}입니다")

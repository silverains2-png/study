num1 = int(input("숫자1을 입력하세요 : "))
num2 = int(input("숫자2를 입력하세요 : "))
cal = input("연산자를 입력하세요 : ")


a = num1 + num2
b = num1 - num2
c = num1 * num2
d = num1 / num2
e = num1 // num2
f = num1 % num2
g = num1**num2

dic = {"+": a, "-": b, "*": c, "/": d, "//": e, "%": f, "**": g}

answer = 0

if cal == "+":
    answer = a
    print(dic)
    print(f"{num1} + {num2} = {a}")
elif cal == "-":
    answer = b
    print(dic)
    print(f"{num1} - {num2} = {b}")
elif cal == "*":
    answer = c
    print(dic)
    print(f"{num1} * {num2} = {c}")
elif cal == "/":
    answer = d
    print(dic)
    print(f"{num1} / {num2} = {d}")
elif cal == "//":
    answer = e
    print(dic)
    print(f"{num1} // {num2} = {e}")
elif cal == "%":
    answer = f
    print(dic)
    print(f"{num1} % {num2} = {f}")
elif cal == "**":
    answer = g
    print(dic)
    print(f"{num1} ** {num2} = {g}")
else:
    print("지원하지 않는 기호 입니다")

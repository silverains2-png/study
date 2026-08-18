# 문자열을 숫자로 바꾸되, 실패하면 0을 돌려주는 함수를 만드세요.

# (앞뒤 공백은 제거할 것)

# [기대 결과]

#   " 100 "  -> 100

#   "50"     -> 50

#   ""       -> 0

#   "삼십"    -> 0

#   "3.5"    -> 0     (int로 못 바꾸므로)

# 그리고 아래 리스트의 합계를 구하세요. -> 150

# ★★★ 이 함수는 앞으로 계속 씁니다. 잘 만들어 두세요.★★★★

#         "".isdigit()      -> False   (빈 문자열)

#         "100".isdigit()   -> True

#         "삼십".isdigit()   -> False

#         "3.5".isdigit()   -> False   (점은 숫자가 아니므로)


def strint(str):
    str = str.strip()
    if str.isdigit():
        return int(str)
    else:
        return 0


sentence = input("숫자를 입력하세요 : ")

print(f'"{sentence}" -> {strint(sentence)}')

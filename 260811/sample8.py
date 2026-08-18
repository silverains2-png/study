# 아래 세 조건을 각각 함수로 만들고, 그 셋을 합친 함수를 만드세요.

#   is_long_enough(pw)  : 8자 이상인가

#   has_number(pw)      : 숫자가 들어있는가

#   has_letter(pw)      : 영문자가 들어있는가

#   check_password(pw)  : 셋 다 만족하면 "안전",

#                         아니면 부족한 조건을 알려주는 문자열

# [기대 결과]

#   "abc12345"  -> 안전

#   "abc123"    -> 8자 이상이어야 합니다

#   "abcdefgh"  -> 숫자를 포함해야 합니다

#   "12345678"  -> 영문자를 포함해야 합니다

# -------------------------------------------------------------
passwords = ["abc12345", "abc123", "abcdefgh", "12345678"]


def is_long_enough(pw):
    return len(pw) >= 8


def has_number(pw):
    return any(ch.isdigit() for ch in pw)


def has_letter(pw):
    return any(ch.isalpha() for ch in pw)


def check_password(pw):
    if not is_long_enough(pw):
        return "8자 이상이어야 합니다"
    if not has_number(pw):
        return "숫자를 포함해야 합니다"
    if not has_letter(pw):
        return "영문자를 포함해야 합니다"
    return "안전"


for i in passwords:
    print(f"{i} -> {check_password(i)}")

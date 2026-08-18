# 함수 두 개를 만드세요.

#   reverse_text(s)  : 문자열을 뒤집어 돌려준다 ([::-1] 금지! 반복문으로)

#   is_palindrome(s) : 앞뒤가 같은 말인지 판정 (공백 무시, 대소문자 무시)

# [기대 결과]

#   reverse_text("hello")  -> "olleh"      (뒤집기 함수 단독 확인)

#   그리고 아래 words 리스트를 판정하면

#   "level"        -> 회문입니다

#   "기러기"        -> 회문입니다

#   "python"       -> 회문이 아닙니다

#   "Never odd or even" -> 회문입니다

# -------------------------------------------------------------
words = ["level", "기러기", "python", "Never odd or even"]


def reverse_text(s):
    rev = ""
    for i in s:
        rev = i + rev
    return rev


def is_palindrome(s):
    word = ""
    for i in s:
        if i != " ":
            word += i
    word = word.lower()

    return word == reverse_text(word)


print(reverse_text("hello"))

for i in words:
    if is_palindrome(i):
        print(f"{i} -> 회문입니다")
    else:
        print(f"{i} -> 회문이 아닙니다")

# 함수를 만드세요.

#   count_words(text) : 단어별 등장 횟수를 딕셔너리로 돌려준다

#                       (소문자로 통일, 공백으로 구분)

# 그리고 가장 많이 나온 단어를 찾는 함수도 만드세요.

#   most_common(counter) : 가장 많이 나온 단어와 횟수를 함께 반환

#                          (return 단어, 횟수  -> 받을 때 w, c = most_common(...))

# [기대 결과]

#   {'python': 3, 'is': 2, 'fun': 1, 'easy': 1}

#   가장 많이 나온 단어: python (3회)

# -------------------------------------------------------------

text = "Python is fun Python is easy Python"


def count_words(text):
    counter = {}
    text = text.lower()

    for i in text.split():
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1

    return counter


def most_common(counter):
    most_word = ""
    most_count = 0

    for i, j in counter.items():
        if j > most_count:
            most_word = i
            most_count = j

    return most_word, most_count


counter = count_words(text)
print(counter)
answer = most_common(counter)
print(f"가장 많이 나온 단어 : {answer[0]} {answer[1]}회")

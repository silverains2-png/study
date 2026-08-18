# 문장을 받아 공백을 제외한 글자 수를 돌려주는 함수를 만드세요.

#

# [기대 결과]

#   "안녕 하세요"      -> 5

#   "파 이 썬 좋 아"   -> 5

#   "hello world"    -> 10

#

# -------------------------------------------------------------
sentences = ["안녕 하세요", "파 이 썬 좋 아", "hello world"]


def freespace(sentence):
    return len(sentence.replace(" ", ""))


for i in sentences:
    print(f"{i} -> {freespace(i)}")

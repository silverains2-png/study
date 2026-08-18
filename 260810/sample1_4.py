# [문제 4] 단어 개수 세기 (딕셔너리)

# 단어를 계속 입력받아 각 단어가 몇 번 나왔는지 딕셔너리에 저장.

# "end"를 입력하면 종료하고 단어별 등장 횟수를 모두 출력.

# 실행 예시)

#   단어 입력(end: 종료): 사과

#   단어 입력(end: 종료): 바나나

#   단어 입력(end: 종료): 사과

#   단어 입력(end: 종료): end

#   사과: 2번

#   바나나: 1번

word_count = {}

while True:
    fruit = input("단어 입력(end : 종료) : ")

    if fruit == "end":
        break

    if fruit in word_count:
        word_count[fruit] += 1
    else:
        word_count[fruit] = 1

for i, j in word_count.items():
    print(f"{i} : {j}번")

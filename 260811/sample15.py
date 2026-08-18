# 함수 두 개를 만들어 차이를 비교하세요.

#   sort_bad(data)  : 원본 리스트를 직접 정렬 (data.sort())

#   sort_good(data) : 원본은 그대로 두고 정렬된 새 리스트 반환

# [기대 결과]

#   원본: [3, 1, 2]

#   sort_good 결과: [1, 2, 3] / 원본: [3, 1, 2]   <- 원본 유지

#   sort_bad  결과: [1, 2, 3] / 원본: [1, 2, 3]   <- 원본 파괴

# -------------------------------------------------------------
data = [3, 1, 2]


def sort_bad(data):
    data.sort()
    return data


def sort_good(data):
    new_data = []

    for i in data:
        new_data.append(i)

    new_data.sort()

    return new_data


print("원본:", data)

result = sort_good(data)
print("sort_good 결과:", result, "/ 원본:", data)

result = sort_bad(data)
print("sort_bad 결과:", result, "/ 원본:", data)

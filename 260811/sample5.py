# max() 를 쓰지 말고, 리스트에서 가장 큰 값을 찾는 함수를 만드세요.

# 빈 리스트가 들어오면 None 을 돌려주세요.

#

# [기대 결과]

#   [3, 9, 1, 7]  -> 9

#   [-5, -2, -9]  -> -2

#   []            -> None


def find_max(numbers):
    if len(numbers) == 0:
        return None

    numbers.sort()
    max_num = numbers[-1]
    return max_num


print(find_max([3, 9, 1, 7]))
print(find_max([-5, -2, -9]))
print(find_max([]))

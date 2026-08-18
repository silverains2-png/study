sales = [1, 2, 2, 1]

first_sem = sales[: int(len(sales) / 2)]
second_sem = sales[int(len(sales) / 2) :]

print(sum(first_sem), sum(second_sem))

if sum(first_sem) > sum(second_sem):
    print("초반 우세")
elif sum(first_sem) < sum(second_sem):
    print("후반 우세")
else:
    print("동일")

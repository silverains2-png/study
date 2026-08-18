# 함수 두 개를 만드세요.

#   withdraw(balance, amount) : 출금 후 잔액을 돌려준다

#                               잔액보다 많이 출금하려 하면

#                               "잔액 부족" 출력 후 잔액 그대로 반환

#   deposit(balance, amount)  : 입금 후 잔액을 돌려준다

# 잔액 10000원으로 시작해 아래 순서대로 처리하세요.

#   3000원 출금 -> 5000원 입금 -> 20000원 출금(실패)

# [기대 결과]

#   출금 3000 -> 잔액 7000

#   입금 5000 -> 잔액 12000

#   잔액 부족 (요청 20000, 잔액 12000)

#   최종 잔액: 12000

# -------------------------------------------------------------
balance = 10000


def withdraw(balance, amount):
    if balance < amount:
        print(f"잔액 부족 (요청 {amount}, 잔액 {balance})")
    else:
        balance -= amount

    return balance


def deposit(balance, amount):
    balance += amount

    return balance


balance = withdraw(balance, 3000)
print(f"출금 3000 -> 잔액 {balance}")

balance = deposit(balance, 5000)
print(f"입금 5000 -> 잔액 {balance}")

balance = withdraw(balance, 20000)
print(f"최종 잔액: {balance}")

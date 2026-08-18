error_rates = [1.0, 1.2, 0.8, 1.0, 1.0, 0.9, 1.1, 1.0, 0.8, 1.2]

before = error_rates[: int(len(error_rates) / 2)]
after = error_rates[int(len(error_rates) / 2) :]

before_sum = sum(before) / len(before)
after_sum = sum(after) / len(after)

if max(after) > 5:
    print(f"{before_sum:.2f} / {after_sum:.2f} / ROLLBACK")
elif before_sum == 0:
    if after_sum > 0:
        print(f"{before_sum:.2f} / {after_sum:.2f} / HOLD")
    else:
        print(f"{before_sum:.2f} / {after_sum:.2f} / PROMOTE")
elif after_sum >= before_sum * 1.5:
    print(f"{before_sum:.2f} / {after_sum:.2f} / ROLLBACK")
elif after_sum >= before_sum * 1.2:
    print(f"{before_sum:.2f} / {after_sum:.2f} / HOLD")
else:
    print(f"{before_sum:.2f} / {after_sum:.2f} / PROMOTE")

scores = [60, 55, 71]

print(scores)

final_score = sum(scores) / len(scores)

print(f"{final_score:.2f}")

if final_score >= 90:
    print("A")
elif final_score >= 80:
    print("B")
elif final_score >= 70:
    print("C")
else:
    print("D")

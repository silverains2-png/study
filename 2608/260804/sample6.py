year = int(input("연도를 입력하세요 : "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("윤년입니다")
else:
    print("평년입니다")


# if year % 400 == 0:
#     print("윤년입니다")
# elif year % 100 == 0:
#     print("평년입니다")
# elif year % 4 == 0:
#     print("윤년입니다")
# else:
#     print("평년입니다")

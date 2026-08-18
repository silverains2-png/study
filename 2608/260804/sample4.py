user_name = input("아이디를 입력하세요 : ")
user_pass = input("비밀번호를 입력하세요 : ")

if user_name == "admin" and user_pass == "1234":
    print("로그인 성공!")
elif user_name == "admin" and user_pass != "1234":
    print("비밀번호가 틀렸습니다")
else:
    print("존재하지 않는 아이디입니다")

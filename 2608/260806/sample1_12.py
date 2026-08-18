user = input("아이디를 입력하세요 : ")
password = input("비밀번호를 입력하세요 : ")

accounts = {
    "alice": {"pw": "1234", "roles": ["admin", "user"]},
    "bob": {"pw": "abcd", "roles": ["user"]},
}

if user in accounts:
    if password == accounts[user]["pw"]:
        if accounts[user]["roles"][0] == "admin":
            print(f"{user}님 로그인 성공\n")
            print(f"권한 목록 : {accounts[user]['roles']}\n")
            print(f"대표 권한 : {accounts[user]['roles'][0]}\n")
            print("관리자 페이지 접근 가능")
        else:
            print(f"{user}님 로그인 성공")
            print(f"권한 목록 : {accounts[user]['roles']}\n")
            print(f"대표 권한 : {accounts[user]['roles'][0]}\n")
            print("일반 사용자 안내")
    else:
        print("비밀번호 불일치")
else:
    print("없는 아이디")

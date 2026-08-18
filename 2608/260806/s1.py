# ---------------------------------------------------
# 딕셔너리 - 이름표를 붙여 저장
# ---------------------------------------------------

# 리스트의 불편함에서 출발

person = ["김철수", "25", "서울"]
print(person[1])  # 25

person = {"name": "김철수", "age": 25, "city": "서울"}
print(person["age"])  # 25 : "age"를 꺼내옴!

# ---------------------------------------------------
# 만들기와 꺼내기
# ---------------------------------------------------

person = {"name": "김철수", "age": 25}
#           키       값      키    값

print(type(person))  # <class 'dict'>
empty = {}  # 빈 딕셔너리

print(person["name"])  # 김철수 : 인덱스 번호 대신 키값!
# print(person["phone"])  # KeyError : 없는 키 이므로

# 팁 get()을 쓰면 없어도 에러가 안납니다

print(person.get("phone"))  # None : 있는지 없는지 확인용
print(person.get("phone"), "있는지 없는지 확인")  # 어딨는지 바로 확인하기!

# 사용자 입력처럼 뭐가 들어올지 모를 땐 [] 대신 get()을 사용하는게 안전하다

print("name" in person)  # True : 값을 찾는게 아니라 키가 '있는지' 검사
print("김철수" in person)  # False : 키가 아니라 값이므로!

# <키> 는 한글로 지정하지 말기!

# ---------------------------------------------------
# 추가 수정 삭제
# ---------------------------------------------------

person = {"name": "김철수", "age": 25}

person["city"] = "서울"  # 없는 키 -> 추가
person["age"] = 26  # 있는 키 -> 수정

# 추가와 수정의 문법이 같아서, 오타를 내면 조용히 새 키가 생긴다.
person["agee"] = 30  # 에러가 안남! : 찾기 어려운 버그의 원인

del person["agee"]  # agee 삭제
removed = person.pop("city")  # 삭제 하면서 값 받기
print(removed)  # 서울

# ---------------------------------------------------
# 키 값 한꺼번에 다루기
# ---------------------------------------------------

scores = {"국어": 90, "과학": 90, "영어": 85, "음악": 85, "수학": 77}
print(list(scores.keys()))  # ["국어","영어","수학"] : 키만 모아서 리스트로
print(list(scores.values()))  # [90, 85, 77] : 값만 모아서 리스트로

# print(scores.keys(), scores.values())  # dict_kys(["국어", "영어", "수학"]) dict_values([90, 85, 77])
# print(type(scores.keys())) # class 가 dict_keys 로 찍힌다

print(len(scores))  # 3 -> 키:값 세트를 하나로 취급

# values()를 뽑으면 리스트처럼 계산할 수 있다!
avg = sum(scores.values()) / len(scores)
print(avg)

max_num = max(scores.values())
print(max_num)

sort_num = sorted(scores.values())
print(sort_num)

# ---------------------------------------------------
# 키 규칙과 중첩
# ---------------------------------------------------

d = {"문자열": 1, 10: 2, (1, 2): 3}  # 문자열 숫자 튜플은 키 가능
# d = {[1,2]: "값"} X : 리스트는 키로 못 씀
print({"a": 1, "a": 2})  # 키 중복시 나중 것이 이김

# 값에는 뭐든 넣을 수 있다
student = {
    "name": "김철수",
    "scores": [90, 85, 77],  # 값이 리스트
    "address": {"city": "서울", "zip": "1234"},  # 값이 딕셔너리
}
print(student["scores"][0])  # 90
print(student["address"]["city"])  # 서울

# 팁 f-string 안에서는 바깥과 다른 따옴표를 쓰세요
me = {"name": "김철수", "age": 25}
print(f"안녕하세요 제 이름은 {me['name']}이고 나이는 {me['age']}입니다")

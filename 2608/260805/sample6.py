todo = ["운동", "공부", "청소"]

x = "독서"

print(todo)
print(x)

if x in todo:
    if len(todo) == 1:
        todo.remove(x)
        print("할일이 없습니다")
        print(todo)
    else:
        todo.remove(x)
        print("삭제 완료")
        print(todo)
else:
    print("목록에 없습니다")
    print(todo)

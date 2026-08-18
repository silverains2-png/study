# -------------------------------------------------
# 클래스(class) - 데이터와 기능을 하나로 묶기
# -------------------------------------------------


# -------------------------------------------------
# 왜 클래스가 필요한가
# -------------------------------------------------

# 데이터가 함수를 따라다닌다

# 지금까지 배운 방식으로 '은행 계좌' 프로그램을 만들어 봅시다.
# 함수와 딕셔너리만 써서 만들면 이렇게 됩니다


def make_account(owner, balance):
    """계좌를 딕셔너리로 만든다"""
    return {"owner": owner, "balance": balance}


def deposit(account, amount):
    """입금하고 바뀐 계좌를 돌려준다"""
    account["balance"] = account["balance"] + amount
    return account


def withdraw(account, amount):
    """출금하고 바뀐 계좌를 돌려준다"""
    if amount > account["balance"]:
        print("잔액부족")
        return account
    account["balance"] = account["balance"] + amount
    return account


def show(account):
    """계좌 정보를 출력한다"""
    print(f"{account['owner']}님의 잔액 : {account['balance']}원")


# 이제 써 봅시다
acc = make_account("김철수", 10000)
acc = deposit(acc, 5000)
acc = withdraw(acc, 3000)
show(acc)


# deposit(account, amount)
# withdraw(account, amount)
# show(account)

# 모든 함수의 첫 번째 자리에 account가 들어갑니다.
# 함수가 5개면 5개 전부, 10개면 10개 전부
# 데이터(account)와 기능(함수)이 항상 붙어 다니는데
# 따로 떨어져 있으니 매번 같이 넘겨줘야 하는 겁니다.

# 더 큰 문제 - 아무나 값을 바꿀 수 있다
acc2 = make_account("이영희", 10000)
show(acc2)

# withdraw 함수는 잔액을 확인하는데...
acc2["balance"] = -99999  # 함수를 안 거치고 직접 바꿔버림
show(acc2)

# withdraw 함수에 잔액 확인 로직을 넣어놨는데도
# 딕셔너리를 직접 건드리면 아무 소용이 없습니다.
# 실수로 이렇게 쓸 수도 있습니다.
# acc2["balnace"] = 5000 <- 오타! balance 가 아니라 balnace
# -> 에러도 안 나고 새 키가 조용히 추가됩니다

# -------------------------------------------------
# 해결책 - 데이터와 기능을 한 덩어리로
# -------------------------------------------------

# 클래스는 이 문제를 이렇게 해결합니다.
# "계좌라는 게 뭔지 설계도를 만들어 두자.
# 거기에 데이터(주인, 잔액)와 기능(입금, 출금)을 같이 넣자.""
# 그러면 함수를 부를 때 계좌를 매번 넘길 필요가 없습니다.
# 함수가 이미 자기 계좌를 알고 있음


class Account:
    """은행 계좌"""

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("잔액 부족")
            return  # 끝남

        self.balance = self.balance - amount

    def show(self):
        print(f"{self.owner}님의 잔액 : {self.balance:,}원")


# 써보기
my_acc = Account("김철수", 10000)
my_acc.deposit(5000)
my_acc.withdraw(3000)
my_acc.show()

# 계좌를 매번 넘기지 않습니다.
# my_acc 가 이미 자기 데이터를 알고 있기 때문입니다.

# -------------------------------------------------
# 클래스를 언제 쓰냐
# -------------------------------------------------

# 모든걸 클래스로 만들 필요는 없습니다.
# 아래 조건에 해당하면 클래스를 고려하세요.

# 1) 데이터와 기능이 항상 붙어 다닌다
#    계좌 + 입출금, 학생 + 성적계산, 장바구니 + 담기/빼기

# 2) 같은 종류를 여러개 만들어야 한다
#    계좌 100개, 학생 30명

# 3) 값이 계속 변한다 (상태를 가진다)
#    잔액이 늘었다 줄었다, 재고가 들어왔다 나갔다

# 반대로 이럴 땐 함수로 충분합니다
# - 값을 넣으면 결과만 나오는 단순 계산
#   예) 평균 구하기, 부가세 계산, 문자열 뒤집기
# - 한 번 쓰고 마는 작업

# 지금까지 만든 my_tools.py 의 함수들을 보세요.
# to_int, get_average, make_bar
# 이건 클래스로 만들 이유가 없습니다. 값을 넣으면 결과만 나오니까요.


# -------------------------------------------------
# 기본 문법
# -------------------------------------------------

# -------------------------------------------------
# 클래스는 설계도, 객체는 실제 물건
# -------------------------------------------------

# 가장 흔한 비유는 '붕어빵 틀' 입니다.

# 클래스 = 붕어빵 틀 (설계도, 하나만 있으면 됨)
# 객체 = 붕어빵 (틀로 찍어낸 실제 물건, 여러 개 가능)

# 붕어빵 틀 자체를 먹을 수 없죠, 찍어내야 먹을 수 있습니다.
# 클래스도 마찬가지입니다. 만들어서 써야 의미가 있습니다.

# [용어 정리]

# 클래스(class)        - 설계도
# 객체(object)         - 설계도로 만든 실제 물건
# 인스턴스(instance)   - 객체와 거의 같은 말
#                      "Account 클래스의 인스턴스" 처럼 씁니다

# 속성(attribute)      - 객체가 가진 데이터 (owner, balance)
# 메서드(method)       - 객체가 가진 기능 (deposit, withdraw)

# 메서드는 그냥 '클래스 안에 있는 함수' 입니다.
# 이름만 다를 뿐 함수와 같습니다.

# 같은 클래스로 계좌 세 개를 만들어 봅시다

a = Account("김철수", 10000)

b = Account("이영희", 50000)

c = Account("박민수", 3000)

a.deposit(5000)
b.withdraw(20000)

a.show()
b.show()
c.show()

# 세 개가 서로 완전히 독립합니다.
# a의 잔액을 바꿔도 b는 영향을 받지 않습니다.
# 설계도는 하나(account)지만
# 찍어낸 물건은 세 개(a, b, c) 입니다.

# -------------------------------------------------
# __init__ 이란?
# -------------------------------------------------

# __init__ 은 객체를 만들 때 자동으로 실행되는 함수입니다.

# Account("김철수", 10000)
# 이렇게 쓰면 파이썬이 알아서 __init__을 불러줍니다.
# 우리가 직접 부르지 않습니다.

# __init__ 이 하는 일
# 객체가 처음 만들어질 때 필요한 값을 채워 넣습니다.
# "이 계좌의 주인은 김철수, 잔액은 10000원이다" 라고 정하는 것


class Student:
    def __init__(self, name):
        print(f"__init__ 실행됨! {name} 학생을 만듭니다")
        self.name = name
        print(self.name)
        self.scores = []  # 빈 리스르토 시작


print(" s1 = Student('김철수') 실행 전")
s1 = Student("김철수")
print("실행 후\n")

print(" s2 = Student('이영희') 실행 전")
s2 = Student("이영희")
print("실행 후\n")

# -------------------------------------------------
# self 란 무엇인가 ?
# -------------------------------------------------

# 클래스를 배울 때 가장 헷갈리는 부분입니다.
# self는 ' 이 객체 자기 자신'을 가리킵니다.

# [왜 필요한가]
# 계좌가 100개 있다고 칩시다
# deposit 메서드를 부를 때 "어느 계좌에 입금할지" 알아야 합니다.
# a.deposit(5000) -> a에 입금
# b.deposit(5000) -> b에 입금

# 점 앞에 있는게 self!
# a.deposit(5000)을 부르면 self 자리에 a가 들어갑니다.

# [중요 : self는 우리가 넘기지 않습니다]
# def deposit(self, amount) <- 정의할 때 self를 씁니다
# a.deposit(5000) <- 부를 때는 안 씁니다
# 파이썬이 알아서 a를 self 자리에 넣어줍니다
# 그래서 정의할 때는 인자가 2개인데 부를 때는 1개입니다.

# [self.balance 와 balance 의 차이]
# self.balance 이 객체의 잔액 (객체가 계속 기억함)
# balance 그냥 지역변수 (메서드가 끝나면 사라짐)
# 앞서 배운 전역변수와 지역번수 개념이 여기서도 쓰입니다.


class Person:
    def __init__(self, name):
        self.name = name

    def who_am_i(self):
        print(f"self는 지금 {self.name}입니다")

    def compare(self, other):
        """self와 다른 객체를 비교"""
        print(f"나는 {self.name}, 상대는 {other.name}")


p1 = Person("김철수")
p2 = Person("이영희")

p1.who_am_i()  # self 자리에 p1 이 들어감
p2.who_am_i()  # self 자리에 p2 가 들어감

p1.compare(p2)  # self = p1, other = p2


# -------------------------------------------------
# self 를 빼먹으면 생기는 일
# -------------------------------------------------

# 초보자가 가장 많이 하는 실수 두 가지입니다.

# 실수 1) 메서드 정의할 때 self를 빼먹음
# def deposit(amount)  <- self 가 없음
# -> TypeError

# 실수 2) 속성 앞에 self 를 안붙임
# def __init__(self, owner):
#     owner = owner  <- self. 이 없음
# -> 지역변수만 만들고 사라짐, 객체에 저장이 안됨


class Wrong:
    def __init__(self, value):
        value = value


class Right:
    def __init__(self, value):
        self.value = value


w = Wrong(100)
r = Right(100)

try:
    print("Wrong 객체의 value", w.value)
except AttributeError as e:
    print("Wrong 객체의 value : 에러 발생")
    print(" ->", e)
    print(" -> self. 을 빼먹으면 객체에 저장되지 않습니다.")

print("Right 객체의 value : ", r.value)


# -------------------------------------------------
# 메서드는 클래스 안의 함수
# -------------------------------------------------

# 메서드도 함수와 똑같습니다.
# - 인자를 받을 수 있고
# - return 으로 값을 돌려줄 수 있고
# - 기본값도 쓸 수 있습니다

# 다른 점은 첫 번째 인자가 self 라는 것 뿐입니다.


class ScoreBook:
    """학생 한 명의 성적을 관리한다"""

    def __init__(self, name):
        self.name = name
        self.scores = []  # 빈 리스트 시작

    def add(self, score):
        """점수를 추가 한다 (돌려주는 값 없음)"""
        self.scores.append(score)

    def avg(self):
        """평균을 계산해서 돌려준다"""
        if not self.scores:  # 빈 리스트면 0을 돌려줌
            return 0
        return round(sum(self.scores) / len(self.scores), 1)

    def grade(self):
        """등급을 돌려준다"""
        avg = self.avg()  # 다른 메서드를 부를 때도 self.
        if avg >= 90:
            return "A"
        if avg >= 80:
            return "B"
        if avg >= 70:
            return "C"
        return "D"

    def report(self, show_scores=True):
        """성적표를 출력한다 (기본값 인자사용)"""
        print(f"{self.name} 평균: {self.avg()} 등급: {self.grade()}")
        if show_scores:
            print(f"점수 : {self.scores}")


book = ScoreBook("김철수")
book.add(90)
book.add(85)
book.add(100)
book.report()

book2 = ScoreBook("이영희")
book2.add(70)
book2.add(75)
book2.report(show_scores=False)


# -------------------------------------------------
# 속성은 나중에 바뀔 수 있다
# -------------------------------------------------

# 객체가 가진 값(속성)은 계속 바뀝니다.
# 이걸 '상태를 가진다' 고 표현합니다.

# 함수는 부르고 나면 아무것도 남지 않지만,
# 객체는 값을 계속 기억합니다. 이게 가장 큰 차이


class Counter:
    """숫자를 세는 도구"""

    def __init__(self):
        self.count = 0  # 인자없이 0 부터 시작

    def up(self):
        self.count = self.count + 1

    def down(self):
        self.count = self.count - 1

    def reset(self):
        self.count = 0


c1 = Counter()
c2 = Counter()

c1.up()
c1.up()
c1.up()
c2.up()

print("c1 의 count : ", c1.count)
print("c2 의 coutn : ", c2.count)

c1.reset()
print("c1 초기화 후 : ", c1.count)
print("c2 는 그대로 : ", c2.count)

# 전역변수를 배울 때 이런 코드를 봤습니다.

# count = 0
# def visit(count):
#     return count + 1

# count = visit(count)  <- 매번 주고 받아야 함
# 클래스를 쓰면 객체가 알아서 기억합니다.

# c = Counter()
# c.up()  <- 애초에 넘길 필요가 없음


# -------------------------------------------------
# 속성에 직접 접근하기
# -------------------------------------------------

# 객체의 속성은 점(.)으로 읽고 쓸 수 있습니다.

# 읽기 : print(acc.balance)
# 쓰기 : acc.balance = 5000

# 다만 쓰기는 조심해야 합니다.
# 메서드를 거치지 않으면 검증 로직을 건너뛰게 됨

acc = Account("최지은", 10000)
print("읽기 ", acc.owner, "/", acc.balance)

# 메서드를 통한 출금 (검증됨)
acc.withdraw(50000)  # 잔액 부족 매세지가 나옴

# 직접 수정 (검증 안 됨)
acc.balance = -9999
print("직접 바꾼 뒤 : ", acc.balance)

""" 파이썬은 속성을 완전히 숨기는 기능이 없습니다.
    대신 관례가 있습니다.
    self.balance 누구나 써도 되는 값
    self._balance "내부용이니 건드리지 마세요" 라는 표시
                  언더바 하나를 앞에 붙입니다
    밑줄이 있어도 기술적으로는 접근 됩니다.
    약속일 뿐입니다. 하지만 지키는게 좋습니다
"""

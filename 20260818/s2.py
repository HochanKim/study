# # -------------------------------------------------------------
# # 클래스(class)
# # -------------------------------------------------------------

# # 클래스가 필요한 이유?
# # => 데이터가 함수를 따라다닌다

# # 지금까지 배운 방식으로 '은행 계좌'를 만들어보자면
# # 함수와 딕셔너리만 써서 만들면 이렇게 구성한다

# def make_account(owner, balance):
#     return {"owner": owner, "balance": balance}

# def deposit(account, amount):
#     account["balance"] = account["balance"] + amount
#     return account

# def withdraw(account, amount):
#     if amount > account["balance"]:
#         print("잔액 부족")
#         return account
#     account["balance"] = account["balance"] - amount
#     return account

# def show(account):
#     print(f"{account['owner']}님의 잔액: {account['balance']:,}원")

# acc = make_account("김철수", 500000)
# acc = deposit(acc, 500000)
# acc = withdraw(acc, 100000)
# show(acc)

# # => 모든 함수의 첫 번째 자리에 account가 들어간다
# # => 함수가 5개면 5개 전부, 10개면 10개 전부, n개면 n개 전부
# # => 데이터(함수 account)와 기능(함수)이 항상 붙어 다니는데
# # => 따로 떨어져 있으니 매번 같이 넘겨줘야 한다

# # 더 큰 문제 - 아무나 값을 바꿀 수 있다
# acc2 = make_account("이영희", 1000000)
# show(acc2)

# # withdraw 함수는 잔액을 확인하는데
# acc2["balance"] = -99999
# show(acc2)
# # => withdraw 함수에 잔액 확인 로직을 넣었는데도 
# # 딕셔너리를 직접 건드리면 아무 소용이 없다
# # 실수로 이렇게 쓸 수도 있다
# # => acc2["balnace"] = 5000 <- 오타를 기입한 경우
# # ====> 에러가 나지 않고 새 키로 조용히 추가된다
# # 
# # -------------------------------------------------------------
# # 해결책 - 데이터와 기능을 한 덩어리로
# # -------------------------------------------------------------
# # => '클래스(class)'를 사용하면 이런 문제를 해결할 수 있다



# 클래스를 언제 쓰나?
# 1) 데이터와 기능이 항상 붙어 다닌다
#     => 계좌 + 입출금, 학생 + 성적 계산, 장바구니 + 담기/빼기 등

# 2) 같은 종류를 여러개 만들어야 한다 (객체 생성)
#     => 계좌 100개, 학생 30명 등등

# 3) 값이 계속 변한다 (상태를 가진다)
#     => 잔액이 늘었다 줄었다, 재고가 들어왔다 나갔다 등

# 반대로 이럴 땐 함수도 충분하다
# ! 값을 넣으면 결과만 나오는 단순 계산
#   => 예) 평균 구하기, 부가세 계산, 문자열 뒤집기
# ! 한 번 쓰고 마는 작업


# -------------------------------------------------------------
# 기본 문법
# -------------------------------------------------------------


# -------------------------------------------------------------
# 클래스는 설계도, 객체는 실제 물건
# -------------------------------------------------------------
# => 클래스는 1개만 있어도 여러개의 객체를 찍어낼 수 있다

# ※ [용어 정리]

# - 클래스(class) - 설계도
# - 객체(object)  - 설계도로 만든 실제 물건
# - 인스턴스(instance)  - 객체와 거의 같은 말
# - 속성(attribute) - 객체가 가진 데이터 (ex. owner, balance)
# - 매서드(method)  - 객체가 가진 기능  (ex. deposit, withdraw)
#   => 메서드는 그냥 '클래스 안에 있는 함수'
#   => 이름만 다를 뿐 함수(def)와 같음

#   ====> 클래스로 생성된 각 객체들은 서로 완전히 독립적이다
#   ====> 설계도는 하나지만(class), 객체는 여러개 생성 가능 (a, b, c, ...)

# # '__init__'이란?
# # => 객체를 만들 때 자동으로 실행되는 함수

# # Account("김철수", 10000)
# # 이렇게 쓰면 파이썬이 알아서 __init__을 호출

# # '__init__'이 하는 일
# # 객체가 처음 만들어질 때 필요한 값을 채워 넣는다

# class Student:
#     def __init__(self, name):
#         print(f"__init__ 실행됨! {name} 학생을 만듭니다")

#         # 클래스 내 세팅
#         self.name = name
#         print(f"{self.name} 생성 완료")
#         self.scores = []  # 빈 리스트

# print("s1 = Student('김철수') 실행 전")
# s1 = Student("김철수")
# print("실행 후\n")

# print("s1 = Student('이영희') 실행 전")
# s1 = Student("이영희")
# print("실행 후\n")

# # self란 무엇인가?
# # self는 "생성 객체" 자신을 가리킴

# # 각 객체들이 작업을 시행할 때
# # a.deposit(5000) -> a에 입금
# # b.deposit(5000) -> b에 입금
# # ==> 점 앞에 a, b 등의 객체명들이 바로 'self'이다

# # 'self'는 파라미터로 넘기는 값이 아니다
# # ==> def deposit(self, amount): 정의할 때 self를 사용
# # ==> 파이썬이 알아서 'a'를 self 자리에 넣는다
# # ※ 그래서 정의할 때는 인자가 2개이지만 부를 때는 1개만

# # [self.balance]와 balance의 차이
# # => self.balance: 이 객체의 잔액 (객체가 계속 기억함) 
# # balance는 그냥 지역 변수 (메서드가 끝나면 사라짐)

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def who_am_i(self):
#         print(f"self는 지금 {self.name}입니다.")

#     def compare(self, other):
#         # 'self'는 '객체명.function()'에서 
#         # '객체명'을 매개변수로 받는다 
#         print(f"나는 {self.name}, 상대는 {other.name}")

    
# p1 = Person("김철수")
# p2 = Person("이영희")

# p1.who_am_i()
# p2.who_am_i()

# p1.compare(p2)

# self가 없으면 생기는 일

# 실수 1) 메서드 정의할 때 self를 빼먹음
# ex. def get_v(value) <- self를 제외하면 'TypeError'가 발생

# 실수 2) 속성 앞에 self를 안붙임
# ex. def __init__(sefl, owner):
#   owner = owner  # 'self.'가 없음
# => 지역변수만 만들고 사라지고 객체에 저장이 안된다

# # 메서드는 클래스 안의 함수

# # 메서드(method) == 함수(def)
# # - 인자를 받을 수 있고
# # - return으로 값을 돌려줄 수 있고
# # - 기본값도 쓸 수 있다
# # ==> 차이점은 인자를 'self'로 받을 수 있다는 것

# class ScoreBook:
#     # 학생 성적 관리
#     def __init__(self, name):
#         self.name = name
#         self.scores = []

#     def add(self, score):
#         # 점수 추가
#         self.scores.append(score)

#     def avg(self):
#         # 평균 계산
#         if not self.scores:
#             return 0
#         return round(sum(self.scores) / len(self.scores), 1)

#     def grade(self):
#         # 등급
#         # 다른 메서드를 부를 때도 self 사용
#         avg = self.avg()
#         if avg >= 90:
#             return "A"
#         elif avg >= 80:
#             return "B"
#         elif avg >= 70:
#             return "C"
#         else:
#             return "D"

#     def report(self, show_scores=True):
#         # 성적표 출력
#         print(f"{self.name} 평균: {self.avg()} 등급: {self.grade()}")
#         if show_scores:
#             print(f"점수: {self.scores}")

# book = ScoreBook("김철수")
# book.add(90)
# book.add(85)
# book.add(100)
# book.report()

# book = ScoreBook("이영희")
# book.add(80)
# book.add(75)
# book.report(show_scores=False)

# -----------------------------
# 속성은 나중에 바뀔 수 있다
# -----------------------------

# 객체가 가진 값(속성)은 계속 바뀐다
# => 이걸 '상태가 가진다'라고 표현

# 함수는 부르고 나면 아무것도 남지 않지만
# 객체는 값을 계속 기억한다 => 이게 가장 큰 차이

class Counter:  # 숫자 세는 도구
    def __init__(self):
        self.count = 0

    def up(self):
        self.count += 1

    def down(self):
        self.count -= 1

    def reset(self):
        self.count = 0

c1 = Counter()
c2 = Counter()

c1.up()
c1.up()
c1.up()

c2.up()

print("c1의 count:", c1.count)
print("c2의 count:", c2.count)

c1.reset()
print("c1의 초기화 후:", c1.count)
print("c2의 카운트는?:", c2.count)

# 속성에 직접 접근하기

# 객체의 속성은 점(.)으로 읽고 쓸 수 있다
# => 읽기: print(acc.balance)
# => 쓰기: acc.balance = 5000

# 쓰기할 때 주의할 점: 메서드를 거치지 않으면 검증 로직을 건너뛰게 됨

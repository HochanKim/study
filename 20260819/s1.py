# -------------------------------------------------------------
# 클래스 상속
# -------------------------------------------------------------

# 이미 만들어 둔 클래스를 '물려받아' 새 클래스를 생성하는 것 
# => 부모의 속성과 매서드를 그대로 물려받고 필요한 것만 추가하거나 바꾸기

# 상속을 사용하는 이유
# => 비슷한 클래스를 여러 개 만들 때 중복을 없앨 수 있다 
# ex) 입출금 계좌, 적금 계좌, 마이너스 통장 등등
# => 입출금 조회, 계좌 현황 등은 똑같지만 계좌의 이율, 출금 한도는 다를 수 있다

class Account:
  # 은행 계좌 클래스
  def __init__(self, owner, balance):
    self.owner = owner
    self.balance = balance

  def deposit(self, amount):
    # 입금 함수
    self.balance += amount

  def withdraw(self, amount):
    # 출금 함수
    if amount > self.balance:
      print("잔액 부족")
      return
    self.balance -= amount

  def show(self):
    # 조회 함수
    print(f"{self.owner}님의 잔액: {self.balance:,}원")


# Account 상속
class SavingAccount(Account):
  # 저축 계좌 클래스 (상속)
  def __init__(self, owner, balance, rate):
    # 부모 클래스의 '__init__' 먼저 시행
    # 'rate' => 이자를 붙인다
    super().__init__(owner, balance)
    # 저축 계좌만의 속성 추가
    self.rate = rate # 이자율

  def add_interest(self):
    """이자를 붙인다"""
    interest = int(self.balance * self.rate)
    self.balance = self.balance + interest
    print(f"이자 {interest:,}원이 붙었습니다")


sa = SavingAccount("김철수", 100000, 0.03)  # 객체 저장

sa.deposit(50000) # 클래스 Account에서 물려받은 메서드
sa.add_interest() # SavingAccount 만의 메서드
sa.show()
print()

# 상속 클래스 SavingAccount는 'deposit'과 'show'를 안만들었지만 
# 상위 클래스(Account)에 '상속'을 받아 사용이 가능
# 'super().__init__(owner, balance)'에서 
# 'super()'는 상위 클래스를 뜻한다


# 메서드 덮어쓰기 (Overriding)
# => 물려받은 메서드를 그대로 쓰지 않고 
#   자식 클래스에서 다시 정의하면 그게 우선한다.

# 이걸 '오버라이딩'이라고 가리킨다 => '덮어쓰기'로 생각하면 된다

class CreditAccount(Account):
  # 마이너스 통장 클래스 (상속)
  def __init__(self, owner, balance, limit):
    super().__init__(owner, balance)
    self.limit = limit  # 마이너스 한도

  def withdraw(self, amount):
    # 잔액 + 한도까지 출금 가능
    # 해당 함수 오버라이딩 01
    if amount > self.balance + self.limit:
      print(f"한도 초과 (최대 {self.balance + self.limit:,}원 가능)")
      return
    self.balance -= amount

  def show(self):
    # 해당 함수 오버라이딩 02 (출력을 다르게)
    if self.balance < 0:
      print(f"{self.owner}님의 잔액: {self.balance:,}원 (마이너스)")
    else:
      print(f"{self.owner}님의 잔액: {self.balance:,}원")

# ca = CreditAccount("이영희", 100000, 500000)

# ca.withdraw(300000)
# ca.show()

# ca.withdraw(1000000)


# 같은 이름, 다른 동작
# => 상속의 진짜 장점은 여기서 나온다, 각자 자기 방식대로 동작

accounts = {
  Account("김철수", 500000),
  SavingAccount("이영희", 100000, 0.03),
  CreditAccount("박민수", 10000, 1000000),
}

# print("전체 계좌 현황")
# for account in accounts:
#     account.show() # 각자 방식으로 출력

# print("\n [모두 20,000원씩 출금 시도]")
# for account in accounts:
#   account.withdraw(20000)
#   account.show()

# 이미 쓰고 있던 객체들
# text = "hello world"
# print("  문자열 객체:", type(text).__name__)
# print("    text.upper()      =", text.upper())
# print("    text.split()      =", text.split())
# print("    text.replace()    =", text.replace("world", "python"))

# nums = [3, 1, 2]
# print("\n  리스트 객체:", type(nums).__name__)

# nums.append(4)
# print("    append 후         =", nums)

# nums.sort()
# print("    sort 후           =", nums)

# info = {"name": "김철수"}
# print("\n  딕셔너리 객체:", type(info).__name__)
# print("    info.get('name')  =", info.get("name"))
# print("    info.keys()       =", list(info.keys()))

# 전부 '객체.메서드()' 형태입니다.
# 누군가 str 클래스, list 클래스를 만들어 뒀고
# 우리는 그걸 가져다 쓰고 있었던 겁니다.


# -------------------------------------------------------------
# 처음 보는 객체를 탐색하는 법
# -------------------------------------------------------------

# 예시) df = pd.read.csv
# df.head()
# df.groupby("부서").mean()

# 'df'가 뭐지?
# => type(df) // 무슨 클래스인지
# => dir(df)  // 뭘 할 수 있는지
# => help(df.head)  // 특정 메서드 설명

# sa = SavingAccount("최지은", 100000, 0.05)
# print("이게 뭐지? type(sa):", type(sa).__name__)

# print("\n 뭘 할 수 있는거지??? dir(sa)")
# method = []
# for name in dir(sa):
#     if not name.startswith("_"):
#       method.append(name)
# print("=>", method)

# print("클래스 내 'add_interest' 함수의 기능 =>", SavingAccount.add_interest.__doc__)


# 클래스를 안 만들어도 쓸 수 있다?

# pandas나 numpy를 쓸 때
# => 클래스를 직접 만들지 않고 '쓰기만'하면 된다

# df = pd.read.csv  ## 남이 만든 클래스로 객체 생성
# df.head() <= 남이 만든 매서드 사용
# => 그래서 클래스를 직접 못 만들어도 'pandas'는 쓸 수 있다


# -------------------------------------------------------------
# 속성과 매서드 구분하기
# -------------------------------------------------------------

# ja = SavingAccount("정하늘", 500000, 0.02)

# # # 속성은 괄호없이
# # print("속성 => '()'없이")
# # print("ja.owner =>", ja.owner)
# # print("ja.balance =>", ja.balance)
# # print("ja.rate =>", ja.rate)

# # 메서드는 괄호를 붙여서 실행
# print("\n메서드 => '()'붙이기 (= 함수)")
# ja.show()


# -------------------------------------------------------------
# 객체지향과 캡슐화
# -------------------------------------------------------------

# 절차지향?
# => "무엇을 할 것인가"를 중심으로 나눈다
# => 기능(함수) 단위로 쪼갠다
# => 데이터 따로, 기능 따로

# 객체지향?
# ==> "무엇이 있는가"를 중심으로 나눈다
# ==> 대상(객체) 단위로 쪼갠다
# ==> 데이터와 기능이 한 덩어리

# 어느게 더 좋은가?
# -> 상황에 따라 사용하는 것이 좋다

# my_tools.py의 to_int, get_average 같은 것은 객체가 필요 없다

# 계좌 100개 생성, 학생 30명 정보 등록 등등
# 각자 다른 상태를 가진 것을 여러 개 만들 때는 객체지향이 낫다


# [객체지향의 네 가지 특징]
# => 캡슐화: 데이터를 안전하게 감싸기
# => 상속: 기존 것을 물려 받기
# => 다형성: 같은 이름, 다른 동작
# => 추상화: 복잡한 것을 단순하게 보여주기


# -------------------------------------------------------------
# 캡슐화는 왜 필요한가?
# -------------------------------------------------------------

# 캡슐로 감싸듯 데이터를 안에 넣고 정해진 통로(메서드)로만 접근하게 하는 것

# 약통을 생각하면 된다, 알약을 손으로 아무 데나 담지 않고 캡슐에 넣듯이
# 꺼내려면 정해진 방법으로 꺼내야 한다

# 파이썬에는 속성을 완전히 숨기는 기능이 없지만
# 관례가 있다

# self.balance => 누구나 써도 되는 값
# self._balance => "내부용이니 건드리지 마세요"라는 표시

# 단순한 밑줄 하나는 '기술적으로' 접근이 가능하지만, 개발자끼리의 약속으로 건드리지 않는다
# 대신 값을 읽고 메서드는 따로 만들어준다

# class SafeAccount:

#   def __init__(self, owner, balance):
#     self.owner = owner
#     self._balance = balance # 밑줄 하나

#   def get_balance(self):
#     return self._balance

#   def deposit(self, amount):
#     if amount <= 0:
#       print("입금액은 0보다 커야 한다")
#       return
#     self._balance += amount

#   def withdraw(self, amount):
#     if amount > self._balance:
#       print("잔액 부족")
#     self._balance -= amount

# sa1 = SafeAccount("이영희", 10000)

# sa1.deposit(5000)
# print("입금 후 잔액:", sa1.get_balance())

# sa1.deposit(-3000)
# print("음수 입금 시도:", sa1.get_balance())

# sa1.withdraw(50000)
# print("초과 출금 시도:", sa1.get_balance())

# # 밑줄 하나가 기술적으로 막는 것은 불가능
# sa1._balance = -999
# print("직접 건드리기:", sa1.get_balance())


class SafeAccount2:
  # 캡슐화 2단계 - 밑줄 추가
  def __init__(self, owner, balacne):
    self.owner = owner
    self.__balance = balacne # 밑줄 하나

  def get_balance(self):
    return self.__balance

  def deposit(self, amount):
    if amount <= 0:
      print("입금액은 0보다 커야 한다")
      return
    self.__balance += amount

  def withdraw(self, amount):
    if amount > self.__balance:
      print("잔액 부족")
      return
    self.__balance -= amount

# sa2 = SafeAccount2("박민수", 10000)
# sa2.deposit(5000)
# print("정상 입금 후:", sa2.get_balance())

# try:
#   print(sa2.__balance)
# except AttributeError as e:
#   print("직접 접근 시도 -> 에러 발생")
#   print("=>", e)

# # 이렇게 해도 원래 값은 바뀌지 않는다
# sa2.__balance = -999
# print("강제로 대입 시도 =>", sa2.get_balance())

# => 이것이 완전한 보안 장치는 아니다
#   방법을 알면 우회할 수 있다

# property - 메서드를 속성처럼 쓰기

# get_balance()처럼 메서드를 부르는 게 번거로울 수 있다
# @property를 쓰면 메서드를 속성처럼 쓸 수 있다

# '@'로 시작하는 것을 데코레이터라고 한다
# => "함수 위에 붙여서 성질을 바꾸는 표시"


class SafeAccount3:
  # 캡슐화 3단계 - @property 사용
  def __init__(self, owner, balacne):
    self.owner = owner
    self._balance = balacne # 밑줄 하나

  @property
  def balance(self):
    # 읽을 때 실행된다 (괄호 없이)
    return self._balance

  @balance.setter
  def balance(self, value):
    """쓸 때 실행된다. 여기서 검증이 가능"""
    if value < 0:
      print("잔액은 음수가 될 수 없다")
    self._balance = value

  def deposit(self, amount):
    self.balance = self.balance + amount  # setter를 거침

  def withdraw(self, amount):
    self.balance = self.balance - amount  # setter가 음수를 막아줌

# sa3 = SafeAccount3("누군가", 10000)
# print("잔액 읽기 (괄호 없이):", sa3.balance)

# sa3.deposit(5000)
# print("입금 후:", sa3.balance)

# sa3.withdraw(50000)
# print("초과 출금 시도 후:", sa3.balance)  # setter가 막아줌

# sa3.balance = -1000
# print("음수 직접 대입 후:", sa3.balance)


# -------------------------------------------------------------
# 추상화 - 복잡한 것을 단순하게 표현
# -------------------------------------------------------------

# 추상화는 "내부가 어떻게 돌아가는지 몰라도 쓸 수 있게" 하는 것
# 만든 클래스도 마찬가지로
# => 'acc.deposit(5000)'을 쓰는 사람은 안에서 어떤 검증을 하는지 몰라도 된다

class Coffee:
  # 커피 머신 클래스, 쓰는 사람은 make()만 알면 된다
  def __init__(self):
    self._water = 1000 # 물 (ml)
    self._beans = 200 # 원두 (g)

  def _heat_water(self):
    # 내부 동작 1 - 물 끓이기
    return "물을 90도로 데움"
  
  def _grind_beans(self):
    # 내부 동작 2 - 원두 갈기
    return "원두를 곱게 갈음"

  def _extract(self):
    # 내부 동작 3 - 추출
    return "9기압으로 추출"
  
  def make(self):
    # 최종 - 커피 제작
    steps = [self._heat_water(), self._grind_beans(), self._extract()]
    self._water = self._water - 150
    self._beans = self._beans - 18
    return steps

machine = Coffee()

print("실제로 안에서 일어난 일")
for step in machine.make():
  print("->", step)


# """ 객체 지향의 네 가지 특징

#     [캡슐화]
#     데이터를 안에 감추고 정해진 통로로만 접근하게 한다
#     _balance, __balance, @property
#     -> 아무나 값을 망가뜨리지 못하게 막는다

#     [상속]
#     기존 클래스의 기능을 물려받아 새 클래스를 만든다
#     class SavingAccount(Account)
#     -> 중복을 없애고 확장하기 쉽게 만든다

#     [다형성]
#     같은 이름의 메서드가 클래스마다 다르게 동작한다
#     account.withdrow()가 계좌 종류마다 다름
#     -> 여러 종류를 같은 코드로 다룰 수 있다

#     [추상화]
#     복작한 내부를 숨기고 필요한 것만 보여준다
#     machine.make() 한 줄이면 커피가 나온다
#     -> 쓰는 사람이 편해진다

#     용어를 외우려 하지 마세요,
#     각각이 어떤 문제를 해결하는지만 기억하면 됩니다.
#     코드를 짜다 보면 자연스럽게 쓰게 됩니다.
# """
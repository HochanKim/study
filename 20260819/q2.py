# # =============================================================
# # [문제 1] 강아지
# # =============================================================

# class Dog:
#   # 클래스 생성
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#     self.count = 0

#   def bark(self):
#     print(f"멍멍! 나는 {self.name}야")

#   def eat(self, count):
#     self.count += count
#     # 간식을 count 개 먹는다
#     print(f"초코가 간식 {count}개를 먹었다 (총 {self.count}개)")

#   def birthday(self):
#     self.age += 1
#     print(f"{self.name}의 생일! 이제 {self.age}살")

#   def is_puppy(self):
#     if self.age <= 2:  # noqa: SIM103
#       return True
#     return False
  
#   def show(self):
#     if self.is_puppy() == True:
#       print(f"{self.name} ({self.age}살, 강아지) 간식 {self.count}개")
#     else :
#       print(f"{self.name} ({self.age}살, 성견) 간식 {self.count}개")
    

# d1 = Dog("초코", 3)
# d1.show()
# d1.bark()
# d1.eat(2)
# d1.eat(3)
# d1.birthday()
# d1.show()

# print()

# d2 = Dog("콩이", 1)
# d2.show()
# print("콩이는 강아지인가?", d2.is_puppy())

# =============================================================
# [문제 2] 성적표
# =============================================================

# class Report:
#   def __init__(self, name):
#     self.name = name
#     # 과목들을 담을 빈 딕셔너리
#     self.subject_dict = {}
#     # 평균값 계산을 위한 합계 변수
#     self.sum_score = 0
#     # 과목 점수
#     self.score = 0
#     # 최고점 과목
#     self.high_subject = ""

#   def add(self, subject, score):
#     if 0 <= score <= 100:
#       # 딕셔너리에 과목명과 점수 넣기
#       self.subject_dict[subject] = score
#       print(f"{subject} {score}점 등록")
#       print(self.subject_dict)
#     else :
#       print(f"잘못된 점수: {score}")
  
#   def average(self):
#     try:
#       for sc in self.subject_dict:
#         self.sum_score += self.subject_dict.get(sc)
#       self.avg = round(self.sum_score / len(self.subject_dict), 1)
#       return self.avg
#     except ZeroDivisionError:
#       if len(self.subject_dict) == 0:
#         return 0
      
  
#   def grade(self):
#     try:
#       if self.avg >= 90:
#         return "A"
#       elif self.avg >= 80:
#         return "B"
#       elif self.avg >= 70:
#         return "C"
#       else:
#         return "D"
#     except AttributeError:
#       return "D"

  
#   def best(self):
#     for sc in self.subject_ls:
#       self.score = max(self.score, self.subject_dict.get(sc))
#       self.high_subject = sc
#       if len(self.subject_dict) == 0:
#         return None  # noqa: RET501
  
#   def show(self):
#     print(f"[{self.name} 성적표]")
#     for sc in self.subject_dict:
#       print(f"{sc} {self.subject_dict.get(sc)}점")
#     print(f"평균 {self.average()} ({self.grade()})")
#     for high in self.subject_dict:
#       if self.score < self.subject_dict.get(high):
#         self.score = self.subject_dict.get(high)
#         self.high_subject = high
#     if self.high_subject == "":
#       print("최고 과목: 없음")
#     else:        
#       print(f"최고 과목: {self.high_subject} {self.score}점")


# r = Report("김철수")
# r.add("국어", 90)
# r.add("영어", 85)
# r.add("과학", 150)
# r.add("수학", 100)
# r.show()

# print()

# r2 = Report("이영희")
# r2.show()


# =============================================================
# [문제 3] 자판기
# =============================================================

# class VendingMachine:
#   def __init__(self):
#     # 투입 금액
#     self.input_money = 0
#     # 판매할 음료 리스트
#     self.drink = {
#       "콜라": [1500, 3],
#       "사이다": [1300, 2],
#       "물": [800, 5],
#     }

#   def insert(self, money):
#     self.input_money += money
#     print(f"{money:,}원 투입 (총 {self.input_money:,}원)")
  
#   def buy(self, name):
#     if self.drink.get(name) == None:
#       print(f"그런 음료는 없습니다: {name}")
#       return
#     elif self.drink.get(name)[1] == 0:
#       print(f"품절입니다: {name}")
#     elif self.input_money < self.drink.get(name)[0]:
#       print(f"금액이 부족합니다. (부족액 {self.drink.get(name)[0] - self.input_money}원)")
#       return
#     else:
#       print(f"{name} 나왔습니다 (거스름돈 {self.input_money - self.drink.get(name)[0]}원)")
#       self.drink[name][1] -= 1
#       self.input_money = 0

#   def show(self):
#     print("[자판기]")
#     for p in self.drink:
#       print(f"{p} {self.drink.get(p)[0]}원 (재고 {self.drink.get(p)[1]}개)")
#     print(f"투입 금액 {self.input_money}원")

# v = VendingMachine()
# v.show()
# v.insert(1000)
# v.buy("콜라")
# v.insert(1000)
# v.buy("콜라")
# v.buy("커피")
# v.show()


# =============================================================
# [문제 4] 도서 대출
# =============================================================

# class Book:
#   def __init__(self, title, author):
#     self.title = title
#     self.author = author
#     #   대출 상태 (처음에는 대출 가능)
#     self.rented = "대출 가능"
#     #   빌린 사람 이름 (처음에는 없음)
#     self.rent_person = ""
#     #   총 대출 횟수 (처음에는 0)
#     self.rent_cnt = 0
    

#   def borrow(self, who):
#     if self.rent_person == "":
#       self.rent_person = who
#       print(f"{self.title} 대출 완료 (대출자: {self.rent_person})")
#       self.rented = "대출 불가"
#       self.rent_cnt += 1
#     else:
#       print(f"이미 대출 중입니다 (대출자: {self.rent_person})")
  
#   def give_back(self):
#     if self.rented == "대출 가능":
#       print("대출 중이 아닙니다")
#     else:
#       print(f"{self.title} 반납 완료 (반납자: {self.rent_person})")
#       self.rented = "대출 가능"
#       self.rent_person = ""

#   def show(self):
#     if self.rented == "대출 불가":
#       print(f"{self.title} / {self.author} / 대출 중 ({self.rent_person}) / 누적 {self.rent_cnt}회")
#     elif self.rented == "대출 가능":
#       print(f"{self.title} / {self.author} / 대출 가능 / 누적 {self.rent_cnt}회")

# b = Book("사피엔스", "유발 하라리")
# b.show()
# b.give_back()
# b.borrow("김철수")
# b.show()
# b.borrow("이영희")
# b.give_back()
# b.borrow("박민수")
# b.show()

# =============================================================
# [문제 5] 직원과 관리자 (상속)
# =============================================================


# class Employee:
#   def __init__(self, name, base_pay, years):
#     self.name = name
#     self.base_pay = base_pay
#     self.years = years
    
#   def get_position(self):
#     return "사원"
  
#   def get_bonus_rate(self):
#     return 0.1
  
#   def get_bonus(self):
#     self.bonus = int((self.base_pay * self.get_bonus_rate()) + (self.years * 100000))
#     return self.bonus

#   def get_total(self):
#     return self.base_pay + self.get_bonus()

#   def show(self):
#     print(
#       f"{self.name} ({self.get_position()}, {self.years}년) 기본급 {self.base_pay:,}원 보너스 {self.get_bonus():,}원 실수령 {self.get_total():,}원"
#     )


# class Manager(Employee):
#   def __init__(self, name, base_pay, years):
#     super().__init__(name, base_pay, years)

#   def get_position(self):
#     return "팀장"

#   def get_bonus_rate(self):
#     return 0.3
      

# e1 = Employee("김철수", 3000000, 3)
# e1.show()

# m1 = Manager("이영희", 3000000, 7)
# m1.show()

# print()
# print("[전체 명단]")
# staff = [e1, m1, Employee("박민수", 2500000, 1)]

# total = 0
# best = staff[0]
# for s in staff:
#     s.show()
#     total = total + s.get_total()
#     if s.get_total() > best.get_total():
#         best = s

# print(f"총 인건비: {total:,}원")
# print(f"최고 실수령: {best.name}")


# # =============================================================
# # [문제 6] 계좌와 저축계좌 (상속 + 캡슐화)
# # =============================================================

# class Account:
#     def __init__(self, owner, balance):
#         self._owner = owner
#         self._balance = balance
#         self._trade = []

#     # 잔액 조회
#     def get_balance(self):
#         return self._balance

#     # 입금
#     def deposit(self, amount):
#         if amount <= 0:
#             print("입금액은 0보다 커야 합니다")
#             return
#         else:
#           self._balance += amount
#           print(f"{amount:,}원 입금 (잔액 {self._balance:,}원)")

#         self._trade.append(f"입금 {amount}")

#     # 출금
#     def withdraw(self, amount):
#         if amount > self._balance:
#             print(f"잔액 부족 (현재 {self._balance:,}원)")
#             return

#         self._balance -= amount

#         print(f"{amount:,}원 출금 (잔액 {self._balance:,}원)")

#         self._trade.append(f"출금 {amount}")

#     # 거래 내역
#     def history(self):
#         print("[거래 내역]")
#         for idx, trade in enumerate(self._trade):
#             print(f"  {idx + 1}. {trade}")

#     # 계좌 정보
#     def show(self):
#         print(f"{self._owner}님 계좌  잔액 {self._balance:,}원  거래 {len(self._trade)}건")


# class SavingsAccount(Account):

#     def __init__(self, owner, balance, rate):
#         # super()를 통해 부모 클래스 상속 적용
#         super().__init__(owner, balance)
#         self._rate = rate

#     def add_interest(self):
#         # 이자 지급
#         self.interest = int(self._balance * self._rate)
#         print(f"이자 {self.interest:,}원 지급")
#         # 부모 클래스의 입금 기능 사용
#         self.deposit(self.interest)

#     # 저축계좌의 출금
#     def withdraw(self, amount):
#         self.fee = 1000
#         total = amount + self.fee
#         if total > self._balance:
#             print(
#                 f"잔액 부족 "
#                 f"(현재 {self._balance:,}원)"
#             )
#             return

#         self._balance -= total

#         print(f"출금 수수료 {self.fee:,}원")
#         print(
#             f"{amount:,}원 출금 "
#             f"(잔액 {self._balance:,}원)"
#         )

#         # 수수료는 거래내역에 기록하지 않는다.
#         self._trade.append(f"출금 {amount}")


# a = Account("김철수", 50000)
# a.show()
# a.deposit(10000)
# a.deposit(-5000)
# a.withdraw(20000)
# a.withdraw(999999)
# a.show()
# a.history()

# print()

# s = SavingsAccount("이영희", 100000, 0.05)
# s.show()
# s.add_interest()
# s.withdraw(20000)
# s.show()
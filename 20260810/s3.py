# ============================================
# 함수는 '자판기'와 같다
# ============================================

# 자판기 3가지 과정
# [넣는다] -> [기계 안] -> 음료수

# [넣는다]: 매개변수 (Parameter)
# [기계 안]: 함수 몸통 (우리가 만든 처리 과정)
# [나오는 것]: 반환값 (return)

# ============================================
# 가장 단순한 함수
# ============================================

# 무조건 2배를 돌려주는 함수
# def double(x):  # x를 넣으면
#     return x * 2  # 2배로 만들어 돌려준다


# print(double(2))
# print(double(3))
# print(double(4))

# 함수 장점: 한 번 만들면 계속 쓰기 가능
# => 같은 코드를 반복해서 쓰지 않기


def hi(name):
    print(f"안녕하세요, {name}님!")
    print("오늘도 좋은 하루 되세요")


# => 진짜 이득은 짧아지는 것만이 아니다
# => 함수의 진짜 장점은, 고칠 곳이 줄어드는 것
# return과 print는 다르다

# 결과를 또 써야할 때
# ex) 쇼핑몰 장바구니
# 상품 가격에 부가세 10%를 붙인 최종 가격을 구하고,
# 그 가격들을 다 더해서 총액 계산


# 부가세
def buga(price):
    return price * 1.1


# a = buga(500000)
# b = buga(50000)
# c = buga(20000)

# print(a + b + c)
# print(a * 0.5)

# => 함수가 값을 돌려준다는 것 = 그 값을 재료로 또 쓸 수 있다는 것
# return이 필요한 이유


# 함수 안에서 함수 부르기


# 할인 함수
def discount(p):
    # 20% 할인가
    return int(p * 0.8)


# 할인을 하고 부가세를 붙이는 함수
# def f_price(p):
#     return buga(discount(p))  # 안쪽 discount가 먼저 실행됨


# print("원가 50,000원")
# print(f"할인만: {discount(50000)}원")
# print(f"부가세만: {buga(50000)}원")
# print(f"할인 후 부가세 적용: {f_price(50000)}원")

# => 안쪽 괄호부터 계산됨
# 작은 함수부터 조합해서 큰 기능을 만드는 것
# 이게 프로그램을 만드는 기본 방식

# 한 줄 코딩은 금물
# => 함수로 보기 편하게 코드 짜기
# pw = "abc12345"


# # 비밀번호 조건을 적용한 함수(def)문
# def safe_pass(pw):
#     # 비밀번호 조건: 8자 이상 + 숫자 포함 + 영문자 포함이면 True
#     if len(pw) < 8:
#         return False
#     if not any(ch.isdigit() for ch in pw):
#         return False
#     if not any(ch.isalpha() for ch in pw):
#         return False
#     return True


# # 적합한 비밀번호 허용을 위한 while문
# while True:
#     pw = input("사용할 비밀번호를 입력하세요: ")
#     if safe_pass(pw):
#         print("사용이 가능한 비밀번호")
#         break
#     else:
#         print("사용 할 수 없습니다.")


# ============================================
# 좋은 함수 이름 짓기
# ============================================

# 규칙
# 1) 동사로 시작하기 => get_, make_, send_, print_ 등등
# 2) True/False를 돌려주면 is_, has_, can_ 으로 시작
# 3) 영어 소문자 + _, get_avg
# 4) 이름만 보고 무슨 일으 하는지 알 수 있게
# 5) 주석을 안 써도 되는 이름이 가장 좋은 이름


# ============================================
# 함수 없이 학생 성적 처리
# ============================================
kor = [90, 85, 100]
eng = [70, 95, 80]
math = [60, 75, 88]

# # 국어(kor)
# avg = sum(kor) / len(kor)
# print("국어 평균: ", round(avg, 1))

# if avg >= 90:
#     print("등급: A")
# elif avg >= 80:
#     print("등급: B")
# else:
#     print("등급: C")

# # 영어(eng)
# avg = sum(eng) / len(eng)
# print("영어 평균: ", round(avg, 1))

# if avg >= 90:
#     print("등급: A")
# elif avg >= 80:
#     print("등급: B")
# else:
#     print("등급: C")

# # 수학(math)
# avg = sum(math) / len(math)
# print("영어 평균: ", round(avg, 1))

# if avg >= 90:
#     print("등급: A")
# elif avg >= 80:
#     print("등급: B")
# else:
#     print("등급: C")

# 함수 없이 사용하면 8줄 짜리 코드를 세 번 복사해서 사용 => 비효율적
# 과목이 더 늘어나거나, 등급 기준이 바뀌면 => 일일이 찾아서 수정해야하는 비효율적인 상황 발생

# ============================================
# 함수를 사용하여 학생 성적 처리
# ============================================
# kor = [90, 85, 100]
# eng = [70, 95, 80]
# math = [60, 75, 88]


# # 평균 구하는 함수
# def get_avg(scores):
#     # 점수 리스트의 평균 (소수점 첫째 자리로 끊기)
#     return round(sum(scores) / len(scores), 1)


# # 등급 구하는 함수
# def get_grade(score):
#     # 평균을 등급으로 전환하는 함수
#     if score >= 90:
#         return "A"
#     if score >= 80:
#         return "B"
#     return "C"


# # 성적표
# def print_std(sub, scores):
#     # 과목 성적표 한 줄 출력
#     avg = get_avg(scores)
#     grade = get_grade(avg)
#     print(f"{sub} 평균: {avg} / 등급: {grade}")


# print_std("국어", kor)
# print_std("영어", eng)
# print_std("수학", math)


# ============================================
# 함수를 써야 하는 순간
# ============================================
# 같은 코드를 두 번 이상 복사했다 -> 반복 제거
# 계산 결과를 다른 곳에서 또 써야 한다 -> return
# 조건식이 길어서 뜻을 모르겠다 -> 이름 짓기
# 코드 덩어리에 주석으로 제목을 달았다 -> 제목이 '함수 이름'

# => 함수는 '자판기'와 같다 (넣고(input parameter) 나온다(return))
# => 진짜 장점은 단순히 짧아지는 것이 아니라 고칠 곳이 한 곳이 되는 것
# => print는 보여주기, return은 반환, 다시 쓸 값이면 return


# 변수에도 사는 곳이 있다
# 전역변수 (global): 함수 '밖'에서 만든 변수
# => 프로그램 전체에서 살아있음

# 지역변수 (local): 함수 '안'에서 만든 변수
# => 해당 함수가 끝나면 사라진다

# count = 10  # 전역변수 (함수 밖)


# def test():
#     temp = 5  # 지역변수 (함수 안)
#     print("함수 안에서 count:", count)
#     print("함수 안에서 temp:", temp)


# test()  # 함수에서 저장한 변수 읽기
# print(count, "밖에서")
# # print(temp, "안에서")

# 읽기는 되는데 쓰기가 안된다 * 가장 헷갈리는 부분 *
# num = 10


# def change():
#     num = 99
#     print("함수 안에서 본 num:", num)


# print("함수 실행 전:", num)
# change()
# print("함수 실행 후:", num)

# 바뀌지 않은 이유?
# => 파이썬은 함수 안에서 '변수 = 값'을 보는 순간
# => 이 함수에서 쓸 새로운 지역변수를 만드는 것으로 판단

# 즉, 함수 안의 num과 함수 밖의 num은
# 이름만 같을 뿐 완전히 다른 변수!
# => 함수 안의 num은 함수가 끝나면서 사라졌고, 함수 밖의 num은 처음부터 손대지 않았다


# 매개변수도 '지역변수'
score = 50


def add_ten(score):  # 이 score는 새로 만들어진 지역변수
    score = score + 10  # 지역변수를 바꿈
    # 함수가 끝나면 이 score는 사라짐


# 함수에 값을 넘길 때 '복사본'이 전달된다고 생각하면 된다
# 원본은 안전하게 보호
# 함수를 불렀는데 밖의 값이 마음대로 바뀌면 이상한 상황

# ============================================
# global 키워드
# ============================================

total = 0


def add_global(x):
    global total  # 밖에 있는 total을 쓰겠다고 선언
    total = total + x


# => global을 쓰면 함수 안에서 전역변수를 바꿀 수 있다.
# ? => global을 쓰지 말아야 하는 이유
# money = 10000


# def buy_lunch():
#     global money
#     money -= 8000


# def buy_coffee():
#     global money
#     money -= 4500


# def get_paid():
#     global money
#     money += 5000


# buy_coffee()
# buy_lunch()
# get_paid()

# print("남은 돈:", money)

# 문제점
# 1) 변수(예시 코드에서 'money')가 어디서 바뀌었는지 추적이 힘듦
# 2) 함수가 100개면 어느 것이 변했는지 다 열어봐야 하는 번거로움
# 3) 함수만 봐서 뭘 하는 기능인지 알 수 없음
# 4) global은 자판기가 몰래 벽을 뚫고 옆방 물건을 바꾸는 것과 같음


# global 없이 사용
def buy(money, price):
    return money - price


money = 10000
print("시작", money)

money = buy(money, 4500)  # 커피
print("커피 구매 후:", money)
print()
# => 변수(예시 코드에서 'money')가 바뀌는 지점이 보임
# => buy 함수는 밖에 무엇도 건드리지 않았다
# => buy 함수만 따로 테스트 할 수 있다
# => 다른 프로그램에서 그대로 사용 가능
# 규칙: 들어가는 것은 매개변수로, 나오는 것은 return으로


# ============================================
# 리스트와 딕셔너리는 다르게 동작한다
# ============================================

# 예시 리스트
scores = [90, 85]
print("함수 실행 전:", scores)


def add_score():
    scores.append(100)
    # global 없이 추가 가능


add_score()  # 함수 실행
print("함수 실행 후:", scores)
print()
# => append, remove, sort 같은 것들은 원본을 바꾼다
# => 딕셔너리의 'dict["키"] = 값'도 마찬가지

names = ["김철수", "이영희"]


def replace_all():
    names = ["박민수"]  # 지역변수
    names.append("박민수")  # 전역으로 선언된 리스트에 값 추가


replace_all()  # 함수 실행
print(names)  # 리스트 그대로
print()

# 대입(=) -> 지역변수가 새로 생김, 밖은 안 바뀜
# 내용 수정 -> 원본이 바뀜(append, 인덱스 접근, 딕셔너리 키 등)
# 이 차이 때문에 바뀌는것 여부에 혼란이 발생할 수 있음


# ============================================
# 리스트도 return으로 다루는 게 안전하다
# ============================================
og = [3, 1, 2]


def sort_bad(data):
    data.sort()  # 리스트에 담긴 값의 원본을 건드리는 케이스
    return data


def sort_good(data):
    new_data = sorted(data)  # 리스트에 담긴 값의 원본이 그대로 유지
    return new_data


result = sort_good(og)
print("sort_good 후 원본:", og, "결과:", result)

result = sort_bad(og)
print("sort_bad 후 원본:", og, "결과:", result)
# 함수가 몰래 원본을 바꾸면, 나중에 맞지 않은 데이터가 출력되는 불상사가 발생
# => 특히 여러 사람이 같이 사용하는 코드에는 반드시 주의

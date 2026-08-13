# [1] 체온 판정기
# -------------------------------------------------------------

# 체온을 받아 상태를 문자열로 돌려주는 함수를 만드세요.
#   37.5 이상        -> "발열"
#   36.0 이상 37.5 미만 -> "정상"
#   36.0 미만        -> "저체온"

# [기대 결과] (아래 temps 5개를 전부 판정)
#   36.5 -> 정상    38.2 -> 발열    35.1 -> 저체온
#   37.0 -> 정상    39.1 -> 발열

# -------------------------------------------------------------
# temps = [36.5, 38.2, 35.1, 37.0, 39.1]


# # 체온 판정을 위한 함수
# def check_temp(temp):
#     if temp >= 37.5:
#         return "발열"
#     if 36 <= temp < 37.5:
#         return "정상"
#     return "저체온"


# # 주어진 리스트의 값들 불러오는 for문
# for i in temps:
#     print(f"{i} -> {check_temp(i)}")


# [2] 가격에 부가세 붙이기
# -------------------------------------------------------------

# 가격을 받아 부가세 10%를 더한 값을 돌려주는 함수를 만드세요.
# (소수점은 버리고 정수로)
# 그리고 아래 상품들의 최종 가격과 총합을 출력하세요.


# [기대 결과]
#   노트북: 1320000원
#   마우스: 27500원
#   키보드: 49500원
#   총합: 1397000원

# -------------------------------------------------------------
# products = {"노트북": 1200000, "마우스": 25000, "키보드": 45000}


# # 부가세 적용하는 함수
# def add_tax(price):
#     buga = int(price + (price * 0.1))
#     return buga


# # 부가세가 포함된 가격들의 합계를 담기 위한 변수 total
# total = 0
# for i in products:
#     # add_tax 함수로 부가세가 포함된 상품가들의 합계를 위한 total
#     total += add_tax(products.get(i))
#     print(f"{i}: {add_tax(products.get(i))}")

# print(f"총합: {total}")


# [3] 글자 수 세기
# -------------------------------------------------------------

# 문장을 받아 공백을 제외한 글자 수를 돌려주는 함수를 만드세요.
# [기대 결과]

#   "안녕 하세요"      -> 5
#   "파 이 썬 좋 아"   -> 5
#   "hello world"    -> 10

# -------------------------------------------------------------
# sentences = ["안녕 하세요", "파 이 썬 좋 아", "hello world"]


# # 글자수 세기 함수 (공백이 replace()로 제거된 글자수 세기)
# def lang_count(sentence):
#     return len(sentence)


# # 리스트 불러오는 for문
# for s in sentences:
#     # 공백을 제거하여 함수 파라미터로 전달
#     lang_count(s.replace(" ", ""))
#     # 출력 결과물
#     print(f"{s}     -> {lang_count(s.replace(' ', ''))}")


# [4] 안전한 숫자 변환
# -------------------------------------------------------------

# 문자열을 숫자로 바꾸되, 실패하면 0을 돌려주는 함수를 만드세요.
# (앞뒤 공백은 제거할 것)

# [기대 결과]
#   " 100 "  -> 100
#   "50"     -> 50
#   ""       -> 0
#   "삼십"    -> 0
#   "3.5"    -> 0     (int로 못 바꾸므로)


# 그리고 아래 리스트의 합계를 구하세요. -> 150
# ★★★ 이 함수는 앞으로 계속 씁니다. 잘 만들어 두세요.★★★★
#         "".isdigit()      -> False   (빈 문자열)
#         "100".isdigit()   -> True
#         "삼십".isdigit()   -> False
#         "3.5".isdigit()   -> False   (점은 숫자가 아니므로)
# -------------------------------------------------------------
# raw = [" 100 ", "50", "", "삼십", "3.5"]


# def int_check(raw, raw_data):
#     if raw == True:
#         return int(raw_data)
#     return 0


# int_sum = 0
# for r in raw:
#     # 리스트 raw 속 자료들의 띄어쓰기 제거
#     raw_data = r.replace(" ", "")
#     # 위의 변수 자료들의 형변환 True/False 여부
#     int_check(raw_data.isdigit(), raw_data)
#     print(f'"{r}"   -> {int_check(raw_data.isdigit(), raw_data)}')
#     int_sum += int_check(raw_data.isdigit(), raw_data)
# print("리스트 raw의 합계:", int_sum)


# [5] 최댓값 직접 만들기
# -------------------------------------------------------------

# max() 를 쓰지 말고, 리스트에서 가장 큰 값을 찾는 함수를 만드세요.
# 빈 리스트가 들어오면 None 을 돌려주세요.


# [기대 결과]
#   [3, 9, 1, 7]  -> 9
#   [-5, -2, -9]  -> -2
#   []            -> None

# -------------------------------------------------------------

# ex_list1 = [3, 9, 1, 7]
# ex_list2 = [-5, -2, -9]
# ex_list3 = []


# # 최대값 판별을 위한 함수
# def maximum(list):
#     # 리스트에 아무것도 없을 때
#     if len(list) == 0:
#         # 'None'으로 반환
#         return None
#     max_num = list[0]
#     for n in list:
#         # max() 사용 없이 큰 값을 판별하는 조건과 대입
#         if n > max_num:
#             max_num = n
#     # 대입한 큰 값을 반환
#     return max_num


# print(maximum(ex_list1))
# print(maximum(ex_list2))
# print(maximum(ex_list3))


# [6] 평균과 등급
# -------------------------------------------------------------
# 함수 두 개를 만드세요.
#   get_average(scores) : 리스트의 평균 (소수 첫째 자리 반올림)
#   get_grade(score)    : 점수 -> 등급 (90이상 A, 80이상 B, 70이상 C, 나머지 D)

# 그리고 아래 학생들의 평균과 등급을 출력하세요.
# [기대 결과]
#   김철수  평균 91.7  등급 A
#   이영희  평균 78.3  등급 C
#   박민수  평균 85.0  등급 B

# students = {
#     "김철수": [90, 85, 100],
#     "이영희": [70, 95, 70],
#     "박민수": [80, 85, 90],
# }


# # 리스트의 평균 (소수 첫째 자리 반올림)
# def get_average(scores):
#     avg = round(scores, 1)
#     return avg


# # 등급 (90이상 A, 80이상 B, 70이상 C, 나머지 D)
# def get_grade(score):
#     if score >= 90:
#         return "A"
#     if score >= 80:
#         return "B"
#     if score >= 70:
#         return "C"
#     return "D"


# for s in students:
#     students_sum = sum(students.get(s))
#     len_test = len(students.get(s))
#     score_avg = students_sum / len_test
#     # 평균값 함수 이동
#     get_average(score_avg)
#     # 등급 함수 이동
#     get_grade(score_avg)
#     print(f"{s}  평균 {get_average(score_avg)}  등급 {get_grade(score_avg)}")


# [7] 급여 계산기
# -------------------------------------------------------------

# 함수 세 개를 만들어 조립하세요.
#   get_overtime_pay(hours) : 초과근무수당 (시간당 20000원)
#   get_tax(amount)         : 세금 (총액의 10%, 정수)
#   get_final_pay(base, hours) : 실수령액
#                             = (기본급 + 초과수당) - 세금

# [기대 결과]
#   김철수: 기본급 3000000, 초과 5시간 -> 실수령 2790000
#   이영희: 기본급 3500000, 초과 0시간 -> 실수령 3150000

# -------------------------------------------------------------
# workers = [
#     {"이름": "김철수", "기본급": 3000000, "초과시간": 5},
#     {"이름": "이영희", "기본급": 3500000, "초과시간": 0},
# ]


# def get_overtime_pay(hours):
#     over_salery = hours * 20000
#     return over_salery


# def get_tax(amount):
#     return amount * 0.1


# def get_final_pay(base, hours, tax):
#     final_pay = (base + hours) - tax
#     return final_pay


# for dic in workers:
#     name = dic.get("이름")
#     salery = dic.get("기본급")
#     over_time = int(dic.get("초과시간"))

#     # 초과근무수당
#     over_pay = get_overtime_pay(over_time)

#     # 총액
#     all_salery = salery + over_pay

#     # 세금
#     get_tax(all_salery)
#     out_tax = int(get_tax(all_salery))

#     # # 실수령액
#     get_final_pay(salery, get_overtime_pay(over_time), get_tax(all_salery))
#     real_salery = get_final_pay(
#         salery, get_overtime_pay(over_time), get_tax(all_salery)
#     )

#     print(f"{name}: 기본급 {salery}, 초과 {over_time}시간 -> 실수령 {int(real_salery)}")


# [8] 비밀번호 검사기
# -------------------------------------------------------------
# 아래 세 조건을 각각 함수로 만들고, 그 셋을 합친 함수를 만드세요.
#   is_long_enough(pw)  : 8자 이상인가
#   has_number(pw)      : 숫자가 들어있는가
#   has_letter(pw)      : 영문자가 들어있는가
#   check_password(pw)  : 셋 다 만족하면 "안전",
#                         아니면 부족한 조건을 알려주는 문자열

# [기대 결과]
#   "abc12345"  -> 안전
#   "abc123"    -> 8자 이상이어야 합니다
#   "abcdefgh"  -> 숫자를 포함해야 합니다
#   "12345678"  -> 영문자를 포함해야 합니다
# -------------------------------------------------------------

# passwords = ["abc12345", "abc123", "abcdefgh", "12345678"]

# # 비밀번호 조건을 적용한 함수(def)문


# # 8자 이상인가
# def is_long_enough(pw):
#     if len(pw) >= 8:
#         return True
#     return False


# # 숫자가 들어있는가
# def has_number(pw):
#     if any(ch.isdigit() for ch in pw):
#         return True
#     return False


# # 영문자를 포함해야 합니다
# def has_letter(pw):
#     if any(ch.isalpha() for ch in pw):
#         return True
#     return False


# def check_password(pw):
#     if is_long_enough(pw) == False:
#         return "8자 이상이어야 합니다"
#     if has_number(pw) == False:
#         return "숫자를 포함해야 합니다"
#     if has_letter(pw) == False:
#         return "영문자를 포함해야 합니다"
#     return "안전"


# for pwd in passwords:
#     print(f'"{pwd}"   -> {check_password(pwd)}')


# [9] 별점 시각화
# -------------------------------------------------------------

# 함수 두 개를 만드세요.
#   make_star(score)     : 점수(0~5)를 별 문자열로. 예) 3 -> "★★★☆☆"
#   show_review(name, score) : "상품명  ★★★☆☆ (3)" 형태로 출력
#                              (make_star 를 불러서 쓸 것)

# [기대 결과]
#   노트북      ★★★★☆ (4)
#   마우스      ★★★★★ (5)
#   키보드      ★★☆☆☆ (2)

# ★ show_review 는 return 없이 print 만 합니다. 이건 괜찮습니다.
# -------------------------------------------------------------
# reviews = {"노트북": 4, "마우스": 5, "키보드": 2}


# # 별점 함수
# def make_star(score):
#     if score == 5:
#         return "★ " * 4 + "★"
#     if score == 4:
#         return "★ " * 4 + "☆"
#     if score == 3:
#         return "★ " * 3 + "☆ ☆"
#     if score == 2:
#         return "★ ★" + " ☆" * 3
#     if score == 1:
#         return "★" + (" ☆" * 4)
#     if score == 0:
#         return "☆ " * 4 + "☆"


# for r in reviews:
#     print(f"{r}     {make_star(reviews.get(r))}  ({reviews.get(r)})")


# [10] 재고 관리
# -------------------------------------------------------------
# 함수 세 개를 만드세요.

#   add_stock(stock, name, count)    : 입고 (없는 상품이면 새로 추가)
#   remove_stock(stock, name, count) : 출고 (재고보다 많으면 "재고 부족" 출력 후 무시)
#   show_stock(stock)                : 전체 재고 출력


# 아래 순서대로 실행하세요.
#   마우스 10개 입고 -> 키보드 5개 입고 -> 마우스 3개 출고
#   -> 키보드 10개 출고(실패) -> 모니터 2개 입고 -> 전체 출력


# [기대 결과]

#   재고 부족: 키보드 (요청 10, 보유 5)

#   [재고 현황]
#     마우스: 7개
#     키보드: 5개
#     모니터: 2개

# ★ 포인트: stock 딕셔너리를 ★매개변수로 주고받으세요★

# -------------------------------------------------------------
# stock = {}


# # 입고 함수 (없는 상품이면 새로 추가)
# def add_stock(stock, name, count):
#     if stock.get(name) == None:
#         into = stock[name] = count
#     return into


# # 출고 함수 (재고보다 많으면 "재고 부족" 출력 후 무시)
# def remove_stock(stock, name, count):
#     if stock.get(name) >= count:
#         stock[name] = stock.get(name) - count
#         return stock[name]
#     return f"재고 부족: {name} (요청 {count}, 보유 {stock.get(name)})"


# # 재고 함수 (전체 재고 출력)
# def show_stock(stock):
#     print("[재고 현황]")
#     for i in stock:
#         print(f"{i}: {stock.get(i)}개")
#     return True


# # 마우스 10개 입고
# add_stock(stock, "마우스", 10)

# # 키보드 5개 입고
# add_stock(stock, "키보드", 5)

# # 마우스 3개 출고
# remove_stock(stock, "마우스", 3)

# # 키보드 10개 출고(실패)
# remove_stock(stock, "키보드", 10)
# print(remove_stock(stock, "키보드", 10))

# # 모니터 2개 입고
# add_stock(stock, "모니터", 2)

# # 전체 출력
# print()
# show_stock(stock)

# [11] 문자열 뒤집기와 회문 판정

# -------------------------------------------------------------

# 함수 두 개를 만드세요.

#   reverse_text(s)  : 문자열을 뒤집어 돌려준다 ([::-1] 금지! 반복문으로)

#   is_palindrome(s) : 앞뒤가 같은 말인지 판정 (공백 무시, 대소문자 무시)

#

# [기대 결과]

#   reverse_text("hello")  -> "olleh"      (뒤집기 함수 단독 확인)

#

#   그리고 아래 words 리스트를 판정하면

#   "level"        -> 회문입니다

#   "기러기"        -> 회문입니다

#   "python"       -> 회문이 아닙니다

#   "Never odd or even" -> 회문입니다

# -------------------------------------------------------------
# words = ["level", "기러기", "python", "Never odd or even"]


# def reverse_text(s):
#     reverse = ""
#     for i in s:
#         reverse = i + reverse
#     return reverse


# print(reverse_text("hello"))
# print()


# def is_palindrome(s):
#     for i in range(len(s) // 2):
#         if s[i] != s[-1 - i]:  # 왼쪽 문자들과 오른쪽 문자들이 다르다면
#             return "회문이 아닙니다"
#     return "회문입니다"


# for w in words:
#     print(f"{w}        -> {is_palindrome(w)}")


# [12] 단어 개수 세기

# -------------------------------------------------------------

# 함수를 만드세요.
#   count_words(text) : 단어별 등장 횟수를 딕셔너리로 돌려준다
#                       (소문자로 통일, 공백으로 구분)

# 그리고 가장 많이 나온 단어를 찾는 함수도 만드세요.
#   most_common(counter) : 가장 많이 나온 단어와 횟수를 함께 반환
#                          (return 단어, 횟수  -> 받을 때 w, c = most_common(...))

# [기대 결과]
#   {'python': 3, 'is': 2, 'fun': 1, 'easy': 1}
#   가장 많이 나온 단어: python (3회)

# -------------------------------------------------------------


# # 키와 값을 받을 빈 딕셔너리 생성
# text = "Python is fun Python is easy Python"


# txt_cnt = {}


# def count_words(text):
#     if txt_cnt.get(text) == None:
#         txt_cnt[text] = 0
#     if (text in txt_cnt) == True:
#         txt_cnt[text] += 1
#     return txt_cnt[text]


# def most_common(counter):
#     word_cnt = 0
#     for v in counter:
#         if counter.get(v) > word_cnt:
#             word_cnt = counter.get(v)  # 가장 큰 수 저장
#             many_word = v  # 가장 큰 수를 갖고 있는 키 저장
#     return many_word, word_cnt


# for txt in text.split():
#     count_words(txt)

# print(txt_cnt)
# most_common(txt_cnt)


# # 저장한 최다 단어(키)와 숫자(밸류)를 리스트화
# many_key = list(most_common(txt_cnt))
# print(f"가장 많이 나온 단어: {many_key[0]} ({many_key[1]}회)")


# [13] 계좌 입출금

# -------------------------------------------------------------

# 함수 두 개를 만드세요.

#   withdraw(balance, amount) : 출금 후 잔액을 돌려준다
#                               잔액보다 많이 출금하려 하면
#                               "잔액 부족" 출력 후 잔액 그대로 반환
#   deposit(balance, amount)  : 입금 후 잔액을 돌려준다
# 잔액 10000원으로 시작해 아래 순서대로 처리하세요.
#   3000원 출금 -> 5000원 입금 -> 20000원 출금(실패)


# [기대 결과]
#   출금 3000 -> 잔액 7000
#   입금 5000 -> 잔액 12000
#   잔액 부족 (요청 20000, 잔액 12000)
#   최종 잔액: 12000

# -------------------------------------------------------------

# # 초기 잔액
# balance = 10000


# # 출금하기 함수
# def withdraw(balance, amount):  # 출금 처리 함수
#     if balance >= amount:  # 잔액이 출금액 이상이면
#         print(f"출금 {amount}  -> 잔액 {balance - amount}")
#         return balance - amount
#     else:  # 잔액이 출금액보다 부족하면
#         print(f"잔액 부족 (요청 {amount}, 잔액 {balance})")
#         return balance


# # 입금하기 함수
# def deposit(balance, amount):  # 입금 처리 함수
#     print(f"입금 {amount} -> 잔액 {balance + amount}")
#     return balance + amount  # 입금 후 잔액 정보 반환


# # 출금 파라미터 전달
# balance = withdraw(balance, 3000)

# # 입금 파라미터 전달
# balance = deposit(balance, 5000)

# # 출금 파라미터 전달
# balance = withdraw(balance, 20000)
# # 입금 후 최종 잔액
# print(f"최종 잔액: {balance}원")


# [14] 장바구니 (원본을 지키는 함수)
# -------------------------------------------------------------
# 함수 두 개를 만드세요.
#   add_item(cart, name)    : 상품을 추가한 새 리스트를 돌려준다
#   remove_item(cart, name) : 상품을 뺀 새 리스트를 돌려준다
#                             (없는 상품이면 "없는 상품입니다" 출력)

# ★ 두 함수 모두 원본 리스트를 바꾸면 안 됩니다.

# [기대 결과]
#   장바구니1: ['사과']
#   장바구니2: ['사과', '우유']
#   장바구니3: ['사과', '우유', '빵']
#   없는 상품입니다: 라면
#   장바구니4: ['사과', '빵']
#   원본 확인 - 장바구니1: ['사과']

# -------------------------------------------------------------

# cart1 = ["사과"]
# print(f"장바구니1: {cart1}")


# # 상품을 추가한 새 리스트를 돌려준다
# def add_item(cart, name):
#     # 원본 데이터 유지를 위한 조치 (리스트 복사)
#     new_cart = sorted(cart)
#     # 복사된 리스트에 상품 추가
#     new_cart.append(name)
#     return new_cart


# add_item(cart1, "우유")
# print(f"장바구니2: {add_item(cart1, '우유')}")

# # 새 리스트 변수에 추가 1
# cart2 = add_item(cart1, "우유")

# add_item(cart2, "빵")
# print(f"장바구니3: {add_item(cart2, '빵')}")

# # 새 리스트를 변수에 추가 2
# cart3 = add_item(cart2, "빵")


# # 상품을 뺀 새 리스트를 돌려준다 (없는 상품이면 "없는 상품입니다" 출력)
# def remove_item(cart, name):
#     # (name in cart) => 'name' 파라미터로 받은 값이 'cart' 리스트에 존재하는가?
#     if (name in cart) == True:
#         # 존재하면 해당 파라미터 값을 삭제
#         return cart.remove(name)
#     # 존재하지 않으면
#     return print(f"없는 상품입니다: {name}")


# remove_item(cart3, "라면")
# remove_item(cart3, "우유")
# print(f"장바구니4: {cart3}")
# print(f"원본확인 - 장바구니1: {cart1}")


# [15] 원본을 지키는 함수
# -------------------------------------------------------------
# 함수 두 개를 만들어 차이를 비교하세요.
#   sort_bad(data)  : 원본 리스트를 직접 정렬 (data.sort())
#   sort_good(data) : 원본은 그대로 두고 정렬된 새 리스트 반환


# [기대 결과]
#   원본: [3, 1, 2]
#   sort_good 결과: [1, 2, 3] / 원본: [3, 1, 2]   <- 원본 유지
#   sort_bad  결과: [1, 2, 3] / 원본: [1, 2, 3]   <- 원본 파괴
# -------------------------------------------------------------
# orgin_list = [3, 1, 2]

# print(f"원본: {orgin_list}")


# # 원본 리스트를 직접 정렬 (data.sort())
# def sort_bad(data):
#     # 원본 리스트(data) 정렬
#     data.sort()
#     return data


# # 원본은 그대로 두고 정렬된 새 리스트 반환
# def sort_good(data):
#     # 원본 리스트(data)를 보호하고 정렬 (정렬한 리스트를 복사)
#     copy_list = sorted(data)
#     return copy_list


# # sort_good 함수 적용
# sort_good(orgin_list)
# print(f"sort_good 결과: {sort_good(orgin_list)} / 원본: {orgin_list}")

# # sort_bad 함수 적용
# sort_bad(orgin_list)
# print(f"sort_bad 결과: {sort_bad(orgin_list)} / 원본: {orgin_list}")



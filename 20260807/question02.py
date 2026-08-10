# ---------------------------------------------------------
# [1] 점수 통계
#   최고점, 최저점, 평균(소수점 1자리)을 출력하세요.
#   max() / min() / sum() 없이 for문으로 직접 구할 것
#   기대 출력: 최고 95 / 최저 67 / 평균 84.2
# ---------------------------------------------------------
# scores = [88, 92, 79, 95, 67, 84]
# max_p = scores[0]
# min_p = scores[0]
# sum_p = 0

# for i in scores:
#     if i >= max_p:
#         max_p = i
#     elif i <= min_p:
#         min_p = i

# for i in scores:
#     sum_p += i

# # 평균값 구하기
# avg_p = round(sum_p / len(scores), 1)

# print(f"기대출력: 최고 {max_p} / 최저 {min_p} / 평균 {avg_p}")

# ---------------------------------------------------------
# [2] 평균 이상만 골라내기
#   평균보다 높은 점수만 새 리스트에 담아 출력하세요.
#   기대 출력: 평균 84.2 이상: [88, 92, 95]
# ---------------------------------------------------------

# scores = [88, 92, 79, 95, 67, 84]
# sum_p = 0
# num = len(scores)

# for i in scores:
#     sum_p += i

# avg_p = round(sum_p / len(scores), 1)

# cnt = []
# for i in scores:
#     if avg_p <= i:
#         cnt.append(i)
# print(cnt)

# ---------------------------------------------------------

# [3] 등급별 인원수

#   A(90+) B(80~89) C(70~79) D(60~69) F(60미만) 각각 몇 명인지 세세요.

#   기대 출력: A: 2명 / B: 2명 / C: 2명 / D: 1명 / F: 1명

# ---------------------------------------------------------

# scores = [88, 92, 79, 95, 67, 84, 55, 73]

# A_class = 0
# B_class = 0
# C_class = 0
# D_class = 0
# F_class = 0

# for i in scores:
#     if i >= 90:
#         A_class += 1
#     elif i >= 80:
#         B_class += 1
#     elif i >= 70:
#         C_class += 1
#     elif i >= 60:
#         D_class += 1
#     else:
#         F_class += 1

# print(
#     f"기대 출력: A: {A_class}명 / B: {B_class}명 / C: {C_class}명 / D: {D_class}명 / F: {F_class}명"
# )

# ---------------------------------------------------------

# [4] 두 번째로 큰 수

#   sort() 없이 for문만으로 두 번째로 큰 수를 찾으세요.

#   기대 출력: 82

# ---------------------------------------------------------

# numbers = [45, 82, 17, 93, 60]

# first_number = numbers[0]
# second_number = numbers[0]

# for i in numbers:
#     if i >= first_number:
#         first_number = i
#     for j in numbers:
#         if j >= second_number and j < first_number:
#             second_number = j
# print(f"기대 출력: {second_number}")

# ---------------------------------------------------------

# [5] 중복 찾기

#   중복된 값만 골라 출력하세요. (중복 자체도 한 번씩만)

#   기대 출력: [3, 7]

# ---------------------------------------------------------

# data = [3, 7, 2, 7, 9, 3, 5, 3]
# same_list = []

# for i in data:
#     if data.count(i) > 1 and i not in same_list:
#         same_list.append(i)

# print(same_list)

# ---------------------------------------------------------

# [6] 연속 상승 구간

#   앞 숫자보다 커지는 경우가 연속으로 몇 번 이어졌는지,

#   가장 긴 구간의 길이를 출력하세요.

#   기대 출력: 3

# ---------------------------------------------------------

# temps = [12, 14, 15, 13, 16, 18, 19, 17]
# temp = temps[0]
# up_cnt = 0
# save_cnt = 0

# for i in temps:
#     if temp < i:
#         up_cnt += 1
#         temp = i
#     else:
#         save_cnt = up_cnt
#         up_cnt = 0
# print(f"기대 출력: {save_cnt}")

# ---------------------------------------------------------

# [7] 리스트 뒤집기

#   [::-1] 과 reverse() 없이 for문으로 거꾸로 만드세요.

#   기대 출력: [5, 4, 3, 2, 1]

# ---------------------------------------------------------

# numbers = [1, 2, 3, 4, 5]
# length = len(numbers)
# my_list = []
# for i in range(length, 0, -1):
#     my_list.append(i)
# print(my_list)

# ---------------------------------------------------------

# [8] 재고 출력

#   "사과: 5개" 형태로 출력하되, 0개면 "바나나: 품절"로 출력하세요.

# ---------------------------------------------------------

# stock = {"사과": 5, "바나나": 0, "포도": 12}

# for i in stock:
#     nums = stock.get(i)
#     if nums == 0:
#         nums = "품절"
#     else:
#         nums = f"{nums}개"
#     print(f"{i}: {nums}")


# ---------------------------------------------------------

# [9] 최고 매출 상품

#   max() 없이 for문으로 가장 많이 팔린 상품명과 금액을 찾으세요.

#   기대 출력: 노트북: 1200

# ---------------------------------------------------------

# sales = {"노트북": 1200, "마우스": 340, "키보드": 780}
# lot = sales.get("노트북")
# prod_keys = list(sales.keys())
# lot_prod = prod_keys[0]

# for i in sales:
#     nums = sales.get(i)
#     if lot <= nums:
#         lot_prod = i
#         lot = nums

# print(f"기대 출력: {lot_prod}: {lot}")


# [10] 총액 계산

#   각 항목의 소계와 전체 총액을 천 단위 쉼표로 출력하세요.

#   기대 출력: 사과 3개 = 4,500원 … 총액: 13,300원

# ---------------------------------------------------------

# cart = {"사과": 3, "우유": 2, "빵": 1}
# price = {"사과": 1500, "우유": 2800, "빵": 3200}

# all_price = []

# for i in cart:
#     gye = cart.get(i)
#     price_ls = price.get(i)
#     all_price.append(price_ls * gye)
#     print(f"{i} {gye}개 = {price_ls * gye: ,}원")

# print(f"총액: {sum(all_price)}원")


# [11] 글자 세기

#   각 글자가 몇 번 나오는지 딕셔너리로 만들어 출력하세요.

#   예) banana 입력 → {'b': 1, 'a': 3, 'n': 2}

# ---------------------------------------------------------

# text = input("문자열: ")
# txt_dict = {}

# for i in text:
#     txt_dict[i] = txt_dict.get(i, 0) + 1

# print(f"{text} 입력 → {txt_dict}")    # part1

# text = input("문자열: ")
# txt_dict = {}

# for i in text:
#     if i in txt_dict:
#         txt_dict[i] = txt_dict[i] + 1
#     else:
#         txt_dict[i] = 1

# print(txt_dict)   # part2


# ---------------------------------------------------------

# [12] 딕셔너리 뒤집기

#   점수를 키로, 이름 리스트를 값으로 하는 딕셔너리를 만드세요.

#   기대 출력: {90: ['철수', '민수'], 85: ['영희']}

# ---------------------------------------------------------

# scores = {"철수": 90, "영희": 85, "민수": 90}
# result = {}

# for i in scores:
#     jumsu = scores.get(i)
#     if (jumsu in result) == True:
#         result[jumsu].append(i)
#     else:
#         result[jumsu] = [i]
# print(result)


# ---------------------------------------------------------

# [13] 투표 집계

#   각 후보의 득표수를 세고, 최다 득표자와 득표율(%)을 출력하세요.

#   기대 출력: A 4표 (50.0%) 당선

# ---------------------------------------------------------

# votes = ["A", "B", "A", "C", "B", "A", "C", "A"]

# sum_votes = len(votes)  # 총 투표수
# vote_gye = {}  # 빈 딕셔너리

# # 리스트의 딕셔너리화
# for i in votes:
#     vote_gye[i] = vote_gye.get(i, 0) + 1

# a_lot = 0  # 최다 득표수
# a_lot_person = ""  # 최다 득표자
# for j in vote_gye:
#     if a_lot <= vote_gye.get(j):
#         a_lot = vote_gye.get(j)
#         a_lot_person = j

# # 득표율
# vote_per = (a_lot / sum_votes) * 100

# # 최종 출력
# print(f"{a_lot_person} {a_lot}표 ({vote_per}%) 당선")

# ---------------------------------------------------------

# [14] 약수 구하기

#   그 수의 약수를 모두 출력하세요.

#   예) 12 입력 → 1 2 3 4 6 12

# ---------------------------------------------------------

# n = int(input("숫자: "))

# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i, end=" ")


# ---------------------------------------------------------

# [15] 소수 판별

#   소수인지 판별하세요.

#   예) 17 입력 → 소수입니다

# ---------------------------------------------------------

# n = int(input("숫자: "))
# # 약수를 담을 빈 리스트
# result = []

# for i in range(1, n + 1):
#     if n % i == 0:
#         result.append(i)

# if len(result) == 2:
#     print(f"{n} 입력 -> 소수입니다")
# else:
#     print(f"{n} 입력 -> 소수가 아닙니다")


# ---------------------------------------------------------

# [16] 자릿수 합

#   각 자리 숫자의 합을 구하세요.

#   예) 4728 입력 → 21

# ---------------------------------------------------------

# number = input("숫자: ")
# num_ls = list(str(number))  # 입력 숫자의 문자열 리스트화

# sum = 0  # 합계를 담을 변수 선언
# for n in num_ls:
#     sum += int(n)  # 문자로 변환된 리스트들을 다시 정수로 변환하고 합 계산

# print(f"{number} 입력 → {sum}")


# [17] 최대공약수

#   두 수의 최대공약수를 구하세요.

#   예) 36과 24 입력 → 12

# ---------------------------------------------------------

# num1_ls = []  # 첫 번째 수의 약수 담을 빈 리스트
# num2_ls = []  # 두 번째 수의 약수 담을 빈 리스트

# a = int(input("첫 번째 수: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         num1_ls.append(i)

# b = int(input("두 번째 수: "))
# for i in range(1, b + 1):
#     if b % i == 0:
#         num2_ls.append(i)

# same_nums = []  # 공통 정수들을 담을 리스트
# for i in num1_ls:
#     for j in num2_ls:
#         if i == j:
#             same_nums.append(i)

# same_biggest = 0  # 공통 정수들 중 가장 큰 수 담을 변수
# for k in same_nums:
#     same_biggest = max(k, same_biggest)  # max()를 사용하여 가장 큰 수 골라내기

# print(f"{a}와(과) {b} 입력 → {same_biggest}")

# ---------------------------------------------------------

# [18] 피보나치 수열

#   앞의 두 수를 더해서 다음 수를 만드는 수열입니다.

#   1, 1로 시작해서  1+1=2 → 1+2=3 → 2+3=5 → 3+5=8 …

#   n개를 출력하세요.

#   예) 8 입력 → 1 1 2 3 5 8 13 21

# ---------------------------------------------------------

# n = int(input("개수: "))

# a, b = 1, 1  # 시작 두 수는 1, 1로 시작

# fibo = []  # 피보나치 수열의 값들을 저장할 빈 리스트 생성

# for i in range(n):
#     fibo.append(a)
#     a, b = b, a + b  # 담은 앞의 두 수를 더하는 방식

# for j in fibo:
#     print(j, end=" ")

# ---------------------------------------------------------

# [19] 완전수 찾기

#   1~100 중 완전수를 모두 찾으세요.

#   완전수 = 자기 자신을 뺀 약수의 합이 자기 자신과 같은 수

#   예) 6의 약수는 1, 2, 3, 6 → 1+2+3 = 6 이므로 완전수

#   기대 출력: 6, 28

# ---------------------------------------------------------

# 1부터 100까지의 수 중에서 완전수 찾기
# for n in range(1, 101):
#     perfect_num = 0  # 완전수를 담을 변수
#     # 자기 자신을 제외한 약수를 구하기 위한 for문
#     for i in range(1, n):
#         if n % i == 0:
#             perfect_num += i

#     # 약수의 합이 자기 자신과 같다면 완전수 출력
#     if perfect_num == n:
#         print(n, end=" ")

# ---------------------------------------------------------

# [20] 모음 세기

#   모음(a,e,i,o,u)이 총 몇 개인지 세세요. 대소문자 구분 없이.

#   예) Hello Python World 입력 → 모음 4개

# ---------------------------------------------------------

# text = input("문장: ")

# text_ls = list(text)

# gather_ls = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
# gather_cnt = 0

# for i in text_ls:
#     for j in gather_ls:
#         if i == j:
#             gather_cnt += 1

# print(f"{text} 입력 → 모음 {gather_cnt}개")


# ---------------------------------------------------------

# [21] 회문 판별

#   앞으로 읽으나 뒤로 읽으나 같은 단어를 회문이라고 합니다. (level, noon)

#   입력받은 단어가 회문인지 판별하세요. [::-1] 없이 for문으로 비교할 것

#   예) level 입력 → 회문입니다

# ---------------------------------------------------------

# word = input("단어: ")

# # 회문을 판별하기 위한 변수 생성 (bool형)
# is_hoimoon = True

# # 회문 판독을 위한 반복문 (글자의 절반을 잘라서 판별하는 방식)
# for i in range(len(word) // 2):
#     if word[i] != word[-1 - i]:  # 왼쪽 문자들과 오른쪽 문자들이 다르다면
#         is_hoimoon = False  # 회문이 아님
#         break  # 종료

# print(is_hoimoon)


# ---------------------------------------------------------

# [22] 단어 길이별 분류

#   단어를 길이별로 딕셔너리에 분류하세요.

#   기대 출력: {1: ['I', 'a'], 2: ['am'], 7: ['student']}

# ---------------------------------------------------------

# sentence = "I am a student"
# result = {}  # 빈 딕셔너리


# # 문장 안의 공백 기준을 나누려면 .split()
# for i in sentence.split():
#     # 나눈 문장의 낱개들의 문자 수를 담는 변수 선언
#     cnt = len(i)

#     # 수가 딕셔너리의 키로 존재하면
#     if (cnt in result) == True:
#         # 해당 키에 i값을 담기
#         result[cnt].append(i)
#     else:
#         # 그렇지 않으면 수를 딕셔너리 키로 생성
#         result[cnt] = [i]
# print(result)

# ---------------------------------------------------------

# [23] 암호화

#   각 글자를 알파벳 순서로 한 칸씩 밀어 출력하세요. (z는 a로)

#   기대 출력: bcd

# ---------------------------------------------------------

# text = "abc"
# for c in text:
#     next_char = chr(ord(c) + 1)
#     if ord(c) == 122:
#         next_char = chr(ord("a"))
#     print(next_char, end="")
# print()
# text = "zabc"
# for c in text:
#     next_char = chr(ord(c) + 1)
#     if ord(c) == 122:
#         next_char = chr(ord("a"))
#     print(next_char, end="")


# ---------------------------------------------------------

# [24] 직각삼각형

#   n을 입력받아 아래 모양을 출력하세요. (n = 5 일 때)

#   *

#   **

#   ***

#   ****

#   *****

# ---------------------------------------------------------

# n = int(input("n: "))
# for i in range(1, n + 1):
#     print("*" * (i))

# [25] 역삼각형

#   n을 입력받아 아래 모양을 출력하세요. (n = 5 일 때)

#   *****

#   ****

#   ***

#   **

#   *

# ---------------------------------------------------------

# n = int(input("n: "))
# print()
# for i in range(n, 0, -1):
#     print("*" * (i))


# [26] 오른쪽 정렬 삼각형

#   n을 입력받아 아래 모양을 출력하세요. (n = 5 일 때)

#       *

#      **

#     ***

#    ****

#   *****

# ---------------------------------------------------------

# n = int(input("n: "))
# n = 5
# for i in range(1, n + 1):
#     # 공백 생성 + 별의 개수
#     print(" " * (n - i) + "*" * (i))


# ---------------------------------------------------------

# [27] 숫자 피라미드

#   n을 입력받아 아래 모양을 출력하세요. (n = 5 일 때)
#       1
#      121
#     12321
#    1234321
#   123454321
# ---------------------------------------------------------

# n = int(input("n: "))

# for i in range(1, n + 1):
#     # 공백 출력
#     print(" " * (n - i), end="")
#     # 숫자 출력 (홀수 개수만큼 증가)
#     for j in range(1, 2 * i):
#         if j <= i:  # j가 i 이하이면 값을 그대로 적용
#             print(j % 10, end="")
#         else:  # j가 i를 초과하면
#             k = j - i  # j가 i보다 크므로 j와 i를 빼는 식을 담는 변수 생성
#             j = j - (2 * k)  # 2의 배수씩 감소하는 규칙을 적용
#             print(j % 10, end="")
#     print()

# ---------------------------------------------------------

# [28] 속이 빈 사각형

#   n을 입력받아 아래 모양을 출력하세요. (n = 5 일 때)

#   *****

#   *   *

#   *   *

#   *   *

#   *****

# ---------------------------------------------------------

# n = int(input("n: "))

# for i in range(1, n + 1):
#     if i == 1 or i == n:
#         print("*" * 5)
#     else:
#         print("*" + " " * 3 + "*")

# ---------------------------------------------------------

# [29] 성적 처리 프로그램

#   각 학생의 총점·평균·등급을 출력하고, 평균 1등을 출력하세요.

#   등급: A(90+) B(80+) C(70+) D(그 외)

#   기대 출력

#     철수  총점 252  평균 84.0  B

#     영희  총점 275  평균 91.7  A

#     민수  총점 200  평균 66.7  D

#     1등: 영희 (91.7점)

# ---------------------------------------------------------

# # 학생 성적 정보를 담은 딕셔너리
# students = {"철수": [90, 85, 77], "영희": [95, 92, 88], "민수": [60, 72, 68]}

# # 등수 비교하기
# number_1 = sum(students.get("철수")) / len(students.get("철수"))
# number_1_stu = "철수"


# for i in students:
#     # 각 학생들의 점수 총합
#     stu_sum = sum(students.get(i))
#     # 학생들이 본 시험 갯수
#     subject_len = len(students.get(i))
#     # 학생들의 평균 점수 (소수점 첫째자리까지)
#     stu_avg = round(stu_sum / subject_len, 1)

#     # 평균 등급 조건문
#     if stu_avg >= 90:
#         stu_class = "A"
#     elif stu_avg >= 80:
#         stu_class = "B"
#     elif stu_avg >= 70:
#         stu_class = "C"
#     else:
#         stu_class = "D"

#     # 동점 발생 시, 1등들을 담을 빈 리스트
#     number_1_same = []

#     if number_1 < stu_avg:
#         number_1 = max(number_1, stu_avg)
#         number_1_stu = i
#     elif number_1 == stu_avg:
#         number_1_same.append(i)

#     print(f"{i} 총점 {stu_sum} 평균 {stu_avg} {stu_class}")
# print(f"1등: {number_1_stu} ({number_1}점)")


# ---------------------------------------------------------

# [30] 장바구니 정산

#   ① 주문 내역을 수량과 함께 정리

#   ② 각 항목 소계와 총액 출력

#   ③ 총액이 20000원 이상이면 10% 할인

#   ④ 최종 금액을 천 단위 쉼표로 출력

#   기대 출력
#     아메리카노 2개 = 9,000원
#     케이크 1개 = 6,500원
#     라떼 1개 = 5,000원
#     합계: 20,500원
#     10% 할인 적용
#     최종: 18,450원

# ---------------------------------------------------------

menu = {"아메리카노": 4500, "라떼": 5000, "케이크": 6500}
order = ["아메리카노", "케이크", "라떼", "아메리카노"]

# 존재하는 메뉴 리스트화
menu_ls = list(menu)

# 아메 주문
order_cnt_1 = 0
# 라떼 주문
order_cnt_2 = 0
# 케이크 주문
order_cnt_3 = 0

# 각 메뉴 주문 수량 체크
for i in menu:
    for j in order:
        if i == j and i == menu_ls[0]:
            order_cnt_1 += 1
        elif i == j and i == menu_ls[1]:
            order_cnt_2 += 1
        elif i == j and i == menu_ls[2]:
            order_cnt_3 += 1

# 각 메뉴 주문가
ame_sum_price = menu.get(menu_ls[0]) * order_cnt_1
latte_sum_price = menu.get(menu_ls[1]) * order_cnt_2
cake_sum_price = menu.get(menu_ls[2]) * order_cnt_3

# 주문가 총액
all_sum_price = ame_sum_price + latte_sum_price + cake_sum_price

# 20000원 이상 할인 적용
if all_sum_price >= 20000:
    dc_msg = "10% 할인 적용"
    sum_price_dc = int(all_sum_price - (all_sum_price * 0.1))


print(f"{menu_ls[0]} {order_cnt_1}개 = {ame_sum_price:,}원")
print(f"{menu_ls[2]} {order_cnt_3}개 = {cake_sum_price:,}원")
print(f"{menu_ls[1]} {order_cnt_2}개 = {latte_sum_price:,}원")
print(f"합계: {all_sum_price:,}원")
if bool(dc_msg) == True:
    print(dc_msg)
    print(f"최종: {sum_price_dc:,}원")
else:
    print(f"최종: {all_sum_price:,}원")

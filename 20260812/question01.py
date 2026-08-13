# [문제 1] 나눗셈 3번 하기

# 3번 반복하여 한 쌍으로 숫자 받기
# for _ in range(3):
#     try:
#         # 값을 받는 곳 (기본 str)
#         num1 = input("숫자1: ")
#         num2 = input("숫자2: ")

#         # input으로 받은 값들을 형변환(정수)을 거쳐 담는 변수들
#         num1 = int(num1)
#         num2 = int(num2)

#         # 정수형 변수들 나누기 계산 후 변수에 담기
#         divide = num1 / num2
#         print(f"결과: {round(divide, 2)}")

#     except ZeroDivisionError:
#         # num2가 0이면 나눌 수 없는 에러가 오는 곳
#         if num2 == 0:
#             print("0으로 나눌 수 없습니다")

#     except ValueError:
#         # 정수형 변환을 할 수 없는 input() 에러가 오는 곳
#         print("숫자를 입력하세요")


# [문제 2] 숫자만 골라서 더하기
# 정수값들을 저장할 빈 리스트
# int_list = []
# for _ in range(5):
#     try:
#         # 값을 입력받기
#         value = input("값: ")

#         # 받은 값을 정수로 변환 (형변환이 불가능한 값은 에러로 이동)
#         value = int(value)

#         # 정수 변환이 성공한 값들을 전역 변수에 저장한 빈 리스트에 이동
#         int_list.append(value)

#     except ValueError:
#         # 정수로 변환이 불가능한 값이 있으면 예외처리 에러 메시지 출력
#         print(f"{value}은(는) 숫자가 아닙니다")

# # 5번 반복하여 값을 입력 받은 후 최종적으로 저장된 리스트 값의 개수
# print(f"유효한 값: {len(int_list)}개")

# # 저장된 정수 리스트 값들의 총합
# print(f"합계: {sum(int_list)}")


# [문제 3] 나이 확인기
# for _ in range(3):
#     try:
#         get_age = input("나이를 입력하세요 (숫자만): ")
#         get_age = int(get_age)
#         if 20 <= get_age <= 122:
#             print("성인입니다")
#         elif 0 <= get_age < 20:
#             print("미성년자입니다")
#         elif get_age > 122:
#             print("비현실적인 나이입니다")
#         elif get_age < 0:
#             print("나이는 0보다 작을 수 없습니다")
#     except ValueError:
#         print("숫자를 입력하세요")

# [문제 4] 리스트에서 값 꺼내기
# data = [10, 20, 30, 40, 50]
# # 정상범위 인덱스 번호 입력 회수
# success = 0

# for _ in range(3):
#     try:
#         idx_catch = input("번호(0~4) : ")
#         idx_catch = int(idx_catch)
#         print(f"값: {data[idx_catch]}")
#         success += 1
#     except IndexError:
#         print("그 번호는 없습니다")
# print(f"성공: {success}번")


# [문제 5] 과일 가격표
# price = {"사과": 1000, "바나나": 1500, "포도": 3000}

# # print("사과" in price) # True
# # print("수박" in price) # False

# sum_price = []

# # 겉 for문: 1번의 반복
# for _ in range(1):
#     # 속 for문: 딕셔너리 price 데이터 개수 만큼 반복 작업 (3번)
#     for fp in price:
#         try:
#             fruit = input("과일 이름: ")
#             if (fruit in price) == True:
#                 print(f"{fp}: {price.get(fp)}")
#                 sum_price.append(price.get(fp))
#             else:
#                 raise ValueError("그런 과일은 없습니다")
#         except ValueError as e:
#             print(e)
# print(f"총 가격: {sum(sum_price)}원")


# [문제 6] 제대로 넣을 때까지 다시 묻기

# 올바른 값들을 모은 빈 리스트
# (리스트 개수가 3개이면 즉각 반복문 종료)
# right_number = []

# while True:
#     try:
#         nums = input("숫자(1~10) : ")
#         one_ten = int(nums)
#         if 1 <= one_ten <= 10:
#             right_number.append(one_ten)
#             if len(right_number) >= 3:
#                 print(f"입력한 숫자: {right_number}")
#                 print(f"합계: {sum(right_number)}")
#                 break
#         else:
#             # raise IndexError("1~10 사이만 가능합니다")
#             print("1~10 사이만 가능합니다")
#     # except IndexError as e:
#     #     print(e)
#     except ValueError:
#         print("숫자를 입력하세요")


# [문제 7] 점수로 학점 매기기

# 입력 받은 학생들 점수를 저장하는 빈 리스트
# 학생 3명의 점수를 입력 받고 종료
# score_ls = []


# # 학점을 만들기 위한 함수
# def score_class(scores):
#     for ss in scores:
#         if ss >= 90:
#             print("학점: A")
#             # 비교 후 리스트(score_ls) 리셋 작업
#             del scores[0]
#         elif ss >= 80:
#             print("학점: B")
#             # 비교 후 리스트(score_ls) 리셋 작업
#             del scores[0]
#         elif ss >= 70:
#             print("학점: C")
#             # 비교 후 리스트(score_ls) 리셋 작업
#             del scores[0]
#         elif 0 <= ss < 70:
#             print("학점: F")
#             # 비교 후 리스트(score_ls) 리셋 작업
#             del scores[0]
#         else:
#             # 범위 밖 예외처리 (raise로 에러 일으키기 - 함수 내)
#             raise IndexError("0~100 사이만 가능합니다")


# for _ in range(3):
#     try:
#         score = input("점수 : ")
#         score = int(score)
#         if 0 <= score <= 100:
#             score_ls.append(score)
#             # 함수에 score_ls를 파라미터로 전달
#             score_class(score_ls)
#         else:
#             # 범위 밖 예외처리
#             raise IndexError("0~100 사이만 가능합니다")
#     except ValueError:
#         # 문자 입력 시, 에러 예외처리
#         print("숫자만 입력이 가능합니다")
#     except Exception as e:
#         print(e)

# [문제 8] 간단 계산기

# for _ in range(3):
#     try:
#         num1 = input("숫자1 : ")
#         oper = input("연산자(+ - * /) : ")
#         num2 = input("숫자2 : ")

#         num1 = int(num1)
#         num2 = int(num2)

#         if oper == "+":
#             plus = num1 + num2
#             print(f"결과: {plus}")
#         elif oper == "-":
#             minus = num1 - num2
#             print(f"결과: {minus}")
#         elif oper == "*":
#             multiple = num1 * num2
#             print(f"결과: {multiple}")
#         elif oper == "/":
#             divide = num1 / num2
#             print(f"결과: {divide}")
#         else:
#             raise Exception("모르는 연산자입니다")

#     except ZeroDivisionError:
#         if oper == "/" and num2 == 0:
#             print("0으로 나눌 수 없습니다")

#     except ValueError:
#         print("숫자를 입력하세요")

#     except Exception as e:
#         print(e)


# [문제 9] 이름과 점수 나눠 담기

# 쉼표(',')를 포함해서 두 개의 값을 받게하는 형식
# 함수 split() 필수 사용
# name, score = input("이름, 점수: ").split(",")
# print(name)
# print(int(score))

# # 두 input() 값을 저장 할 빈 딕셔너리
# name_score = {}


# # 두 input() 값을 처리 할 함수
# def save(score_dic):
#     for k in score_dic:
#         print(f"{k}: {score_dic.get(k)}점")


# for _ in range(3):
#     try:
#         # 두 가지 input()을 담는 것을 우선 한 가지 변수에 저장한다
#         stu_info = input("이름, 점수: ")
#         if "," in stu_info:
#             # 만약 input()에 ','를 포함할 경우
#             name, score = stu_info.split(
#                 ","
#             )  # ','는 필수 포함 => split()을 사용했기 때문에
#             score = int(score)
#             if (name in name_score) == False:
#                 name_score[name] = score
#         else:
#             # 필수로 사용해야 할 ','를 포함하지 않았을 경우에 에러 발생 시키기
#             raise Exception("이름,점수 형태로 입력하세요")

#     except ValueError:
#         # score에 정수 변환이 불가능한 문자열을 입력했을 시
#         print("점수는 숫자여야 합니다")

#     except Exception as e:
#         print(e)
# save(name_score)


# [문제 10] 종합 - 성적 관리

# 학생 성적 담을 빈 딕셔너리
stu_test = {}


#   (1) 점수 하나를 올바르게 받아내는 함수 (재입력 포함)
def right_score(number):
    score = int(number)
    if score is int and 0 <= score <= 100 and (stu_name in stu_test) is False:
        stu_test[stu_name] = score
    elif score < 0 and score > 100:
        print("0~100 사이만 가능합니다")


#   (2) 이름과 점수를 받아 성적표를 출력하는 함수
def report_card(name, score):
    if (name in stu_test) == False:
        stu_test[name] = score


for _ in range(3):
    try:
        stu_name = input("이름 : ")
        if stu_name is False:
            raise ValueError("이름을 입력하세요")
        stu_score = input("점수 : ")
        stu_score = int(stu_score)
        right_score(stu_score)
        report_card(stu_name, stu_score)

    except ValueError:
        print("숫자를 입력하세요")
        stu_score = int(input("점수 : "))
        # 다시 받은 정수값을 이용해서 각각 함수 파라미터로 전달
        right_score(stu_score)
        report_card(stu_name, stu_score)

    except Exception as e:
        print(e)

# 딕셔너리에 키, 값이 잘 저장되었는지 확인용
# print(stu_test)

sum_score = 0
number_one = list(stu_test.keys())[0]
high_score = list(stu_test.values())[0]
for item in stu_test:
    sum_score += stu_test.get(item)
    data_cnt = len(stu_test)
    score_avg = round(sum_score / data_cnt, 2)

    if high_score < stu_test.get(item):
        high_score = stu_test.get(item)
        number_one = item
    print(f"{item}: {stu_test.get(item)}점")
print(f"평균: {score_avg}")
print(f"1등: {number_one}")

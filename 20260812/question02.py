# # [문제 1] 계산 기록이 남는 나눗셈기

# # 나눗셈 계산
# divide = 0

# # 성공한 나눗셈 계산식 리스트
# success_ls = []


# # 두 값을 받아 나눗셈 결과를 반환
# def divide_calc(first, second):
#     # 계산 성공 (로컬)
#     local_success = 0

#     # 정상적인 나눗셈 계산
#     divide = round(first / second, 2)

#     # 풀어 쓴 계산식
#     divide_calc = f"{first}/{second} = {divide}"
#     print(divide_calc)

#     # 위의 값을 리스트에 보관
#     success_ls.append(divide_calc)

#     # 성공 카운트 업데이트
#     local_success += 1
#     return local_success


# # 성공/실패 기록 받아 성공률 반환
# def suc_fail(success, fail):
#     if success == fail == 0:
#         return 0.0
#     suc_avg = round(success / (success + fail), 2)
#     return suc_avg


# # 최종 기록 출력
# def final_cnt(num1, num2):
#     print("[성공 기록]")
#     for calc in success_ls:
#         if len(success_ls) != 0:
#             print(f"{calc}")
#         else:
#             print("계산한 식이 없습니다")
#     if num1 == "q" and num2 == "":
#         # 처음 순서에 "q"를 입력하여 종료할 경우
#         print(f"성공률: {avg_cnt * 100}%")

# # 계산 성공 (전역)
# g_success_cnt = 0

# # 계산 오류
# g_fail_cnt = 0

# while True:
#     try:
#         num1 = input("숫자1(종료: q) : ")
#         num2 = ""
#         num1 = int(num1)
#         if type(num1) is int:
#             num2 = input("숫자2 : ")
#             num2 = int(num2)
#             g_success_cnt = divide_calc(num1, num2)
#     except ZeroDivisionError:
#         if num2 == 0:
#             g_fail_cnt += 1
#             print("실패 - 0으로 나눌 수 없습니다")

#     except ValueError:
#         if num1 == "q" and num2 == "":
#             avg_cnt = suc_fail(g_success_cnt, g_fail_cnt)
#             final_cnt(num1, num2)
#             break
#         else:
#             g_fail_cnt += 1
#             print("실패 - 숫자를 입력하세요")


# # [문제 1] 계산 기록이 남는 나눗셈기

# # 계산 성공
# success_cnt = 0

# # 계산 오류
# fail_cnt = 0

# # 실행 합계
# sum_cnt = 0

# # 나눗셈 계산
# divide = 0

# # 성공한 나눗셈 계산식 리스트
# success_ls = []

# while True:
#     try:
#         num1 = input("숫자1(종료: q) : ")
#         num2 = ""
#         num1 = int(num1)
#         if type(num1) is int:
#             num2 = input("숫자2 : ")
#             num2 = int(num2)

#             # 정상적인 나눗셈 계산
#             divide = round(num1 / num2, 2)

#             # 풀어 쓴 계산식
#             divide_calc = f"{num1}/{num2} = {divide}"

#             # 위의 값을 리스트에 보관
#             success_ls.append(divide_calc)

#             # 계산 성공 카운트 추가
#             success_cnt += 1

#     except ZeroDivisionError:
#         if num2 == 0:
#             fail_cnt += 1
#             print("실패 - 0으로 나눌 수 없습니다")

#     except ValueError:
#         if num1 == "q":
#             sum_cnt = success_cnt + fail_cnt
#             print("[성공 기록]")
#             for calc in success_ls:
#                 if len(success_ls) != 0:
#                     print(f"{calc}")
#                 else:
#                     print("계산한 식이 없습니다")
#             if num1 == "q" and num2 == "" and sum_cnt == 0:
#                 # 처음 순서에 "q"를 입력하여 종료할 경우
#                 print(f"성공률: {success_cnt}.{sum_cnt}%")
#                 break
#             print(f"성공률: {round((success_cnt / sum_cnt), 1) * 100}%")
#             break
#         else:
#             fail_cnt += 1
#             print("실패 - 0으로 나눌 수 없습니다")




# ------------------------------------------------------
# [문제 2] 데이터 정제기
# ------------------------------------------------------

# 여러 값을 한 줄로 입력받아, 유효한 숫자만 골라 통계를 내시오.

# [입력 형식]
#   input("값 입력(공백 구분) : ")   -> 한 줄에 여러 값, 공백으로 구분
#   입력은 1회만 받는다
#   예) 10 20 abc 9999 30 -5

# [조건]
#   - 반복문으로 값을 하나씩 정수 변환
#   - 변환 실패 → "무시된 값" 목록에 저장
#   - 변환은 됐지만 0 미만 또는 1000 초과 → raise 로 처리해 "범위 초과" 목록에 저장
#   - 최댓값·최솟값은 max/min 없이 반복문으로 직접 구할 것
#   - 유효 값이 하나도 없으면 평균 계산에서 나는 예외를 처리

# [출력 형식]
#   "무시된 값 : abc"            (여러 개면 쉼표로 이어서, 없으면 이 줄 생략)
#   "범위 초과 값 : 9999, -5"     (없으면 이 줄 생략)
#   "합계 : 60"
#   "평균 : 20.00"
#   "최대 : 30 / 최소 : 10"
#   유효 값이 없으면 "유효한 숫자가 없습니다" 만 출력

# [필요한 함수 : 3개]
#   (1) 값 하나를 검사해 정수로 반환 (문제가 있으면 예외 발생)
#   (2) 숫자 리스트를 받아 (합계, 평균, 최댓값, 최솟값) 반환
#   (3) 결과를 출력

# [실행 예시]
#   값 입력(공백 구분) : 10 20 abc 9999 30 -5
#   무시된 값 : abc
#   범위 초과 값 : 9999, -5
#   합계 : 60
#   평균 : 20.00
#   최대 : 30 / 최소 : 10

ex_int = []
over_int = []


# # 정수 반환 함수
# def chg_int(value):
#     try:
#         int_var = int(value)
#         if 0 > value or 1000 < value:
#             over_int.append(value)
#         return int_var
#     except ValueError:
#         ex_int.append(value)


# # 범위 내 숫자 리스트
# def right_int(number):
#     num_list = []
#     num_list.append(number)
#     max_n = 0
#     min_n = 0
#     for n in num_list:
#         if max_n < n:
#             max_n = n
#         if min_n > n:
#             min_n = n
#     return max_n, min_n, num_list


# while True:
#     rd_value = input("값 입력(공백 구분) : ")
#     param = chg_int(rd_value)
#     if type(param) is int:
#         right_int(param)
#     max_number, min_number, right_num_ls = right_int(param)

#     if rd_value == 'end':
#         break
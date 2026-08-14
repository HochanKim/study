# [문제 1] 계산 기록이 남는 나눗셈기
# 계산 성공 (전역)
g_success_cnt = 0

# 계산 오류
g_fail_cnt = 0

# 실행 합계
sum_cnt = 0

# 나눗셈 계산
divide = 0

# 성공한 나눗셈 계산식 리스트
success_ls = []


# 두 값을 받아 나눗셈 결과를 반환
def divide_calc(first, second):
    # 계산 성공 (로컬)
    local_success = 0

    # 정상적인 나눗셈 계산
    divide = round(first / second, 2)
    # 풀어 쓴 계산식
    divide_calc = f"{first}/{second} = {divide}"
    print(divide_calc)
    # 위의 값을 리스트에 보관
    success_ls.append(divide_calc)
    # 계산 성공 카운트 추가
    local_success += 1
    return local_success


# 성공/실패 기록 반환


def suc_fail(success, fail):
    if success >= 1:
        return success
    if fail >= 1:
        return fail


while True:
    try:
        num1 = input("숫자1(종료: q) : ")
        num2 = ""
        num1 = int(num1)
        if type(num1) is int:
            num2 = input("숫자2 : ")
            num2 = int(num2)
            g_success_cnt = divide_calc(num1, num2)
    except ZeroDivisionError:
        if num2 == 0:
            g_success_cnt = 0
            g_fail_cnt += 1

            print("실패 - 0으로 나눌 수 없습니다")

    except ValueError:
        if num1 == "q":
            sum_cnt = g_success_cnt + g_fail_cnt
            print("[성공 기록]")
            for calc in success_ls:
                if len(success_ls) != 0:
                    print(f"{calc}")
                else:
                    print("계산한 식이 없습니다")
            if num1 == "q" and num2 == "" and sum_cnt == 0:
                # 처음 순서에 "q"를 입력하여 종료할 경우
                print(f"성공률: {g_success_cnt}.{sum_cnt}%")
                break
            print(f"성공률: {round((g_success_cnt / sum_cnt), 1) * 100}%")
            break
        else:
            g_fail_cnt += 1
            print("실패 - 0으로 나눌 수 없습니다")


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

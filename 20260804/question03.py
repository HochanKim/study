# =========================================================
#  일급 비밀 보안 시스템
#  사용 범위: 변수 / 자료형 / 형변환 / 입출력 / 연산자 / 조건문
#  ※ 반복문, 리스트, 함수, 문자열 인덱싱은 사용 금지
# =========================================================

# 당신은 적 기지에 잠입한 특수 요원입니다.
# 메인 서버실로 가는 마지막 보안 문은 3중 잠금 장치로 보호되고 있습니다.
# 제한 시간 안에 모든 관문을 통과하십시오.

# ---------------------------------------------------------
#  [1단계] 요원 정보 입력
# ---------------------------------------------------------

# input()으로 아래 5가지를 순서대로 입력받고, 알맞게 형변환하세요.

#   ① 요원 코드명        (문자열)   예: Falcon
code_name = input("CODE NAME? : ")

#   ② 5자리 보안 코드     (정수)     예: 84269
security_code = int(input("PASSWORD NUMBER? : "))

#   ③ 마스터키 등급       (문자열)   "S" / "A" / "N" 중 하나
master_key_level = input("당신의 마스터키 등급을 입력하세요 : ")

#   ④ 현재 체온          (실수)     예: 36.5
body_temp = float(input("당신의 체온을 입력하세요 : "))

#   ⑤ 남은 시간(초)      (정수)     예: 200
spare_time = int(input("현재 남은 시간은? (초 단위) : "))

maan = security_code // 10000
cheon = (security_code // 1000) % 10
baek = (security_code // 100) % 10
sip = (security_code // 10) % 10
il = (security_code // 1) % 10
code_numbers = [maan, cheon, baek, sip, il]
print("→ 분해: ", maan, cheon, baek, sip, il)


if maan == il and cheon == sip:
    print("복제된 코드 감지! 즉시 폐쇄합니다.")
else:
    # 세 가지 조건을 각각 판별하세요.
    #   조건 A : (만의 자리 + 천의 자리) >= (십의 자리 + 일의 자리)
    cond1 = 1 if (maan + cheon) >= (sip + il) else 0

    #   조건 B : 보안 코드 전체가 짝수이거나 3의 배수
    cond2 = 1 if code_numbers[0] % 2 == 0 or code_numbers[0] % 3 == 0 else 0
    cond2 = 1 if code_numbers[1] % 2 == 0 or code_numbers[1] % 3 == 0 else 0
    cond2 = 1 if code_numbers[2] % 2 == 0 or code_numbers[2] % 3 == 0 else 0
    cond2 = 1 if code_numbers[3] % 2 == 0 or code_numbers[3] % 3 == 0 else 0
    cond2 = 1 if code_numbers[4] % 2 == 0 or code_numbers[4] % 3 == 0 else 0

    #   조건 C : 백의 자리 숫자가 홀수
    cond3 = 1 if baek % 2 == 1 else 0

    # 통과 기준은 마스터키 등급에 따라 달라집니다.
    #   등급 "S" : 조건 A 만 만족하면 통과
    if master_key_level == "S":
        if cond1 == 1:
            passed = True
        else:
            passed = False
            print("보안 시스템 작동! 침입자를 체포하라!")
    #   등급 "A" : 조건 A 를 만족하고, B 와 C 중 하나 이상 만족하면 통과
    if master_key_level == "A":
        if cond1 == 1 and (cond2 == 1 or cond3 == 1):
            passed = True
        else:
            passed = False
            print("보안 시스템 작동! 침입자를 체포하라!")
    #   등급 "N" : 조건 A, B, C 를 모두 만족해야 통과
    if master_key_level == "N":
        if cond1 == 1 and (cond2 == 1 and cond3 == 1):
            passed = True
        else:
            print("보안 시스템 작동! 침입자를 체포하라!")
            passed = False

    # ---------------------------------------------------------
    #  [5단계] 2차 보안 - 생체 인식  (1차 통과 시에만)
    # ---------------------------------------------------------
    body_condition = ""
    basic_danger = ""
    if passed == True and 36.0 <= body_temp <= 37.5:
        body_condition = "정상"
        basic_danger = float(format((maan * cheon) / (sip + 1), ".2f"))
        passed = True
    elif passed == True and (35.0 <= body_temp <= 38.5 and body_condition != "정상"):
        body_condition = "주의"
        basic_danger = float(format(int((maan * cheon) / (sip + 1)) * 1.5, ".2f"))
        passed = True
    elif passed == True and (35.0 > body_temp or 38.5 < body_temp):
        body_condition = "위독"
        basic_danger = None
        print("생체 신호 위독! 의무실로 강제 이송합니다. (위험도: 측정 불가)")
        passed = False

    # ---------------------------------------------------------
    #  [6단계] 3차 보안 - 시간 제한  (2차 통과 시에만)
    # ---------------------------------------------------------
    need_time = ""
    if passed == True and basic_danger >= 50:
        #   위험도가 50 이상 : 필요 시간 180초
        need_time = 180
        if spare_time >= need_time:
            # 남는 시간이 필요 시간보다 많을 경우
            change_time = spare_time - need_time
            minute = change_time // 60
            second = change_time % 60
        else:
            # 시간이 부족할 경우
            less_time = need_time - spare_time
            minute = less_time // 60
            second = less_time % 60
            print(
                f"시간 초과! 문이 다시 잠겼습니다. (부족한 시간: {minute}분 {second:02d}초)"
            )
            passed = False
    elif passed == True and basic_danger < 50:
        #   위험도가 50 미만 : 필요 시간 60초
        need_time = 60
        if spare_time >= need_time:
            # 남는 시간이 필요 시간보다 많을 경우
            change_time = spare_time - need_time
            minute = change_time // 60
            second = change_time % 60
            passed = True
        else:
            # 시간이 부족할 경우
            less_time = need_time - spare_time
            minute = less_time // 60
            second = less_time % 60
            print(
                f"시간 초과! 문이 다시 잠겼습니다. (부족한 시간: {minute}분 {second:02d}초)"
            )
            passed = False
# ---------------------------------------------------------
#  [7단계] 최종 출력
# ---------------------------------------------------------

# 모든 관문을 통과했다면 아래 형식으로 출력하세요.
if passed == True:
    print(
        f"[{code_name}] 서버실 개방! 상태: {body_condition} / 위험도: {basic_danger} / 잔여 {minute}분 {second:02d}초"
    )


#   "[Falcon] 서버실 개방! 상태: 정상 / 위험도: 12.50 / 잔여 2분 20초"

# ※ 잔여 시간 = 남은 시간 - 필요 시간

#    문을 여는 데 '필요 시간'을 썼으므로 그만큼 빼야 합니다.

#    (예: 남은 200초, 필요 60초 → 잔여 140초 → "2분 20초")

# ※ 위험도는 소수점 둘째 자리까지 표시합니다.

# ※ 코드명은 대괄호로 감싸 출력합니다.

# =========================================================

#  ▣ 테스트 케이스 (이 값으로 확인해 보세요)

# =========================================================

# ① 코드명 Falcon / 코드 84269 / 등급 N / 체온 36.5 / 시간 200

#    → 분해: 8,4,2,6,9

#       A: 8+4=12 >= 6+9=15 ?  → False

#       결과: 보안 시스템 작동! 침입자를 체포하라!

# ② 코드명 Hawk / 코드 96124 / 등급 N / 체온 36.5 / 시간 200

#    → 분해: 9,6,1,2,4

#       A: 15 >= 6 → True

#       B: 96124는 짝수 → True

#       C: 백의 자리 1은 홀수 → True

#       상태 정상 / 위험도 = 9*6/(2+1) = 18.0 / 필요 60초

#       잔여 = 200 - 60 = 140초

#    → [Hawk] 서버실 개방! 상태: 정상 / 위험도: 18.00 / 잔여 2분 20초

# ③ 코드명 Wolf / 코드 84248 / 등급 S / 체온 36.5 / 시간 300

#    → 대칭 코드

#    → 복제된 코드 감지! 즉시 폐쇄합니다.

# ④ 코드명 Bear / 코드 97035 / 등급 S / 체온 38.0 / 시간 300

#    → A: 16 >= 8 → True, 등급 S이므로 통과

#       체온 38.0 → '주의'

#       위험도 = 9*7/(3+1) = 15.75 → 1.5배 = 23.625

#       필요 60초, 남은 300초 → 통과 / 잔여 = 300 - 60 = 240초

#    → [Bear] 서버실 개방! 상태: 주의 / 위험도: 23.62 / 잔여 4분 00초

#       ※ 23.625인데 23.63이 아니라 23.62입니다.

#          파이썬의 반올림은 '가운데 값일 때 짝수 쪽으로' 가기 때문입니다.

#          (자료형 챕터의 float 오차와 이어지는 내용)

# ⑤ 코드명 Snake / 코드 98761 / 등급 S / 체온 36.5 / 시간 100

#    → A: 17 >= 7 → True, 통과

#       정상 / 위험도 = 9*8/(6+1) = 10.28...  50 미만 → 필요 60초

#       남은 100초 → 통과 / 잔여 = 100 - 60 = 40초

#    → [Snake] 서버실 개방! 상태: 정상 / 위험도: 10.29 / 잔여 0분 40초

# ⑥ 코드명 Tiger / 코드 99801 / 등급 S / 체온 34.0 / 시간 300

#    → A: 18 >= 1 → True, 통과 / 체온 34.0 → 위독

#    → 생체 신호 위독! 의무실로 강제 이송합니다. (위험도: 측정 불가)

# ⑦ 코드명 Owl / 코드 99801 / 등급 S / 체온 36.5 / 시간 200

#    → ⑥과 같은 코드지만 체온이 정상이라 이번엔 위험도를 계산합니다.

#       십의 자리가 0 → 위험도 = 9*9/(0+1) = 81.0   ('+1' 이 없으면 여기서 에러)

#       81 >= 50 이므로 필요 180초, 남은 200초 → 통과

#       잔여 = 200 - 180 = 20초

#    → [Owl] 서버실 개방! 상태: 정상 / 위험도: 81.00 / 잔여 0분 20초

# ⑧ 코드명 Bat / 코드 99801 / 등급 S / 체온 36.5 / 시간 115

#    → 필요 180초, 남은 115초 → 부족 65초

#    → 시간 초과! 문이 다시 잠겼습니다. (부족한 시간: 1분 05초)

# ⑨ 코드명 Lynx / 코드 95321 / 등급 A / 체온 36.5 / 시간 200

#    → 분해: 9,5,3,2,1

#       A: 9+5=14 >= 2+1=3 → True

#       B: 95321은 홀수이고 3의 배수도 아님 → False

#       C: 백의 자리 3은 홀수 → True

#       등급 A는 "A 이고 (B 또는 C)" → 통과

#       정상 / 위험도 = 9*5/(2+1) = 15.0 / 필요 60초 / 잔여 = 200-60 = 140초

#    → [Lynx] 서버실 개방! 상태: 정상 / 위험도: 15.00 / 잔여 2분 20초

# ⑩ 코드명 Crow / 코드 95221 / 등급 A / 체온 36.5 / 시간 200

#    → A: True 지만 B(홀수·3의 배수 아님)도 C(백의 자리 2는 짝수)도 False

#    → 보안 시스템 작동! 침입자를 체포하라!

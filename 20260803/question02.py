# 입력 및 형변환 :

# 영화 1인당 관람료 => 변수명: movie_ticket = int(input("1인당 영화 관람료를 입력하세요: "))
# 예매할 인원 수 => 변수명: book_persons = int(input("예매할 인원을 입력하세요: "))
# 팝콘 세트 1개의 가격  => 변수명: pop_corn_set = int(input("구매하고자 할 팝콘 세트 가격을 입력하세요: "))
# 구매할 팝콘 세트 수 => 변수명: buy_set_number = int(input("몇 세트를 구매하실건가요?: "))
# VIP 회원 여부 (문자열 y/n 입력 -> 나중에 bool이나 비교 연산으로 활용)
# => 변수명: vip_person = input("VIP 회원이신가요?: (y/n만 입력 가능)")
# => real_vip = bool("y" == vip_person)
# => none_vip = bool("n" == vip_person)
# 사용자가 가진 현금 총액 => 변수명: all_money = int(input("가지고 있는 현금 총액을 입력하세요: "))

# 연산 (고급 산술, 비교, 논리):

# 기본 영화 금액 = 영화 1인당 가격 x 인원 수
# 기본 팝콘 금액 = 팝콘 가격 x 팝콘 세트 수
# 총 상품 금액 = 영화 금액 + 팝콘 금액
# VIP 할인 적용 (논리/비교 연산 활용): VIP 입력값이 'y'인지 확인하는 비교 연산 결과와 총금액을 엮어서, VIP라면 총금액의 20%를 할인, 아니면 0% 할인을 적용 (단, 조건문 없이 산술 연산으로 처리: 예시 -> VIP 여부(True/False)를 정수로 바꿔서 계산하는 응용 필요!)
# 결제 잔돈 및 10원 단위 절사(버림): 최종 결제 금액의 1의 자리(10원 미만)를 깔끔하게 없애기 위해 정수 나눗셈(/, //, %) 활용
# 최종 구매 성공 조건 (논리 연산 and, not):
# 조건 1: 가진 돈 >= 최종 결제 금액 (충분한 현금)
# 조건 2: 예매 인원이 0명이 아님 (not (인원수 == 0))
# 출력 (print, f-string):

#  •  • 복잡한 영수증 내역 출력 및 최종 시스템 정상 승인 여부(True / False) 출력

print("🎬 VIP 통합 무인 키오스크 시스템 🎬")
print("------------------------------------------------------------------")
movie_ticket = int(input("영화 1인 관람료를 입력하세요 (예: 15000) : "))
book_persons = int(input("예매할 총 인원수를 입력하세요 (예: 3) : "))
pop_corn_set = int(input("팝콘 세트 1개의 가격을 입력하세요 (예: 9000) : "))
buy_set_number = int(input("구매할 팝콘 세트 수를 입력하세요 (예: 2): "))
vip_person = input("VIP 회원이신가요? (y/n만 입력 가능) : ")
all_money = int(input("보유한 현금 총액을 입력하세요 (예: 150000): "))

# 기본 영화 금액
basic_price = movie_ticket * book_persons

# 기본 팝콘 금액
all_pop_price = pop_corn_set * buy_set_number

# 총 금액
last_price = basic_price + all_pop_price

# VIP 할인 적용 여부
vip_dc_apply = bool("y" and vip_person == "y")
vip_dc_price = last_price * 0.2 * int(vip_dc_apply)
# 할인 금액 10원 단위 절사
vip_dc_ten = int((vip_dc_price // 10) * 10)

# 거스름돈
change = int(all_money - (last_price - vip_dc_price))

# 정상 예매 승인
normal_book = bool(change > 0 and "1 == 1")

print("=" * 10)
print("          [최종 정산 및 영수증]         ")
print("=" * 10)

print(f"● 영화 관람료 합계 : {basic_price}원")
print(f"● 팝콘 세트 합계   : {all_pop_price}원")
print(f"● 총 주문 금액     : {(last_price)}원")
print(f"● VIP 할인 적용    : -{vip_dc_ten}원 (VIP 회원 여부: {vip_dc_apply})")
print("● 10원 단위 절사    : 적용 완료")
print("-" * 10)
print(f"● 최종 결제 금액  : {int(last_price - vip_dc_price)}원")
print(f"● 보유 현금 총액  : {all_money}원")
print(f"● 거스름돈        : {change}원")
print("-" * 10)
print(f"● 정상 예매 승인  : {normal_book}")
print("=" * 10)

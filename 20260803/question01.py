# 스마트 무인 카페
# 입력 (input, 형변환):

# 아메리카노 1잔의 가격
# => 변수명 선언 (americano)
# => americano = int(input("아메리카노 1잔의 가격을 입력하세요: "))

# 주문할 아메리카노 잔 수
# => 변수명 선언 (order)
# => order = int(input("몇 잔을 주문하실 건가요?: "))

# 카페에서 제공하는 기본 할인율 %
# => 변수명 선언 (discount)
# => discount = float(input("오늘의 할인율을 입력하세요: "))

# 사용자가 가진 현금 총액
# => 변수명 선언 (pocket_money)
# => pocket_money = int(input("지갑에 가진 현금 총액을 입력하세요: "))

# 연산 (산술, 비교, 논리):
# 산술 1) 구매 총액 => all_price = americano * order
# 산술 2) 할인율 적용 => dc_price = (americano * order) * discount
# 산술 3) 할인율이 적용된 금액 => real_price = all_price - dc_price

# 총 상품 금액 = 가격 x 잔 수
# 할인된 금액 = 총 상품 금액 x (할인율 / 100)
# 최종 결제 금액 = 총 상품 금액 - 할인된 금액 (정수형으로 형변환 필요 시 처리)
# 구매 가능 여부 확인 (비교 연산): 현금 총액 >= 최종 결제 금액
# 잔돈 계산 = 현금 총액 - 최종 결제 금액
# 출력 (print):

# 영수증 형태로 깔끔하게 출력하기
# 비교 연산 결과를 통해 구매 성공 여부(True / False) 출력하기

# 변수 입력란
americano = int(input("아메리카노 1잔의 가격을 입력하세요: "))
order = int(input("몇 잔을 주문하실 건가요?: "))
discount = float(input("오늘의 할인율을 입력하세요: "))
discount_rate = discount * 0.01
pocket_money = int(input("지갑에 가진 현금 총액을 입력하세요: "))


# 계산식 (할인 전 주문 총액, 할인 가격, 할인이 적용된 총 금액)
all_price = americano * order  # 할인 전 주문 총액
dc_price = int((americano * order) * discount_rate)  # 할인 가격
real_price = all_price - dc_price  # 할인이 적용된 총 금액

print("=" * 10)
print("          [영수증 및 결제 내역]         ")
print("=" * 10)
print(f"● 메뉴 가격: {americano}원")
print(f"● 주문 수량: {order}잔")
print(f"● 총 주문액: {all_price}원")
print(f"● 할인 적용: -{dc_price}원 ({discount}%)")
print("-" * 10)
print(f"● 최종 결제: {int(real_price)}원")
print(f"● 보유 현금: {pocket_money}원")
print("-" * 10)
print(f"● 결제 가능 여부: {pocket_money > real_price}")
print(f"● 남은 돈: {pocket_money - real_price}원")
print("=" * 10)
print("이용해 주셔서 감사합니다. 좋은 하루 보내세요! 😀")

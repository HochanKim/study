# ================================================================
# 파이썬 종합 연습문제 20제
# 변수 / 자료형 변환 / 입출력 / 연산자 / 조건문 / 딕셔너리
# ================================================================

# 사용 O : 변수, input(), print(), int() float() str(), 산술연산자,
#          비교연산자, 논리연산자(and or not), if / elif / else,
#          리스트, 딕셔너리
#          (딕셔너리 안에 딕셔너리, 딕셔너리 안에 리스트가 들어갑니다)
# 사용 X : for 문, while 문, 함수 정의(def)

# [입력 안내]
#   - 값은 input() 으로 직접 받으세요.
#   - input() 은 항상 문자열을 돌려줍니다. 숫자로 계산하려면 반드시 변환하세요.
#   - 입력 안내 문구는 자유롭게 작성해도 됩니다.
#   - 아래 <입력값> 은 채점 기준 예시입니다. 다른 값으로도 테스트하세요.
#   - 출력 문구는 예시와 똑같지 않아도 됩니다. 필요한 정보가 나오면 정답입니다.

# [공통 가정]
#   - 숫자를 입력하라는 문제에서는 항상 올바른 형태의 숫자가 입력된다고 가정합니다.
#     ("abc" 같은 잘못된 입력은 처리하지 않아도 됩니다.)
#   - 나누기를 하는 문제에서 0 은 입력하지 않는다고 가정합니다.
#   - 딕셔너리 자료는 문제에 주어진 것을 그대로 복사해서 사용하세요.

print("[문제 1] 회원 카드 만들기")
print()

name = input("당신의 이름을 입력하세요: ")
age = int(input("당신의 나이를 입력하세요 (예: 20): "))
adult = ""
if age >= 19:
    adult = True
else:
    adult = False

# 회원카드 딕셔너리 생성
member_card = {"name": name, "age": age, "adult": adult}
print(member_card)
print()
print("=" * 30)

print("[문제 2] 연산 결과 딕셔너리")
num1 = int(input("숫자1: "))
num2 = int(input("숫자2: "))
operator = input("연산자: ")

# 연산하여 받는 값 변수
calc = 0

# 받은 값들의 연산 (if 필터를 거쳐 변수에 저장)
plus = num1 + num2
minus = num1 - num2
multiply = num1 * num2

if num2 != 0:
    divide = num1 / num2
    share = num1 // num2
    excess = num1 % num2
else:
    divide = share = excess = "0으로 나눌 수 없습니다"
    print("0으로 나눌 수 없습니다")

square = num1**num2

all_calc_dic = {
    "+": plus,
    "-": minus,
    "*": multiply,
    "/": divide,
    "//": share,
    "%": excess,
    "**": square,
}

# 입력한 연산자에 맞게 계산하기 위한 조건문 생성
if operator == "+":
    calc = plus = num1 + num2
    print(f"{num1} {operator} {num2} = {calc}")
    print(all_calc_dic)
elif operator == "-":
    calc = minus = num1 - num2
    print(f"{num1} {operator} {num2} = {calc}")
    print(all_calc_dic)
elif operator == "*" or operator == "x":
    calc = multiply = num1 * num2
    print(f"{num1} {operator} {num2} = {calc}")
    print(all_calc_dic)
elif (operator == "/" or operator == "÷") and num2 != 0:
    calc = divide = num1 / num2
    print(f"{num1} {operator} {num2} = {calc}")
    print(all_calc_dic)
    if num2 == 0:
        calc = divide = "0으로 나눌 수 없습니다"
        print(divide)
elif operator == "//" and num2 != 0:
    calc = share = num1 // num2
    print(f"{num1} {operator} {num2} = {calc}")
    print(all_calc_dic)
    if num2 == 0:
        calc = share = "0으로 나눌 수 없습니다"
        print(share)
elif operator == "%" and num2 != 0:
    calc = excess = num1 % num2
    print(f"{num1} {operator} {num2} = {calc}")
    print(all_calc_dic)
    if num2 == 0:
        calc = excess = "0으로 나눌 수 없습니다"
        print(excess)
elif operator == "**":
    calc = square = num1**num2
    print(f"{num1} {operator} {num2} = {calc}")
    print(all_calc_dic)
elif operator not in ["+", "-", "*", "x", "/", "÷", "//", "%", "**"]:
    print("적절한 연산 기호가 아닙니다.")
print()
print("=" * 30)

print("[문제 3] 카페 주문과 무료 배송")
menu = {
    "아메리카노": {"price": 3000, "kcal": 10},
    "라떼": {"price": 4000, "kcal": 180},
    "케이크": {"price": 5500, "kcal": 420},
}

# 메뉴 이름과 수량을 입력받아 총 금액과 총 칼로리를 출력하세요.
order_menu = input("주문하실 메뉴를 입력하세요: ")
number = int(input("수량을 입력하세요 (예: 2): "))
print()

# 없는 메뉴면 안내 문구를 출력합니다.
if menu.get(order_menu) == None:
    print("해당 메뉴는 없는 상품입니다.")
else:
    price = int(menu[f"{order_menu}"]["price"] * number)
    kcal_info = int(menu[f"{order_menu}"]["kcal"] * number)
    print(f"{order_menu} X {number} = {price} / {kcal_info}kcal")

# 총 금액이 10000원 이상이면 무료 배송 대상,
# 미만이면 얼마가 더 필요한지 출력하세요.
if menu.get(order_menu) != None and price >= 10000:
    print("무료 배송 대상입니다.")
elif menu.get(order_menu) != None and price < 10000:
    print(f"{10000 - price}원 어치 더 구매하시면 무료 배송 대상입니다.")
print()
print("=" * 30)

print("[문제 4] 숫자 분석 딕셔너리")
#   number  : 입력받은 수
number = int(input("숫자를 입력하세요: "))

#   짝수    : 짝수인지 여부를 True / False 로 저장
if number % 2 == 0:
    even = True
    num_type = "짝수"
else:
    even = False
    num_type = "홀수"

#   몫      : 3으로 나눈 몫
divide_calc = number // 3

#   나머지  : 3으로 나눈 나머지
excess_calc = number % 3

num_dic = {"number": number, "짝수": even, "몫": divide_calc, "나머지": excess_calc}

print(num_dic)
print(f"{number}은(는) {num_type}입니다.")
print()
print("=" * 30)

print("[문제 5] 지폐 교환기")
change_money = int(input("바꾸고자 할 돈의 액수를 입력하세요: "))
bills = {"오만원권": 50000, "만원권": 10000, "천원권": 1000}
# 각각 몇 장씩 바꿀 수 있는지 출력하고 마지막에 남는 돈을 출력하세요.

fifty_thou = change_money // bills["오만원권"]
ten_thou = (change_money // bills["만원권"]) - (5 * fifty_thou)
one_thou = change_money // bills["천원권"] - ((5 * 10 * fifty_thou) + (10 * ten_thou))
excess = change_money % bills["천원권"]
# 권종 금액은 반드시 아래 딕셔너리에서 꺼내 쓰세요.

print(f"오만 원권 {fifty_thou}장")
print(f"만 원권 {ten_thou}장")
print(f"천 원권 {one_thou}장")
print(f"남는 돈 {excess}원")
print()
print("=" * 30)

print("[문제 6] BMI 계산기")
weight = float(input("몸무게를 입력하세요 (예: 75.59kg => 75.59): "))
weight = round(weight, 2)
height = float(input("키를 입력하세요 (예: 185cm => 1.85): "))
height = round(height, 2)


bmi = round(weight / (height**2), 2)


if bmi < 18.5:
    condition = "저체중"
elif 18.5 <= bmi < 23:
    condition = "정상"
elif 23 <= bmi < 25:
    condition = "과체중"
else:
    condition = "비만"
bmi_dic = {"bmi": bmi, "판정": condition}
print(bmi_dic)
print(f"BMI {bmi} -> {condition}")

print()
print("=" * 30)

print("[문제 7] 초를 시분초로 바꾸기")
seconds = int(input("초 단위의 숫자를 아무거나 입력하세요 (예: 1650초 => 1650): "))
hours = seconds // 3600
if hours == 0:
    minutes = seconds // 60
else:
    minutes = (seconds - 3600) // 60
last_seconds = (seconds - 3600) % 60

print(f"{seconds}초 = {hours}시간 {minutes}분 {last_seconds}초")
print()
print("=" * 30)

print("[문제 8] 온도 변환과 날씨 안내")
# 섭씨 변수
sub_c_temp = float(input("섭씨 온도를 입력하세요: "))

# 화씨 변수
usa_temp = (sub_c_temp * 9) / 5 + 32

if sub_c_temp >= 28:
    weather = "무더위입니다."
elif 15 <= sub_c_temp < 28:
    weather = "활동하기 좋은 날씨입니다."
else:
    weather = "쌀쌀합니다."

print(f"섭씨 {sub_c_temp} = 화씨 {usa_temp}")
print(f"{weather}")

print()
print("=" * 30)

print("[문제 9] 요일 조회기")
week = {
    1: {"name": "월요일", "weekend": False},
    2: {"name": "화요일", "weekend": False},
    3: {"name": "수요일", "weekend": False},
    4: {"name": "목요일", "weekend": False},
    5: {"name": "금요일", "weekend": False},
    6: {"name": "토요일", "weekend": True},
    7: {"name": "일요일", "weekend": True},
}

number = int(input("1부터 7까지 숫자 입력: "))
if week.get(number) == None:
    text = "입력된 숫자가 아닙니다."
else:
    print(f"{number}번째 요일: {week[number]['name']}")
    rest = week[number]["weekend"]
    if rest == True:
        text = "주말입니다"
    else:
        text = "평일입니다"
print(text)

print()
print("=" * 30)

print("[문제 10] 학생 성적 조회")
scores = {"김철수": [90, 85, 100], "이영희": [70, 65, 80]}
stu_name = input("학생 이름을 입력하세요: ")

if scores.get(stu_name) == None:
    print("입력된 학생이 아닙니다.")
else:
    print(f"{stu_name} 점수: {scores[stu_name]}")
    print(f"1과목 점수: {scores[stu_name][0]}")
    # 점수 합산
    sum_scores = sum(scores[stu_name])
    # 점수 평균
    avg_scores = round(sum(scores[stu_name]) / len(scores[stu_name]), 1)
    print(f"총점: {sum_scores} / 평균: {avg_scores}")
    # 최고점/최저점 판별을 위한 정렬 리스트
    other_list = sorted(scores[stu_name])
    print(f"최고점: {other_list[-1]} / 최저점: {other_list[0]}")
    # 합격 / 불합격
    if avg_scores >= 80:
        print("합격")
    else:
        print("불합격")
print()
print("=" * 30)

print("[문제 11] 자판기")
vending = {
    "콜라": {"price": 1500, "stock": 2},
    "사이다": {"price": 1400, "stock": 1},
    "물": {"price": 800, "stock": 5},
}

drink = input("상품을 입력하세요: ")

if vending.get(drink) == None:
    print("존재하지 않는 상품입니다.")
else:
    send = int(input("금액을 투입하세요: "))
    if vending[drink]["stock"] == 0:
        print("재고가 없습니다.")
    else:
        if send < (vending[drink]["price"]):
            print("금액이 부족합니다.")
        else:
            change = send - (vending[drink]["price"])
            vending[drink]["stock"] -= 1
            print(f"{drink} 구매 완료 / 거스름돈 {change}원")
            print(f"{drink} 남은 재고: {vending[drink]['stock']}개")
print()
print("=" * 30)

print("[문제 12] 로그인과 권한 확인")
accounts = {
    "alice": {"pw": "1234", "roles": ["admin", "user"]},
    "bob": {"pw": "abcd", "roles": ["user"]},
}

set_member_id = input("아이디를 입력: ")
check_member_id = accounts.get(set_member_id)

if check_member_id == None:
    print("존재하지 않는 회원입니다.")
else:
    set_member_pw = input("비밀번호를 입력: ")
    get_member_pw = accounts.get(set_member_id)["pw"]
    member_role = accounts.get(set_member_id)["roles"]
    member_class = accounts.get(set_member_id)["roles"][0]
    if set_member_pw == get_member_pw:
        print(f"{set_member_id}님 로그인 성공")
        print(f"권한 목록: {member_role}")
        print(f"대표 권한: {member_class}")
        if member_class == "admin":
            print("관리자 페이지 접근 가능")
    else:
        print("비밀번호가 맞지 않습니다")
print()
print("=" * 30)

print("[문제 13] 재고 차감 주문")
stock = {
    "사과": {"qty": 10, "price": 1500},
    "바나나": {"qty": 0, "price": 3000},
    "포도": {"qty": 5, "price": 8000},
}

in_stock = input("주문할 과일을 입력하세요: ")
qty = int(input("수량을 입력하세요: "))

if stock.get(in_stock) == None:
    print("존재하지 않는 상품입니다.")
elif stock.get(in_stock)["qty"] == 0 or qty > stock.get(in_stock)["qty"]:
    print("재고가 주문 수량보다 적습니다")
else:
    price = stock.get(in_stock)["price"] * qty
    in_qty = stock.get(in_stock)["qty"] - qty
    print(f"{in_stock} {qty}개 주문 / 결제금액 {price}")
    print(f"{in_stock} 남은 재고: {in_qty}개")
print()
print("=" * 30)

print("[문제 14] 자료형 변환 확인하기")
jumsu = int(input("시험 점수를 입력하세요: "))

if jumsu >= 90:
    test_class = "A"
elif jumsu >= 80:
    test_class = "B"
else:
    test_class = "C"

print(f"입력값 타입: {type(jumsu)}")
print(f"문자열로 변환: {jumsu!s}점")
print(f"실수로 변환: {float(jumsu)}")
print(f"등급: {test_class}")
print()
print("=" * 30)

print("[문제 15] 한 줄 입력을 데이터로 바꾸기")
name = input("이름: ")
age = int(input("나이: "))
city = input("지역: ")

profile = {"name": name, "age": age, "city": city}
print(profile)

after_years = 10
print(f"{after_years}년 뒤 나이: {age + after_years}")

if city in ["서울", "인천", "경기"]:
    print("수도권 거주자입니다.")
else:
    print("지방 거주자입니다.")
print()
print("=" * 30)

print("[문제 16] 장바구니 상품 조회")
cart = {
    "items": ["티셔츠", "양말", "모자"],
    "prices": [15000, 3000, 12000],
}

prod_num = int(input("상품 번호: "))

if prod_num > len(cart["items"]):
    # 입력한 숫자가 등록된 items 값의 수를 넘길 경우
    print("없는 상품 번호입니다.")
else:
    prod_name = cart["items"][prod_num - 1]
    prod_price = cart["prices"][prod_num - 1]
    all_prod_price = sum(cart["prices"])
    print(f"{prod_num}번 상품: {prod_name} / {prod_price}원")
    print(f"전체 합계: {all_prod_price}원")
print()
print("=" * 30)

print("[문제 17] 통신 요금 계산")
plans = {
    "basic": {"기본요금": 12000, "무료통화": 100, "초과요금": 50},
    "premium": {"기본요금": 25000, "무료통화": 300, "초과요금": 30},
}

plan_level = input("요금제 등급: ")
used_call = int(input("이번 달 통화 사용량(분): "))
chogwa = used_call - plans.get(plan_level)["무료통화"]

if chogwa <= 0:
    chogwa = 0
    yogeum = plans.get(plan_level)["기본요금"]
else:
    yogeum = plans.get(plan_level)["기본요금"] + (
        chogwa * plans.get(plan_level)["초과요금"]
    )

print(f"요금제: {plan_level} / 사용량: {used_call}분 / 초과: {chogwa}분")
print(f"이번 달 요금: {yogeum}")
print()
print("=" * 30)

print("[문제 18] 설문 응답 기록")
survey = {"질문": "개인정보 수집에 동의하십니까?", "응답": [], "동의수": 0}


agree = input("개인정보 수집에 동의하십니까?: ")

if agree == "y":
    survey["동의수"] += 1
    survey["응답"].append("동의")
    print("동의해 주셔서 감사합니다.")
    print(survey)
    print("마지막 응답: 동의")
else:
    print("거절하였습니다.")
print()
print("=" * 30)

print("[문제 19] 영화관 요금 계산")
ticket = {
    "성인": {"price": 12000, "학생할인": 2000},
    "청소년": {"price": 9000, "학생할인": 1000},
    "어린이": {"price": 6000, "학생할인": 0},
}

your_age = int(input("당신의 나이: "))
your_type = input("학생인가요? 일반인인가요?: ")

if your_age >= 20:
    recent = "성인"
    if your_type == "학생":
        print(f"학생 할인 {ticket.get(recent)['학생할인']}원 적용")
        student_dc = ticket.get(recent)["price"] - ticket.get(recent)["학생할인"]
        print(f"구분: {recent} / 최종 요금: {student_dc}원")
elif 13 <= your_age < 20:
    recent = "청소년"
    if your_type == "학생":
        print(f"학생 할인 {ticket.get(recent)['학생할인']}원 적용")
        student_dc = ticket.get(recent)["price"] - ticket.get(recent)["학생할인"]
        print(f"구분: {recent} / 최종 요금: {student_dc}원")
else:
    recent = "어린이"
    if your_type == "학생":
        print(f"학생 할인 {ticket.get(recent)['학생할인']}원 적용")
        student_dc = ticket.get(recent)["price"] - ticket.get(recent)["학생할인"]
        print(f"구분: {recent} / 최종 요금: {student_dc}원")
print()
print("=" * 30)

print("[문제 20] 학급 명단 조회")
school = {
    "3학년": {
        "1반": {"teacher": "박선생", "students": ["김철수", "이영희", "박민수"]},
        "2반": {"teacher": "최선생", "students": ["정수진", "한동훈"]},
    }
}

class_num = input("반 이름 입력(예: 1반): ")
in_number = int(input("해당 반의 학생 번호를 입력: "))

if school.get("3학년").get(class_num) == None:
    print("이 반은 존재하지 않습니다.")
elif len(school.get("3학년").get("1반").get("students")) < in_number:
    print("해당 번호의 학생이 존재하지 않습니다.")
else:
    print(f"3학년 {class_num} 담임: {school.get('3학년')['1반']['teacher']}")
    print(f"학생 수: {len(school.get('3학년')['1반']['students'])}")
    print(
        f"{in_number}번 학생: {school.get('3학년')['1반']['students'][in_number - 1]}"
    )

print()
print("=" * 30)

# ======================
# 1. 조건문 (if)  - 주어진 조건이 참일때 실행
# ======================

age = 25

if age >= 19:  # 파이썬 조건문에서는 콜론(:)이 필수
    print("만 19세 이상 성인입니다.")  # 조건이 '참'일때만 실행
else:
    print("미성년자입니다.")  # 조건이 '거짓(False)'일때 넘어와서 실행

print("프로그램 끝")  # 들여쓰기 밖: 조건문과 상관이 없는 영역
print()

# "들여쓰기"는 파이썬에서 조건문을 묶는 역할  (Java의 중괄호와 같은 역할)

score = 100

if score >= 90:
    print("A등급")
    print("축하합니다")
else:
    print("A등급이 아닙니다.")

print("확인 완료")
print()

# ======================
# 2. if-else 문
# ======================

age = 15

if age >= 20:
    print("입장 가능합니다")  # 참일때 실행
else:
    print("입장 불가 합니다")  # 거짓일때 실행
print()

# 파이썬 포함 어떤 언어에서 else는 반드시 if 뒤에 위치
# 둘 중 '반드시 하나만' 실행

# ======================
# 3. if-elif-else 문
# ======================

score = 85
if score >= 90:
    print("A 등급")
elif score >= 80:
    print("B 등급")
elif score >= 70:
    print("C 등급")
elif score >= 60:
    print("D 등급")
else:
    print("F 등급")

print()

# --- 핵심: 위에서부터 검사하고, 하나만 걸리면 나머지는 건너뜁니다.
# -> 그래서 조건문은 순서가 매우 중요!
# -> 까다로운 조건을 위에서부터 쓰기

# ※ elif는 여러개 작성 가능, else는 생략이 가능
weather = "비"
if weather == "맑음":
    print("산책하기 좋아요")
elif weather == "비":
    print("우산을 챙기세요")
elif weather == "흐림":
    print("구름이 많아요")
print()

# ======================
# 4. if 여러개와 elif 사용의 차이는?
# ======================
# 겉보기엔 비슷하지만 동작이 완전히 다름

number = 15

# --- elif: 하나만 실행
if number > 10:
    print("10보다 큼")
elif number > 5:
    print("5보다 큼")
print()

# --- if 여러개: 각각 따로 검사 -> 모든 if가 실행될 수 있다
if number > 10:
    print("10보다 큼")
if number > 5:
    print("5보다 큼")
print()

# 등급 판정처럼 '하나만 골라야'하면? -> elif
# 조건들이 서로 독립적이면(각각 검사) -> if 여러 개 사용

# ======================
# 5. 조건을 여러 개 묶기 (연산자 복습)
# ======================

age = 25
has_ticket = True

if age >= 20 and has_ticket:
    print("입장 가능")  # 반드시 둘 다 참이면 실행

if age < 8 or age >= 80:
    print("할인 대상")  # 하나만 참이여도 실행

if not has_ticket:
    print("티켓을 구매하세요")  # 뒤집기
print()

# 'in'을 쓰면 조건문이 깔끔해짐
day = "토"

if day in ["토", "일"]:
    print("주말입니다.")
else:
    print("평일입니다.")
print()

# ======================
# 6. 조건 자리에 값을 그대로 넣기
# ======================
# 파이썬은 True/False가 아닌 값도 참, 거짓으로 판단합니다.
# 거짓 취급: 0, 0.0, "", None, [], {}
# 그 외 전부 참

name = ""
if name:
    print(f"{name}님 안녕하세요!")
else:
    print("이름이 입력되지 않았습니다.")

count = 0
if count:
    print("항목이 있습니다.")
else:
    print("항목이 없습니다.")
print()

# ======================
# 7. 중첩 조건문 (조건문 안에 조건문)
# ======================

age = 25
has_ticket = False

if age >= 20:
    print("나이 확인 완료")

    if has_ticket:
        print("입장 가능합니다")
    else:
        print("티켓을 구매해 주세요")
else:
    print("성인만 입장 가능합니다")
print()

# 조건문 코드가 길어지면 가독성이 떨어짐
# -> 위의 코드는 'and' 등의 비교 연산으로 합칠 수 있다
if age >= 20 and has_ticket:
    print("입장 하세요")

# -> 중첩은 2단계까지 허용, 3단계를 넘으면 구조를 다시 생각해야

# ======================
# 8. 한 줄 버전 조건문
# ======================
# 기본 형태
age = 25
status = ""

if age >= 20:
    status = "성인"
else:
    status = "미성년자"

# 한줄 버전
status = "성인" if age >= 20 else "미성년자"
print(f"{'짝수' if 10 % 2 == 0 else '홀수'}")

# [문제 1] 성인 판별 (★)
# 나이를 입력받아 20살 이상이면 "성인", 아니면 "미성년자" 출력

age = int(input("당신의 나이를 입력하세요 : "))

if age >= 20:
    print("성인")
else:
    print("미성년자")
print()

# [문제 2] 짝수 홀수 (★)
# 숫자를 입력받아 짝수인지 홀수인지 출력
# 힌트: % 연산자

number = int(input("숫자를 입력하세요: "))

if number % 2 == 0:
    print("짝수")
else:
    print("홀수")
print()

# [문제 3] 학점 계산기 (★★)
# 점수를 입력받아 등급 출력
# 90 이상 A / 80 이상 B / 70 이상 C / 60 이상 D / 그 외 F

score = int(input("당신의 학점을 입력하세요: "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
print()

# [문제 4] 로그인 (★★)
# 아이디와 비밀번호를 입력받아,
# 아이디가 "admin"이고 비밀번호가 "1234"면 "로그인 성공"
# 아이디만 맞으면 "비밀번호가 틀렸습니다"
# 아이디가 틀리면 "존재하지 않는 아이디입니다"

user_id = input("아이디를 입력하세요: ")
if user_id == "admin":
    user_pwd = input("비밀번호를 입력하세요: ")
    if user_pwd == "1234":
        print("로그인 성공")
    else:
        print("비밀번호가 틀렸습니다")
else:
    print("존재하지 않는 아이디입니다")
print()

# [문제 5] 세 수 중 최댓값 (★★★)
# 세 개의 숫자를 입력받아 가장 큰 수를 출력
# (max() 함수를 쓰지 말고 조건문으로)

num1 = int(input("임의의 숫자를 입력하세요 : "))
num2 = int(input("임의의 숫자를 입력하세요 : "))
num3 = int(input("임의의 숫자를 입력하세요 : "))
max_num = ""

if num1 >= num2 and num1 >= num3:
    max_num = num1
elif num2 >= num1 and num2 >= num3:
    max_num = num2
else:
    max_num = num3
print(max_num)
print()

# [문제 6] 윤년 판별 (★★★)
# 연도를 입력받아 윤년인지 판별
# 규칙: 4로 나누어떨어지면 윤년,
# 단 100으로 나누어떨어지면 평년,
# 단 400으로 나누어떨어지면 윤년

year = int(input("연도를 입력하세요 (예: 1993) : "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("입력한 연도는 윤년입니다.")
else:
    print("입력한 연도는 평년입니다.")

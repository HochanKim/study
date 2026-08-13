# ============================================
# 1. for 문 (반복)
# ==============================================
# 반복문이 왜 필요한가?

fruits = ["사과", "바나나", "포도"]
# -> 반복문 없이 리스트 속 값을 꺼내려면 일일이 인덱스 번호를 체크해서
# 하나하나 값을 직접 꺼내야 한다.
# 인덱스 번호가 맞지 않으면 Error가 발생

# 반복문이면 개수와 상관없이 두 줄
for fruit in fruits:
    print(fruit)
print()

# 들어있는 값의 길이만큼 호출
numbers = [1, 2, 3, 4, 5, 6]
print("길이: ", len(numbers))

for i in numbers:
    print(i)
print()

## range() 함수
# for i in range(1, 101):
#     print(i)
# print()

# list = [1, 2, 3, 4, "사과", "바나나", [1, 2]]
# for a in list:
#     print(a)
# print()

# 딕셔너리와 반복
name_dic = {"name": "철수", "age": 25, "region": "인천"}

for i in name_dic:
    # print(i)  # 딕셔너리 key 출력
    # print(name_dic[i])  # 딕셔너리 value 출력
    print(f"{i}은 {name_dic[i]}")
print()

# 다른 자료형도 반복된다
for ch in "파이썬":
    print(ch)
print()

# 딕셔너리에서 기본적으로 Key를 먼저 뽑는다
scores = {"국어": 90, "영어": 85, "수학": 77}

for i in scores:
    print(i)  # Key 호출

for i in scores.values():
    print(i)  # Value 호출

for subject, score in scores.items():
    print(f"{subject}: {score}점")
print()

# 간단 실습
# 1. 각각 평균 구하기
# -> 민수 평균 : ??
# -> 철수 평균 : ??
# 2. 두 사람 평균
# -> 두 사람의 평균은: ?? 입니다.
# 3. 평균 비교 후 '민수 or 철수'가 더 우수한 학생입니다.
# ※ for문은 선택 사용 가능
student = [
    {"name": "민수", "국어": 95, "영어": 100},
    {"name": "철수", "국어": 75, "영어": 50},
]

stu1_test = student[0]  # {"name": "민수", "국어": 95, "영어": 100}
stu2_test = student[1]  # {"name": "철수", "국어": 75, "영어": 50}

# 민수 자료 리스트화
stu1_list = list(stu1_test.values())
stu1_name = stu1_list[0]  # 이름 담기
del stu1_list[0]  # 이름 제거

# 민수 평균값 구하기
stu1_avg = (stu1_list[0] + stu1_list[1]) / len(stu1_list)


# 철수 자료 리스트화
stu2_list = list(stu2_test.values())
stu2_name = stu2_list[0]  # 이름 담기
del stu2_list[0]  # 이름 제거

# 철수 평균값 구하기
stu2_avg = (stu2_list[0] + stu2_list[1]) / len(stu2_list)

print(f"{stu1_name} 평균: {stu1_avg}")
print(f"{stu2_name} 평균: {stu2_avg}")

# 두 사람 평균값
avgs_list = []
avgs_list.append(stu1_avg)
avgs_list.append(stu2_avg)

all_avgs = (avgs_list[0] + avgs_list[1]) / len(avgs_list)
print(f"두 사람의 평균은: {all_avgs}점 입니다.")

# 둘의 평균 비교
if stu1_avg > stu2_avg:
    print("민수가 더 우수한 학생입니다.")
elif stu1_avg == stu2_avg:
    print("둘의 평균이 같습니다.")
else:
    print("철수가 더 우수한 학생입니다.")
print()

# # ============================================
# 2. range() - 숫자를 순서대로
# ==============================================
for i in range(5):
    print(i)
print()

# range(끝): 0부터 끝-1 까지
print(list(range(6)))

# range(시작, 끝): 시작 번호부터 끝-1까지
print(list(range(1, 6)))

# range(시작, 끝, 간격): 간격만큼 건너뛰며
print(list(range(1, 12, 2)))
print()
# -> range() 최다 실수: 끝값은 포함되지 않는다 (끝 번호 -1까지)

# 1 2 3 4 5
for i in range(1, 6):
    print(i)

# 안녕 안녕 안녕
for i in range(3):
    print("안녕")
print()

# 누적하기
# -> 반복하면서 결과를 쌓아나가는 방식
# -> 수학의 '시그마(∑)'와 비슷한 패턴

# 값을 담을 변수 설정
sum = 0
for i in range(1, 101):
    sum += i
print(f"1부터 100까지 모두 더한 값 = {sum}")
print()


# 곱셈 누적은 1로 시작
result = 1
for i in [1, 2, 3, 4, 5]:
    result *= i
print(result)
print()

# 개수 세기
count = 0
scores = [90, 55, 77, 40, 88]
for score in scores:
    if score >= 60:
        count += 1
print(f"합격자는 총 {count}명 입니다.")
print()

# 리스트에 모으기
events01 = []  # 값들을 받을 빈 리스트 생성
for i in range(1, 11):
    if i % 2 == 0:
        events01.append(i)
print(events01)
print()

events02 = []
for i in range(1, 11):
    if i % 2 != 0:
        events02.append(i)
print(events02)
print()

# for문으로 최대값 찾기 - max() 해부
scores = [90, 85, 77, 92, 60, 92]
biggest = scores[0]  # 첫 값을 최대값으로 지정
for s in scores:
    if s > biggest:
        biggest = s
print(biggest)


# for문으로 최소값 찾기 - min() 해부
numbers = [44, 22, 66, 32, 11, 677, 22]
mini = scores[0]  # 첫 값을 최소값으로 지정
for s in numbers:
    if s < mini:
        mini = s
print(mini)
print()

# # ============================================
# 3. break / continue
# ==============================================

# break: 반복 즉시 중단
for i in range(1, 10):
    if i == 5:
        break  # 5에서 반복 중단
    print(i)
print()

# continue: 지정 회차 건너뛰기
for i in range(1, 6):
    if i == 3:
        continue  # 3 제외 출력
    print(i)
print()

# # ============================================
# 4. 중첩 반복문
# ==============================================
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i * j}")
    print()

# 정삼각형 모양
n = 5
for i in range(1, n + 1):
    print((" " * (n - i)) + ("*" * (2 * i - 1)))
print()

# 역삼각형 모양
n = 5
for i in range(n, 0, -1):
    print((" " * (n - i)) + ("*" * (2 * i - 1)))
print()

# 구구단 역순
for i in range(9, 1, -1):
    for j in range(9, 0, -1):
        print(f"{i}X{j}={i * j}")
    print()
print()

# 마름모(다이아몬드) 만들기
n = 5
for i in range(1, n + 1):
    print((" " * (n - i)) + ("*" * (2 * i - 1)))
    if i == 5:
        for i in range(n - 1, 0, -1):
            print((" " * (n - i)) + ("*" * (2 * i - 1)))
print()

# 알아두면 좋은 기능
fruits = ["사과", "바나나", "포도"]

for i, fruit in enumerate(fruits):  # 인덱스 번호와 값을 함께 출력
    print(f"{i}번: {fruit}")
print()
for i, x in enumerate(fruits, 1):  # 1번 부터
    print(f"{i}번: {x}")
print()

names = ["철수", "영희"]
ages = [25, 22]
for name, age in zip(names, ages):
    print(f"{name} : {age}살")
print()

#  시그마(∑)
# -> 주어진 수들을 모두 '다 더해라'
# -> 파이썬 for문으로 구현
total = 0
for i in range(1, 11):
    total += i
print()

print("1. 문제")
#   5
#   Σ i
#   i=2
answer01 = 0
for i in range(2, 6):
    answer01 += i
print(answer01)
print()

print("2. 문제")
#   15
#   Σ i^3
#   i=1
answer02 = 0
for i in range(1, 16):
    answer02 += i**3
print(answer02)
print()

print("3. 문제")
#   25
#   Σ 3i
#   i=1
answer03 = 0
for i in range(1, 26):
    answer03 += i * 3
print(answer03)
print()

print("4. 문제")
#   20
#   Σ 3
#   i=2
answer04 = 0
for i in range(2, 21):
    answer04 += 3
print(answer04)
print()

print("5. 문제")
#   12
#   Σ i^2
#   i=3
answer05 = 0
for i in range(3, 13):
    answer05 += i**2
print(answer05)
print()

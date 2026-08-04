# ======================
# 1. 산술 연산자
# ======================

# --- '//'와 '%'는 자주 쓰인다
print(10 % 2 == 0)  # 짝수 판별 (나머지가 0인 경우)

print(130 // 60, "분", 130 % 60, "초")  # 130초 => 2분 10초

# --- 문자열에도 쓸 수 있는 연산자 ---
print("파이" + "썬")  # 문자 '파이썬' 이어붙이기
print("-" * 20)  # 구분선 만들기

# ======================
# 2. 대입 연산자
# ======================

# 코드는 위에서 아래로 진행, 계산도 그렇다
x = 10  # 기본 대입: 오른쪽 값을 왼쪽에 넣기

# 자기 자신을 이용해 값을 바꾸는 축약형
x += 5  # x = x + 5 == 15
x -= 3  # x = x - 3 == 12
x *= 2  # x = x * 2 == 24
x /= 4  # x = x / 4 == 6.0 (float으로 변환됨)
x //= 2  # x = x // 2 == 3.0
x **= 2  # x = x ** 3.0 == 9.0

print(x)

# ======================
# 3. 비교 연산자  * 조건문의 핵심
# ======================

print(10 > 5)  # True
print(10 < 5)  # False
print(10 >= 10)  # True
print(10 <= 9)  # True
print(10 == 10)  # True
print(10 != 10)  # False
print()

# --- 문자열도 비교가 된다
print("abc" == "abc")  # True
print("abc" == "ABC")  # False, 대소문자를 구분함
print("apple" < "banana")  # True, 알파벳, 사전 순서로 비교 (a, b, c, d, ..., z)
print()

# 자료형이 다르면 비교가 안 되는 경우
print(10 == "10")  # False, 숫자와 문자열은 절대 같지 않음
# print(
#     10 > "5"
# )  # TypeError: 크기 비교는 아예 불가 (TypeError: '>' not supported between instances of 'int' and 'str')

# 파이썬 만의 편한 문법: 범위를 한번에 사용 가능
score = 85
print(60 <= score <= 100)
print()

# ======================
# 4. 논리 연산자  * 조건문의 핵심
# ======================
# 여러 조건을 묶을 때 사용합니다

# and: 둘 다 참이여야 True 성립
print(True and True)  # True
print(True and False)  # False
print(False and True)  # True
print()

# or: 하나라도 참이면 참
print(True or True)  # True
print(True or False)  # True
print(False or False)  # False
print()

# not: 결과물 뒤집기
print(not True)  # False
print(not True)  # True
print(not (10 > 5))  # False
print()

# ======================
# 5. 멤버십 연산자 (in / not in)
# ======================
# 어떤 값이 안에 들어있는지 확인

# --- 문자열에서
text = "python programing"
print("python" in text)  # True (포함되어 있나?)

print("java" in text)  # False
print("java" not in text)  # True
print()

# --- 리스트에서
fruits = ["사과", "바나나", "포도"]
print("사과" in fruits)  # True
print("딸기" in fruits)  # False
print()

# --- 실제 활용 예시
answer = "y"
print(answer in {"y", "Y", "yes"})  # True
# 여러가지 값 중 하나인지 한 번에 확인


# ======================
# 6. 식별 연산자 (is / is not)
# ======================
# '같은 값'이 아니라 '완전히 같은 것' 인지 확인

# --- 주 용도는 None 확인 ---
result = None
print(result is None)  # True  (권장되는 방식)
print(result is not None)  # False
print(result == None)  # True (동작은 하지만 'is'를 쓰는 것이 관례)

# ※ 값 비교에는 is를 쓰면 안됨
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True, 내용이 같다
print(a is b)  # False, 서러 다른 리스트 두 개

# 정리: 값 비교는 ==, None 확인은 is


# 연산자 우선순위
# 위에 있을수록 먼저 계산이 적용
# 1) () 괄호
# 2) ** 거듭제곱
# 3) *, /, //, % 곱셈과 나눗셈
# 4) +, - 덧셈과 뺄셈
# 5) > < >= <= == != in is 비교 연산자
# 6) not
# 7) and
# 8) or

# --- and가 or보다 먼저 연산
print(True or False and False)  # and에서 False, True or False => True
print((True or False) and False)  # False, 괄호 연산이 먼저

# 형 변환이 왜 필요한가?
# 파이썬은 종류가 다른 값끼리는 계산을 거부합니다.
age = "20"  # 문자열

# 문자열을 정수로 변환하기
print(int(age) + 1)
print()


# =================
# 두 가지 형 변환
# =================

# (1) 자동 형변환 : 파이썬이 알아서 맞춰주는 것
result = 3 + 0.5  # int + float
print(result)  # 3.5
print(type(result))  # float <- 더 정밀한 쪽으로 자동 변환
print(True + 1)  # 2 / bool은 숫자로 자동 변환
print(10 / 2)  # 2.0 / 나눗셈은 항상 float
print()

# (2) 수동 형변환 : 내가 직접 바꾸는 것
print(int("10"))
print(str(10))
print(float("3.14"))
print()

# int() - 정수로 바꾸기
print(int("100"))
print(int("-50"))
print(int(" 42 "))
print()

# 실수(float) -> 정수(int)
print(int(3.9))
print(int(3.1))
print(int(-3.9))
print()

# 반올림은 어떻게 하는건가? -> round()
print(round(3.9))  # 4
print(round(3.1))  # 3
print()

# bool -> 정수
print(int(True))  # 1
print(int(False))  # 0
print()

# int()가 실패하는 경우
# print(int("3.14")): ValueError, 소수점이 든 문자열은 바로 안됨
# -> print(int(float("3.14"))): float 변환을 거쳐 두 번째 가능
# print(int("삼")): 한글로 표현한 숫자는 불가능
# print(int("")): 빈 문자열 불가
# print(int(None)): NoneType 불가

# (참고) 2진수, 16진수 문자열 변환
print(int("1010", 2))  # 10을 2진수로 해석
print(int("ff", 16))  # 255 16진수로 해석
print()

# float() - 실수로 바꾸기
print(float("3.14"))  # 3.14
print(float("10"))  # 10.0 <- 정수처럼 생겨도 '.0'이 붙음
print(float(10))  # 10.0
print(float(True))  # 1.0
print()

# 실패하는 경우는 int()와 같습니다.
# print(float("삼점일사")): 한글로 표현한 소수점(실수)는 불가능

# float -> int로 되돌릴 때 소수점이 사라지는 것에 주의
price = 3.99
print(int(price))  # 3
print()

# str() - 문자열로 바꾸기
# -> 문자열 변환은 거의 실패하지 않음
print(str(True))  # "True"
print(str(None))  # "None"
print(str([1, 2, 3]))  # "[1, 2, 3]"
print()

# print("점수 :" + score) X
score = 95
print(f"점수 : {score}")
# f-string을 쓰면 str()이 필요 없음
print()

# 문자열이 된 숫자는 계산이 안된다
num = 10
print(num * 3)  # 30
num = str(10)
print(num * 3)  # 101010, 곱셈이 아닌 문자 반복
print()

# bool() - 참/거짓으로 바꾸기
# 비어 있거나 0이면 False, 나머지는 전부 True
# 내용 상관없이 빈 문자열이 아님이 기준
print(bool(0))  # False
print(bool("0"))  # True
print(bool(""))  # False
print(bool(-5))  # true
print(bool([]))  # False

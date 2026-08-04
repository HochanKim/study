# ====================================
# 자료형이란?
# ====================================
# 변수? => 값에 이름을 붙이는 "이름표"
# 자료형? => 값이 "어떤 종류"인지를 판단

# 왜 종류를 나눌까? => 종류마다 할 수 있는 일이 다르기 때문
print(10 + 5)  # 숫자끼리 더하면 "계산"
print("10" + "5")  # 문자끼리 더하면 "이어붙이기"
# print(
#   "10" + 5
# )  # TypeError: 종류가 다르면 더할 수 없음 (※ TypeError: can only concatenate str (not "int") to str)

# 자료형을 확인하는 법
# type() <= 타입 안에 넣으면 확인 가능
print(type(10))  # int(정수)
print(type(3.14))  # float(실수)
print(type("Hello, world"))  # str(문자열)
print(type(True))  # bool(불리언)
print(type(None))  # NoneType
print()

# 특정 자료형이 맞는지 확인할 때는 isinstance()
print(isinstance(10, int))  # True
print(isinstance(10, str))  # False
print()

# int - 정수
age = 25
temperature = -10
zero = 0

# 자릿수 제한이 없습니다. (아주 큰 수도 그대로 계산됨)
big = 1234567890 * 99999
# print(big)

# 읽기 어려운 큰 숫자는 언더바로 구분 가능 (실행엔 영향 없음)
population = 51_000_000
print(population)
print()

# --- 정수 연산 ---
print(7 + 3)
print(7 - 3)
print(7 * 3)
print(7 / 3)  # 나눗셈은 무조건 float으로 출력
print(7 // 3)  # 나눗셈의 몫값만 출력 (int로 나옴)
print(7 % 3)  # 나눗셈의 나머지값 출력
print(7**3)  # 거듭제곱
print()

# float - 실수
height = 182.2
pi = 3.141592718
minus = -0.5
exp = 1.5e3  # 지수표기 = 1.5 * (10 ** 3)
print(exp)

# float의 함정: 소수 계산에 오차 발생
print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)
# 이유: 컴퓨터는 2진수로 저장하는데 0.1을 2진수로 정확히 표현할 수 없음
# 10진수로 1/3을 0.3333...로 밖에 못 쓰는 것과 같은 원리

# 해결법 1: 반올림해서 배교
print(round(0.1 + 0.2, 2) == 0.3)  # True, round(값, 소수점자리)
print()

# 해결법 2: 돈 계산처럼 정확해야 하면 decimal 모듈 사용
from decimal import Decimal

print(Decimal("0.1") + Decimal("0.2"))
print()
# int(정수)와 float(실수)를 섞으면?
# => 더 정밀한 float으로 맞춰짐


# str - 문자열
# - 따옴표로 감싸면 전부 문자열 (작은 따옴표, 큰 따옴표 차이 없음)

name = "김철수"
city = "서울"
number_string = "1234"  # number_string + 1 : X 문자열과 정수의 계산은 불가능!

# 따옴표 골라쓰기
say1 = "그는 '안녕'이라고 했다"
say2 = "It's a book"  # 같은 따옴표를 쓰려면 '\'로 탈출 => say2 = 'It\'s a book'

# 여러줄 문자열
long_text = """첫 번째 줄
두 번째 줄
세 번째 줄"""  # 따옴표 3개로 감싸면 줄바꿈이 그대로 저장됨
print(long_text)
print()

# 자주쓰는 이스케이프 문자
print("줄바꿈\n 다음 줄")  # \n: 줄바꿈
print("이름\t나이")  # \t: 탭(간격)
print("역슬래시 \\ 출력")  # \\ = 역슬래시 자체
print(r"C:\new\folder")  # 앞에 r을 붙이면 \를 그대로 (경로 쓸 때 사용)
print()

# 문자열 연산
print("파이" + "썬")  # "파이썬" 이어붙이기
print("하하" * 3)  # 문자열의 반복
print(len("파이썬"))  # 문자열의 길이 세기
print()

word = "PYTHON"
# P Y T H O N
# 0 1 2 3 4 5 (인덱스 번호는 '0'부터 시작)
# -6 -5 -4 -3 -2 -1 (뒤에서부터 셀 땐 음수)


# 잘라내기 (슬라이싱 기능)
print(word[0:3])  # 'PYT' => 0번부터 2번까지 (끝번 제외)
print(word[2:])
print(word[:3])
print()

# 자주 쓰는 문자열 기능
text = "       Hello Python     "
print(text.strip())  # 문자의 앞 뒤 공백을 제거
print(text.upper())  # 모든 영문자를 대문자로 변환
print(text.lower())  # 모든 영문자를 소문자로 변환
print(text.replace("o", "0"))  # 문자 바꾸기 (ex. "o"를 "0"으로 교체)
print("사과, 배, 감".split(","))  # ['사과', '배', '감'] 구분자로 출력

# 문자열은 한 번 만들면 수정할 수 없습니다.
# word[0] = "J" => 에러 발생 (TypeError: 'str' object does not support item assignment)
word = "JYTHON"
print(word)
print()

# bool - 불리언 (참/거짓)
is_student = True
is_adult = False

# 비교 연산자의 결과가 bool입니다.
print(10 > 5)  # True
print(10 == 5)  # False
print(10 != 5)  # True

# bool은 사실 숫자 (※ 2진수 개념, 1 == true, 0 == false)
print(int(True))  # 1
print(True + True)  # 2
print()

# None - 값이 없음
result = None
print(type(None))  # NoneType

# "아직 값이 정해지지 않았다"를 표현할 때 사용
# 0, "", False와는 다른 개념 ('0'이라는 숫자가 존재, "" 빈 문자열이라는 값이 존재, False(거짓)라는 값이 존재)
# 'None'은 값 자체가 없다
# None인지 어떻게 확인? => is를 쓰는 게 관례
print(result is None)  # True
print(result is not None)  # False

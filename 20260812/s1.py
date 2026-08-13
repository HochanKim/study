# ============================================
# 1. 예외처리 - 프로그램이 죽지 않게 만들기
# ============================================

# 프로그램을 만들 때
# => 1. 사람이 직접 코딩 (오타 가능성)
# => 2. 파일에서 읽어오고 (빈칸이 있을 가능성)
# => 3. 인터넷에서 받아오기 (형식이 다름)

# ※ 내가 통제할 수 없는 값이 들어온다
# => 그럴 때, 프로그램이 죽지 않게 하는 것이 '예외처리(Exception)'


# ============================================
# 2. 먼저 알아야 할 것: '에러 메시지'는 안내문
# ============================================
# 프로그래밍 처음 하는 사람이 가장 많이 하는 실수는
# 빨간 글씨가 나오면 읽지 않고 당황하는 것
# => 에러 메시지는 컴퓨터가 화를 내는 게 아닌,
# 몇 번째 줄에서 '이런 문제가 생겼다'를 알려주는 안내문
# 읽는 법만 알면 문제의 90%는 스스로 해결할 수 있다.


# [에러 메시지의 구조]
#   Traceback (most recent call last):
#     File "C:/work/test.py", line 5, in <module>
#       num = int("가나다")
#   ValueError: invalid literal for int() with base 10: '가나다'
# => 에러는 '아래에서 위로' 읽는다.
# 가장 중요한 정보가 맨 아래에 있기 때문에


# 1. 맨 아랫줄 왼쪽 -> ValueError
# - "무슨 종류의 문제인가" (에러의 이름)
# 2. 맨 아랫줄 콜론 뒤 -> invalid literal for int()...
# - "왜 문제인가" (설명. 영어지만 핵심 단어만 봐도 됩니다)
#     여기서는 int()로 바꿀 수 없는 값 '가나다'가 들어왔다는 의미
# 3. 그 위의 line 5 => "몇 번째 줄에서 에러가 생겼나"
# - 내 파일의 5번째 줄로 가면 문제의 코드가 있습니다

# 에러 이름을 그대로 복사해서 검색하면
# 같은 문제를 겪은 사람들의 해결법이 잔뜩 나옵니다
# 참고) https://stackoverflow.com/questions
# AI 말고 위의 링크로 에러 체크하는것이 유용

# ============================================
# 3. 자주 만나는 에러 6종
# ============================================

# ① valueError: 자료형은 맞는데 '값'이 이상할 때 / ex) int("가나다")
# => int()는 문자열('123' 등)을 받을 수 있지만, '가나다' 등의 문자를 숫자로 바꿀 수 없음

# ② TypeError: 아예 '자료형'이 안 맞을 때
# "3" + 5
# => 문자열 "3"과 숫자 5는 더할 수 없습니다
# => "3"+"5"는 "35"가 되고, 3+5는 8이 됩니다.
# 섞으면 파이썬은 뭘 원하는지 알 수 없어 에러를 냅니다.

# ③ ZeroDivisionError: 0으로 나눌 때
# => 수학에서 0으로 나눌 수 없듯이 파이썬도 같다.

# ④ IndexError: 리스트 범위를 벗어날 때
# [1, 2, 3][10]
# 원소가 3개인데 11번째(인덱스 10)를 달라고 하면 없습니다 (인덱스 범위 이탈)
# 인덱스 0부터 시작하므로 이 리스트는 0, 1, 2만 가능

# ⑤ KeyError: 딕셔너리에 없는 키를 찾을 때
# {"a": 1}["b"]
# => 'b'라는 키가 없다 / 이걸 피하려면 .get("b", 0)을 쓰면 된다. (키가 없으면 키를 생성하고 0을 돌려줌)


# ⑥ FileNotFoundError: 파일이 없을 때
# open("없는파일.txt")


# ※ 에러가 발생하면 프로그램은 멈춘다
# => "에러가 났다"가 아니라
# 프로그램이 그 자리에서 완전히 멈춘다

# print("1단계: 데이터 읽기 완료")
# # age = int("스물 다섯")  <= 에러 발생
# print("2단계: 계산 완료")  # <= 에러 이후로 코드는 실행이 안됨
# print("3단계: 저장 완료")  # <= 에러 이후로 코드는 실행이 안됨

# # => 만약 1000줄 짜리 데이터를 처리하다가 500번째 줄에서 에러가 발생하면
# # 앞의 499줄 작업도 저장을 못해서 전부 날아갈 위험이 있다

# user_input = "스물다섯"  # 입력을 가정
# print("1단계: 입력값 받음 ->", user_input)
# age = input(user_input)
# print("2단계: 나이 계산 ->", age + 1)

# ============================================
# 4. 해결책: try / except
# ============================================
# try:
#     위험할 수 있는 코드
# except 에러이름:
#     에러가 났을 때 대신 할 일
#
# 동작 방식
# try 안의 코드를 실행한다
# - 아무 문제 없으면 -> except는 건너 뛴다
# - 에러가 나면 -> 그 즉시 except로 이동 (try 안의 남은 코드는 실행되지 않음)
# 어느 쪽이든 '프로그램이 죽지 않는다'가 핵심

# age = "싫어요"

# try:
#     print(f"내년이면 {age + 1}살이네요")
# except Exception as ex:
#     print(f"숫자를 입력해 주세요. (입력값: {age})")
#     print(ex)
# print("프로그램이 죽지않고 여기까지 왔습니다")


# except 뒤에는 반드시 에러 이름을 적기
# => except 뒤에 아무것도 안쓰면 '모든 에러'를 잡지만
# 위험 부담이 있는 방법이다

# 예시 코드
# try :
#   result = calculat(10) # <= 오타 에러
# except :
#   print("에러 발생")
# => 오타를 냈지만 에러 발생만 출력
# => 오타를 못 찾고 시간 낭비할 가능성


# 규칙: 내가 예상하는 에러만 알기
# def divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return "0으로 나눌 수 없습니다"
#     except TypeError:
#         return "숫자만 가능합니다"


# print(divide(15, 3), "<= 첫 번째")
# print(divide(6, 0), "<= 두 번째")
# print(divide(2, "가"), "<= 세 번째")

# except를 여러 개 쓰면 위에서부터 차례로 확인한다
# 해당하는 것을 만나면 그것만 실행하고 나머지는 건너뛴다
# if / elif와 같은 방식으로 작동


# 에러 메시지를 직접 꺼내 쓰기 (as e)
# except ValueError as e:
# => 잡을 에러 / 담아둘 변수 이름
# => 이렇게 하면 에러 정보를 변수처럼 다룰 수 있다.
# e 대신 다른 이름을 써도 되지만, 관례상 'e'나 'err'를 많이 쓴다

# try:
#     num = int("가나다")
# except ValueError as e:
#     print("에러가 발생했습니다")
#     print("에러 종류:", type(e).__name__)  # 에러 이름
#     print("에러 내용:", e)  # 설명 내용

# 언제 쓰나요?
# - 사용자에게는 친절한 메시지를, 로그에는 상세 내용을 남길 때
# - 여러 에러를 한꺼번에 잡고 구체적인 내용을 기록하고 싶을 때

# type(e).__name__은 지금 이해 못해도 된다
# => "에러의 이름만 문자열로 꺼내는 방법"정도만 알고 있어라


# ============================================
# 5. else와 finally
# ============================================
# ===============
# try: 위험한 코드
# except: 에러가 났을 때만
# else: 에러가 '안'났을 때만
# finally: 에러가 나던, 안 나던 무조건

# 실행 순서 정리
# 에러가 안 나면: tryt 전체 -> else -> finally
# 에러가 나면: try 일부 -> except -> finally
# 어느 쪽이던 finally는 항상 실행된다


# def check(value):
#     print(f"[함수 실행]\n[{value}] 처리 시작")
#     try:
#         num = int(value)
#     except ValueError:
#         print("except 실행: 변환 실패")
#     else:
#         print(f"else 실행: 변환 성공! {num}")
#         # else는 언제 쓰나요?
#         # => try안에 에러가 날 수 있는 최소한의 코드만 두고
#         # 성공했을 때 할 일은 else로 빼면 코드가 명확해진다
#     finally:
#         print("finally 실행: 이 줄은 항상 나온다")
#         # finally는 언제 쓰나요?
#         # 뒷정리에 쓴다. 대표적인게 파일 닫기
#         # 파일을 열었으면 에러가 나던지, 안나던지 닫아야 함
#         # 좀 있따가 배울 with문이 이걸 자동으로 처리해준다


# check("15")
# print()
# check(100)
# print()
# check("백")

# ============================================
# 6. 실전 패턴 / 올바른 값을 넣을 때까지 다시 묻기
# ============================================

# while True와 try/excpet를 조합하는 패턴
# 사용자에게 입력받는 프로그램에서 거의 항상 사용된다

# 구조
# while True: <- 무한 반복
#   입력받기
#   try:
#     변환시도
#     return 결과 <- 성공하면 함수가 끝나므로 반복도 끝남
#   except:
#     안내 메시지 <- 실패하면 다시 while 처음으로
#
# 핵심은 return이 반복문을 빠져나오는 열쇠라는 점
# break를 써도 되지만, 함수 안이라면 return이 더 깔끔함


# def ask_num(msg):
#     # 숫자를 제대로 입력할 때까지 계속 물어볼거다
#     while True:
#         value = input(msg)
#         try:
#             return int(value)
#         except ValueError:
#             print("숫자가 아닙니다")


# n = ask_num("숫자 입력: ")
# print(n)


# def ask_age():
#     # 0~120 사이의 나이 입력
#     while True:
#         value = input("나이 입력 (0~120): ")
#         try:
#             age = int(value)
#         except ValueError:
#             print("숫자를 입력해 주세요")
#             # continue  # 발생 에러 메시지를 건너뛰기
#         else:
#             if 0 <= age <= 120:
#                 return age
#             print("0에서 120 사이에 입력하세요")


# a = ask_age()
# print(f"입력한 나이: {a}")

# ============================================
# 7. 실전 패턴 여러 건 중 일부만 실패할 때...
# ============================================

# 데이터를 다룰 때 가장 자주 만나는 상황
# 1000건 중 3건이 이상해도, 나머지 997건을 처리해야 한다

# 잘못된 접근
# => 이상한 데이터가 없게 만들자 => 불가능한 일, 데이터는 항상 지저분하다

# 올바른 접근
# => 이상한 건 따로 모아두고, 나머지는 처리하자
# => 그리고 10건 중 2건 실패, 목록은 '여기 있다'라고 보고
# 이게 실무에서 데이터를 다루는 기본 자세


# # 실제 데이터는
# raw_data = ["100", "200", "삼백", "400", "", "600", "700"]

# numbers = []  # 성공한 값을 담을 리스트
# errors = []  # 실패한 값을 담을 리스트

# for item in raw_data:
#     try:
#         numbers.append(int(item.strip()))
#     except ValueError:
#         errors.append(item)

# print("정상처리:", numbers)
# print("처리 실패:", errors)
# print(f"총 {len(raw_data)}건 중 {len(numbers)}건 성공, {len(errors)}건 실패")
# print(f"합계: {sum(numbers)}")
# 여기서 배울 점
# 1. for 안에 try를 넣으면, 한 건이 실패해도 다음 건으로 넘어갑니다
# 2. 실패한 것을 버리지 말고 따로 모아둔다
# 3. 마지막에 "몇 건 성공, 몇 건 실패"를 보고한다
# 4. CSV에서 이 패턴을 그대로 쓴다


# ============================================
# 8. 실전 패턴에서 안전한 변환 함수 만들기
# ============================================
# 앞으로 계속 쓰게 될 함수이니 여기서 제대로 만들고 활용하자
# => 변환에 실패하면 프로그램을 먼추는 대신, 미리 정해둔 '기본값'을 돌려주자


# def to_int(value, default=0):
#     # 문자열을 정수로 바꾼다, 실패하면 default를 돌려준다
#     # value: 바꿀 값
#     # default: 실패했을 때 대신 돌려줄 값 (기본 0)
#     try:
#         # str(value)로 한번 감싼 이유
#         # value에 숫자나 None이 들어와도 에러없이 처리하기 위함
#         # None.strip()은 에러가 나지만
#         return int(str(value).strip())  # strip(): 공백제거
#     except (ValueError, TypeError):
#         # 괄호로 묶으면 여러 에러를 한꺼번에 잡을 수 있다
#         return default


# print(to_int("100"))
# print(to_int("삼백"))
# print(to_int("삼백", -1))


# def to_float(value, default=0.0):
#     # 문자열을 실수로 바꾼다, 실패하면 default를 돌려준다
#     # value: 바꿀 값
#     # default: 실패했을 때 대신 돌려줄 값 (기본 0)
#     try:
#         # str(value)로 한번 감싼 이유
#         # value에 숫자나 None이 들어와도 에러없이 처리하기 위함
#         # None.strip()은 에러가 나지만
#         return float(str(value).strip())  # strip(): 공백제거
#     except (ValueError, TypeError):
#         # 괄호로 묶으면 여러 에러를 한꺼번에 잡을 수 있다
#         return default


# print(to_float("3.14"))
# print(to_float(None))
# print(to_float("3.14만원"))
# =======> 에러를 잡는 방법

# 반대로 에러를 내는 방법
# def set_age(age):
#     # 나이를 설정한다, 이상한 값이면 에러를 낸다
#     if age < 0:
#         raise ValueError("나이는 음수가 될 수 없습니다")
#     if age > 150:
#         raise ValueError("도깨비입니다")
#     return f"나이 {age}세로 설정되었습니다"


# print(" ", set_age(30))
# print(" ", set_age(-30))
# print(" ", set_age(151))

# 잘못된 값을 넣으면?

# try:
#     print(set_age(-5))
# except ValueError as e:
#     print("설정 실패", e)

# raise를 만나면 즉시 함수가 끝나고 에러가 발생합니다
# 함수를 부른 쪽에서 try/except로 받아 처리하면 됩니다

# 정리
# raise = 에러를 던진다 (문제를 알린다)
# except = 에러를 받는다 (문제에 대응한다)

# ※ 이럴 땐 try를 쓰지 마세요
#
# => try/except가 만능은 아니다, 남용하면 오히려 문제를 숨길 수 있다.

# 나쁜 예 - 범위가 너무 넓다
# try:
#     data = read.file()
#     result = calculate(data)
#     save(result)
# except:
#     print("에러")
#
# => 셋 중 어디에 에러가 나왔는지 명확하게 알 수 없다

# 나쁜 예 - 에러를 무시한다
# try:
#     중요한 작업()
# except:
#     pass 아무것도 안함
# => 문제가 생겨도 아무도 모른다, 최소한 기록을 남겨야 한다

# 나쁜 예 - if로 충분한데 try를 쓴다
# try:
#   print(my_list[0])
# except IndexError:
#   print("비었음")

# 이건 이렇게 쓰는 게 낫다!!!
# if len(my_list) > 0:
#   print(my_list[0])
# else:
#   print("비어있음")

# -> 미리 확인할 수 있는 건 if로 확인하세요
# try는 예상되지만 미리 막을 수 없는 상황에 써야 한다
#
# try 범위를 넓게 잡지 말자 (어디가 문제인지 모르게 된다)
# except에서 pass만 하지 마세요 (문제가 숨겨집니다)
# if로 확인할 수 있으면 if를 쓰라

practice_data = ["10", "20", "삼십", "40", "", "60"]
# 1. 위 리스트에서 숫자로 바꿀 수 있는 것만 골라 합계와 실패 개수를 돌려주는 함수 만들기
# 숫자 바꾸기 가능 문자열 모음
success_number = []
# 바꿀 수 없는 문자열 모음
# fail_number = []


# # 함수 만들기
# def change_num(datas):
#     for data in datas:
#         try:
#             success_number.append(
#                 int(data.strip())
#             )  # 값의 공백 제거를 위한 strip() 사용
#         except ValueError:
#             fail_number.append(data)
#     return fail_number


# print(f"합계: {len(practice_data)} / 실패 개수: {len(change_num(practice_data))}")


# 2. 두 수를 나누는 함수를 만들기. 0으로 나누면 "나눌 수 없음" / 숫자가 아니면 "숫자가 아님"을 돌려주기
# def divide(num1, num2):
#     try:
#         return num1 / num2
#     except ZeroDivisionError:
#         if num2 == 0:
#             return "나눌 수 없음"
#     except TypeError:
#         if str(num1) or str(num2):
#             return "숫자가 아님"


# print(divide(9, 3))
# print(divide(9, 0))
# print(divide(9, "가"))


# 3. 점수(0~100)를 받아 등급을 돌려주는 함수를 만들기. 범위를 벗어나면 raise로 valueError를 내기
# => 등급 (90이상 A / 80이상 B, 70이상 C, 그 외 D)
# def score_check(score):
#     if score < 0:
#         raise ValueError("점수는 음수일 수 없다")
#     elif score > 100:
#         raise ValueError("100을 넘을 수 없다")
#     elif 0 <= score <= 100 and score >= 90:
#         return "A"
#     elif 0 <= score <= 100 and score >= 80:
#         return "B"
#     elif 0 <= score <= 100 and score >= 70:
#         return "C"
#     elif 0 <= score <= 100 and score < 70:
#         return "D"


# print(score_check(101))

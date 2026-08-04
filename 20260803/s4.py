# =================
# 출력 print()
# =================

# 기본 사용법
print("Hello, World")
print(100)
print(3.14)

# 변수로 넣기
name = "김철수"
print(name)  # 저장된 변수가 출력
print("name")  #'name' 출력
print()

# end를 바꾸면 줄바꿈 없애기 가능
print("로딩 중", end="")
print("...")

print("A", end=" -> ")
print("B", end=" -> ")
print("C")

# input() 사용 시, 주의할 점
# input()에서 입력한 결과는 무조건 문자열
# -> 사용자가 숫자 '20'을 입력해도 정수(int) 20이 아닌 문자열(str) 20으로 인식

# ex) age = input("나이는? :") / 사용자가 20을 입력
# print(type(age))  / 문자열(str)로 나옴

# 형변환으로 해결하기
# -> age = int(input("나이는? :"))  / 입력값을 받으면서 바로 정수로 변환하기
# print(type(age))  / 정수(int)로 나옴
# height = float(input("키는? :"))  / 소수점이 있는 값은 float으로 변환

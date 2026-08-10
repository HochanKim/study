print("4. 중앙값 찾기")
# 세 개의 정수 변수를 만들고, 그중 크기가 가운데인 값을 출력하시오.
# 단, 정렬 기능(sort, sorted)은 사용할 수 없다. 같은 값이 중복될 수 있다.
num1 = 7
num2 = 2
num3 = 5
new_list = [num1, num2, num3]
middle_number = ""

if (num1 >= num2 and num1 <= num3) or (num1 <= num2 and num1 >= num3):
    middle_number = num1
elif (num2 >= num1 and num2 <= num3) or (num2 <= num1 and num2 >= num3):
    middle_number = num2
else:
    middle_number = num3
print(middle_number)
print()

num1 = 1
num2 = 1
num3 = 9
new_list = [num1, num2, num3]
middle_number = ""

if (num1 >= num2 and num1 <= num3) or (num1 <= num2 and num1 >= num3):
    middle_number = num1
elif (num2 >= num1 and num2 <= num3) or (num2 <= num1 and num2 >= num3):
    middle_number = num2
else:
    middle_number = num3
print(middle_number)
print()

num1 = 10
num2 = 3
num3 = 8
new_list = [num1, num2, num3]
middle_number = ""

if (num1 >= num2 and num1 <= num3) or (num1 <= num2 and num1 >= num3):
    middle_number = num1
elif (num2 >= num1 and num2 <= num3) or (num2 <= num1 and num2 >= num3):
    middle_number = num2
else:
    middle_number = num3
print(middle_number)
print()

num1 = 4
num2 = 4
num3 = 4
new_list = [num1, num2, num3]
middle_number = 0

if (num1 >= num2 and num1 <= num3) or (num1 <= num2 and num1 >= num3):
    middle_number = num1
elif (num2 >= num1 and num2 <= num3) or (num2 <= num1 and num2 >= num3):
    middle_number = num2
else:
    middle_number = num3
print(middle_number)
print("=" * 30)

# 실행 결과
# 5
# 다른 값으로도 확인
# * a, b, c = 1, 1, 9 → 1
# * a, b, c = 10, 3, 8 → 8
# * a, b, c = 4, 4, 4 → 4


print("5. 안전한 삭제")
# 할 일 목록과 지우려는 항목을 만들고 아래처럼 처리하시오.
# 존재하지 않는 항목을 지우려 해도 프로그램이 에러로 멈추면 안 된다.
# * 목록에 없으면 → 목록에 없습니다
# * 있으면 제거 후 → 삭제 완료
# * 단, 제거한 결과 목록이 비면 삭제 완료 대신 → 할 일이 없습니다
# 마지막 줄에는 처리 후의 목록을 출력한다.

todo = ["운동", "공부", "청소"]
x = "독서"

if x not in todo:
    print("목록에 없습니다.")
else:
    todo.remove(x)
    print("삭제 완료")
    print(todo)
print()

x = "공부"
if x not in todo:
    print("목록에 없습니다.")
else:
    todo.remove(x)
    print("삭제 완료")
    print(todo)
print()

todo = ["운동"]
x = "운동"
if x not in todo:
    # 만약 변수 'x'의 값이 리스트 'todo'에 존재하지 않는다면
    print("목록에 없습니다.")
elif (
    x in todo and len(todo) == 1
):  # 만약 변수 'x'의 값이 리스트 'todo'에 존재하면서 'todo'의 원소가 1개라면
    todo.remove(x)
    print("할 일이 없습니다.")
    print(todo)
else:  # 그 외 나머지 조건들
    print("삭제 완료")
    print(todo)
print("=" * 30)
# 실행 결과

# 목록에 없습니다
# ['운동', '공부', '청소']


# 다른 값으로도 확인 — x = "공부" 로 바꾸면

# 삭제 완료
# ['운동', '청소']


# todo = ["운동"], x = "운동" 으로 바꾸면

# 할 일이 없습니다
# []


print("6. 전반기 vs 후반기")
# 월별 매출 리스트를 만들고,
# 앞쪽 절반과 뒤쪽 절반의 합계를 한 줄에 나란히 출력한 뒤,
# 다음 줄에 더 큰 쪽을 전반 우세 / 후반 우세, 같으면 동일로 출력하시오.
# 리스트의 길이는 항상 짝수다.
sales = [10, 20, 30, 40, 50, 60]
all_period = len(sales)
early_period = sum(sales[: (int(all_period / 2))])
lately_period = sum(sales[-(int(all_period / 2)) :])
print(early_period, lately_period)
if early_period > lately_period:
    print("전반 우세")
elif early_period == lately_period:
    print("동일")
else:
    print("후반 우세")
print()

sales = [1, 2, 2, 1]
all_period = len(sales)
early_period = sum(sales[: (int(all_period / 2))])
lately_period = sum(sales[-(int(all_period / 2)) :])
print(early_period, lately_period)
if early_period > lately_period:
    print("전반 우세")
elif early_period == lately_period:
    print("동일")
else:
    print("후반 우세")
# 실행 결과

# 60 150
# 후반 우세


# 다른 값으로도 확인 — sales = [1, 2, 2, 1] 로 바꾸면

# 3 3
# 동일

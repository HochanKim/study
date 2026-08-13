# [16] 설정값은 상수로
# -------------------------------------------------------------
# 배달 앱 요금 계산기를 만드세요.

#   전역 상수 : BASE_FEE = 3000 (기본 배달료)
#              FREE_LIMIT = 20000 (무료배달 기준액)
#              EXTRA_PER_KM = 500 (1km당 추가요금)

#   함수 : get_delivery_fee(order_price, distance_km)
#         - 주문액이 FREE_LIMIT 이상이면 배달료 0원
#         - 아니면 BASE_FEE + (거리 × EXTRA_PER_KM)

# [기대 결과]
#   주문 15000원, 3km -> 배달료 4500원, 총 19500원
#   주문 25000원, 5km -> 배달료 0원, 총 25000원
#   주문  8000원, 1km -> 배달료 3500원, 총 11500원
# -------------------------------------------------------------
# 아래 주문 목록을 모두 처리하세요. [주문금액, 거리km]

# orders = [[15000, 3], [25000, 5], [8000, 1]]

# # 전역 상수
# BASE_FEE = 3000  # (기본 배달료)
# FREE_LIMIT = 20000  # (무료배달 기준액)
# EXTRA_PER_KM = 500  # (1km당 추가요금)


# def get_delivery_fee(order_price, distance_km):
#     if order_price >= FREE_LIMIT:
#         free_fee = 0
#         return free_fee
#     else:
#         deliver_fee = BASE_FEE + (distance_km * EXTRA_PER_KM)
#         return deliver_fee


# for o in orders:
#     get_delivery_fee(o[0], o[1])
#     print(
#         f"주문 {o[0]}원, {o[1]}km -> 배달료 {get_delivery_fee(o[0], o[1])}원, 총 {get_delivery_fee(o[0], o[1]) + o[0]}원"
#     )


# [17] 방문자 카운터
# -------------------------------------------------------------
# 함수 세 개를 만드세요.
#   visit(count)        : 방문자 수를 1 늘려서 돌려준다
#   reset()             : 0 을 돌려준다
#   show_count(count)    : "현재 방문자: N명" 형태로 출력

# 아래 순서대로 실행하세요.
#   방문 -> 방문 -> 방문 -> 현황 출력 -> 초기화 -> 현황 출력

# [기대 결과]

#   현재 방문자: 3명
#   현재 방문자: 0명
# -------------------------------------------------------------
# count = 0


# def visit(count):
#     count += 1
#     return count


# def reset():
#     return 0


# def show_count(count):
#     print(f"현재 방문자: {count}명")
#     return count


# visit(count)
# count = visit(count)  # 변수에 return값(+1) 대입

# visit(count)
# count = visit(count) # 변수에 return값(+1) 대입

# visit(count)
# count = visit(count) # 변수에 return값(+1) 대입

# show_count(count) # 현황 출력 (3)

# count = reset() # 변수에 return값(0) 대입

# show_count(count) # 현황 출력 (0)


# [18] 성적 관리 프로그램

# -------------------------------------------------------------

# 아래 함수들을 조립해서 성적표를 출력하세요.

#   get_average(scores)       : 평균 (소수 첫째 자리)   ← 6번에서 만든 것 재사용!

#   get_grade(avg)            : 등급 (90 A / 80 B / 70 C / 그 외 D) ← 6번 재사용!

#   get_best(students)        : 평균이 가장 높은 학생 이름

#   print_report(students)    : 성적표 전체 출력

#

# [기대 결과]

#   ===== 성적표 =====

#   김철수   91.7  A

#   이영희   78.3  C

#   박민수   85.0  B

#   최지은   62.7  D

#   ------------------

#   전체 평균: 79.4

#   최고 득점: 김철수

#

#   6번에서 만든 함수를 다시 만들지 말고 그대로 쓰세요.

# -------------------------------------------------------------
# class_scores = {
#     "김철수": [90, 85, 100],
#     "이영희": [70, 95, 70],
#     "박민수": [80, 85, 90],
#     "최지은": [55, 70, 63],
# }


# # 리스트의 평균 (소수 첫째 자리 반올림)
# def get_average(scores):
#     avg = round(scores, 1)
#     return avg


# # 등급 (90이상 A, 80이상 B, 70이상 C, 나머지 D)
# def get_grade(score):
#     if score >= 90:
#         return "A"
#     if score >= 80:
#         return "B"
#     if score >= 70:
#         return "C"
#     return "D"


# # 평균 높은 학생 담는 함수
# def get_best(students):
#     avg_rank = 0
#     high_stu = list(students.keys())[0]  # noqa: RUF015
#     for s in students:
#         # 학생 점수 합계
#         stu_sum = sum(students.get(s))

#         # 시험 과목
#         len_test = len(students.get(s))

#         # 점수 평균
#         score_avg = stu_sum / len_test

#         if avg_rank < score_avg:
#             avg_rank = score_avg
#             high_stu = s
#     return high_stu


# # 학생 평균 합계 담을 변수
# avg_sum = 0

# for s in class_scores:
#     # 학생 수
#     students = len(class_scores)

#     # 학생 점수 합계
#     students_sum = sum(class_scores.get(s))

#     # 시험 과목
#     len_test = len(class_scores.get(s))

#     # 점수 평균
#     score_avg = students_sum / len_test

#     # 평균값 함수 이동
#     get_average(score_avg)

#     # 등급 함수 이동
#     get_grade(score_avg)

#     # 학생이름 / 평균 / 등급
#     # print(f"{s}  평균 {get_average(score_avg)}  등급 {get_grade(score_avg)}")

#     # 학생 평균 합계
#     avg_sum += get_average(score_avg)


# print(f"전체 평균: {round(avg_sum / students, 2)}")
# print(f"최고 득점: {get_best(class_scores)}")


# [19] 지출 분석기

# -------------------------------------------------------------

# 한 달 지출 내역을 분석하는 프로그램입니다. 함수로 나눠 만드세요.

#   total_spent(records)         : 총 지출액

#   spent_by_category(records)   : 카테고리별 합계 딕셔너리

#   biggest_category(records)    : 가장 많이 쓴 카테고리

#   over_budget(records, budget) : 예산 초과 여부(True/False)와 차액을 함께 반환

#                                  (return 초과여부, 차액)

#   make_bar(amount, unit)       : 막대그래프 문자열

#                                  (1만원당 ■ 하나. unit 기본값 10000)

# records = [
#     {"항목": "점심", "분류": "식비", "금액": 45000},
#     {"항목": "지하철", "분류": "교통", "금액": 45000},
#     {"항목": "저녁", "분류": "식비", "금액": 75000},
#     {"항목": "옷", "분류": "쇼핑", "금액": 90000},
#     {"항목": "영화", "분류": "문화", "금액": 30000},
# ]
# BUDGET = 250000


# # 총 지출액
# def total_spent(records):
#     sum_spent = 0
#     for r in records:
#         sum_spent += r.get("금액")
#     return sum_spent


# # 카테고리별 합계 딕셔너리
# def spent_by_category(records):
#     category = {}
#     for c in records:
#         if (c["분류"] in category) == True:
#             category[c["분류"]] += 1
#         else:
#             category[c["분류"]] = 1
#     return category


# # 가장 많이 쓴 카테고리
# def biggest_category(records):
#     biggest_cnt = 0
#     big_categroy = ""
#     for pick in records:
#         if records.get(pick) > biggest_cnt:
#             biggest_cnt = records.get(pick)
#             big_categroy = pick
#     return big_categroy


# # 예산 초과 여부(True/False)와 차액을 함께 반환
# def over_budget(records, budget):
#     if records > budget:
#         over_cash = records - budget
#         print(f"예산 {budget} -> {over_cash}원 초과!")
#         return over_cash
#     return False


# # 막대그래프 문자열
# def make_bar(amount, unit):
#     # for문으로 돌아가는 결과물을 누적하여 저장하기 위한 변수 설정
#     rt = ""
#     for rs in amount:
#         # 사각형 출력을 위한 정수형 변수
#         bar_count = int(amount.get(rs) // unit)
#         rt += f"{rs}   {amount.get(rs)}    {'■ ' * bar_count} \n"
#     return rt


# total_spent(records)

# spent_by_category(records)
# spent_dic = spent_by_category(records)

# biggest_category(spent_dic)


# records_spent = {}
# for r in records:
#     if records_spent.get(r.get("분류")) is None:
#         records_spent[r.get("분류")] = 0 + r.get("금액")
#     else:
#         records_spent[r.get("분류")] += r.get("금액")

# print(f"총 지출: {total_spent(records)}")
# print()
# print("[카테고리별]")
# print(make_bar(records_spent, 10000))
# print(f"가장 많이 쓴 곳: {biggest_category(spent_dic)}")
# print()
# print(f"카테고리 딕셔너리: {spent_by_category(records)}")

# [기대 결과]

#   총 지출: 285000원

#   [카테고리별]

#     식비    120000  ■■■■■■■■■■■■

#     교통     45000  ■■■■

#     쇼핑     90000  ■■■■■■■■■

#     문화     30000  ■■■

#   가장 많이 쓴 곳: 식비

#   예산 250000원 -> 35000원 초과!


# -------------------------------------------------------------
# [20] 간단한 메뉴 프로그램
# -------------------------------------------------------------

# 반복문 + 함수 + 딕셔너리를 모두 쓰는 종합 문제입니다.

# 할 일 목록(To-do) 프로그램을 만드세요.
#   add_task(tasks, name)      : 할 일 추가 (완료 여부는 False로)
#   done_task(tasks, name)     : 완료 처리 (없으면 안내 메시지)
#   show_tasks(tasks)          : 전체 목록 출력 (완료는 [v], 미완료는 [ ])
#   count_done(tasks)          : 완료한 개수


# 아래 순서로 실행하세요.
#   "보고서 작성" 추가 -> "회의 준비" 추가 -> "메일 확인" 추가
#   -> "회의 준비" 완료 -> "없는일" 완료 시도 -> 목록 출력


# [기대 결과]
#   '없는일' 은(는) 목록에 없습니다
#   [할 일 목록]
#     [ ] 보고서 작성
#     [v] 회의 준비
#     [ ] 메일 확인

#   완료: 1 / 3


# while True + input() 으로 실제 메뉴를 만들어 보세요.
#     1. 추가  2. 완료  3. 목록  4. 종료

# -------------------------------------------------------------
tasks = {}


# 할 일 추가 (완료 여부는 False로)
def add_task(tasks, name):
    if tasks.get(name) is None:
        # 완료 여부는 'False'로 넣기
        tasks[name] = False
    return tasks


# 완료 처리 (없으면 안내 메시지)
def done_task(tasks, name):
    if (name in tasks) == True:
        tasks[name] = True
        return tasks
    if (name in tasks) == False:
        print(f"{name}은(는) 목록에 없습니다")


# 전체 목록 출력 (완료는 [v], 미완료는 [ ])
def show_tasks(tasks):
    for t in tasks:
        if tasks.get(t) == True:
            print(f"[v] {t}")
        else:
            print(f"[ ] {t}")


# 완료한 개수
def count_done(tasks):
    wan_cnt = 0
    tasks_len = len(tasks)
    for t in tasks:
        if tasks.get(t) == True:
            wan_cnt += 1
    print(f"완료: {wan_cnt} / {tasks_len}")


while True:
    work = int(input("원하는 작업을 입력하세요 (1. 추가  2. 완료  3. 목록  4. 종료): "))
    if work == 1:
        into = input("할 일 추가: ")
        add_task(tasks, into)
    elif work == 2:
        clear = input("완료한 일: ")
        done_task(tasks, clear)
    elif work == 3:
        show_tasks(tasks)
        count_done(tasks)
    elif work == 4:
        break

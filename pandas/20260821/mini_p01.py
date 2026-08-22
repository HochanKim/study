# """
# ============================================================
#  미니 프로젝트 1 - 성적 관리 프로그램
# ============================================================

#  [예상 소요 시간]  2시간

#  [사용하는 것]
#    조건문, 반복문, 함수, 리스트, 딕셔너리

#  [만들 것]
#    학생들의 성적을 관리하고 통계를 내는 프로그램

#  [진행 방법]
#    단계가 8개로 나뉘어 있습니다. 순서대로 하나씩 완성하세요.
#    각 단계 아래의 [확인] 코드를 실행해서 결과를 맞춰보면 됩니다.

#    한 단계에서 막히면 그 단계는 건너뛰고 다음으로 가도 됩니다.
#    뒤 단계에서 앞 함수를 쓰는 경우, 임시로 값을 직접 넣어서
#    진행할 수 있습니다.
# ============================================================
# """


# -------------------------------------------------------------
# 데이터 (이 부분은 그대로 두세요)
# -------------------------------------------------------------
# 학생 한 명은 딕셔너리 하나로 표현합니다.
students = [
    {"이름": "김철수", "반": "A", "국어": 90, "영어": 85, "수학": 100},
    {"이름": "이영희", "반": "A", "국어": 70, "영어": 95, "수학": 70},
    {"이름": "박민수", "반": "B", "국어": 55, "영어": 70, "수학": 63},
    {"이름": "최지은", "반": "A", "국어": 80, "영어": 85, "수학": 90},
    {"이름": "정하늘", "반": "B", "국어": 95, "영어": 92, "수학": 88},
    {"이름": "강동원", "반": "B", "국어": 60, "영어": 45, "수학": 72},
    {"이름": "윤서연", "반": "A", "국어": 88, "영어": 91, "수학": 79},
    {"이름": "임재현", "반": "B", "국어": 45, "영어": 58, "수학": 51},
]

SUBJECTS = ["국어", "영어", "수학"]

# print(students[0].get("이름"))
# print(students[3].get("이름"))
# print(students[2].get("반"))
# print(students[5].get("국어"))

# =============================================================
# 1단계. 기본 계산 함수 만들기
# =============================================================
#
# 함수 세 개를 만드세요.
#
#   get_total(student)
#     한 학생의 세 과목 총점을 돌려준다
#
#   get_average(student)
#     한 학생의 평균을 돌려준다 (소수 첫째 자리까지)
#
#   get_grade(average)
#     평균으로 등급을 돌려준다
#     90 이상 A / 80 이상 B / 70 이상 C / 60 이상 D / 그 외 F
#
# SUBJECTS 리스트를 반복문으로 돌면 과목 이름을 하나씩 얻을 수 있습니다.
# -------------------------------------------------------------
# [확인]
# [출력]
#   김철수  총점 275  평균 91.7  등급 A
#   이영희  총점 235  평균 78.3  등급 C
#   임재현  총점 154  평균 51.3  등급 F

# for s in [students[0], students[1], students[7]]:
#     avg = get_average(s)
#     print(f"{s['이름']}  총점 {get_total(s)}  평균 {avg}  등급 {get_grade(avg)}")

# 합계 함수
def get_total(student):
  sum_scores = student.get("국어") + student.get("영어") + student.get("수학")
  return sum_scores

# 평균 함수
def get_average(student):
  set_avg = round(student / len(SUBJECTS), 1)
  return set_avg

# 등급 함수
def get_grade(average):
  if average >= 90:
    return "A"
  elif average >= 80:
    return "B"
  elif average >= 70:
    return "C"
  elif average >= 60:
    return "D"
  else:
    return "F"


for s in [students[0], students[1], students[7]]:
    avg = get_average(get_total(s))
    print(f"{s['이름']}  총점 {get_total(s)}  평균 {avg}  등급 {get_grade(avg)}")
print()

# =============================================================
# 2단계. 성적표 출력하기
# =============================================================
#
# 함수 하나를 만드세요.
#
#   print_report(students)
#     전체 학생의 성적표를 표 형태로 출력한다
#     아래 형태를 참고하세요.
#
#       이름     반   국어  영어  수학   총점   평균  등급
#       ------------------------------------------------
#       김철수    A    90   85  100   275   91.7   A
#       ...
#
#     칸을 맞추려면 f"{값:<6}" (왼쪽) f"{값:>4}" (오른쪽) 을 씁니다.
# -------------------------------------------------------------
# [확인]
# print_report(students)

for d in students:
  # 총점, 평균, 등급 추가 (각 딕셔너리에)
  d["총점"] = get_total(d)
  d["평균"] = get_average(d["총점"])
  d["등급"] = get_grade(d["평균"])

def print_report(students):
  for i in students:
    # 키값들을 리스트화
    keys_ls = list(i.keys())

  for k in keys_ls:
    # 리스트에 담은 키값들 풀기
    print(f"{k:<5}", end=" ")
  print()
  print("-"*60)
  # 학생 정보 리스트를 파라미터로 전달 받아
  for i in students:
    # 밸류값들을 리스트화
    v_ls = list(i.values())
    for v in v_ls:
      # 리스트에 담은 밸류값들을 나열하기
      print(f"{v:<8}", end="")
    # 리스트 덩어리에 맞게 줄바꿈
    print()

print_report(students)
print()

# =============================================================
# 3단계. 과목별 통계
# =============================================================
#
# 함수 세 개를 만드세요.
#
#   subject_average(students, subject)
#     특정 과목의 전체 평균을 돌려준다 (소수 첫째 자리)
#
#   subject_max(students, subject)
#     특정 과목의 최고점을 받은 학생 이름과 점수를 함께 돌려준다
#     동점이면 먼저 나온 학생을 돌려준다
#
#   print_subject_stats(students)
#     아래 형태로 출력한다
#
#       [과목별 통계]
#         국어  평균 72.9  최고 정하늘(95)
#         영어  평균 77.6  최고 OOO(00)
#         수학  평균 76.6  최고 OOO(000)
# -------------------------------------------------------------
# [확인]
# print_subject_stats(students)


def subject_average(students, subject):
  subj_sum = 0
  for s in students:
    subj_sum += s.get(subject)
  subj_avg = subj_sum / len(students)
  return round(subj_avg, 1)

def subject_max(students, subject):
  max_num = 0
  max_stu = ""
  for s in students:
    if s.get(subject) > max_num:
      max_num = s.get(subject)
      max_stu = s.get("이름")
  return max_stu, max_num


def print_subject_stats(students):
  # SUBJECTS 리스트를 활용한 for문으로 각각 함수로 파라미터 전달
  for subject in SUBJECTS:
    avg = subject_average(students, subject)
    name, score = subject_max(students, subject)
    print(f"{subject}  평균 {avg}  최고 {name}({score})")

print_subject_stats(students)
print()

# =============================================================
# 4단계. 등수 매기기
# =============================================================
#
# 함수 두 개를 만드세요.
#
#   get_rank(students, name)
#     그 학생의 등수를 돌려준다
#     평균이 높을수록 1등이다
#     같은 평균이면 같은 등수로 본다
#     없는 이름이면 None 을 돌려준다
#
#   print_ranking(students)
#     평균이 높은 순으로 정렬해서 출력한다
#
#       [전체 등수]
#         1등  김철수  91.7
#         2등  정하늘  91.7
#         3등  윤서연  86.0
#         ...
#
#     김철수와 정하늘은 평균이 같습니다.
#     동점이면 먼저 나온 사람이 앞에 오도록 하세요.
#
#     정렬은 아래처럼 하면 됩니다.
#       sorted(리스트, key=lambda x: 기준값, reverse=True)
# -------------------------------------------------------------
# [확인]
# print_ranking(students)
# print("김철수의 등수:", get_rank(students, "김철수"))
# print("없는사람의 등수:", get_rank(students, "없는사람"))

def get_rank(students, name):
  # 이름 등록 여부 변수
  check_name = None
  for stu in students:
    if stu["이름"] == name:
      check_name = stu
      break
  if check_name is None:
    # 존재하지 않으면 None으로 반환
    return None
  # 평균 함수에 보낼 합계
  total = get_total(check_name)
  # 찾는 학생의 평균 구하기
  avg = get_average(total)

  # 평균 비교를 위한 변수
  over_avg_cnt = 1

  for stu in students:
    # 리스트 내 학생들의 합계
    stu_total = get_total(stu)
    if get_average(stu_total) > avg:
      over_avg_cnt += 1

  # 평균이 높은 사람 최종 카운트를 등수로 return
  return f"{over_avg_cnt}등"

def print_ranking(students):
  # 정렬식
  sorted_students = sorted(
    students, key=lambda stu: get_average(get_total(stu)), reverse=True
  )

  print("[전체 등수]")
  # 등수 출력을 위한 enumerate for문
  # 1등부터 체크 (start=1)
  for idx, sort in enumerate(sorted_students, start=1):
    print(f"{idx}등 {sort.get("이름")} {get_average(get_total(sort))}")


print_ranking(students)
print("김철수의 등수:", get_rank(students, "김철수"))
print("없는사람의 등수:", get_rank(students, "없는사람"))
print()


# =============================================================
# 5단계. 반별 비교
# =============================================================
#
# 함수 두 개를 만드세요.
#
#   group_by_class(students)
#     반별로 학생을 묶어 딕셔너리로 돌려준다
#     {"A": [학생1, 학생2, ...], "B": [...]}
#
#   print_class_stats(students)
#     반별로 아래를 출력한다
#
#       [반별 통계]
#         A반  4명  평균 85.2  최고 김철수(91.7)
#         B반  4명  평균 66.2  최고 정하늘(91.7)
#
#     반 이름은 가나다순으로 출력하세요.
# -------------------------------------------------------------
# [확인]
# print_class_stats(students)

def group_by_class(students):
  class_divid = {}
  for i in students:
    class_name = i.get("반")
    if (class_name in class_divid) is True:
      # 값이 딕셔너리에 존재하면 "이름"의 밸류를 딕셔너리 내 리스트에 추가
      class_divid[class_name].append(i)
    else:
      # 값이 없으면 "이름"의 밸류를 리스트로 만들어서 추가
      class_divid[class_name] = [i]
  return class_divid

def print_class_stats(students):
  class_a = group_by_class(students).get('A')
  class_a_sum = 0
  a_avg_d = {}
  for a in class_a:
      # A반 합계
      a_totals = get_total(a)
      # A반 전체 평균
      a_avgs = get_average(a_totals)
      # A반 학생 성적을 딕셔너리로 저장
      a_avg_d[a.get("이름")] = a_avgs
      class_a_sum += a_avgs
  class_a_avg = round(class_a_sum / len(class_a), 1)

  a_max_num = 0 # 최고 평균 점수
  a_max_stu = ""  # 최고 평균 학생 이름
  for p in a_avg_d:
      if a_avg_d.get(p) > a_max_num:
          a_max_num = a_avg_d.get(p)
          a_max_stu = p

  class_b = group_by_class(students).get('B')
  class_b_sum = 0
  b_avg_d = {}
  for b in class_b:
      # B반 합계
      b_totals = get_total(b)
      # B반 전체 평균
      b_avgs = get_average(b_totals)
      # B반 학생 성적을 딕셔너리로 저장
      b_avg_d[b.get("이름")] = b_avgs
      class_b_sum += b_avgs
  class_b_avg = round(class_b_sum / len(class_b), 1)

  b_max_num = 0 # 최고 평균 점수
  b_max_stu = ""  # 최고 평균 학생 이름
  for p in b_avg_d:
      if b_avg_d.get(p) > b_max_num:
          b_max_num = b_avg_d.get(p)
          b_max_stu = p


  print("[반별 통계]")
  #         A반  4명  평균 85.2  최고 김철수(91.7)
  print(f"A반 {len(class_a)}명 평균 {class_a_avg} 최고 {a_max_stu}({a_max_num})")
  print(f"B반 {len(class_b)}명 평균 {class_b_avg} 최고 {b_max_stu}({b_max_num})")

print_class_stats(students)
print()

# =============================================================
# 6단계. 조건으로 찾기
# =============================================================
#
# 함수 세 개를 만드세요.
#
#   find_by_grade(students, grade)
#     특정 등급인 학생 이름 리스트를 돌려준다
#
#   find_failed(students, cutoff=60)
#     한 과목이라도 cutoff 미만인 학생을 찾아
#     [(이름, [과락과목들]), ...] 형태로 돌려준다
#
#   print_warning(students)
#     과락자를 아래 형태로 출력한다
#
#       [과락 경고]
#         박민수  국어(55)
#         강동원  영어(45)
#         임재현  국어(45), 영어(58), 수학(51)
#
#     과락자가 없으면 "과락자 없음" 을 출력한다
# -------------------------------------------------------------
# [확인]
# print("A등급:", find_by_grade(students, "A"))
# print("F등급:", find_by_grade(students, "F"))
# print()
# print_warning(students)

# 등급별 리스트 리턴 함수
def find_by_grade(students, grade):
  grade_ls = []
  for s in students:
    avg = get_average(get_total(s))
    if get_grade(avg) == grade:
      grade_ls.append(s["이름"])
  return grade_ls


def find_failed(students, cutoff=60):
  # 과락 점수 있는 학생 리스트
  cutoff_ls = []
  for s in students:
    # 과락 과목들 담는 리스트
      f_subjects = []
      # 각 과락 값들을 과목과 해당 과목 점수(s.get("국어"))를 같이 저장
      if s.get("국어") < cutoff:
        f_subjects.append(f"국어({s.get("국어")})")
      if s.get("영어") < cutoff:
        f_subjects.append(f"영어({s.get("영어")})")
      if s.get("수학") < cutoff:
        f_subjects.append(f"수학({s.get("수학")})")

      if f_subjects:
        # 과락 과목에 포함된 점수의 학생들과 튜플로
        # 리스트에 묶어서 담기
        cutoff_ls.append(
          (s.get("이름"), f_subjects)
        )
  return cutoff_ls


def print_warning(students):
  warning_out = find_failed(students)
  if len(warning_out) == 0:
    print("과락자 없음")
  else:
    print("[과락 경고]")
    for name, subj in warning_out:
      print(name, end=" ")
      for idx, s in enumerate(subj):
        # 리스트로 묶인 subj 값들을 풀어주기
        if idx == len(subj) - 1:
          # idx => 0 1 2
          # len(subj) = 3 // 1 2 3
          print(s)
        else:
          # 마지막 리스트 값의 다음에 쉼표(,) 붙이기
          print(s, end=", ")

print("A등급:", find_by_grade(students, "A"))
print("F등급:", find_by_grade(students, "F"))
print()
print_warning(students)
print()


# =============================================================
# 7단계. 학생 추가와 수정
# =============================================================
#
# 함수 세 개를 만드세요.
# 원본 리스트를 직접 바꾸지 말고 새 리스트를 돌려주세요.
#
#   add_student(students, name, class_name, kor, eng, math)
#     학생을 추가한 새 리스트를 돌려준다
#     이미 있는 이름이면 "이미 있는 학생: 김철수" 출력하고
#     원본과 같은 내용의 새 리스트를 돌려준다
#
#   update_score(students, name, subject, score)
#     특정 학생의 특정 과목 점수를 바꾼 새 리스트를 돌려준다
#     0~100 범위를 벗어나면 "잘못된 점수: 150" 출력하고 바꾸지 않는다
#     없는 학생이면 "없는 학생: 홍길동" 출력
#
#   remove_student(students, name)
#     학생을 뺀 새 리스트를 돌려준다
#     없는 학생이면 "없는 학생: 홍길동" 출력
#
# 딕셔너리도 복사해야 합니다. dict(원본) 을 쓰면 됩니다.
# -------------------------------------------------------------
# [확인]
# [출력]
#   추가 후 인원: 9명
#   이미 있는 학생: 김철수
#   잘못된 점수: 150
#   없는 학생: 홍길동
#   김철수 수학: 95
#   원본 김철수 수학: 100
#   삭제 후 인원: 8명

# new_list = add_student(students, "한지민", "A", 85, 90, 88)
# print(f"추가 후 인원: {len(new_list)}명")
#
# new_list = add_student(new_list, "김철수", "A", 50, 50, 50)
#
# new_list = update_score(new_list, "김철수", "수학", 150)
# new_list = update_score(new_list, "홍길동", "수학", 90)
# new_list = update_score(new_list, "김철수", "수학", 95)
#
# for s in new_list:
#     if s["이름"] == "김철수":
#         print("김철수 수학:", s["수학"])
# for s in students:
#     if s["이름"] == "김철수":
#         print("원본 김철수 수학:", s["수학"])
#
# new_list = remove_student(new_list, "한지민")
# print(f"삭제 후 인원: {len(new_list)}명")


def add_student(students, name, class_name, kor, eng, math):
  # 새로 생성한 빈 리스트에 원본 리스트 복사
  new_list = []
  for s in students:
      new_list.append(s.copy())
  add_stu = {}
  for s in students:
    if s["이름"] == name:
      print(f"이미 있는 학생: {name}")
      break
    add_stu["이름"] = name
    add_stu["반"] = class_name
    add_stu["국어"] = kor
    add_stu["영어"] = eng
    add_stu["수학"] = math
  if add_stu: # 'add_stu'에 값이 존재하면 True
    new_list.append(add_stu)
    return new_list
  else:
    return new_list

def update_score(students, name, subject, score):
  for s in students:
    if (s["이름"] == name) is True:
      if 0 > score or 100 < score:
        print(f"잘못된 점수: {score}")
        return students
      s[subject] = score
      return students
  print(f"없는 학생: {name}")
  return students


def remove_student(students, name):
  for i in students:
      # 리스트 내 딕셔너리(i) 중 name값과 맞는 것은
      # 해당 딕셔너리 내용 전부 제거
      if i.get("이름") == name:
          i.clear()

  for ls in students:
      # 제거된 값의 흔적(빈 딕셔너리: {}) 찾아서 삭제 
      if ls == {}:
          students.remove(ls)
  return students


new_list = add_student(students, "한지민", "A", 85, 90, 88)
print(f"추가 후 인원: {len(new_list)}명")
new_list = add_student(new_list, "김철수", "A", 50, 50, 50)
print(f"추가 후 인원: {len(new_list)}명")

new_list = update_score(new_list, "김철수", "수학", 150)
new_list = update_score(new_list, "홍길동", "수학", 90)
new_list = update_score(new_list, "김철수", "수학", 95)

for s in new_list:
    if s["이름"] == "김철수":
        print("김철수 수학:", s["수학"])
for s in students:
    if s["이름"] == "김철수":
        print("원본 김철수 수학:", s["수학"])

new_list = remove_student(new_list, "한지민")
print(f"삭제 후 인원: {len(new_list)}명")
print()

# =============================================================
# 8단계. 전체 리포트
# =============================================================
#
# 함수 하나를 만드세요.
#
#   print_full_report(students)
#     지금까지 만든 함수들을 모두 불러서
#     아래 형태의 종합 리포트를 출력한다
#
#       ==================================================
#        성적 종합 리포트
#       ==================================================
#       전체 인원: 8명
#       전체 평균: 75.7
#
#       (성적표)
#
#       (과목별 통계)
#
#       (반별 통계)
#
#       (전체 등수)
#
#       (과락 경고)
#       ==================================================
#
# 새로 계산하지 말고 앞에서 만든 함수를 재사용하세요.
# -------------------------------------------------------------
# [확인]
# print_full_report(students)


def print_full_report(students):
  print("=" * 30)
  print("성적 종합 리포트")
  print("=" * 30)
  print(f"전체 인원: {len(students)}명")
  sum_avg = 0
  for s in students:
    totals = get_total(s)
    avg = get_average(totals)
    sum_avg += avg
  all_avg = sum_avg / len(students)
  print(f"전체 평균: {round(all_avg, 1)}")
  print()
  print_report(students)
  print()
  print_subject_stats(students)
  print()
  print_class_stats(students)
  print()
  print_ranking(students)
  print()
  print_warning(students)

print_full_report(students)



# =============================================================
# 도전 과제 (시간이 남으면)
# =============================================================
#
# 1) 메뉴가 있는 프로그램으로 만들기
#    while True 와 input() 을 써서 아래 메뉴를 만드세요.
#      1. 성적표 보기
#      2. 학생 추가
#      3. 점수 수정
#      4. 등수 보기
#      5. 종료
#
# 2) 과목을 늘려도 동작하게 만들기
#    SUBJECTS 에 "과학" 을 추가해도
#    모든 함수가 그대로 동작하는지 확인하세요.
#    안 되는 함수가 있다면 고치세요.
#
# 3) 등급별 인원수를 막대그래프로 보여주기
#      A ***
#      B **
#      C *
#      D *
#      F *
# -------------------------------------------------------------
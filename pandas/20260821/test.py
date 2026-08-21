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

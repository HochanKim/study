from pathlib import Path
import csv
import os

BASE = Path(__file__).parent  # 이 파일이 있는 폴더
DATA = BASE / "data"  # 그 안에 data 폴더
DATA.mkdir(exist_ok=True)  # 폴더 만들기

e_file = DATA / "employees.csv"
#  ---------------------------------------------------------
# 3-7. 읽고 변환하는 함수 만들기
# -------------------------------------------------------------
#
# 매번 파일 열고 변환하는 코드를 쓰면 번거롭습니다.
# 함수로 만들어 두면 한 줄로 끝납니다.

print("\n" + "=" * 60)
print(" 3-7. 재사용 함수 만들기")
print("=" * 60)


def to_int(value, default=0):
    """문자열을 정수로 바꾼다. 실패하면 default 를 돌려준다"""
    try:
        return int(str(value).strip())
    except (ValueError, TypeError):
        return default


def read_csv(path, encoding="utf-8"):
    """CSV 를 읽어 딕셔너리 리스트로 돌려준다. 없으면 빈 리스트"""
    rows = []
    try:
        with open(path, "r", encoding=encoding, newline="") as f:
            for row in csv.DictReader(f):
                rows.append(row)
    except FileNotFoundError:
        pass
    return rows


def load_employees(path):
    """직원 CSV 를 읽고 숫자 항목을 변환해서 돌려준다"""
    rows = read_csv(path)
    for row in rows:
        row["연봉"] = to_int(row["연봉"])
        row["입사년도"] = to_int(row["입사년도"])
    return rows


employees = load_employees(e_file)

print(f"  {len(employees)}명의 데이터를 읽었습니다")
print("  첫 번째 사람:", employees[0])
print("  연봉의 자료형:", type(employees[0]["연봉"]).__name__, " <- 이제 숫자!")


#  ---------------------------------------------------------
# 3-8. 집계하기 - 합계, 평균, 최대, 최소
# -------------------------------------------------------------
print("\n" + "=" * 60)
print(" 3-8. 기본 집계")
print("=" * 60)

salaries = []
for e in employees:
    salaries.append(e["연봉"])

print("  연봉 목록:", salaries)
print("  인원     :", len(salaries), "명")
print("  합계     :", sum(salaries), "만원")
print("  평균     :", round(sum(salaries) / len(salaries), 1), "만원")
print("  최고     :", max(salaries), "만원")
print("  최저     :", min(salaries), "만원")

# 필터링도 해봅시다
print("\n  [개발팀만]")
for e in employees:
    if e["부서"] == "개발":
        print(f"     {e['이름']} - {e['연봉']}만원")

print("\n  [연봉 5000 이상]")
for e in employees:
    if e["연봉"] >= 5000:
        print(f"     {e['이름']} - {e['연봉']}만원")


# ============================================================
#                    4 부 .  실    전
# ============================================================

# %% ---------------------------------------------------------
# 4-1. ★핵심★ 그룹별로 묶기
# -------------------------------------------------------------
#
# 이게 데이터 분석의 기본 동작입니다.
#
# [하고 싶은 일]
#   부서별로 인원, 연봉 합계, 평균을 구하기
#
# [방법]
#   딕셔너리를 '누적 통'으로 쓰면 됩니다.
#     - 처음 보는 부서면 0으로 시작
#     - 이미 본 부서면 기존 값에 더하기

print("\n" + "=" * 60)
print(" 4-1. 부서별 집계")
print("=" * 60)

dept_total = {}  # {부서: 연봉합계}
dept_count = {}  # {부서: 인원수}

for e in employees:
    dept = e["부서"]
    pay = e["연봉"]

    # .get(키, 0) 은 키가 없으면 0을 돌려줍니다
    dept_total[dept] = dept_total.get(dept, 0) + pay
    dept_count[dept] = dept_count.get(dept, 0) + 1

print(f"  {'부서':<6}{'인원':>4}{'합계':>9}{'평균':>10}")
print("  " + "-" * 29)

for dept in dept_total:
    avg = dept_total[dept] / dept_count[dept]
    print(f"  {dept:<6}{dept_count[dept]:>4}{dept_total[dept]:>9}{avg:>10.1f}")


# .get(키, 기본값) 설명

#  dept_total[dept] = dept_total.get(dept, 0) + pay
#                     └──────────┬──────────┘
#                     키가 있으면 그 값, 없으면 0

#  if 로 쓰면 이렇게 됩니다 (같은 동작)

#  if dept not in dept_total:
#      dept_total[dept] = 0
#  dept_total[dept] = dept_total[dept] + pay

#  .get() 을 쓰면 세 줄이 한 줄로 줄어듭니다.
#  집계할 때 정말 자주 쓰는 방법입니다.


#  ---------------------------------------------------------
# 4-2. 집계 함수로 만들기
# -------------------------------------------------------------
# 같은 코드를 상품별, 지점별에도 쓸 수 있게 함수로 뺍니다.

# print("\n" + "=" * 60)
# print(" 4-2. 집계 함수")
# print("=" * 60)


def sum_by(rows, group_key, value_key):
    """group_key 별로 value_key 를 합산한 딕셔너리를 돌려준다

    rows      : 딕셔너리 리스트
    group_key : 묶을 기준 키   (예: "부서")
    value_key : 합산할 값의 키 (예: "연봉")
    """
    result = {}
    for row in rows:
        key = row[group_key]
        result[key] = result.get(key, 0) + row[value_key]
    return result


def count_by(rows, group_key):
    """group_key 별 개수를 센 딕셔너리를 돌려준다"""
    result = {}
    for row in rows:
        key = row[group_key]
        result[key] = result.get(key, 0) + 1
    return result


def make_bar(value, unit=1000, mark="■"):
    """숫자를 막대그래프 문자열로 만든다"""
    return mark * int(value / unit)


by_dept = sum_by(employees, "부서", "연봉")
cnt_dept = count_by(employees, "부서")

print("  [부서별 연봉 합계]")
for dept, total in by_dept.items():
    print(f"     {dept:<5}{total:>7}만원  ({cnt_dept[dept]}명)  {make_bar(total, 500)}")

# 같은 함수를 입사년도별로도 쓸 수 있습니다
print("\n  [입사년도별 인원]")
by_year = count_by(employees, "입사년도")
for year in sorted(by_year):
    print(f"     {year}년: {by_year[year]}명  {make_bar(by_year[year], 1, '●')}")

# print("""
#   ★ 함수로 만들어 두니 부서별, 연도별에 그대로 재사용됩니다.
#     이게 함수를 만드는 이유입니다.
# """)


#  ---------------------------------------------------------
# 4-3. CSV 쓰기 - 그리고 엑셀 한글 깨짐 문제
# -------------------------------------------------------------
#
# [문법]
#
#   with open(경로, "w", encoding="utf-8-sig", newline="") as f:
#       writer = csv.writer(f)
#       writer.writerow(["열1", "열2"])       # 한 줄 쓰기
#       writer.writerows([[1, 2], [3, 4]])    # 여러 줄 한 번에
#
#
# ★★★ encoding="utf-8-sig" 에 주목하세요 ★★★
#
#   그냥 "utf-8" 로 저장하면
#   엑셀에서 열 때 한글이 깨집니다
#
#   [왜 그럴까요?]
#     엑셀은 파일을 열 때 "이거 무슨 인코딩이지?" 를 스스로 추측합니다.
#     그런데 한국어 윈도우에서는 cp949 라고 잘못 찍는 경우가 많습니다.
#
#   [utf-8-sig 는 뭐가 다른가요?]
#     파일 맨 앞에 아주 작은 표시를 붙입니다. (BOM 이라고 부릅니다)
#     "나는 UTF-8이야" 라는 이름표 같은 겁니다.
#     엑셀이 그걸 보고 제대로 열어줍니다.
#
#
#   [정리]
#     읽을 때        encoding="utf-8"
#     엑셀용 저장    encoding="utf-8-sig"
#
#   실무에서 "왜 엑셀로 열면 글자가 깨지죠?" 의 99%가 이것 때문입니다.

# print("\n" + "=" * 60)
# print(" 4-3. 결과를 CSV 로 저장하기")
# print("=" * 60)

# result_file = DATA / "부서별_집계.csv"

# with open(result_file, "w", encoding="utf-8-sig", newline="") as f:
#     writer = csv.writer(f)

#     writer.writerow(["부서", "인원", "연봉합계", "평균연봉"])  # 헤더

#     for dept in by_dept:
#         avg = round(by_dept[dept] / cnt_dept[dept], 1)
#         writer.writerow([dept, cnt_dept[dept], by_dept[dept], avg])

# print(f"  '{result_file.name}' 저장 완료")
# print("   이 파일을 엑셀로 열어보세요. 한글이 안 깨집니다.")

# # 저장한 파일 확인
# print("\n  [저장된 내용]")
# with open(result_file, "r", encoding="utf-8-sig", newline="") as f:
#     for row in csv.reader(f):
#         print("     ", row)

# #    읽을 때도 utf-8-sig 로 열었습니다.
# #   utf-8 로 열면 첫 번째 값 앞에 이상한 글자가 붙어 보입니다.
# #   (BOM 표시가 그대로 읽히기 때문)


# # ---------------------------------------------------------
# # 4-4. DictWriter 로 저장하기
# # -------------------------------------------------------------
# #
# # DictReader 로 읽었으면, 쓸 때도 DictWriter 가 편합니다.
# # 열 이름을 지정하면 순서를 알아서 맞춰줍니다.

# print("\n" + "=" * 60)
# print(" 4-4. DictWriter")
# print("=" * 60)


# def save_csv(path, rows, fieldnames, encoding="utf-8-sig"):
#     """딕셔너리 리스트를 CSV 로 저장한다"""
#     with open(path, "w", encoding=encoding, newline="") as f:
#         writer = csv.DictWriter(f, fieldnames=fieldnames)
#         writer.writeheader()  # 헤더 자동 작성
#         writer.writerows(rows)  # 여러 줄 한 번에
#     return Path(path)


# new_people = [
#     {"이름": "신입A", "부서": "개발", "연봉": 3800},
#     {"이름": "신입B", "부서": "영업", "연봉": 3600},
#     {"이름": "신입C", "부서": "인사", "연봉": 3500},
# ]

# new_file = save_csv(DATA / "신입사원.csv", new_people, ["이름", "부서", "연봉"])

# print(f"  '{new_file.name}' 저장 완료")
# with open(new_file, "r", encoding="utf-8-sig") as f:
#     print(f.read())

# # [fieldnames 설명]
# #   어떤 열을 어떤 순서로 쓸지 지정합니다.
# #   딕셔너리에 이 목록에 없는 키가 있으면 에러가 납니다.
# #   반대로 목록에 있는데 딕셔너리에 없으면 빈 칸이 됩니다.


# #  ---------------------------------------------------------
# # 4-5. 실전: 지저분한 데이터 정리하기
# # -------------------------------------------------------------
# #
# # 실제 데이터는 절대 깨끗하지 않습니다.
# # 실무에서 흔히 만나는 문제들입니다.
# #
# #   - 값 앞뒤에 공백이 있음      " 4500 "
# #   - 값이 비어 있음             ""
# #   - 숫자 자리에 글자가 있음     "오천"
# #   - 단위가 붙어 있음           "4,500원"
# #
# # 이걸 어떻게 처리하느냐가 실무 능력입니다.

# print("\n" + "=" * 60)
# print(" 4-5. 지저분한 데이터 다루기")
# print("=" * 60)

# dirty = DATA / "dirty.csv"
# with open(dirty, "w", encoding="utf-8", newline="") as f:
#     f.write("이름,연봉\n")
#     f.write("김철수, 4500 \n")  # 공백이 섞임
#     f.write("이영희,\n")  # 값이 비어 있음
#     f.write("박민수,오천\n")  # 숫자가 아님
#     f.write("최지은,5100\n")  # 정상
#     f.write("정하늘,4200원\n")  # 단위가 붙음

# # ── 1차 시도: to_int 로만 처리
# clean = []
# problems = []

# with open(dirty, "r", encoding="utf-8", newline="") as f:
#     # enumerate(..., start=2) : 2번부터 번호를 매김
#     #   왜 2부터? 1번 줄은 헤더이므로 데이터는 2번 줄부터입니다.
#     #   나중에 "몇 번째 줄이 문제인지" 알려줄 때 씁니다.
#     for line_no, row in enumerate(csv.DictReader(f), start=2):
#         name = row["이름"].strip()
#         raw = row["연봉"].strip()

#         if raw == "":
#             problems.append((line_no, name, "값 없음"))
#             continue  # 다음 줄로

#         try:
#             clean.append({"이름": name, "연봉": int(raw)})
#         except ValueError:
#             problems.append((line_no, name, f"숫자 아님: {raw}"))

# print("  [1차 시도 - 단순 변환]")
# print(f"    정상 {len(clean)}건 / 문제 {len(problems)}건")
# for line_no, name, reason in problems:
#     print(f"      {line_no}번째 줄 {name}: {reason}")


# # ── 2차 시도: 값을 정리하는 함수를 만들어서 더 살려내기
# def clean_number(value, default=None):
#     """단위와 쉼표를 제거하고 숫자만 뽑아낸다

#     '4,500원'  ->  4500
#     ' 30개 '   ->  30
#     '오천'      ->  None (또는 default)
#     """
#     if value is None:
#         return default

#     text = str(value).strip()

#     # 제거할 문자들을 하나씩 없앱니다
#     for remove in [",", "원", "만원", "개", "명", "건", "%", " "]:
#         text = text.replace(remove, "")

#     if text == "":
#         return default

#     try:
#         return int(text)
#     except ValueError:
#         return default


# print("\n  [clean_number 함수 테스트]")
# print("     ' 4500 '   ->", clean_number(" 4500 "))
# print("     '4,500원'  ->", clean_number("4,500원"))
# print("     '4200원'   ->", clean_number("4200원"))
# print("     '오천'      ->", clean_number("오천"))
# print("     ''         ->", clean_number(""))

# # 2차 처리
# recovered = []
# still_bad = []

# with open(dirty, "r", encoding="utf-8", newline="") as f:
#     for line_no, row in enumerate(csv.DictReader(f), start=2):
#         name = row["이름"].strip()
#         n = clean_number(row["연봉"])
#         if n is None:
#             still_bad.append((line_no, name, row["연봉"]))
#         else:
#             recovered.append({"이름": name, "연봉": n})

# print("\n  [2차 시도 - clean_number 적용]")
# print(f"    정상 {len(recovered)}건 / 문제 {len(still_bad)}건")
# for r in recovered:
#     print("     ", r)

# print(f"\n   1차에서 {len(clean)}건이던 게 {len(recovered)}건으로 늘었습니다.")
# print("    '4200원' 이 살아났습니다. 정리 함수를 잘 만들면 버리는 데이터가 줄어듭니다.")

# # ── 문제 목록도 파일로 남기기
# err_file = DATA / "오류목록.csv"
# with open(err_file, "w", encoding="utf-8-sig", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["줄번호", "이름", "원본값"])
#     writer.writerows(still_bad)

# print(f"\n  '{err_file.name}' 저장 완료")
# print("""
#   ★ 실무 포인트
#     문제 데이터를 그냥 버리지 마세요.
#     "몇 번째 줄이 왜 문제인지" 목록을 파일로 만들어 두면
#     담당자에게 보내 수정을 요청할 수 있습니다.

#     "10건 중 2건 실패, 목록은 첨부합니다" 라고 보고할 수 있어야 합니다.
# """)


# # ============================================================
# #                   5 부 .  연 습 문 제
# # ============================================================

# # ---------------------------------------------------------
# # 5-1. 연습 문제
# # -------------------------------------------------------------
# print("\n" + "=" * 60)
# print(" 5-1. 연습 문제")
# print("=" * 60)

# # 실습용 매출 데이터를 만듭니다 (일부러 지저분하게)
# sales_file = DATA / "sales.csv"
# with open(sales_file, "w", encoding="utf-8", newline="") as f:
#     f.write("날짜,지점,상품,수량,단가\n")
#     f.write("2026-01-05,강남,노트북, 3 ,1200000\n")
#     f.write("2026-01-05,홍대,키보드,10,45000\n")
#     f.write("2026-01-06,강남,마우스,,25000\n")
#     f.write("2026-01-06,부산,노트북,2,1200000\n")
#     f.write("2026-01-07,홍대,모니터,4,350000\n")
#     f.write("2026-01-07,강남,키보드,다섯,45000\n")
#     f.write("2026-01-08,부산,마우스,15,25000\n")
#     f.write("2026-01-08,홍대,노트북,1,1200000\n")

# print("  sales.csv 준비 완료 (이상한 값 2개 포함)\n")

# # ※ input() 은 쓰지 않습니다. 코드에 직접 적어서 호출하세요.
# #
# # [연습 1] sales.csv 를 읽어 각 줄의 매출액(수량 × 단가)을 계산하고
# #          정상 데이터 리스트와 문제 목록을 돌려주는 함수를 만드세요.
# #          함수 이름: load_sales(path)
# #          반환: (정상리스트, 문제목록)
# # TODO


# # [연습 2] 지점별 매출 합계를 구해 막대그래프와 함께 출력하세요.
# #          (4-2 의 sum_by 함수를 재사용하세요)
# # TODO


# # [연습 3] 상품별 판매 수량을 구하세요.
# # TODO


# # [연습 4] 지점별 매출 결과를 'data/지점별매출.csv' 로 저장하세요.
# #          엑셀에서 한글이 안 깨져야 합니다.
# # TODO

# print("  (아래 5-2 에 정답이 있습니다)")


# #  ---------------------------------------------------------
# # 5-2. 연습 문제 정답
# # -------------------------------------------------------------
# print("\n" + "=" * 60)
# print(" 5-2. 연습 문제 정답")
# print("=" * 60)


# # ── [정답 1]
# def load_sales(path):
#     """매출 CSV 를 읽어 (정상데이터, 문제목록)을 돌려준다"""
#     clean_rows = []
#     problem_rows = []

#     with open(path, "r", encoding="utf-8", newline="") as f:
#         for line_no, row in enumerate(csv.DictReader(f), start=2):
#             qty = clean_number(row["수량"])
#             price = clean_number(row["단가"])

#             # 둘 중 하나라도 변환에 실패하면 문제 목록으로
#             if qty is None:
#                 problem_rows.append(
#                     (line_no, row["상품"], f"수량 이상: '{row['수량']}'")
#                 )
#                 continue
#             if price is None:
#                 problem_rows.append(
#                     (line_no, row["상품"], f"단가 이상: '{row['단가']}'")
#                 )
#                 continue

#             row["수량"] = qty
#             row["단가"] = price
#             row["매출액"] = qty * price  # 새 항목 추가
#             clean_rows.append(row)

#     return clean_rows, problem_rows


# sales, sales_problems = load_sales(sales_file)

# total = 0
# for s in sales:
#     total += s["매출액"]

# print(f"  [정답1] 정상 {len(sales)}건 / 문제 {len(sales_problems)}건")
# for line_no, product, reason in sales_problems:
#     print(f"          {line_no}번째 줄 {product}: {reason}")
# print(f"          전체 매출: {total:,}원")

# #  f"{숫자:,}" 로 쓰면 천 단위 쉼표가 자동으로 붙습니다.


# # ── [정답 2]
# by_branch = sum_by(sales, "지점", "매출액")

# print("\n  [정답2] 지점별 매출")
# for branch, amount in by_branch.items():
#     print(f"          {branch:<5}{amount:>11,}원  {make_bar(amount, 500000)}")


# # ── [정답 3]
# by_product = sum_by(sales, "상품", "수량")

# print("\n  [정답3] 상품별 판매 수량")
# for product, qty in by_product.items():
#     print(f"          {product:<6}{qty:>3}개  {make_bar(qty, 1, '●')}")


# # ── [정답 4]
# out_file = DATA / "지점별매출.csv"

# with open(out_file, "w", encoding="utf-8-sig", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["지점", "매출액"])
#     for branch, amount in by_branch.items():
#         writer.writerow([branch, amount])

# print(f"\n  [정답4] '{out_file.name}' 저장 완료")
# with open(out_file, "r", encoding="utf-8-sig", newline="") as f:
#     for row in csv.reader(f):
#         print("         ", row)


# #  ---------------------------------------------------------
# # 전체 정리
# # -------------------------------------------------------------
# #
# #   1부. 경로
# #   │
# #   │   from pathlib import Path
# #   │
# #   │   BASE = Path(__file__).parent   # 이 파일의 폴더
# #   │   DATA = BASE / "data"           # 데이터 폴더
# #   │   DATA.mkdir(exist_ok=True)      # 없으면 만들기
# #   │
# #   │   DATA.glob("*.csv")             # 파일 목록 찾기
# #
# #
# #   2부. 텍스트 파일
# #   │
# #   │   # 읽기
# #   │   with open(경로, "r", encoding="utf-8") as f:
# #   │       for line in f:
# #   │           print(line.strip())
# #   │
# #   │   # 쓰기
# #   │   with open(경로, "w", encoding="utf-8") as f:
# #   │       f.write("내용\n")
# #
# #
# #   3부. CSV
# #   │
# #   │   import csv
# #   │
# #   │   # 읽기
# #   │   with open(경로, "r", encoding="utf-8",
# #   │             newline="") as f:
# #   │       for row in csv.DictReader(f):
# #   │           print(row["열이름"])
# #   │
# #   │   # 쓰기 (엑셀용)
# #   │   with open(경로, "w", encoding="utf-8-sig",
# #   │             newline="") as f:
# #   │       writer = csv.writer(f)
# #   │       writer.writerow(["열1", "열2"])
# #
# #
# #   4부. 집계
# #   │
# #   │   result = {}
# #   │   for row in rows:
# #   │       key = row["부서"]
# #   │       result[key] = result.get(key, 0) + row["연봉"] │
# #
# #
# #
# #   ★ 반드시 기억할 7가지
# #     1. 경로는 Path(__file__).parent 기준으로 잡는다
# #     2. encoding="utf-8" 을 항상 붙인다 (한글 깨짐 방지)
# #     3. 엑셀로 열 파일은 encoding="utf-8-sig" 로 저장
# #     4. 파일은 with 로 연다 (자동으로 닫힘)
# #     5. "w" 는 기존 내용을 지운다. 이어쓰려면 "a"
# #     6. csv 모듈을 쓸 땐 newline="" 을 붙인다
# #     7. CSV 의 모든 값은 문자열. 계산하려면 int() 변환
# #
# #

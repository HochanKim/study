from pathlib import Path
import csv
import os

BASE = Path(__file__).parent  # 이 파일이 있는 폴더
DATA = BASE / "practice"  # 그 안에 data 폴더
DATA.mkdir(exist_ok=True)  # 폴더 만들기

# ============================================================
#                   5 부 .  연 습 문 제
# ============================================================

# ---------------------------------------------------------
# 5-1. 연습 문제
# -------------------------------------------------------------
print("\n" + "=" * 60)
print(" 5-1. 연습 문제")
print("=" * 60)

# 실습용 매출 데이터를 만듭니다 (일부러 지저분하게)
sales_file = DATA / "sales.csv"
with open(sales_file, "w", encoding="utf-8", newline="") as f:
    f.write("날짜,지점,상품,수량,단가\n")
    f.write("2026-01-05,강남,노트북, 3 ,1200000\n")
    f.write("2026-01-05,홍대,키보드,10,45000\n")
    f.write("2026-01-06,강남,마우스,,25000\n")
    f.write("2026-01-06,부산,노트북,2,1200000\n")
    f.write("2026-01-07,홍대,모니터,4,350000\n")
    f.write("2026-01-07,강남,키보드,다섯,45000\n")
    f.write("2026-01-08,부산,마우스,15,25000\n")
    f.write("2026-01-08,홍대,노트북,1,1200000\n")

print("  sales.csv 준비 완료 (이상한 값 2개 포함)\n")


# # ※ input() 은 쓰지 않습니다. 코드에 직접 적어서 호출하세요.
# #
# # [연습 1] sales.csv 를 읽어 각 줄의 매출액(수량 × 단가)을 계산하고
# #          정상 데이터 리스트와 문제 목록을 돌려주는 함수를 만드세요.
# #          함수 이름: load_sales(path)
# #          반환: (정상리스트, 문제목록)
# # TODO
# 함수 선언 1
def clean_number(para):
    try:
        change_type = int(para)
        return change_type
    except ValueError:
        return None


# 함수 선언 2
# 받은 파라미터를 'path'에 담기
def load_sales(path):
    # 정상 데이터를 담을 빈 리스트
    clean_rows = []
    # 오류 데이터를 담을 빈 리스트
    error_rows = []

    # "utf-8"로 인코딩하여 읽고("r") 'path' 자료를 열어서 변수 'f'에 담기
    # with를 사용하면 open()한 파일을 close() 없이 자동으로 닫는다
    with open(path, "r", encoding="utf-8", newline="") as f:
        for line_no, row in enumerate(csv.DictReader(f), start=2):
            # 읽어온 값들을 함수 clean_rows로 보낸 후 return을 각각 변수에 담기
            qty = clean_number(row["수량"])
            price = clean_number(row["단가"])

            # 둘 중 하나라도 변환에 실패하면 문제목록(error_rows)으로 이동
            if qty is None:
                error_rows.append((line_no, row["상품"], f"수량 이상: {row['수량']}"))
                continue
            if price is None:
                error_rows.append((line_no, row["상품"], f"단가 이상: {row['단가']}"))
                continue

            # 정상적인 데이터들
            row["수량"] = qty
            row["단가"] = price

            # 새 항목 추가
            row["매출액"] = price * qty

            # 정상적인 데이터들 리스트에 담기
            clean_rows.append(row)
    return clean_rows, error_rows


# return 값들을 각각 변수에 저장
sales, sales_problem = load_sales(sales_file)

# 매출액 합계를 저장할 변수 선언
total = 0
for s in sales:
    total += s.get("매출액")

# 정상 / 오류 데이터 개수 파악
print(f"정상 데이터: {len(sales)}건 // 오류 데이터: {len(sales_problem)}건")

# 오류 데이터에서 이상 있는 데이터 파악
for line_no, product, reason in sales_problem:
    print(f"{line_no}번째 줄 {product}: {reason}")

# 총 매출
print(f"전체 매출: {total:,}원")
print()

# print(sales)

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


# # [연습 2] 지점별 매출 합계를 구해 막대그래프와 함께 출력하세요.
# #          (4-2 의 sum_by 함수를 재사용하세요)
# # TODO


def sum_by(rows, group_key, value_key):
    # """
    # group_key 별로 value_key 를 합산한 딕셔너리를 돌려준다
    # rows      : 딕셔너리 리스트
    # group_key : 묶을 기준 키   (예: "부서")
    # value_key : 합산할 값의 키 (예: "연봉")
    # """
    result = {}
    for row in rows:
        key = row[group_key]
        result[key] = result.get(key, 0) + row[value_key]
    return result


by_branch = sum_by(sales, "지점", "매출액")
print(by_branch)


# # 막대그래프 함수
def make_bar(value, unit=500000, mark="■"):
    # """숫자를 막대그래프 문자열로 만든다"""
    return mark * int(value // unit)


for earn in by_branch:
    make_bar(by_branch.get(earn))
    print(f"{earn}: {by_branch.get(earn):,} 원 {make_bar(by_branch.get(earn))}")

# for branch, amount in by_branch.items():
#     print(f"{branch:<5}{amount:,} 원  {make_bar(amount, 500000)}")

# # ── [정답 2]
# by_branch = sum_by(sales, "지점", "매출액")

# print("\n  [정답2] 지점별 매출")
# for branch, amount in by_branch.items():
#     print(
#   f"{branch:<5}{amount:>11,}원  {make_bar(amount, 500000)}"
# )

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

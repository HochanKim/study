# ============================================================
#  파일 다루기 연습문제 - 카페 주문 데이터
# ============================================================

#  [출제 범위]
#    경로(pathlib) / 파일 읽기와 쓰기 / CSV / 집계

#  [푸는 방법]
#    - 각 문제 아래의 빈 줄에 코드를 작성하세요.
#    - 각 문제의 [출력 예시] 와 비슷하게 나오면 성공입니다.
#    - 숫자를 0 으로 가려둔 곳은 직접 구해야 하는 값입니다.
#      자릿수는 실제 답과 같으니 참고하세요.
#    - input() 은 쓰지 않습니다. 코드에 값을 직접 적어서 호출하세요.
#    - 함수로 만들라고 한 것은 반드시 함수로 만드세요.

#  [실행하면]
#    data 폴더에 orders.csv 가 자동으로 만들어집니다.
#    이 데이터에는 일부러 이상한 값이 섞여 있습니다.
#    코드를 짜기 전에 파일을 직접 열어서 먼저 찾아보세요.
# ============================================================


from pathlib import Path

import csv


BASE = Path(__file__).parent

DATA = BASE / "data"

DATA.mkdir(exist_ok=True)

# -------------------------------------------------------------
# 실습 데이터 준비 (이 부분은 그대로 두세요)
# -------------------------------------------------------------

orders_file = DATA / "orders.csv"

with open(orders_file, "w", encoding="utf-8", newline="") as f:
    f.write("주문일,시간대,매장,메뉴,분류,수량,단가,포장\n")

    f.write("2026-03-02,오전,강남점,아메리카노,커피,3,4500,N\n")

    f.write("2026-03-02,오후,강남점,카페라떼,커피, 2 ,5000,Y\n")

    f.write("2026-03-02,오전,홍대점,녹차라떼,논커피,1,5500,N\n")

    f.write("2026-03-03,오후,강남점,치즈케이크,디저트,2,6500,Y\n")

    f.write("2026-03-03,오전,부산점,아메리카노,커피,5,4500,N\n")

    f.write("2026-03-03,오후,홍대점,아메리카노,커피,,4500,N\n")

    f.write("2026-03-04,오전,강남점,크로플,디저트,3,6000,Y\n")

    f.write("2026-03-04,오후,부산점,카페라떼,커피,4,5000,N\n")

    f.write("2026-03-05,오전,홍대점,아메리카노,커피,2,4500,Y\n")

    f.write("2026-03-05,오후,강남점,녹차라떼,논커피,3,사천,N\n")

    f.write("2026-03-06,오전,부산점,치즈케이크,디저트,1,6500,N\n")

    f.write("2026-03-06,오후,홍대점,카페라떼,커피,6,5000,Y\n")

print("orders.csv 준비 완료")
print("data 폴더에서 직접 열어보고, 이상한 값이 몇 개인지 세어 보세요.\n")


# -------------------------------------------------------------
# [문제 1] 파일 읽어서 그대로 출력하기
# -------------------------------------------------------------

# orders.csv 를 csv.DictReader 로 읽어
# 모든 줄을 화면에 출력하세요.
# [힌트] encoding="utf-8", newline="" 을 잊지 마세요.


# [출력 예시]
#   {'주문일': '2026-03-02', '시간대': '오전', '매장': '강남점', ...}
#   {'주문일': '2026-03-02', '시간대': '오후', '매장': '강남점', ...}
#   ...
# -------------------------------------------------------------

# # print("--- 문제 1 ---")
# # utf-8로 인코딩하여
# # 변수 orders_file('orders.csv' 파일을 불러온 거)을 열고
# # 변수 f로 설정, with를 써서 close()는 생략 가능 (자동으로 파일을 닫음)
# with open(orders_file, "r", encoding="utf-8", newline="") as f:
#     # orders_file의 첫째 줄을 헤더로 지정
#     # 첫 줄의 값들을 key로 생성 후 해당 값들(values)을 딕셔너리로 생성
#     read_orders = csv.DictReader(f)
#     for row in read_orders:
#         # 한 줄씩 생성된 딕셔너리를 'row'로 불러오기
#         print(row)

# -------------------------------------------------------------
# [문제 2] 값을 정리하는 함수 만들기
# -------------------------------------------------------------
# 문자열의 앞뒤 공백을 없애고 숫자로 바꾸는 함수를 만드세요.
# 바꿀 수 없으면 None 을 돌려줍니다.

#   함수 이름 : clean_number(value)

# [확인]
#   clean_number(" 3 ")    ->  3
#   clean_number("4500")   ->  4500
#   clean_number("")       ->  None
#   clean_number("사천")    ->  None
# -------------------------------------------------------------

# print("\n--- 문제 2 ---")


# def clean_number(value):
#     try:
#         # 받는 값의 앞뒤 공백 제거
#         value.strip()
#         # 값을 정수로 변환후 리턴
#         can_change = int(value)
#         return can_change
#     except ValueError:
#         # 정수 변환이 불가능하면 None으로 리턴
#         return None


# print(clean_number(" 3 "))
# print(clean_number("4500"))
# print(clean_number(""))
# print(clean_number("사천"))


# -------------------------------------------------------------
# [문제 3] 데이터를 읽고 금액을 계산하는 함수
# -------------------------------------------------------------

# 함수 이름 : load_orders(path)

# 하는 일
#   1) CSV 를 읽는다
#   2) 수량과 단가를 숫자로 바꾼다 (문제 2의 함수 사용)
#   3) 둘 중 하나라도 변환에 실패하면 문제 목록에 담고 건너뛴다
#   4) 성공한 줄에는 금액을 계산해 새 항목으로 추가한다
#        금액 = 수량 x 단가
#   5) (정상리스트, 문제목록) 두 개를 돌려준다

# 문제 목록에는 (줄번호, 메뉴, 사유) 를 담으세요.

# [힌트] 줄번호는 enumerate(csv.DictReader(f), start=2) 로 셉니다.
#        1번 줄은 헤더이므로 데이터는 2번 줄부터입니다.

# 함수를 만든 뒤 아래 내용을 출력하세요.
#   - 정상 건수와 문제 건수
#   - 문제 목록 전체
#   - 전체 매출 합계


# [출력 예시]
#   정상 00건 / 문제 0건
#     0번째 줄 아메리카노: 수량 이상 ''
#     00번째 줄 녹차라떼: 단가 이상 '사천'
#   전체 매출: 000,000원
# -------------------------------------------------------------

print("\n--- 문제 3 ---")


# 올바른 값을 필터링하는 함수
def clean_number(value):
    try:
        # 받는 값의 앞뒤 공백 제거
        value.strip()
        # 값을 정수로 변환후 리턴
        can_change = int(value)
        return can_change
    except ValueError:
        # 정수 변환이 불가능하면 None으로 리턴
        return None


# 문제 목록 분류 함수
def load_orders(path):
    with open(path, "r", encoding="utf-8", newline="") as f:
        for line_no, row in enumerate(csv.DictReader(f), start=2):
            sooryang = clean_number(row["수량"])
            price = clean_number(row["단가"])

            # 잘못된 데이터들 분류해서 처리
            if sooryang is None:
                wrong_datas.append(
                    (line_no, row["메뉴"], f"수량 이상 -> '{row['수량']}'")
                )
                continue
            if price is None:
                wrong_datas.append(
                    (line_no, row["메뉴"], f"단가 이상 -> '{row['단가']}'")
                )
                continue

            # 정상 데이터들 처리
            row["수량"] = sooryang
            row["단가"] = price
            row["전체 매출"] = sooryang * price
            right_datas.append(row)
        return right_datas, wrong_datas


right_datas = []  # 정상 데이터를 담는 빈 리스트
wrong_datas = []  # 잘못된 데이터를 담는 빈 리스트
right_datas, wrong_datas = load_orders(orders_file)


# 전체 매출 합계 함수
def sum_earns(list):
    sum_earns = 0
    for i in list:
        sum_earns += i.get("전체 매출")
    return sum_earns


print(f"정상: {len(right_datas)}건 / 문제: {len(wrong_datas)}건")
for line_no, menu, reason in wrong_datas:
    print(f"{line_no}번째 줄 {menu}: {reason}")

print(f"전체 매출: {sum_earns(right_datas):,}원")


# -------------------------------------------------------------
# [문제 4] 집계 함수 두 개 만들기
# -------------------------------------------------------------

# 앞으로 계속 쓸 함수 두 개를 만드세요.
#   sum_by(rows, group_key, value_key)
#     group_key 별로 value_key 를 합산한 딕셔너리를 돌려준다

#   count_by(rows, group_key)
#     group_key 별 건수를 센 딕셔너리를 돌려준다

# [확인] 아래처럼 쓸 수 있어야 합니다
#   sum_by(orders, "매장", "금액")   ->  {'강남점': 00000, ...}
#   count_by(orders, "매장")         ->  {'강남점': 0, ...}

# [힌트] 딕셔너리의 .get(키, 0) 을 쓰면 짧아집니다.
# -------------------------------------------------------------

print("\n--- 문제 4 ---")


def sum_by(rows, group_key, value_key):
    # 합산 자료를 넣을 빈 딕셔너리 'result'
    # group_key: 매장명
    # value_key: 매출 금액
    sum_result = {}
    for row in rows:
        key = row[group_key]
        sum_result[key] = sum_result.get(key, 0) + row[value_key]
    return sum_result


print(sum_by(right_datas, "매장", "전체 매출"))


def count_by(rows, group_key):
    # 매장별 매출 개수를 담는 빈 딕셔너리
    cnt_result = {}
    for row in rows:
        key = row[group_key]
        cnt_result[key] = cnt_result.get(key, 0) + len(row[group_key])
    return cnt_result


print(count_by(right_datas, "매장"))

# -------------------------------------------------------------
# [문제 5] 매장별 매출과 막대그래프
# -------------------------------------------------------------

# 문제 4의 sum_by 를 써서 매장별 매출을 구하고,
# 옆에 막대그래프를 그려 출력하세요.
# 막대는 1만원당 ■ 하나로 그리세요.

# [출력 예시]
#   강남점    00,000원  ■■■■■
#   홍대점    00,000원  ■■■■
#   부산점    00,000원  ■■■■


# [힌트] "■" * (금액 // 10000)
#        f"{금액:,}" 로 쓰면 천 단위 쉼표가 붙습니다.
# -------------------------------------------------------------

print("\n--- 문제 5 ---")

# 매출 딕셔너리 저장하는 변수 'cafe_earning'
cafe_earning = sum_by(right_datas, "매장", "전체 매출")

print(cafe_earning)


def make_bar(value, unit, mark="■"):
    # 숫자들을(value, unit) 받아 막대그래프 문자열(mark) 생성
    return int(value // unit) * mark


for earn in cafe_earning:
    earn_graph = make_bar(cafe_earning.get(earn), 10000)
    print(f"{earn:<7}: {cafe_earning.get(earn):,}원 {earn_graph}")

# -------------------------------------------------------------
# [문제 6] 분류별 집계표
# -------------------------------------------------------------

# 분류(커피/논커피/디저트)별로 아래 세 가지를 구해 표로 출력하세요.
#   - 주문 건수
#   - 매출 합계
#   - 건당 평균 (소수 첫째 자리까지)
# => key: 분류, 전체 매출


# [출력 예시]
#   분류      건수      합계      평균
#   ------------------------------------
#   커피         0   000,000   00000.0
#   논커피       0     0,000    0000.0
#   디저트       0    00,000   00000.0


# [힌트] 문제 4에서 만든 함수 두 개를 모두 씁니다.
# => sum_by(rows, group_key, value_key) // count_by(rows, group_key)
#        칸 맞추기: f"{값:<6}" 왼쪽 정렬, f"{값:>8}" 오른쪽 정렬
# -------------------------------------------------------------

print("\n--- 문제 6 ---")

kind_sum = sum_by(right_datas, "분류", "전체 매출")
kind_cnt = count_by(right_datas, "분류")

print("분류       건수     합계       평균")
print("-" * 40)
for s in kind_sum:
    print(
        f"{s:<10} {kind_cnt.get(s):<5} {kind_sum.get(s):<5,} {round(kind_sum.get(s) / kind_cnt.get(s), 1):>10}"
    )

# -------------------------------------------------------------
# [문제 7] 조건으로 걸러내기
# -------------------------------------------------------------

# 아래 두 가지를 각각 구해 출력하세요.
#   1) 포장 주문(포장 열이 "Y")의 건수와 매출 합계
#   2) 오전 매출 합계와 오후 매출 합계

# [출력 예시]
#   포장 주문: 0건, 00,000원
#   오전 매출: 00,000원
#   오후 매출: 00,000원
# -------------------------------------------------------------

print("\n--- 문제 7 ---")
# 포장 주문 건수
pack_cnt = 0
# 포장 주문 매출
pack_earning = 0
# 오전 매출
before_twelve = 0
# 오후 매출
after_twelve = 0

for rd in right_datas:
    if rd["포장"] == "Y":
        # 포장 주문 건수와 매출 합계
        pack_cnt += 1
        pack_earning += rd["전체 매출"]

    if rd["시간대"] == "오전":
        before_twelve += rd["전체 매출"]
    else:
        after_twelve += rd["전체 매출"]

print(f"포장 주문: {pack_cnt}건, {pack_earning:,}원")
print(f"오전 매출: {before_twelve:,}원")
print(f"오후 매출: {after_twelve:,}원")

# -------------------------------------------------------------
# [문제 8] 가장 많이 팔린 메뉴 찾기
# -------------------------------------------------------------

# 메뉴별 판매 수량을 합산하고,
# 가장 많이 팔린 메뉴와 그 수량을 찾는 함수를 만드세요.


#   함수 이름 : best_menu(rows)
#   반환      : (메뉴이름, 수량) 두 개를 함께 돌려줄 것


# 만든 뒤 메뉴별 수량 전체와 1등을 출력하세요.

# [출력 예시]
#   메뉴별 판매 수량
#     아메리카노  00개
#     카페라떼    00개
#     ...
#   가장 많이 팔린 메뉴: OOO (00개)

# [힌트] 현재 1등을 변수에 담아두고 하나씩 비교하며 갱신합니다.
#        수량 합산은 문제 4의 sum_by 를 재사용하세요.
# -------------------------------------------------------------

print("\n--- 문제 8 ---")

# 빈 딕셔너리 - 전역 (총 메뉴 리스트)
all_menu = {}


def best_menu(rows):
    # 많이 팔린 메뉴 담는 빈 변수
    many_sell_menu = ""
    # 많이 팔린 개수
    many_cnt = 0
    # 빈 딕셔너리 - 로컬 (동점자 처리)
    many_sells = {}

    for i in rows:
        menu_name = i.get("메뉴")
        menu_cnt = len(menu_name)
        all_menu[menu_name] = i.get(menu_name, 0) + menu_cnt
        if many_cnt <= len(menu_name):
            many_sell_menu = menu_name
            many_cnt = len(menu_name)
            many_sells[many_sell_menu] = many_cnt

    return many_sells, many_cnt


ingi_menu, many_sell = best_menu(right_datas)

print("메뉴별     판매 수량")
for j in all_menu:
    menu_name = j
    menu_cnt = all_menu.get(j)
    print(f"{menu_name:<8} {menu_cnt}개")
print()
for k in ingi_menu:
    print(f"가장 많이 팔린 메뉴: {k} ({many_sell}개)")

# -------------------------------------------------------------
# [문제 9] 결과를 CSV 로 저장하기
# -------------------------------------------------------------
# 아래 두 파일을 만드세요.
#   1) data/매장별_매출.csv
#      열 구성 : 매장, 주문건수, 매출합계
#   2) data/오류목록.csv
#      열 구성 : 줄번호, 메뉴, 사유
#      (문제 3에서 걸러낸 이상한 데이터)

# 조건 : 엑셀로 열었을 때 한글이 깨지지 않아야 합니다.
# 저장한 뒤 두 파일을 다시 읽어서 내용을 출력해 확인하세요.
# [힌트] encoding 을 뭘로 해야 할까요? 그냥 utf-8 이 아닙니다.
# -------------------------------------------------------------

print("\n--- 문제 9 ---")

# 필요 값들을 담기 위한 빈 딕셔너리
stores_data = {}

store_name = list(sum_by(right_datas, "매장", "전체 매출").keys())
store_earning = list(sum_by(right_datas, "매장", "전체 매출").values())
store_sell_cnt = list(count_by(right_datas, "매장").values())

stores_data["매장"] = store_name
stores_data["주문건수"] = store_sell_cnt
stores_data["전체 매출"] = store_earning

# 필요한 값들을 따로 리스트에 저장
stores_data_ls = []
for i in range(len(stores_data.get("매장"))):
    stores_data_ls.append(
        {
            # 'Key: Value' 형식으로 딕셔너리 형태로 묶어서
            # 리스트에 저장
            "매장": stores_data["매장"][i],
            "주문건수": stores_data["주문건수"][i],
            "전체 매출": stores_data["전체 매출"][i],
        }
    )

right_datas_report = DATA / "매장별_매출.csv"

with open(right_datas_report, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["매장", "주문건수", "매출합계"])
    for branch in stores_data_ls:
        writer.writerow(
            [branch.get("매장"), branch.get("주문건수"), branch.get("전체 매출")]
        )

wrong_ls1 = {}
wrong_ls1["줄번호"] = wrong_datas[0][0]
wrong_ls1["메뉴"] = wrong_datas[0][1]
wrong_ls1["사유"] = wrong_datas[0][2]

wrong_ls2 = {}
wrong_ls2["줄번호"] = wrong_datas[1][0]
wrong_ls2["메뉴"] = wrong_datas[1][1]
wrong_ls2["사유"] = wrong_datas[1][2]

wrong_list = [wrong_ls1, wrong_ls2]


wrong_datas_report = DATA / "오류목록.csv"

with open(wrong_datas_report, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["줄번호", "메뉴", "사유"])
    for branch in wrong_list:
        writer.writerow([branch.get("줄번호"), branch.get("메뉴"), branch.get("사유")])

# -------------------------------------------------------------
# [문제 10] 보고서 만들기
# -------------------------------------------------------------

# 지금까지 구한 내용을 모아 data/일일보고서.txt 로 저장하세요.
# CSV 가 아니라 그냥 텍스트 파일입니다.

# [파일에 들어갈 내용 예시]
#   ========================================
#    카페 매출 보고서
#   ========================================
#   총 주문: 00건
#   총 매출: 000,000원

#   [매장별]
#     강남점  00,000원
#     홍대점  00,000원
#     부산점  00,000원

#   [분류별]
#     커피    000,000원
#     논커피    0,000원
#     디저트   00,000원

#   가장 많이 팔린 메뉴: OOO
#   ----------------------------------------

#   처리 실패: 0건 (오류목록.csv 참고)

# [힌트] 여러 줄을 쓸 때는 f.write() 를 여러 번 부르면 됩니다.
#        줄 끝에 \n 을 꼭 붙이세요.
# 저장한 뒤 파일을 다시 읽어서 화면에도 출력해 보세요.

# -------------------------------------------------------------

print("\n--- 문제 10 ---")


cafe_report = DATA / "일일보고서.txt"

# 총 주문 개수
all_orders = len(right_datas)

# 총 매출
all_earns = 0

for i in right_datas:
    all_earns += i.get("전체 매출")


def best_menu_price(rows):
    # 분류별 넣기
    menu_kind = {}
    # 종류별 매출
    for i in rows:
        if menu_kind.get(i.get("분류")) == None:
            menu_kind[i.get("분류")] = menu_kind.get(i.get("분류"), 0) + i.get(
                "전체 매출"
            )
        else:
            menu_kind[i.get("분류")] += i.get("전체 매출")
    return menu_kind


best_sell = best_menu_price(right_datas)

with open(cafe_report, "w", encoding="utf-8-sig", newline="") as f:
    f.write(f"{'=' * 30}\n")
    f.write("카페 매출 보고서\n")
    f.write(f"{'=' * 30}\n")
    f.write(f"총 주문: {all_orders}건\n")
    f.write(f"총 매출: {all_earns:,}원\n")
    f.write("\n[매장별]\n")
    for i in stores_data_ls:
        f.write(f"{i.get('매장')} {i.get('전체 매출'):>10,}원\n")
    f.write("\n[분류별]\n")
    for j in best_sell:
        f.write(f"{j:<10} {best_sell.get(j):>10,}원\n")
    f.write("\n")
    for k in ingi_menu:
        f.write(f"가장 많이 팔린 메뉴: {k} ({many_sell}개)\n")
    f.write(f"{'-' * 30}\n")
    for i in right_datas:
        if i.get("사유") == None:
            zero = i.get("사유")
            zero = 0
    f.write(f"처리 실패: {zero}건")

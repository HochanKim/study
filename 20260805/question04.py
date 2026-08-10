print("1. API 지연시간 SLO 리포트")
# 서비스 모니터링 담당자다. 최근 20회 API 응답시간(ms)이 리스트로 기록되어 있다.
# 여기서 p50(중앙값)과 p95를 구해 리포트를 출력하시오.
latencies = [
    120,
    95,
    340,
    110,
    88,
    205,
    130,
    99,
    410,
    150,
    102,
    118,
    260,
    91,
    175,
    133,
    108,
    96,
    220,
    145,
]

latencies.sort()  # 리스트 'latencies' 정렬

# * p50: 정렬했을 때 가운데 값. 개수가 짝수면 가운데 두 값의 평균.
# => 정렬: latencies.sort() or sort_list = sorted(latencies)
# =>if len(latencies) % 2 == 1 :
#     p50 = latencies[len(latencies) // 2]  # 홀수개 리스트의 가운데 값
# else :
#     p50 = (latencies[len(latencies) // 2 - 1] + latencies[len(latencies) // 2]) / 2  # 짝수개 리스트의 가운데 위치 평균값

p50 = ""
if len(latencies) % 2 == 1:
    p50 = latencies[len(latencies) // 2]  # 홀수개 리스트의 가운데 값
else:
    p50 = (
        latencies[len(latencies) // 2 - 1] + latencies[len(latencies) // 2]
    ) / 2  # 짝수개 리스트의 가운데 위치 평균값
print(f"p50: {p50}")

# * p95: 정렬했을 때 하위 95% 지점의 값.
#   순위 k = 전체 개수 × 0.95 를 계산해 정수가 아니면 반올림하고, 정렬된 리스트의 k번째 값(1번째부터 셈 => 인덱스 번호 - 1)을 쓴다.
#   전체 개수 = len(latencies)
#   정렬된 리스트의 k번째 값(1번째부터 셈) => latencies[전체 개수]

lank_k = int(round((len(latencies) * 0.95), 0))
p95 = latencies[lank_k - 1]
print(f"p95: {p95}")

# * 판정: p95가 300 초과면 SLO 위반, 200 초과면 주의, 그 외는 정상.
if p95 > 300:
    print("SLO 위반")
elif p95 > 200:
    print("주의")
else:
    print("정상")

# 실행 결과
# p50: 125.0
# p95: 340
# SLO 위반
print()
# 다른 값으로도 확인
latencies = [
    120,
    95,
    140,
    110,
    88,
    205,
    130,
    99,
    160,
    150,
    102,
    118,
    190,
    91,
    175,
    133,
    108,
    96,
    185,
    145,
]

latencies.sort()  # 리스트 'latencies' 정렬

# * p50: 정렬했을 때 가운데 값. 개수가 짝수면 가운데 두 값의 평균.
# => 정렬: latencies.sort() or sort_list = sorted(latencies)
# =>if len(latencies) % 2 == 1 :
#     p50 = latencies[len(latencies) // 2]  # 홀수개 리스트의 가운데 값
# else :
#     p50 = (latencies[len(latencies) // 2 - 1] + latencies[len(latencies) // 2]) / 2  # 짝수개 리스트의 가운데 위치 평균값

p50 = ""
if len(latencies) % 2 == 1:
    p50 = latencies[len(latencies) // 2]  # 홀수개 리스트의 가운데 값
else:
    p50 = (
        latencies[len(latencies) // 2 - 1] + latencies[len(latencies) // 2]
    ) / 2  # 짝수개 리스트의 가운데 위치 평균값
print(f"p50: {p50}")

# * p95: 정렬했을 때 하위 95% 지점의 값.
#   순위 k = 전체 개수 × 0.95 를 계산해 정수가 아니면 반올림하고, 정렬된 리스트의 k번째 값(1번째부터 셈 => 인덱스 번호 - 1)을 쓴다.
#   전체 개수 = len(latencies)
#   정렬된 리스트의 k번째 값(1번째부터 셈) => latencies[전체 개수]

lank_k = int(round((len(latencies) * 0.95), 0))
p95 = latencies[lank_k - 1]
print(f"p95: {p95}")

# * 판정: p95가 300 초과면 SLO 위반, 200 초과면 주의, 그 외는 정상.
if p95 > 300:
    print("SLO 위반")
elif p95 > 200:
    print("주의")
else:
    print("정상")
# p50: 125.0
# p95: 190
# 정상
print("=" * 30)

print("2. 카나리 배포 자동 롤백 판정")
# 새 버전을 배포했다. 분당 에러율(%)이 10분치 기록되어 있고,
# 앞 절반은 배포 전, 뒤 절반은 배포 후다.
# 아래 규칙을 위에서부터 순서대로 적용해 가장 먼저 걸리는 판정 하나를 출력하시오.
error_rates = [0.4, 0.6, 0.5, 0.3, 0.7, 1.2, 0.9, 1.4, 1.1, 1.0]
early_rates = error_rates[: int(len(error_rates) / 2)]  # 배포 전 에러율
lately_rates = error_rates[int(len(error_rates) / 2) :]  # 배포 후 에러율


avg_early = sum(early_rates) / len(early_rates)
print(f"배포 전 평균: {avg_early}")

# 배포 후 평균: 1.12
avg_lately = sum(lately_rates) / len(lately_rates)
print(f"배포 후 평균: {avg_lately:.2f}")

condition = ""  # 판정 결과값을 담을 변수 (중복 출력 방지)
# 1. 배포 후 구간에 에러율 5.0 이상인 순간이 한 번이라도 있으면 → ROLLBACK
if max(lately_rates) > 5.0:
    condition = "ROLLBACK"

# 2. 배포 전 평균이 0인 경우: 배포 후 평균이 0보다 크면 HOLD, 아니면 PROMOTE
elif (avg_early) == 0:
    if (avg_lately) > 0:
        condition = "HOLD"
    else:
        condition = "PROMOTE"

# 3. 배포 후 평균이 배포 전 평균의 1.5배 이상이면 → ROLLBACK
elif (avg_lately) >= (avg_early) * 1.5:
    condition = "ROLLBACK"

# 4. 배포 후 평균이 배포 전 평균의 1.2배 이상이면 → HOLD
elif (avg_lately) >= 1.2:
    condition = "HOLD"
# 5. 그 외 → PROMOTE
else:
    condition = "PROMOTE"
print(condition)

# 첫 줄에 배포 전 평균, 둘째 줄에 배포 후 평균(둘 다 소수점 둘째 자리 반올림), 셋째 줄에 판정을 출력한다.
# 규칙 2가 없으면 프로그램이 죽는 상황이 생긴다. 왜 그런지 생각해보고 처리할 것.

# 실행 결과
# 배포 전 평균: 0.5
# 배포 후 평균: 1.12
# ROLLBACK


# 다른 값으로도 확인
# error_rates                                                	  출력
# [3.0, 3.2, 2.8, 3.0, 3.0, 1.0, 0.9, 1.1, 1.0, 5.5]	  3.0 / 1.9 / ROLLBACK
print()
error_rates = [3.0, 3.2, 2.8, 3.0, 3.0, 1.0, 0.9, 1.1, 1.0, 5.5]
early_rates = error_rates[: int(len(error_rates) / 2)]  # 배포 전 에러율
lately_rates = error_rates[int(len(error_rates) / 2) :]  # 배포 후 에러율

# 배포 전 에러율 평균
avg_early = sum(early_rates) / len(early_rates)
print(f"배포 전 평균: {avg_early}")

# 배포 후 에러율 평균
avg_lately = sum(lately_rates) / len(lately_rates)
print(f"배포 후 평균: {avg_lately:.2f}")

condition = ""  # 판정 결과값을 담을 변수 (중복 출력 방지)
# 1. 배포 후 구간에 에러율 5.0 이상인 순간이 한 번이라도 있으면 → ROLLBACK
if max(lately_rates) > 5.0:
    condition = "ROLLBACK"

# 2. 배포 전 평균이 0인 경우: 배포 후 평균이 0보다 크면 HOLD, 아니면 PROMOTE
elif (avg_early) == 0:
    if (avg_lately) > 0:
        condition = "HOLD"
    else:
        condition = "PROMOTE"

# 3. 배포 후 평균이 배포 전 평균의 1.5배 이상이면 → ROLLBACK
elif (avg_lately) >= (avg_early) * 1.5:
    condition = "ROLLBACK"

# 4. 배포 후 평균이 배포 전 평균의 1.2배 이상이면 → HOLD
elif (avg_lately) >= 1.2:
    condition = "HOLD"
# 5. 그 외 → PROMOTE
else:
    condition = "PROMOTE"
print(condition)

# [0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.1, 0.0, 0.3, 0.1]	  0.0 / 0.14 / HOLD
print()
error_rates = [0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.1, 0.0, 0.3, 0.1]
early_rates = error_rates[: int(len(error_rates) / 2)]  # 배포 전 에러율
lately_rates = error_rates[int(len(error_rates) / 2) :]  # 배포 후 에러율

# 배포 전 에러율 평균
avg_early = sum(early_rates) / len(early_rates)
print(f"배포 전 평균: {avg_early}")

# 배포 후 에러율 평균
avg_lately = sum(lately_rates) / len(lately_rates)
print(f"배포 후 평균: {avg_lately:.2f}")

condition = ""  # 판정 결과값을 담을 변수 (중복 출력 방지)
# 1. 배포 후 구간에 에러율 5.0 이상인 순간이 한 번이라도 있으면 → ROLLBACK
if max(lately_rates) > 5.0:
    condition = "ROLLBACK"

# 2. 배포 전 평균이 0인 경우: 배포 후 평균이 0보다 크면 HOLD, 아니면 PROMOTE
elif (avg_early) == 0:
    if (avg_lately) > 0:
        condition = "HOLD"
    else:
        condition = "PROMOTE"

# 3. 배포 후 평균이 배포 전 평균의 1.5배 이상이면 → ROLLBACK
elif (avg_lately) >= (avg_early) * 1.5:
    condition = "ROLLBACK"

# 4. 배포 후 평균이 배포 전 평균의 1.2배 이상이면 → HOLD
elif (avg_lately) >= 1.2:
    condition = "HOLD"
# 5. 그 외 → PROMOTE
else:
    condition = "PROMOTE"
print(condition)

# [1.0, 1.2, 0.8, 1.0, 1.0, 0.9, 1.1, 1.0, 0.8, 1.2]	  1.0 / 1.0 / PROMOTE
print()
error_rates = [1.0, 1.2, 0.8, 1.0, 1.0, 0.9, 1.1, 1.0, 0.8, 1.2]
early_rates = error_rates[: int(len(error_rates) / 2)]  # 배포 전 에러율
lately_rates = error_rates[int(len(error_rates) / 2) :]  # 배포 후 에러율

# 배포 전 에러율 평균
avg_early = sum(early_rates) / len(early_rates)
print(f"배포 전 평균: {avg_early}")

# 배포 후 에러율 평균
avg_lately = sum(lately_rates) / len(lately_rates)
print(f"배포 후 평균: {avg_lately:.2f}")

condition = ""  # 판정 결과값을 담을 변수 (중복 출력 방지)
# 1. 배포 후 구간에 에러율 5.0 이상인 순간이 한 번이라도 있으면 → ROLLBACK
if max(lately_rates) > 5.0:
    condition = "ROLLBACK"

# 2. 배포 전 평균이 0인 경우: 배포 후 평균이 0보다 크면 HOLD, 아니면 PROMOTE
elif (avg_early) == 0:
    if (avg_lately) > 0:
        condition = "HOLD"
    else:
        condition = "PROMOTE"

# 3. 배포 후 평균이 배포 전 평균의 1.5배 이상이면 → ROLLBACK
elif (avg_lately) >= (avg_early) * 1.5:
    condition = "ROLLBACK"

# 4. 배포 후 평균이 배포 전 평균의 1.2배 이상이면 → HOLD
elif (avg_lately) >= 1.2:
    condition = "HOLD"
# 5. 그 외 → PROMOTE
else:
    condition = "PROMOTE"
print(condition)
print("=" * 30)

print("3. 서버 로그 알람 등급 판정")
# 최근 서버 로그 레벨 20건이 시간순으로 기록되어 있다.
logs = [
    "INFO",
    "INFO",
    "WARN",
    "INFO",
    "ERROR",
    "INFO",
    "INFO",
    "WARN",
    "INFO",
    "ERROR",
    "INFO",
    "INFO",
    "WARN",
    "INFO",
    "INFO",
    "INFO",
    "WARN",
    "INFO",
    "INFO",
    "INFO",
]
# 아래 형식으로 집계 결과와 알람 등급을 출력하시오.
# 등급은 위에서부터 순서대로 적용해 가장 먼저 걸리는 것 하나만 출력한다.

# 총 로그
all_logs = len(logs)
print(f"총 로그: {all_logs}")

error_cnt = logs.count("ERROR")
warn_cnt = logs.count("WARN")
print(f"ERROR: {error_cnt} / WARN: {warn_cnt}")

error_percent = (error_cnt / all_logs) * 100  # 에러율
warn_percent = (
    warn_cnt / all_logs
) * 100  # WARN이 전체의 절반 이상인지 판단하기 위한 변수
print(
    f"에러율: {error_percent:.1f} %"
)  # 에러율은 소수점 첫째 자리까지 반올림하고 %를 붙여 출력한다.

# 1. 가장 최근 3건이 모두 ERROR 이면 → CRITICAL - 연속 장애 감지
if logs[-3] == logs[-2] == logs[-1] == "ERROR":
    print("CRITICAL - 연속 장애 감지")

# 2. 에러율이 20% 이상이면 → CRITICAL
elif error_percent >= 20:
    print("CRITICAL")
# 3. 에러율이 10% 이상이거나, WARN이 전체의 절반 이상이면 → WARNING

elif error_percent >= 10 or warn_percent >= 50:
    print("WARNING")
# 4. 그 외 → HEALTHY
else:
    print("HEALTHY")
print()

# 실행 결과
# 총 로그: 20
# ERROR: 2 / WARN: 4
# 에러율: 10.0%
# WARNING


# 다른 값으로도 확인

logs = [
    "INFO",
    "INFO",
    "WARN",
    "INFO",
    "ERROR",
    "INFO",
    "INFO",
    "WARN",
    "INFO",
    "INFO",
    "INFO",
    "INFO",
    "WARN",
    "INFO",
    "INFO",
    "INFO",
    "WARN",
    "ERROR",
    "ERROR",
    "ERROR",
]
# 아래 형식으로 집계 결과와 알람 등급을 출력하시오.
# 등급은 위에서부터 순서대로 적용해 가장 먼저 걸리는 것 하나만 출력한다.

# 총 로그
all_logs = len(logs)
print(f"총 로그: {all_logs}")

error_cnt = logs.count("ERROR")
warn_cnt = logs.count("WARN")
print(f"ERROR: {error_cnt} / WARN: {warn_cnt}")

error_percent = (error_cnt / all_logs) * 100  # 에러율
warn_percent = (
    warn_cnt / all_logs
) * 100  # WARN이 전체의 절반 이상인지 판단하기 위한 변수
print(f"에러율: {error_percent:.1f} %")

# 1. 가장 최근 3건이 모두 ERROR 이면 → CRITICAL - 연속 장애 감지
if logs[-3] == logs[-2] == logs[-1] == "ERROR":
    print("CRITICAL - 연속 장애 감지")

# 2. 에러율이 20% 이상이면 → CRITICAL
elif error_percent >= 20:
    print("CRITICAL")
# 3. 에러율이 10% 이상이거나, WARN이 전체의 절반 이상이면 → WARNING

elif error_percent >= 10 or warn_percent >= 50:
    print("WARNING")
# 4. 그 외 → HEALTHY
else:
    print("HEALTHY")
print("=" * 30)

# 총 로그: 20
# ERROR: 4 / WARN: 4
# 에러율: 20.0%
# CRITICAL - 연속 장애 감지


print("4. 주문 결제 금액 계산 엔진")
# 쇼핑몰 결제 로직이다. 장바구니 상품 가격 리스트, 회원 등급, 정액 할인 쿠폰이 주어진다.
items = [12000, 8500, 30000, 4500]
grade = "GOLD"
coupon = 5000

# 아래 정책을 순서대로 적용해 최종 결제 금액을 계산하시오.
# 1. 상품 합계 = 모든 상품 가격의 합
sum_price = sum(items)

# 2. 등급 할인: GOLD 10%, SILVER 5%, NONE 0% (상품 합계 기준, 원 미만 절사)
if grade == "GOLD":
    gold_dc = sum_price * 0.1
    # print(f"{gold_dc:.0f}")
elif grade == "SILVER":
    silver_dc = sum_price * 0.05

# 3. 총 할인액 = 등급 할인 + 쿠폰 금액
all_dc = 0
if grade == "GOLD":
    all_dc = gold_dc + coupon
    # print(f"{gold_dc:.0f}")
elif grade == "SILVER":
    all_dc = silver_dc + coupon

# 4. 총 할인액은 상품 합계의 30%를 넘을 수 없다. 넘으면 30%(원 미만 절사)까지만 적용
if all_dc > (sum_price * 0.3):
    all_dc = min(all_dc, sum_price * 0.3)

# 5. 할인 적용 후 금액이 30,000원 이상이면 배송비 무료, 미만이면 3,000원
if (sum_price - all_dc) >= 30000:
    delivery_fee = 0
else:
    delivery_fee = 3000

# 6. 최종 결제 금액 = 할인 적용 후 금액 + 배송비
print(f"상품 합계: {sum_price}")
print(f"총 할인: {int(all_dc)}")
print(f"배송비: {delivery_fee}")
print(f"최종 결제 금액: {int(sum_price - all_dc + delivery_fee)}")
print()

# 실행 결과

# 상품 합계: 55000
# 총 할인: 10500
# 배송비: 0
# 최종 결제 금액: 44500


# 다른 값으로도 확인
# items	                       grade	  coupon	      출력
# [9000, 6000]	              "GOLD"	   8000	    15000 / 4500 / 3000 / 13500
# 두 번째 케이스가 4번 정책이 실제로 동작하는지 확인하는 지점이다.
# 여기서 할인이 9,500원으로 나오면 틀린 것.

items = [9000, 6000]
grade = "GOLD"
coupon = 8000

# 아래 정책을 순서대로 적용해 최종 결제 금액을 계산하시오.
# 1. 상품 합계 = 모든 상품 가격의 합
sum_price = sum(items)

# 2. 등급 할인: GOLD 10%, SILVER 5%, NONE 0% (상품 합계 기준, 원 미만 절사)
if grade == "GOLD":
    gold_dc = sum_price * 0.1
    # print(f"{gold_dc:.0f}")
elif grade == "SILVER":
    silver_dc = sum_price * 0.05

# 3. 총 할인액 = 등급 할인 + 쿠폰 금액
all_dc = 0
if grade == "GOLD":
    all_dc = gold_dc + coupon
    # print(f"{gold_dc:.0f}")
elif grade == "SILVER":
    all_dc = silver_dc + coupon

# 4. 총 할인액은 상품 합계의 30%를 넘을 수 없다. 넘으면 30%(원 미만 절사)까지만 적용
if all_dc > (sum_price * 0.3):
    all_dc = min(all_dc, sum_price * 0.3)

# 5. 할인 적용 후 금액이 30,000원 이상이면 배송비 무료, 미만이면 3,000원
if (sum_price - all_dc) >= 30000:
    delivery_fee = 0
else:
    delivery_fee = 3000

# 6. 최종 결제 금액 = 할인 적용 후 금액 + 배송비
print(f"상품 합계: {sum_price}")
print(f"총 할인: {int(all_dc)}")
print(f"배송비: {delivery_fee}")
print(f"최종 결제 금액: {int(sum_price - all_dc + delivery_fee)}")
print()

# [9000, 6000]	             "SILVER"	    0	    15000 / 750 / 3000 / 17250
items = [9000, 6000]
grade = "SILVER"
coupon = 0

# 아래 정책을 순서대로 적용해 최종 결제 금액을 계산하시오.
# 1. 상품 합계 = 모든 상품 가격의 합
sum_price = sum(items)

# 2. 등급 할인: GOLD 10%, SILVER 5%, NONE 0% (상품 합계 기준, 원 미만 절사)
if grade == "GOLD":
    gold_dc = sum_price * 0.1
    # print(f"{gold_dc:.0f}")
elif grade == "SILVER":
    silver_dc = sum_price * 0.05

# 3. 총 할인액 = 등급 할인 + 쿠폰 금액
all_dc = 0
if grade == "GOLD":
    all_dc = gold_dc + coupon
    # print(f"{gold_dc:.0f}")
elif grade == "SILVER":
    all_dc = silver_dc + coupon

# 4. 총 할인액은 상품 합계의 30%를 넘을 수 없다. 넘으면 30%(원 미만 절사)까지만 적용
if all_dc > (sum_price * 0.3):
    all_dc = min(all_dc, sum_price * 0.3)

# 5. 할인 적용 후 금액이 30,000원 이상이면 배송비 무료, 미만이면 3,000원
if (sum_price - all_dc) >= 30000:
    delivery_fee = 0
else:
    delivery_fee = 3000

# 6. 최종 결제 금액 = 할인 적용 후 금액 + 배송비
print(f"상품 합계: {sum_price}")
print(f"총 할인: {int(all_dc)}")
print(f"배송비: {delivery_fee}")
print(f"최종 결제 금액: {int(sum_price - all_dc + delivery_fee)}")
print()

# [12000, 8500, 30000, 4500]	  "NONE"	    0	    55000 / 0 / 0 / 55000
items = [12000, 8500, 30000, 4500]
grade = "NONE"
coupon = 0

# 아래 정책을 순서대로 적용해 최종 결제 금액을 계산하시오.
# 1. 상품 합계 = 모든 상품 가격의 합
sum_price = sum(items)

# 2. 등급 할인: GOLD 10%, SILVER 5%, NONE 0% (상품 합계 기준, 원 미만 절사)
if grade == "GOLD":
    gold_dc = sum_price * 0.1
    # print(f"{gold_dc:.0f}")
elif grade == "SILVER":
    silver_dc = sum_price * 0.05

# 3. 총 할인액 = 등급 할인 + 쿠폰 금액
all_dc = 0
if grade == "GOLD":
    all_dc = gold_dc + coupon
    # print(f"{gold_dc:.0f}")
elif grade == "SILVER":
    all_dc = silver_dc + coupon

# 4. 총 할인액은 상품 합계의 30%를 넘을 수 없다. 넘으면 30%(원 미만 절사)까지만 적용
if all_dc > (sum_price * 0.3):
    all_dc = min(all_dc, sum_price * 0.3)

# 5. 할인 적용 후 금액이 30,000원 이상이면 배송비 무료, 미만이면 3,000원
if (sum_price - all_dc) >= 30000:
    delivery_fee = 0
else:
    delivery_fee = 3000

# 6. 최종 결제 금액 = 할인 적용 후 금액 + 배송비
print(f"상품 합계: {sum_price}")
print(f"총 할인: {int(all_dc)}")
print(f"배송비: {delivery_fee}")
print(f"최종 결제 금액: {int(sum_price - all_dc + delivery_fee)}")
print()

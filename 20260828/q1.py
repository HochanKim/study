설비명 = "M-101"
담당자 = "김정비"
센서ID = "TEMP-M101-A-0007"
온도 = [71.2, 68.5, 75.9, 80.1, 66.3, 72.4, 69.8, 95.6, 70.0, 73.1, 68.9, 71.5]
측정값문자 = ["71.2", "68.5", "75.9", "80.1"]
점검메모 = "  정상가동 / 진동 약간 있음  "

print("문제 1. 변수와 자료형")
print(f"설비 {설비명} / 담당 {담당자} / 측정 {len(온도)}회")
print()

print("문제 2. 문자열 쪼개기")
split_str = 센서ID.split("-")
for i in split_str:
    try:
        i = int(i)
        print(i, end=" ")
    except ValueError:
        print(i, end=" ")

print()
print()
print("문제 3. 문자열 다듬기")
# 양쪽 공백 제거: strip()
memo = 점검메모.strip()
# 특정 문자 대체: replace()
memo = memo.replace("/", "·")
print(memo)
# 모든 대문자 변환: upper() / 모든 소문자 변환:  lower()
sensor_id = 센서ID.lower()
# 어떤 문자 또는 단어로 시작하는 것의 여부(True/False)를 판별하는 함수: startwith()
# 어떤 문자 또는 단어가 시작하는 인덱스 번호 찾는 함수: find()
print(sensor_id, 센서ID.startswith("TEMP"), 센서ID.find("M101"))
print()

print("문제 4. 글자를 숫자로")
num_ls = []
for i in 측정값문자:
    i = float(i)
    num_ls.append(i)

print(num_ls)
print(round(sum(num_ls) / len(num_ls), 2))
print()

print("문제 5. 연산자 감각")
print(f"{len(온도) // 5} {len(온도) % 5} {2**5}")
print(70 < 온도[0] < 75)
print((90 < 온도[7]) or (온도[4] < 60))
print()

print("문제 6. 조건문으로 등급 매기기")
if 온도[7] >= 90:
    print(f"{온도[7]} 이상")
elif 온도[7] >= 75:
    print(f"{온도[7]} 주의")
else:
    print(f"{온도[7]} 정상")
print()

print("문제 7. 반복문 안의 조건문")
wrong_cnt = 0
warn_cnt = 0
right_cnt = 0
for t in 온도:
    if t >= 90:
        wrong_cnt += 1
    elif t >= 75:
        warn_cnt += 1
    else:
        right_cnt += 1
print(right_cnt, warn_cnt, wrong_cnt)
print()

print("문제 8. 합계·평균·최대·최소를 직접")
temps_sum = 0
temps_max = 0
temps_min = 온도[0]
for t in 온도:
    temps_sum += t
    if temps_max < t:  # noqa: PLR1730
        temps_max = t
    if temps_min > t:  # noqa: PLR1730
        temps_min = t
print(temps_sum)
print(round(temps_sum / len(온도), 2))
print(temps_max, temps_min)
print()

print("문제 9. while 과 break")
idx = 0
while True:
    temps = 온도[idx]
    if temps >= 90:
        print(idx, temps)
        break
    idx += 1
print()

print("문제 10. continue 와 range")
idx = 0
cnt = 0
new_temps = []
for t in 온도:
    if t >= 75:
        continue
    new_temps.append(t)
print(len(new_temps))

for idx, i in enumerate(온도):
    if idx % 4 == 0:
        print(idx, i)
print()

print("문제 11. 리스트 정렬과 자르기")
# 오름차순(작은 것에서 큰 것): 기본값이므로 reverse=False를 생략합니다.
# 내림차순(큰 것에서 작은 것): reverse=True로 지정합니다
# 원본 건드리는 정렬: sort()
# 원본 건드리지 않는 정렬: sorted("리스트")
ascd_temp = sorted(온도, reverse=False)
desd_temp = sorted(온도, reverse=True)
print(ascd_temp[:3])
print(desd_temp[:3])
print(온도[2:6], 온도[9:])
print()

print("문제 12. 리스트 고치기")
temps = 온도.copy()
temps.remove(95.6)
# 리스트 추가 (뒤에) -> append()
temps.append(70.5)
# 리스트 추가 (맨앞에) -> insert(0, 값)
temps.insert(0, 69.0)
print(len(temps), temps[0], temps[-1])
# 리스트 값의 인덱스: index(값)
print(온도)
print(온도.index(80.1), temps.index(71.2))
print()

print("문제 13. 딕셔너리")
temps_dict = {"M-101": 71.2, "M-102": 78.4, "M-203": 85.0}
temps_dict["M-305"] = 66.8

temps_key = []
values_sum = 0
for t in temps_dict:
    temps_key.append(t)  # noqa: PERF402
    values_sum += temps_dict.get(t)

try:
    print(temps_key)
    print(round(values_sum / len(temps_key), 2))
    print(temps_dict["M-999"])
except KeyError:
    print("없음")
print()

print("문제 14. 셋과 튜플")
rank_ls = ["정상", "주의", "정상", "이상", "정상", "주의"]
# 중복 제거
set(rank_ls)
print(set(rank_ls), len(set(rank_ls)))

from datetime import datetime

set_tuple = ("M-101", "A라인", 2019)
now_year = datetime.now().year
print(f"{set_tuple[0]}({set_tuple[1]}) 사용 {now_year - set_tuple[2]}년차")
print()

print("문제 15. 이상값 골라내기")
item_ls = []
idx_ls = []
for idx, i in enumerate(온도):
    if i > 75:
        idx_ls.append(idx)
        item_ls.append(i)

print(item_ls)
print(idx_ls)
print(round(len(item_ls) / len(온도) * 100, 1))

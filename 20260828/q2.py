import math
import random
import numpy as np

온도 = [71.2, 68.5, 75.9, 80.1, 66.3, 72.4, 69.8, 95.6, 70.0, 73.1, 68.9, 71.5]
측정값문자 = ["71.2", "68.5", "이상", "80.1", "N/A"]

print("문제 1. 함수로 묶기")


def avgs(values):
    v_sum = 0
    v_len = len(values)
    for v in values:
        v_sum += v
        v_avg = round((v_sum / v_len), 2)
    return v_avg


print(avgs(온도))
print(avgs([70.0, 72.0, 74.0]))
print()

print("문제 2. 기본값과 키워드 인자")


def level(number):
    if number >= 90:
        return "이상"
    elif number >= 75:
        return "주의"
    else:
        return "정상"


print(level(온도[7]), level(온도[2]), level(온도[0]))


def level(number):
    if number >= 100:
        return "이상"
    elif number >= 80:
        return "주의"
    else:
        return "정상"


print(level(온도[2]), level(온도[7]))
print()

print("문제 3. 값 여러 개 돌려주기")


def set_result(list):
    ls_sum = 0  # 합계
    ls_max = list[0]
    ls_min = list[0]
    for i in list:
        ls_sum += i
        if ls_max < i:  # noqa: PLR1730
            ls_max = i
        if ls_min > i:  # noqa: PLR1730
            ls_min = i
    ls_avg = round(ls_sum / len(list), 2)
    return ls_sum, ls_avg, ls_max, ls_min


print(set_result(온도))
print()

print("문제 4. 전역 변수와 지역 변수")
stnd_temp = 75


def stnd(list):
    # 전역변수 가져오기: global
    global stnd_temp  # noqa: PLW0602
    over = []
    for t in list:
        if stnd_temp < t:
            over.append(t)
    return over


print(len(stnd(온도)), stnd_temp)
print()

print("문제 5. 표준 라이브러리 쓰기")
print(math.sqrt(16), round(math.pi, 4), math.ceil(73.61), math.floor(73.61))
# 리스트 컴프리헨션: 중복 O, 숫자 n개 생성 / [random.randint(1, 10) for _ in range(n)]
# choices(): 중복 O, k 인자 설정 / random.choices(range(1, 11), k=n)
# sample(): 중복 X / random.sample(range(1, 11), n)

# random의 시드를 고정: 난수를 매번 같은 순서로 생성하도록 설정
random.seed(42)
print(random.sample(range(1, 11), 3))
random.seed(42)
print(random.sample(range(1, 11), 3))
print()

print("문제 6. 예외 처리")
num_ls = []
err_ls = []
for i in 측정값문자:
    try:
        ii = float(i)
        num_ls.append(ii)
    except ValueError:
        err_ls.append(i)

print(num_ls)
print(err_ls)
print(len(num_ls), len(err_ls))
print()

print("문제 7. 파일을 직접 열어 읽기")
# 모듈 csv 사용
import csv

datas = []
header_ls = []
first = []
with open("설비온도기록.csv", "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)

    for x in reader:
        # reader로 저장한 csv.DictReader(f)의 내용을 for문으로 불러오기
        # 그냥 출력할 시, 주소값이 출력됨
        header_ls = list(x.keys())
        datas.append(x)
print(header_ls)
print(len(datas))

for idx, i in enumerate(datas):
    first = list(datas[0].values())
    f_temp = float(datas[0].get("온도"))
print(first, f_temp)
print()

print("문제 8. 결과를 파일로 남기기")
temps = []
for idx, i in enumerate(datas):
    temps.append(float(i.get("온도")))
temps_avg = avgs(temps)
print(f"측정 {len(temps)} / 평균 {temps_avg} / 최고 {max(temps)}")

# txt 파일로 저장할 내용을 리스트에 넣기
점검보고서 = [[f"{len(temps)} / 평균 {temps_avg} / 최고 {max(temps)}"]]


with open("점검보고서.txt", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    # 자료를 써서 추가하는 함수(write): csv.writer(파일).writerows(추가할 데이터)
    writer.writerows(점검보고서)
    # PC 보안 내 권한 이상으로 파일 output에 문제가 있었음
print()

print("문제 9. 클래스 만들기")


class sensor:
    def __init__(self, name, list):
        self.name = name
        self.list = list
        self.ls = []

    def avgs(self):
        total = 0
        for i in self.list:
            self.ls.append(i)
            total += i
        i_avg = round((total / len(self.list)), 2)
        return i_avg

    def show(self):
        return f"{self.name} 센서 / 측정 {len(self.list)}회 / 평균 {self.avgs()}"


info = sensor("범용", 온도)
print(info.name, info.avgs())
print(info.show())
print()

print("문제 10. 상속")


class temp_sensor(sensor):
    def __init__(self, name, list, limit=90):
        super().__init__(name, list)
        self.limit = limit
        self.wrong_ls = []

    def wrong(self):
        for i in self.list:
            if i > self.limit:
                self.wrong_ls.append(i)
        return self.wrong_ls

    def wrong_cnt(self):
        print(f"{len(self.wrong())} {self.limit}")


ts = temp_sensor("온도", 온도)
print(ts.show())
ts.wrong_cnt()
print()

print("문제 11. 오버라이딩")


class vib_sensor(sensor):
    def __init__(self, name, list, limit=35):
        super().__init__(name, list)
        self.limit = limit

    def show(self):
        return f"[진동] {self.name} / 평균 {self.avgs()} / 한계 {self.limit}"


vs = vib_sensor("진동", [30.1, 31.4, 41.2, 29.8])
vs.show()
ts.show()
print(isinstance(vs, vib_sensor), isinstance(vs, temp_sensor))
print()

print("문제 12. 서로 다른 객체를 같은 방법으로 다루기")
all_ss = []
all_ss.append(vs)
all_ss.append(ts)

for o in all_ss:
    print(o.show())
print()

print("문제 13. NumPy 배열로 바꿔 보기")
temp_arr = np.array(온도)
print(temp_arr.shape, temp_arr.dtype)
print(
    np.round(np.sum(temp_arr), 1),
    np.round(np.mean(temp_arr), 2),
    np.max(temp_arr),
    np.min(temp_arr),
)
print(temp_arr + 3)
print()

print("문제 14. 불리언 인덱싱")
print(temp_arr[temp_arr > 75])
print(np.where([temp_arr > 75])[1])
print(f"{(temp_arr > 75).mean() * 100}")
print()

print("문제 15. z-점수 이상 탐지를 함수로 - 오늘의 마무리")
import pandas as pd

# 데이터 프레임에 담은 csv 자료 (이름: m_records)
m_records = pd.read_csv("설비온도기록.csv")

# DF에 담은 자료를 numpy 배열에 담음
m_arr = m_records.to_numpy()

# "온도"열을 따로 지정하여 numpy 배열에 담음
m_temps = m_records["온도"].to_numpy()
print(m_arr.shape, len(m_temps))
print(round(m_temps.mean(), 2), round(m_temps.std(), 2))

# z-점수
zm_temps = (m_temps - m_temps.mean()) / m_temps.std()
# 임계값 설정
stnd_abs = np.abs(-3)

# 임계치 넘는 값
over_z = m_temps[np.where(zm_temps > stnd_abs)]
# 이상값의 위치
where_z = np.where(zm_temps > stnd_abs)[0]
# True의 개수
sum_z = np.sum(zm_temps > stnd_abs)
print(over_z, where_z, sum_z)

# 임계값 재조정
stnd_abs = np.abs(-2)
over_z = m_temps[np.where(zm_temps > stnd_abs)]
where_z = np.where(zm_temps > stnd_abs)[0]
sum_z = np.sum(zm_temps > stnd_abs)
print(over_z, where_z, sum_z)

# 전체 대비 비율
print(np.round((len(over_z) / len(m_temps)) * 100, 1))

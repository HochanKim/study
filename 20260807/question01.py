data = [
    {
        "id": "B001",
        "loc": "울산",
        "line": 2,
        "eq": "P-01",
        "type": "프레스",
        "year": 2018,
        "m": {"temp": 85.2, "pres": 120.5, "vib": 1.2},
        "logs": [
            {"t": "08:00", "state": "RUN", "err": None},
            {"t": "09:00", "state": "WARN", "err": "TEMP_H"},
        ],
        "qc": {"insp": "Kim", "defect": True, "types": ["CRACK", "DENT"]},
    },
    {
        "id": "B002",
        "loc": "울산",
        "line": 1,
        "eq": "W-03",
        "type": "용접",
        "year": 2020,
        "m": {"temp": 450.5, "pres": 45.2, "vib": 0.4},
        "logs": [
            {"t": "08:00", "state": "RUN", "err": None},
            {"t": "10:00", "state": "RUN", "err": None},
        ],
        "qc": {"insp": "Lee", "defect": False, "types": []},
    },
    {
        "id": "B003",
        "loc": "창원",
        "line": 1,
        "eq": "I-02",
        "type": "사출",
        "year": 2015,
        "m": {"temp": 260.1, "pres": 230.2, "vib": 4.5},
        "logs": [
            {"t": "08:30", "state": "RUN", "err": None},
            {"t": "11:00", "state": "ERROR", "err": "PRES_L"},
            {"t": "11:15", "state": "STOP", "err": "EMER"},
        ],
        "qc": {"insp": "Park", "defect": True, "types": ["BURR"]},
    },
    {
        "id": "B004",
        "loc": "창원",
        "line": 2,
        "eq": "P-02",
        "type": "프레스",
        "year": 2019,
        "m": {"temp": 82.0, "pres": 115.0, "vib": 0.9},
        "logs": [{"t": "09:00", "state": "RUN", "err": None}],
        "qc": {"insp": "Kim", "defect": False, "types": []},
    },
    {
        "id": "B005",
        "loc": "울산",
        "line": 2,
        "eq": "I-01",
        "type": "사출",
        "year": 2021,
        "m": {"temp": 235.0, "pres": 210.0, "vib": 2.1},
        "logs": [
            {"t": "09:30", "state": "RUN", "err": None},
            {"t": "10:30", "state": "WARN", "err": "VIB_H"},
        ],
        "qc": {"insp": "Choi", "defect": True, "types": ["CRACK", "BURR"]},
    },
    {
        "id": "B006",
        "loc": "부산",
        "line": 1,
        "eq": "D-01",
        "type": "도장",
        "year": 2017,
        "m": {"temp": 60.5, "pres": 15.0, "vib": 0.2},
        "logs": [
            {"t": "07:30", "state": "RUN", "err": None},
            {"t": "12:00", "state": "ERROR", "err": "TEMP_L"},
        ],
        "qc": {"insp": "Lee", "defect": True, "types": ["SCRATCH"]},
    },
    {
        "id": "B007",
        "loc": "부산",
        "line": 2,
        "eq": "D-02",
        "type": "도장",
        "year": 2022,
        "m": {"temp": 65.0, "pres": 16.5, "vib": 0.3},
        "logs": [
            {"t": "08:00", "state": "RUN", "err": None},
            {"t": "13:00", "state": "RUN", "err": None},
        ],
        "qc": {"insp": "Park", "defect": False, "types": []},
    },
    {
        "id": "B008",
        "loc": "울산",
        "line": 1,
        "eq": "W-01",
        "type": "용접",
        "year": 2016,
        "m": {"temp": 470.2, "pres": 48.0, "vib": 0.8},
        "logs": [
            {"t": "09:00", "state": "WARN", "err": "TEMP_H"},
            {"t": "11:30", "state": "ERROR", "err": "GAS_ERR"},
        ],
        "qc": {"insp": "Choi", "defect": True, "types": ["CRACK", "HOLE"]},
    },
    {
        "id": "B009",
        "loc": "창원",
        "line": 1,
        "eq": "P-03",
        "type": "프레스",
        "year": 2020,
        "m": {"temp": 88.9, "pres": 122.0, "vib": 1.1},
        "logs": [{"t": "10:00", "state": "RUN", "err": None}],
        "qc": {"insp": "Kim", "defect": False, "types": []},
    },
    {
        "id": "B010",
        "loc": "부산",
        "line": 1,
        "eq": "I-03",
        "type": "사출",
        "year": 2019,
        "m": {"temp": 250.0, "pres": 215.5, "vib": 3.2},
        "logs": [
            {"t": "08:10", "state": "RUN", "err": None},
            {"t": "14:20", "state": "WARN", "err": "PRES_H"},
        ],
        "qc": {"insp": "Lee", "defect": True, "types": ["BURR", "DENT"]},
    },
]

#
# => 리스트: data
# => data 안에 저장된 딕셔너리들
# => 딕셔너리 키값: id, loc, line, eq, type, year,
# m (여기 안에 중복 딕셔너리), logs (여기 안에 리스트와 딕셔너리들이 포함), qc (여기 안에 중복 딕셔너리, 그리고 리스트 값이 포함)


# 문제 1: 검사자별 불량 판정 건수 집계
# * 요구사항:
#     1. 전체 데이터를 순회하며 각 검사자(insp)가 담당한 전체 검사 횟수를 세어보세요.
#     2. 그중에서 실제로 불량(defect)이 True로 판정된 건수가 각각 몇 건인지 구하여,
#         검사자 이름을 키로 하고 불량 판정 건수를 값으로 하는 딕셔너리를 만드시오.
# -> "defect": True의 횟수를 value ("False"는 정상 기계) / insp를 key로 하는 딕셔너리

insp_cnt = {}  # 검사자들의 전체 검사 횟수들을 담을 딕셔너리 (key: insp / value: 횟수)
for check in data:
    # 각 검사자(insp)가 담당한 전체 검사 횟수
    last_name = check["qc"]["insp"]
    insp_cnt[last_name] = insp_cnt.get(last_name, 0) + 1
# print(f"검사자들 검사 회수: {insp_cnt}")

for reset in data:
    # 딕셔너리값 리셋
    last_name = reset["qc"]["insp"]
    insp_cnt[last_name] = 0
# print(f"검사자들 검사 회수 리셋: {insp_cnt}")

for error in data:
    last_name = error["qc"]["insp"]
    error_check = error["qc"]["defect"]
    if error_check == True:
        insp_cnt[last_name] = insp_cnt.get(last_name, 0) + 1
# print(f"검사자들 에러 체크 회수: {insp_cnt}")

# # 에러 여부 가져오기
# 최종 출력된 검사자들의 에러 발견 횟수
# 출력 예시:
# {"Kim": 1, "Lee": 2, "Park": 1, "Choi": 2}


# 문제 2: 조건부 설비 타입별 평균 진동 계산
# * 요구사항:
#     1. year가 2018년 미만인 설비는 계산 대상에서 제외합니다. (2018년 이전에 설치된 설비들)
#     2. 남은 설비들을 타입(type)별로 묶어서 각 타입의 평균 진동(m['vib']) 값을 구하시오.
#     3. 단, logs에 "ERROR" 상태가 포함된 설비는 진동 값에 1.2배를 곱한 뒤 평균 계산에 반영합니다.
#     4. 최종 결과는 타입 이름을 키, 계산된 평균 진동 값을 값으로 하는 딕셔너리로 출력하시오.

# 설비들의 진동을 담기 위한 빈 딕셔너리 생성
first_vibe = {}

for idx, i in enumerate(data):
    vib_get = i.get("m")["vib"]
    type_name = i.get("type")
    machine_year = i.get("year")
    logs_data = i.get("logs", {})
    print(type_name, machine_year, logs_data)
    # print(f"모든 기계: {type_name}, {machine_year}, {vib_get}, {log_error}")
    if (type_name in first_vibe) == True and machine_year >= 2018:
        # 딕셔너리 키에 존재하고 2018년 이후에 제작된 설비
        first_vibe[type_name].append(vib_get)  # 생성된 키에 리스트 형식으로 값을 포함
    elif (type_name in first_vibe) == False and machine_year >= 2018:
        # 딕셔너리 키에 존재하지 않으면서 2018년 이후에 제작된 설비
        first_vibe[type_name] = [vib_get]  # 딕셔너리 키 생성
# print(first_vibe)  # 2018년 미만 설비들을 제외한 딕셔너리 정보

# 진동 평균 구하기
# avg_vibe = {}
# for k, v in first_vibe.items():
#     print(sum(v))
#     print(len(v))
# print(avg_vibe)

# 출력 예시:
# {"프레스": 1.0, "용접": 0.4, "사출": 2.1, "도장": 0.3}


# 문제 3: 설비별 종합 리스크 점수 계산
# * 요구사항: 모든 설비를 대상으로 다음 채점 기준에 따라 리스크 점수를 각각 계산하고, 설비 id를 키, 총 리스크 점수를 값으로 하는 딕셔너리를 만드시오.
#     * 기본 점수: qc['defect']가 True이면 50점, False이면 0점
#     * 불량 유형 추가 점수: qc['types']에 들어있는 불량 개수당 10점씩 추가 (예: 불량이 2개면 +20점)
#     * 로그 경고 페널티: logs에서 state가 "ERROR"인 항목당 +15점, "WARN"인 항목당 +5점 추가
# 출력 예시: {"B001": 70, "B002": 0, "B003": 80, ...}

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

# 문제 2: 조건부 설비 타입별 평균 진동 계산
# * 요구사항:
#     1. year가 2018년 미만인 설비는 계산 대상에서 제외합니다.
#     2. 남은 설비들을 타입(type)별로 묶어서 각 타입의 평균 진동(m['vib']) 값을 구하시오.
#     3. 단, logs에 "ERROR" 상태가 포함된 설비는 진동 값에 1.2배를 곱한 뒤 평균 계산에 반영합니다.
#     4. 최종 결과는 타입 이름을 키, 계산된 평균 진동 값을 값으로 하는 딕셔너리로 출력하시오.

# 출력 예시:
# {"프레스": 1.0, "용접": 0.4, "사출": 2.1, "도장": 0.3}

vibsum = {}  # 기계종류:해당기계의 진동값 합계
typecount = {}  # 기계종류:해당기계의 댓수

for i in data:
    if i["year"] < 2018:
        continue
    type = i["type"]
    vib = i["m"]["vib"]

    for x in i["logs"]:
        if x["state"] == "ERROR":
            vib *= 1.2
            break

    if type not in vibsum:
        vibsum[type] = vib
        typecount[type] = 1
    else:
        vibsum[type] += vib
        typecount[type] += 1

avg = {}  # 기계종류:해당기계의 진동값 평균

for i in vibsum:
    avg[i] = round(vibsum[i] / typecount[i], 1)

print(avg)

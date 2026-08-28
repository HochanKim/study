import numpy as np

hourly = np.array(
    [
        82,
        88,
        85,
        84,
        80,
        84,  # 0~5시
        90,
        88,
        120,
        86,
        85,
        75,  # 6~11시
        85,
        84,
        86,
        85,
        84,
        86,  # 12~17시
        91,
        88,
        125,
        87,
        90,
        86,
    ]
)  # 18~23시
# 핵심: 한 줄로 늘어선 긴 배열을 '각 행이 한 시간 구간'이 되도록 reshape로 접습니다.
# 스물네 개를 여섯 개씩 네 구간으로 → reshape(4, 6).
# reshape가 '값은 그대로, 배치만 바꾸는' 성질을 시간 묶기에 쓰는 거예요.
blocks = hourly.reshape(4, 6)
print(blocks)

print(
    "구간별 평균:", np.round(blocks.mean(axis=1), 2)
)  # → 구간별 평균: [83.83 90.67 85. 94.5 ]
print("구간별 최대:", blocks.max(axis=1))  # → 구간별 최대: [ 88 120 86 125]

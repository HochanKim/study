# 주어진 데이터를 활용하여 나만의 선형 모델 만들기
# x6 개 이상
# 가중치 조절하면서 만들기
# 실제 데이터를 가져와서 대입해 순위 보여주기
# - 코드로 제출
# 순위표 csv만들어 코드와 함께 제출

import pandas as pd

df_movie = pd.read_csv("korea_boxoffice_top10_59_260907_Question.csv")
# print(df_movie["제목"][0])
# print(len(df_movie))

# 천만 관객까지 하루 평균 관객 수
df_movie["x1_천만 관객까지 하루 평균 관객 수"] = round(
    10000000 / df_movie["천만 돌파 소요일"]
)

print(df_movie["x1_천만 관객까지 하루 평균 관객 수"])
print()


# 평점
movie_rate = [
    8.88,  # 명량
    8.87,  # 왕과 사는 남자
    9.21,  # 극한직업
    8.73,  # 신과함께-죄와 벌
    9.16,  # 국제시장
    9.42,  # 아바타(2009)
    9.50,  # 어벤져스: 엔드게임
    8.94,  # 겨울왕국 2
    9.24,  # 베테랑(2015)
    9.39,  # 서울의 봄
]

df_movie["x2_영화 평점"] = movie_rate
print(df_movie["x2_영화 평점"])
print()

# 제작비
movie_invest = [
    # 1억 원 기준
    190,  # 명량
    105,  # 왕과 사는 남자
    65,  # 극한직업
    200,  # 신과함께-죄와 벌
    180,  # 국제시장
    3020,  # 아바타(2009)
    4147,  # 어벤져스: 엔드게임
    1748,  # 겨울왕국 2
    60,  # 베테랑(2015)
    232,  # 서울의 봄
]

df_movie["x3_영화 제작비"] = movie_invest
print(df_movie["x3_영화 제작비"])
print()

# 제작비 대비 관객수 (국내 한정)
rate_invest = df_movie["누적관객수 (명)"] / df_movie["x3_영화 제작비"]
df_movie["x4_제작비 대비 관객 비율"] = rate_invest.round(0)
print(df_movie["x4_제작비 대비 관객 비율"])
print()

# 누적 관객수
sum_audience = df_movie["누적관객수 (명)"]

# 천만 돌파 소요일
pass_thou = df_movie["천만 돌파 소요일"]


# --- [정규화 함수 정의] ---
# 서로 다른 단위를 가진 데이터를 0~1 사이의 값으로 변환합니다.
def min_max_scale(series, ascending=True):
    min_val = series.min()
    max_val = series.max()
    if max_val == min_val:
        # 에러(ZeroDivisionError) 방지를 위한 조치 (모든 값을 0으로 맞추기)
        return series * 0
    if ascending:
        return (series - min_val) / (max_val - min_val)
    else:
        # 제작비처럼 값이 낮을수록 유리한 경우 역방향 처리 가능
        return (max_val - series) / (max_val - min_val)


# 각 변수별로 정규화 적용 (s1 ~ s6)
df_movie["s1"] = min_max_scale(df_movie["x1_천만 관객까지 하루 평균 관객 수"])
df_movie["s2"] = min_max_scale(df_movie["x2_영화 평점"])
df_movie["s3"] = min_max_scale(
    df_movie["x3_영화 제작비"], ascending=False
)  # 제작비는 적을수록 좋다면 ascending=False
df_movie["s4"] = min_max_scale(df_movie["x4_제작비 대비 관객 비율"])
df_movie["s5"] = min_max_scale(sum_audience)
df_movie["s6"] = min_max_scale(pass_thou)


# --- [가중치(w) 설정 및 최종 점수 계산] ---
# 중요도에 따라 가중치의 합이 보통 1.0(또는 100%)이 되도록 조절합니다.
w1 = 0.25  # 하루 평균 관객 수 가중치 (25%)
w2 = 0.3  # 평점 가중치 (30%)
w3 = 0.1  # 제작비 가중치 (10%)
w4 = 0.15  # 제작비 대비 관객 비율 가중치 (15%)
w5 = 0.1  # 누적 관객수 비율 가중치 (10%)
w6 = 0.1  # 천만 돌파 비율 가중치 (10%)


df_movie["최종_선형점수"] = round(
    (
        (df_movie["s1"] * w1)
        + (df_movie["s2"] * w2)
        + (df_movie["s3"] * w3)
        + (df_movie["s4"] * w4)
        + (df_movie["s5"] * w5)
        + (df_movie["s6"] * w6)
    )
    * 100,
    2,
)  # 100점 만점으로 환산

# 최종 점수 기준 순위 부여
df_movie["최종_순위"] = (
    df_movie["최종_선형점수"].rank(ascending=False, method="min").astype(int)
)

# 결과 확인 및 CSV 내보내기
df_result = df_movie[["제목", "최종_선형점수", "최종_순위"]].sort_values(by="최종_순위")
print(df_result)

df_result.to_csv("movie_ranking_result.csv", index=False, encoding="utf-8-sig")


# SSE / MSE 계산
# 데이터 3개 선택
sample = df_movie.iloc[[0, 2, 9]].copy()

# 예측값
sample["예측값"] = sample["최종_선형점수"]

# 실제 누적 관객수를 Max-Min 정규화
sample["실제값"] = min_max_scale(sample["누적관객수 (명)"]) * 100

# 오차 계산
sample["오차"] = sample["실제값"] - sample["예측값"]

# 오차 제곱
sample["오차^2"] = sample["오차"] ** 2


# SSE
SSE = sample["오차^2"].sum()

# MSE
MSE = SSE / len(sample)

print(sample[["제목", "예측값", "실제값", "오차", "오차^2"]])

print()
print("SSE :", round(SSE, 2))
print("MSE :", round(MSE, 2))

import numpy as np

진동_실측 = [3.0, 3.2, 2.9, 15.2, 3.1, 2.8]  # 4번째가 이상값(15.2)
진동_예측 = [3.1, 3.1, 3.1, 3.1, 3.1, 3.1]  # 기준 3.1
# 오차 = 실측 - 예측
# zip은 두 리스트를 같은 자리끼리 짝지어 줍니다.
# 그 짝마다 실제에서 예측을 빼면 그 칸의 오차가 나옵니다.

오차목록 = [a - b for a, b in zip(진동_실측, 진동_예측)]
print("오차 다섯 개:", [round(e, 2) for e in 오차목록])


# SSE - 오차 제곱합
def sse(y, yhat):
    return sum((a - b) ** 2 for a, b in zip(y, yhat))
    # sum_val = 0
    # for a, b in zip(y, yhat):
    #     sum_val += (a - b) ** 2
    # return sum_val


# MSE - 제곱합의 평균
def mse(y, yhat):
    return sse(y, yhat) / len(y)


# MAE - 절댓값의 평균
def mae(y, yhat):
    return sum(abs(a - b) for a, b in zip(y, yhat)) / len(y)


print("[실습 - 진동 케이스 B]")
print(" SSE =", round(sse(진동_실측, 진동_예측), 2))  # → SSE = 146.56
print(" MSE =", round(mse(진동_실측, 진동_예측), 2))  # → MSE = 24.43
print(" MAE =", round(mae(진동_실측, 진동_예측), 2))  # → MAE = 2.13

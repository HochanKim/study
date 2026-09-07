import numpy as np

회전수 = [1500, 1520, 1490, 1510, 1505, 1495, 1600, 1480, 1510, 1490]


# 평균 함수
def 평균(xs):
    return sum(xs) / len(xs)


# 중앙값 함수
def 중앙값(xs):
    # 크기 순 정렬
    s = sorted(xs)
    n = len(s)
    middle = n // 2
    if n % 2 == 1:
        # 홀수개: 정 가운데 위치 하나
        return s[middle]
    else:
        # 짝수개: 가운데 두 개 값의 평균
        return (s[middle - 1] + s[middle]) / 2


# 최빈값 함수 (가장 자주 나온 값)
def 최빈값(xs):
    count = {}
    for x in xs:
        count[x] = count.get(x, 0) + 1
    many_cnt = max(count.values())
    return [k for k, v in count.items() if v == many_cnt]


# 분산 함수
def 분산(xs):
    m = 평균(xs)
    return sum((x - m) ** 2 for x in xs) / len(xs)


# 표준편차 함수
def 표준편차(xs):
    return 분산(xs) ** 0.5


# 분위수 함수
def 분위수(xs, q):
    s = sorted(xs)
    n = len(s)
    위치 = q * (n - 1)
    아래 = int(위치)
    나머지 = 위치 - 아래
    if 아래 + 1 < n:
        return s[아래] + 나머지 * (s[아래 + 1] - s[아래])
    return s[아래]


# (실습 정답 예시)
# print("[실습 · 회전수 요약]")
# print("평균:", round(평균(회전수), 4), "/ numpy:", round(np.mean(회전수), 4))
# print("중앙값:", 중앙값(회전수), "/ numpy:", np.median(회전수))
# print("최빈값:", 최빈값(회전수))
# print("분산:", round(분산(회전수), 4), "/ numpy:", round(np.var(회전수), 4))
# print("표준편차:", round(표준편차(회전수), 4), "/ numpy:", round(np.std(회전수), 4))
# print("최소/최대/범위:", min(회전수), max(회전수), max(회전수) - min(회전수))
# Q1r = 분위수(회전수, 0.25)
# Q3r = 분위수(회전수, 0.75)
# print("Q1/Q3/IQR:", Q1r, Q3r, Q3r - Q1r)


# 벡터덧셈 함수
def 벡터덧셈(x, y):
    result = []
    for i in range(len(x)):
        result.append(x[i] + y[i])
    return result


# 스칼라곱 함수
def 스칼라곱(s, x):
    result = []
    for i in range(len(x)):  # 자리마다
        result.append(s * x[i])  # 그 자리 값에 s 를 곱함
    return result


# 내적 함수
def 내적(x, y):
    sum = 0
    for i in range(len(x)):  # 같은 자리끼리
        sum = sum + x[i] * y[i]  # 곱해서 합에 누적 (Σ)
    return sum


u = [2, 4, 6]
t = [1, 3, 5]
print("행렬덧셈:", 벡터덧셈(u, t))
print("numpy 덧셈:", np.array(u) + np.array(t))
print("스칼라곱 2 x a:", 스칼라곱(3, u))
print("numpy 스칼라곱:", 3 * np.array(u))
print("내적 a·b:", 내적(u, t))
print("numpy dot:", np.dot(u, t))
print()


# 행렬곱 함수
def 행렬곱(A, B):
    m = len(A)
    n = len(A[0])
    p = len(B[0])
    C = [[0] * p for _ in range(m)]
    for i in range(m):
        for j in range(p):
            합 = 0
            for k in range(n):
                합 = 합 + A[i][k] * B[k][j]
            C[i][j] = 합
    return C


# (실습 정답 예시 — 케이스 B 행렬곱)
R = [[1, 0, 2], [3, 1, 1]]  # (2 × 3)
S = [[4, 1], [2, 5], [0, 3]]  # (3 × 2) → 안쪽 3 == 3, 결과 (2 × 2)
# A = [[1, 2, 3, 4], [5, 6, 7, 8]]  # (2 × 4)
# B = [[4, 1, 2], [2, 5, 0], [0, 3, 4], [1, 3, 3]]  # (4 × 3) → 안쪽 4 == 4, 결과 (2 × 3)
직접 = 행렬곱(R, S)
넘파이 = (np.array(R) @ np.array(S)).tolist()
print("[실습 예시 · 행렬곱]")
print("직접 :", 직접)
# → 직접 : [[4, 7], [14, 11]]
print("numpy:", 넘파이)
# → numpy: [[4, 7], [14, 11]]
print("일치 :", 직접 == 넘파이)
print()
# → 일치 : True
# 손 검산: 직접[0] = R의 0행[1,0,2]을 S의 각 열과 내적
# 0열[4,2,0]: 1×4+0×2+2×0 = 4 / 1열[1,5,3]: 1×1+0×5+2×3 = 7 ✓

# 온도 : 그날 설비 평균 온도(도)
# 불량 : 그날 나온 불량품 개수(개)
# 압력 : 그날 설비 평균 압력(bar)
온도 = [70, 72, 74, 76, 78, 80, 82, 84]
불량 = [3, 4, 4, 6, 7, 7, 9, 8]
압력 = [4.0, 4.1, 4.0, 4.2, 4.3, 4.2, 4.5, 4.4]


# 지난 편에서 만든 세 함수를 그대로 가져옵니다(이 편의 밑돌).
# 공분산·상관은 이 위에 쌓입니다.
def AVG(xs):
    return sum(xs) / len(xs)  # Σx / n


def VAR(xs):
    m = 평균(xs)
    return sum((x - m) ** 2 for x in xs) / len(xs)  # Σ(x-평균)² / n


def STD(xs):
    return 분산(xs) ** 0.5  # √분산


def COV(xs, ys):
    mx = 평균(xs)  # x̄
    my = 평균(ys)  # ȳ
    합 = 0
    for x, y in zip(xs, ys):  # 같은 날의 x, y 를 짝지어
        합 += (x - mx) * (y - my)  # (x-x̄)(y-ȳ) 를 누적
    return 합 / len(xs)  # Σ(...) / n


print("cov(온도, 불량):", round(COV(온도, 불량), 4))
# → cov(온도, 불량): 8.75
수율 = [96, 94, 95, 92, 91, 90, 88, 89]  # 온도 오르면 대체로 내려감
print("cov(온도, 수율):", round(COV(온도, 수율), 4))
# → cov(온도, 수율): -11.875
print("cov(온도, 온도):", round(COV(온도, 온도), 4))
print("var(온도) :", round(VAR(온도), 4))
# → cov(온도, 온도): 21.0
# → var(온도) : 21.0
# 두 값이 똑같죠. 분산은 공분산의 특별한 경우(자기 자신과의)입니다.
print("cov(온도, 압력):", round(COV(온도, 압력), 4))
# → cov(온도, 압력): 0.6875
print()


def 상관계수(xs, ys):
    return COV(xs, ys) / (STD(xs) * STD(ys))  # cov / (σx·σy)


print("r(온도, 불량):", round(상관계수(온도, 불량), 4))
# → r(온도, 불량): 0.9547
print("r(온도, 압력):", round(상관계수(온도, 압력), 4))
# → r(온도, 압력): 0.8872
print("r(온도, 수율):", round(상관계수(온도, 수율), 4))
# → r(온도, 수율): -0.9552

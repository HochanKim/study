def weight(weight):
    # 실제 만족도
    grd_man = 39
    swi_man = 70
    ice_man = 111
    ny_man = 93

    # 동행 수
    grd_person = 3
    swi_person = 6
    ice_person = 9
    ny_person = 8

    # 예상
    yesang_grd = grd_person * weight
    yesang_swi = swi_person * weight
    yesang_ice = ice_person * weight
    yesang_ny = ny_person * weight

    # 오차
    grd_dif = grd_man - yesang_grd
    swi_dif = swi_man - yesang_swi
    ice_dif = ice_man - yesang_ice
    ny_dif = ny_man - yesang_ny

    # SSE
    sse_sum = (grd_dif**2) + (swi_dif**2) + (ice_dif**2) + (ny_dif**2)

    return sse_sum


print("가중치 9:", weight(9))  # 가중치 10
print("가중치 10:", weight(10))  # 가중치 10
print("가중치 11:", weight(11))  # 가중치 11
print("가중치 12:", weight(12))  # 가중치 12
print("가중치 13:", weight(13))  # 가중치 13
print("가중치 14:", weight(14))  # 가중치 14
print("가중치 15:", weight(15))  # 가중치 15
print()

# 손실 함수
temp = [20, 22, 24, 26, 28, 30, 32, 34, 36, 38]
error = [3, 4, 5, 5, 7, 8, 8, 10, 11, 12]

b = -7.2  # 오늘은 b 를 이 값에 고정. w 하나만 움직인다.


def loss(w):
    # 각 (온도, 불량) 쌍마다 예측(w·x + b)과 실제(y)의 차이를 제곱해 더하고
    # 개수로 나눈다. 순수 파이썬 — for 를 한 줄 안에 담은 것뿐이다.
    SSE = sum((y - (w * x + b)) ** 2 for x, y in zip(temp, error))
    return SSE / len(temp)


# w 하나를 넣어 손실을 재봅니다. w=0.5 는 지난 편의 정답이었죠.
print("손실(w=0.5):", round(loss(0.5), 4))
print("손실(w=0.3):", round(loss(0.3), 4))


# 기울기
h = 0.00001  # 아주 작은 걸음. 너무 크면 부정확, 너무 작으면 오차가 낀다.
# h = 0.1


def inclination(w):
    # 기울기 함수
    return (loss(w + h) - loss(w - h)) / (2 * h)


# w=0.3 자리의 기울기를 재봅니다.
print("w=0.3 의 기울기:", round(inclination(0.3), 4))
print("w=0.35 의 기울기:", round(inclination(0.35), 4))
print("w=0.4 의 기울기:", round(inclination(0.4), 4))
print("w=0.45 의 기울기:", round(inclination(0.45), 4))
print("w=0.5 의 기울기:", round(inclination(0.5), 4))
print()

# 한 발 내려가기
lr = 0.0003
# w=0.3 에서 한 발 내려가 봅시다.
current_w = 0.3
g = inclination(current_w)
new_w = current_w - lr * g


print("[w=0.3 에서 한 발 내려가기]")
print(" 기울기:", round(g, 4))
print(" 현재 w:", current_w, "→ 새 w:", round(new_w, 6))
print()
print(" 손실 이전 (w=0.3):", round(loss(current_w), 4))
print(" 손실 이후 (w=0.40488):", round(loss(new_w), 4))
print()


# 실습
시작w = 0.7
g2 = inclination(시작w)
새w2 = 시작w - lr * g2
print("[실습 · w=0.7 에서 한 발]")
print(" 기울기:", round(g2, 4))
print(" 현재 w:", 시작w, "→ 새 w:", round(새w2, 6))
print(" 손실 이전 (w=0.7):", round(loss(시작w), 4))
print(" 손실 이후 (w=0.59512):", round(loss(새w2), 4))
print()


# 시그모이드 영역
z = [-2, 2, 1]


# 시그모이드 함수
def sigmoid(input):
    z = 1 / (1 + (2.718 ** (-input)))
    return z


for z_num in z:
    print(f"{z_num}의 시그모이드:", sigmoid(z_num))


# print(sigmoid(0.4 * 5 + 4))
# print(sigmoid(0.4 * 10 + 4))
# print(sigmoid(0.4 * 15 + 4))
print()
print(sigmoid(0.4 * 10 + 4))
print(sigmoid(0.4 * 10 - 4))
print(sigmoid(2 * 2 - 5))
print(sigmoid(2 * (2 - 5)))
print(2 * sigmoid(2 - 5))
print(sigmoid(2) - 5)

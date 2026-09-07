# 1 예측하고 싶은 것 y를 정한다
# 2 영향을 주는 변수 x를 2개 이상 정한다
# 3 각 변수의 방향과 가중치 w를 정한다
# 4 필요하다면 보정값 b를 정한다
# 5 실제 숫자를 1번 넣어 계산한다

# MLB WS 기대 우승 가치
# => LA D, 애틀랜타 B, 시카고 C, 밀워키 B, 필라델피아 P
# => 뉴욕 Y, 클리블랜드 G, 휴스턴 A, 탬파베이 R, 시카고 W

# 변수 x: 2개 이상
# 1) 구단 가치 / ex) 85억 달러 => 85
# 2) 선수 가치 / ex) 3억 4천만 달러 => 3.4

"""
구단            구단 가치       선수 가치
LA D            78              3.36
애틀랜타 B      33.5            2.59
시카고 C        50              2.41
밀워키 B        19              1.45
필라델피아 P    34              2.88

뉴욕 Y          85              2.94
클리블랜드 G    16.6            0.77
휴스턴 A        32              2.39
탬파베이 R      17              1.07
시카고 W        19.4            1.02
"""


# 기본 계산
def calc_basic(team, x1, x2):
    return f"{team} 계산: {round(x1 - x2, 2)}"


# 보정치 적용
def calc_weight(team, x1, x2, weight):
    return f"{team} 계산: {round(x1 - x2 + weight, 2)}"


# 계산
print("=" * 10, "계산", "=" * 10)
print(calc_basic("LA D", 78, 3.36))
print(calc_basic("애틀랜타 B", 33.5, 2.59))
print(calc_basic("시카고 C", 50, 2.41))
print(calc_basic("밀워키 B", 19, 1.45))
print(calc_basic("필라델피아 P", 34, 2.88))
# LA D > 시카고 C > 필라델피아 P > 애틀랜타 B > 밀워키 B
print()
print(calc_basic("뉴욕 Y", 85, 2.94))
print(calc_basic("클리블랜드 G", 16.6, 0.77))
print(calc_basic("휴스턴 A", 32, 2.39))
print(calc_basic("탬파베이 R", 17, 1.07))
print(calc_basic("시카고 W", 19.4, 1.02))
print()
# 뉴욕 Y > 휴스턴 A > 시카고 W > 탬파베이 R > 클리블랜드 G


# 보정치 적용 (1) => +30
print("=" * 10, "보정치 적용 (+30)", "=" * 10)
print(calc_weight("LA D", 78, 3.36, 30))
print(calc_weight("애틀랜타 B ", 33.5, 2.59, 30))
print(calc_weight("시카고 C", 50, 2.41, 30))
print(calc_weight("밀워키 B", 19, 1.45, 30))
print(calc_weight("필라델피아 P", 34, 2.88, 30))
# LA D > 시카고 C > 필라델피아 P > 애틀랜타 B > 밀워키 B
print()
print(calc_weight("뉴욕 Y", 85, 2.94, 30))
print(calc_weight("클리블랜드 G", 16.6, 0.77, 30))
print(calc_weight("휴스턴 A", 32, 2.39, 30))
print(calc_weight("탬파베이 R", 17, 1.07, 30))
print(calc_weight("시카고 W", 19.4, 1.02, 30))
# 뉴욕 Y > 휴스턴 A > 시카고 W > 탬파베이 R > 클리블랜드 G
print()

# 보정치 적용 (2) => -100
# => 모든 점수가 음수로 적용한 순위
print("=" * 10, "보정치 적용 (-100)", "=" * 10)
print(calc_weight("LA D", 78, 3.36, -100))
print(calc_weight("애틀랜타 B ", 33.5, 2.59, -100))
print(calc_weight("시카고 C", 50, 2.41, -100))
print(calc_weight("밀워키 B", 19, 1.45, -100))
print(calc_weight("필라델피아 P", 34, 2.88, -100))
# LA D > 시카고 C > 필라델피아 P > 애틀랜타 B > 밀워키 B
print()
print(calc_weight("뉴욕 Y", 85, 2.94, -100))
print(calc_weight("클리블랜드 G", 16.6, 0.77, -100))
print(calc_weight("휴스턴 A", 32, 2.39, -100))
print(calc_weight("탬파베이 R", 17, 1.07, -100))
print(calc_weight("시카고 W", 19.4, 1.02, -100))
# 뉴욕 Y > 휴스턴 A > 시카고 W > 탬파베이 R > 클리블랜드 G
print()


# 곱셈으로 가치 조정 (구단 가치 ↓ / 선수 가치 ↑)
# 곱셈으로 가치 조정한 함수
def calc_control(team, x1, x2, weight):
    # x1 * 0.1 / x2 * 10 가치 조정
    return f"{team} 가치 조정: {round(x2 * 10 - x1 * 0.1 + weight, 2)}"


print("=" * 10, "가치 조정", "=" * 10)
print(calc_control("LA D", 78, 3.36, 30))
print(calc_control("애틀랜타 B ", 33.5, 2.59, 30))
print(calc_control("시카고 C", 50, 2.41, 30))
print(calc_control("밀워키 B", 19, 1.45, 30))
print(calc_control("필라델피아 P", 34, 2.88, 30))
# LA D > 필라델피아 P > 애틀랜타 B > 시카고 C > 밀워키 B
# => 가치 조정 이전 순위: LA D > 시카고 C > 필라델피아 P > 애틀랜타 B > 밀워키 B
print()
print(calc_control("뉴욕 Y", 85, 2.94, 30))
print(calc_control("클리블랜드 G", 16.6, 0.77, 30))
print(calc_control("휴스턴 A", 32, 2.39, 30))
print(calc_control("탬파베이 R", 17, 1.07, 30))
print(calc_control("시카고 W", 19.4, 1.02, 30))
# 뉴욕 Y > 휴스턴 A > 탬파베이 R > 시카고 W > 클리블랜드 G
# => 가치 조정 이전 순위: 뉴욕 Y > 휴스턴 A > 시카고 W > 탬파베이 R > 클리블랜드 G
print()

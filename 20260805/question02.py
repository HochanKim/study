print("1. 편차 판단")
# 다음 리스트를 만들고, 가장 큰 값과 가장 작은 값의 차이를 출력하시오.
# 그 다음 줄에는 차이가 5 이상이면 차이가 큽니다, 5 미만이면 차이가 작습니다를 출력하시오.
nums = [3, 7, 2, 9, 4]
# -> 가장 큰 값
max_num = max(nums)
# -> 가장 작은 값
min_num = min(nums)

print(max_num - min_num)
if (max_num - min_num) >= 5:
    print("차이가 큽니다.")
else:
    print("차이가 작습니다.")
print()

# 실행 결과
# 7
# 차이가 큽니다

# 다른 값으로도 확인 — nums = [10, 12, 11] 로 바꾸면
nums = [10, 12, 11]
# -> 가장 큰 값
max_num = max(nums)
# -> 가장 작은 값
min_num = min(nums)

print(max_num - min_num)
if (max_num - min_num) >= 5:
    print("차이가 큽니다.")
else:
    print("차이가 작습니다.")

print("=" * 30)
print("2. 학점 계산기")
# 세 과목 점수 리스트를 만들고,
# 평균을 소수점 둘째 자리까지 출력한 뒤 => format(계산식, ".2f") 다음 줄에 학점을 출력하시오.
# 90점 이상은 A, 80점 이상은 B, 70점 이상은 C, 그 미만은 D다.
scores = [88, 92, 79]
avg_scores = sum(scores) / len(scores)
print(f"{avg_scores:.2f}")
if avg_scores >= 90:
    print("A")
elif avg_scores >= 80:
    print("B")
elif avg_scores >= 70:
    print("C")
else:
    print("D")
print()
# 실행 결과

# 86.33
# B

# 다른 값으로도 확인 — scores = [60, 55, 71] 로 바꾸면
scores = [60, 55, 71]
avg_scores = sum(scores) / len(scores)
print(f"{avg_scores:.1f}")
if avg_scores >= 90:
    print("A")
elif avg_scores >= 80:
    print("B")
elif avg_scores >= 70:
    print("C")
else:
    print("D")
# 62.0
# D
print("=" * 30)

print("3. 장바구니 중복 체크")
# 장바구니 리스트와 담으려는 상품을 만들고, 그 상품이 이미 장바구니에 있으면 이미 담겨 있습니다를 출력하시오.
# 없으면 장바구니 맨 뒤에 추가한 뒤 전체 장바구니를 출력하시오.

cart = ["사과", "우유", "빵"]
item = "계란"
if item not in cart:
    cart.append(item)
else:
    print("이미 담겨 있습니다")
print(cart)
print()

cart = ["사과", "우유", "빵"]
item = "우유"
if item not in cart:  # 만약 리스트 'cart'에 변수 'item' 값이 들어있지 않으면
    cart.append(item)  # 해당 리스트에 추가
else:  # 그렇지 않으면 (리스트 값이 중복되면)
    print("이미 담겨 있습니다")  # 담지 않고 해당 프린트문을 출력
print(cart)
print("=" * 30)

# 실행 결과

# ['사과', '우유', '빵', '계란']

# 다른 값으로도 확인 — item = "우유" 로 바꾸면

# 이미 담겨 있습니다

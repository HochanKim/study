# # ============================================
# 1. 딕셔너리 - 이름표를 붙여 저장
# ==============================================
# 리스트의 불편함에서 출발

# 예시 (리스트)
person = ["김철수", 25, "서울"]
print(person[1])  # 25 <= 값만 봐서는 어떤건지 알 수 없음

# 리스트 => 딕셔너리
person = {"name": "김철수", "age": 25, "city": "서울"}
print(person["age"])  # 나이 25 <- 명확하게 어떤 값을 꺼냈는지 알 수 있음
print()

# 만들기와 꺼내기
person = {"name": "김아무개", "age": 30}
# -> "name", "age" => 키(key)
# -> "김아무개", 30 => 값(value)
print(type(person))  # dict
empty = {}  # 빈 딕셔너리
print()

print(person["name"])  # "김아무개"
# print(person["phone"])  # KeyError 발생: 없는 키

# Tip: get()을 쓰면 없어도 에러가 나오지 않음
print(person.get("phone"))  # None
print(person.get("phone"), "<= 있는지 없는지 확인")
# -> 사용자 입력처럼 뭐가 들어올지 모를 땐 '[]' 대신 'get()'이 안전합니다.
print()

print("name" in person)  # True, 값이 아닌 '키'를 검사
print("김철수" in person)  # False, ※ 딕셔너리 키는 한글로 지정하지 않는 것이 좋다
print()

# 추가, 수정, 삭제
person = {"name": "김철수", "age": 25}

person["city"] = (
    "서울"  # 없는 키, 값 -> 추가   / {"name": "김철수", "age": 25, "city": "서울"}
)
person["age"] = 26  # 있는 키 -> 수정
# -> 추가와 수정의 문법이 같아서, 오타를 내면 조용히 새로운 키가 생성
person["agee"] = 30  # 에러가 안 남, 찾기 어려운 버그의 원인
print(person)

del person["agee"]  # 키: agee 삭제
removed = person.pop("city")  # 삭제하면서 값을 받기
print(removed)
print()

# 키 값 한꺼번에 다루기
scores = {"국어": 90, "영어": 85, "수학": 77}
print(list(scores.keys()))  # ["국어", "영어", "수학"]  / 키를 담음
print(list(scores.values()))  # [90, 85, 77]  / 값을 담음
# -> values()를 뽑으면 리스트처럼 계산이 가능하다
print(len(scores))  # 3 / 딕셔너리의 개수
print()

# 키 규칙과 중첩
ddd = {"문자열": 1, 10: 2, (1, 2): 30}  # 0, 문자열, 숫자, 튜플 담는 것이 가능
# -> error = {[1, 2]: "값"} # X, 리스트는 키로 못씀
print({"a": 1, "a": 2})  # 키 중복시 나중 것이 이김

# 값에는 뭐든 넣을 수 있습니다
student = {
    "name": "김철수",
    "score": [90, 85, 77],  # 값이 리스트
    "address": {"city": "서울", "zip": "1234"},  # 값이 딕셔너리
}
print(student["score"][0])  # 90
print(student["address"]["city"])  # 서울

me = {"name": "원이", "age": 22}
print(f"안녕하세요 {me['name']}입니다, 나이는 {me['age']}살입니다. 잘 부탁드립니다")

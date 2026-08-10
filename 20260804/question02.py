# 모험가 정보 입력받기
# input()을 사용해 모험가의 이름, 레벨, 공격력, 그리고 방패 소지 여부를 입력받습니다.
user_name = input("모험가의 닉네임을 입력하세요: ")
user_level = int(input("레벨을 입력하세요 (예: 10): "))
user_attack = int(input("현재 공격력을 입력하세요 (예: 50): "))
using_shield = input("방패를 소지하고 있나요? (y/n): ")

is_using_shield = int(bool(using_shield == "y" and "1=1"))  # 방패 소지 y: True
is_not_using = int(bool(using_shield == "n" and "1=1"))  # 방패 소지 n: False

# 입력받은 데이터 중 숫자가 필요한 항목은 알맞은 자료형으로 형변환하고, 방패 소지 여부는 적절히 변환해 주세요.
# => int(), float() 등등 사용

# 던전 입장 자격 심사
# 모험가의 레벨이 10 이상이고, 공격력이 50 이상이어야 던전 입장이 가능합니다.
# 조건을 만족하지 못했다면, "입장 자격 미달입니다. 더 수련하고 오세요!"를 출력하고 프로그램을 종료합니다.

# 특수 보너스 판별
# 던전 입장이 가능한 모험가 중, 방패를 가지고 있거나(True) 혹은 레벨이 30 이상인 모험가에게는 "전설의 버프"를 부여합니다.
# 버프 대상자에게는 최종 공격력에 1.5배를 적용하고, "전설의 버프가 발동하여 공격력이 상승합니다!"라는 메시지를 출력합니다. (버프 대상이 아니라면 원래 공격력을 그대로 사용합니다.)
# 최종 결과 출력
# 모든 심사가 끝난 뒤, f-string을 이용해 모험가의 이름, 최종 레벨, 그리고 최종 계산된 전투력(공격력)을 깔끔하게 출력해 주세요.

if user_level >= 10 and user_attack >= 50:
    print("던전 입장이 가능합니다.")
    if is_using_shield == 1 or user_level >= 30:
        user_attack = user_attack * 1.5
        print("전설의 버프가 발동하여 공격력이 상승합니다!")
else:
    print("입장 자격 미달입니다. 더 수련하고 오세요!")

print("=" * 15)
print(f"모험가 이름: {user_name}")
print(f"모험가 레벨: {user_level}")
print(f"모험가의 공격력: {user_attack}")
print("=" * 15)

# input("리스트를 입력해 주세요 (end 입력시 종료)")
# 멜론 차트 1위: Love Attack (리센느)
# end 종료
# 파일명: top100.txt 새로 생성

# import(가져오기)
from pathlib import Path

# 폴더 생성을 위한 상수 설정
# '20260813' 폴더 안에서
BASE = Path(__file__).parent
# "test"라는 폴더를 만들기 설정
DATA = BASE / "test_data"
# 폴더 생성
DATA.mkdir(exist_ok=True)

# 파일 생성
top100 = DATA / "top100.txt"

# 빈 리스트
song_ls = []


# 입력값 등록을 위한 함수
def write_txt(list):
    # 파일 생성 후 자료 넣기
    with open(top100, "w", encoding="utf-8") as f:
        for ls in list:  # noqa: FURB122
            # "\n" -> 줄바꿈
            f.write(f"{ls}\n")


while True:
    # while로 반복해서 입력 받기
    input_datas = input("곡명과 아티스트 입력하기: ")
    if input_datas == "end":
        # "end" 입력시
        print("입력을 종료합니다")
        # 종료
        break
    else:
        # 입력값들을 리스트에 추가
        song_ls.append(input_datas)

print(song_ls)
write_txt(song_ls)


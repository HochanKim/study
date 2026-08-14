# -----------------------------
# 파일 다루기 - 경로부터 CSV까지
# -----------------------------


# ── 필요한 도구 가져오기 ──────────────────────────────────
# pathlib : 경로를 다루는 도구 (파이썬에 기본 내장)
# csv     : CSV 파일을 다루는 도구 (파이썬에 기본 내장)
# os      : 운영체제 관련 도구
#
# 이 셋은 설치가 필요 없습니다. import 만 하면 바로 씁니다.
from pathlib import Path
import csv
import os


# # ============================================================
# #                    1 부 .  경    로
# # ============================================================

# # ---------------------------------------------------------
# # 1-1. 경로란 무엇인가
# # -------------------------------------------------------------
# #
# # 경로(path)는 '파일이 어디 있는지 알려주는 주소' 입니다.
# #
# #   C:\Users\hong\Documents\보고서.txt
# #
# #  드라이브    폴더들          파일 이름
# #
# #
# # [두 가지 종류]
# #
# #   ① 절대경로 - 처음부터 끝까지 다 적은 것
# #      C:/Users/hong/Documents/보고서.txt
# #
# #      장점: 어디서 실행하든 항상 같은 파일을 가리킴
# #      단점: 다른 컴퓨터에서는 안 됨 (사용자 이름이 다르니까)
# #
# #   ② 상대경로 - 지금 있는 위치를 기준으로 적은 것
# #      data/보고서.txt
# #
# #      장점: 짧고 편함. 다른 컴퓨터에서도 작동
# #      단점: '지금 있는 위치'가 어디냐에 따라 달라짐   ← 여기서 문제 발생
# #
# #
# # 대부분 상대경로를 씁니다. 그런데 "지금 있는 위치"가 뭘까요?
# # 이게 초보자가 가장 많이 막히는 지점입니다.

# print("=" * 60)
# print(" 1-1. 경로의 두 종류")
# print("=" * 60)
# print("""
#   절대경로   C:/Users/hong/Documents/보고서.txt    (전체 주소)
#   상대경로   data/보고서.txt                       (현재 위치 기준)
# """)


# # ---------------------------------------------------------
# # 1-2. 함정: "현재 위치"는 내 파일 위치가 아닐 수 있다
# # -------------------------------------------------------------
# #
# # 파이썬이 "data.txt 열어줘" 라는 말을 들으면
# # '어느 폴더에서' 찾아야 할지 정해야 합니다.
# #
# # 그 기준이 되는 곳을 '현재 작업 폴더' 라고 합니다.
# # 영어로 current working directory, 줄여서 CWD 입니다.
# #
# #
# #  함정
# #
# #   현재 작업 폴더는 '내 .py 파일이 있는 폴더'가 아닐 수 있습니다!
# #
# #   VS Code 에서 어떤 폴더를 열었는지,
# #   터미널에서 어느 위치에서 실행했는지에 따라 달라집니다.
# #
# #
# # [실제로 이런 일이 벌어집니다]
# #
# #   내 파일 위치      : C:/work/project/main.py
# #   VS Code 로 연 폴더 : C:/work            ← project 가 아니라 work 를 열었음
# #
# #   -> 현재 작업 폴더는 C:/work 가 됩니다
# #   -> main.py 에서 open("data.txt") 를 하면
# #      C:/work/data.txt 를 찾습니다 (project 폴더가 아니라!)
# #   -> 파일이 project 폴더에 있으면 못 찾습니다
# #
# #   이것 때문에 "분명 파일이 옆에 있는데 없다고 나와요" 사태가 생깁니다.
# #   초보자가 몇 시간씩 헤매는 대표적인 원인입니다.

# print("\n" + "=" * 60)
# print(" 1-2. 내 위치 확인하기")
# print("=" * 60)

# print("  현재 작업 폴더 :", os.getcwd())
# print("  이 파일의 위치 :", Path(__file__).parent)

# print("""
#   	 위 두 줄이 다르게 나올 수 있습니다. 그게 정상입니다.

#     직접 실험해 보세요.
#       ① VS Code 에서 이 파일이 있는 폴더를 열고 실행 -> 두 줄이 같음
#       ② 그 상위 폴더를 열고 실행               -> 첫 줄만 바뀜
# """)

# # [용어 설명]
# #
# #   os.getcwd()        현재 작업 폴더를 알려줌
# #                      (get current working directory 의 줄임말)
# #
# #   __file__           지금 실행 중인 .py 파일의 경로
# #                      파이썬이 자동으로 만들어 주는 변수입니다
# #                      앞뒤에 밑줄 두 개가 붙은 건 '특별한 변수'라는 표시
# #
# #   Path(__file__)     그 경로를 Path 객체로 만든 것
# #                      문자열보다 다루기 편해집니다
# #
# #   .parent            그 파일이 들어 있는 '폴더'
# #                      부모(parent) 폴더라는 뜻


# # ---------------------------------------------------------
# # 1-3. 해결책: 항상 '이 파일 기준'으로 경로를 잡는다
# # -------------------------------------------------------------
# #
# # ★★★ 이 세 줄을 외우세요 ★★★
# #
# #   BASE = Path(__file__).parent      # 이 .py 파일이 있는 폴더
# #   DATA = BASE / "data"              # 그 안의 data 폴더
# #   DATA.mkdir(exist_ok=True)         # 없으면 만들기
# #
# # 이렇게 하면 어디서 실행하든 항상 같은 곳을 가리킵니다.
# # 앞으로 파일을 다루는 모든 코드는 이렇게 시작하세요.
# # 나중에 pandas 로 CSV 를 읽을 때도 똑같이 씁니다.

# print("\n" + "=" * 60)
# print(" 1-3. 기준 폴더 정하기")
# print("=" * 60)

BASE = Path(__file__).parent  # 이 파일이 있는 폴더
DATA = BASE / "data"  # 그 안에 data 폴더
DATA.mkdir(exist_ok=True)  # 폴더 만들기

# print("  기준 폴더  :", BASE)
# print("  데이터 폴더:", DATA)
# print(" 이제 어디서 실행하든 항상 같은 곳을 가리킵니다")

# # [mkdir 옵션 설명]
# #
# #   DATA.mkdir()
# #     폴더를 만든다. 이미 있으면 FileExistsError 발생!
# #
# #   DATA.mkdir(exist_ok=True)              ← 이걸 쓰세요
# #     이미 있으면 그냥 넘어간다
# #
# #   DATA.mkdir(parents=True, exist_ok=True)
# #     중간 폴더까지 다 만든다
# #     예) a/b/c 를 만들 때 a, b 도 없으면 함께 생성


# # ---------------------------------------------------------
# # 1-4. 함정: 윈도우의 역슬래시(\) 문제
# # -------------------------------------------------------------
# #
# # 윈도우 경로는 역슬래시를 씁니다.
# #
# #   C:\work\data.txt
# #
# # 그런데 파이썬에서 역슬래시는 '특수 기호'입니다.
# #
# #   \n  줄바꿈
# #   \t  탭
# #   \\  역슬래시 자체
# #
# # 그래서 이렇게 쓰면 문제가 생깁니다.
# #
# #   "C:\work\new.txt"
# #         ↑    ↑
# #        \w   \n   ← \n 이 줄바꿈으로 해석됨!
# #
# #   경로가 "C:\work" + 줄바꿈 + "ew.txt" 가 되어 버립니다.
# #
# #
# # [해결 방법 3가지]
# #
# #   ① pathlib 사용           ← 가장 권장
# #      Path("C:/work") / "new.txt"
# #
# #   ② 슬래시(/)로 쓰기
# #      "C:/work/new.txt"
# #      윈도우도 슬래시를 알아듣습니다
# #
# #   ③ 문자열 앞에 r 붙이기 (raw string)
# #      r"C:\work\new.txt"
# #      r 이 붙으면 역슬래시를 특수 기호로 안 봅니다

# print("\n" + "=" * 60)
# print(" 1-4. 역슬래시 함정 직접 보기")
# print("=" * 60)

# print("  '경로\\new.txt' 를 출력하면:")
# print("   >>>", "경로\new.txt")  # \n 이 줄바꿈으로 해석됨
# print()
# print("  r'경로\\new.txt' 를 출력하면:")
# print("   >>>", r"경로\new.txt")  # r 을 붙이면 그대로 나옴

# print("""
#    위쪽은 줄이 바뀌어 버렸죠? 경로가 깨진 겁니다.

#    결론: pathlib 을 쓰면 이런 고민이 필요 없습니다.
#     게다가 윈도우/맥/리눅스에서 알아서 맞춰줍니다.
# """)


# #  ---------------------------------------------------------
# # 1-5. pathlib 으로 경로 다루기
# # -------------------------------------------------------------
# #
# # Path 객체는 슬래시(/)로 이어 붙일 수 있습니다.
# # 나눗셈이 아니라 '경로 연결'로 동작합니다.
# #
# #   DATA / "memo.txt"        ->  .../data/memo.txt
# #   BASE / "sub" / "a.txt"   ->  .../sub/a.txt

# print("\n" + "=" * 60)
# print(" 1-5. 경로 조립하고 정보 꺼내기")
# print("=" * 60)

# file_path = DATA / "memo.txt"  # / 로 이어 붙이기

# print("  전체 경로 :", file_path)
# print("  파일 이름 :", file_path.name)  # memo.txt
# print("  확장자    :", file_path.suffix)  # .txt
# print("  이름만    :", file_path.stem)  # memo
# print("  상위 폴더 :", file_path.parent)
# print("  존재하나? :", file_path.exists())  # 아직 안 만들었으니 False

# # [자주 쓰는 Path 기능 정리]
# #
# #   ── 경로 만들기 ──
# #     Path("폴더") / "파일.txt"    경로 이어 붙이기
# #
# #   ── 정보 꺼내기 ──
# #     .name        파일 이름 (확장자 포함)     report.csv
# #     .stem        확장자 뺀 이름              report
# #     .suffix      확장자                      .csv
# #     .parent      상위 폴더
# #
# #   ── 확인하기 ──
# #     .exists()    있는지 확인
# #     .is_file()   파일인지
# #     .is_dir()    폴더인지
# #
# #   ── 조작하기 ──
# #     .mkdir()     폴더 만들기
# #     .rename()    이름 바꾸기 / 옮기기
# #     .unlink()    파일 삭제 (되돌릴 수 없음!)


# # ---------------------------------------------------------
# # 1-6. 폴더 안의 파일 목록 보기
# # -------------------------------------------------------------
# #
# # 폴더에 쌓인 파일 100개를 한 번에 처리하려면
# # 먼저 목록을 가져와야 합니다.
# #
# #   .iterdir()      폴더 안의 모든 것
# #   .glob("패턴")   패턴에 맞는 것만
# #
# #
# # [glob 패턴 규칙]
# #
# #   *          아무 글자나 0개 이상
# #   ?          아무 글자 하나
# #
# #   *.csv           모든 csv 파일
# #   report*         report 로 시작하는 모든 파일
# #   *2026*          이름에 2026 이 들어간 파일
# #   report_?월.txt   report_1월.txt, report_2월.txt ... (한 글자만)

# print("\n" + "=" * 60)
# print(" 1-6. 파일 목록 다루기")
# print("=" * 60)

# # 실습을 위해 파일 몇 개를 만들어 둡니다 (내용은 2부에서 자세히)
# for name in ["report_1월.txt", "report_2월.txt", "report_3월.txt", "note.md"]:
#     with open(DATA / name, "w", encoding="utf-8") as f:
#         f.write(f"{name} 의 내용입니다\n")

# print("  [data 폴더 전체]")
# for p in sorted(DATA.iterdir()):  # sorted 로 이름순 정렬
#     print("     ", p.name)

# print("\n  [txt 파일만]  glob('*.txt')")
# for p in sorted(DATA.glob("*.txt")):
#     print("     ", p.name)

# print("\n  [report 로 시작]  glob('report*')")
# for p in sorted(DATA.glob("report*")):
#     print("     ", p.name)

# #   실무 활용
# #   월별 보고서 100개가 쌓인 폴더에서
# #   glob("report_*.csv") 하나로 전부 가져올 수 있습니다.
# #   파일 이름을 손으로 100개 적을 필요가 없습니다.


# # ============================================================
# #                2 부 .  텍 스 트  파 일
# # ============================================================

# #  ---------------------------------------------------------
# # 2-1. 파일 쓰기 - open 과 with
# # -------------------------------------------------------------
# #
# # [기본 문법]
# #
# #   with open(경로, 모드, encoding="utf-8") as f:
# #       f.write("내용")
# #
# #
# # [모드 - 세 가지만 알면 됩니다]
# #
# #   "r"  읽기(read)     파일을 읽기만 함. 기본값
# #   "w"  쓰기(write)    ★파일이 있으면 내용을 전부 지우고★ 새로 씀
# #   "a"  추가(append)   기존 내용 뒤에 이어 붙임
# #
# #   ★★ "w" 주의 ★★
# #     중요한 파일을 "w" 로 여는 순간 내용이 전부 사라집니다.
# #     되돌릴 수 없습니다. 이어 붙이려면 반드시 "a" 를 쓰세요.
# #
# #
# # [encoding="utf-8" 을 꼭 쓰세요]
# #
# #   컴퓨터는 글자를 숫자로 저장합니다. => 0과 1로만 이루어진 컴퓨터
# #   그 '변환 규칙'이 인코딩입니다.
# #
# #   문제는 규칙이 여러 개라는 것입니다.
# #     utf-8    전 세계 표준. 한글도 잘 됩니다
# #     cp949    옛날 윈도우 한국어 방식
# #
# #   쓸 때와 읽을 때 규칙이 다르면 글자가 깨집니다.
# #   그래서 항상 utf-8 로 통일하는 게 안전합니다.
# #
# #   encoding 을 안 쓰면 파이썬이 알아서 정하는데,
# #   윈도우에서는 cp949 를 고르는 경우가 있어 문제가 생깁니다.
# #
# #
# # [with 를 쓰는 이유]
# #
# #   파일을 열면 반드시 닫아야 합니다. 안 닫으면
# #     - 다른 프로그램이 그 파일을 못 씁니다
# #     - 쓴 내용이 저장이 안 될 수도 있습니다
# #
# #   with 를 쓰면 블록이 끝날 때 자동으로 닫힙니다
# #   중간에 에러가 나도 닫힙니다.
# #
# #   [with 없이 쓰면 - 권장하지 않음]
# #     f = open(경로, "w", encoding="utf-8")
# #     f.write("내용")
# #     f.close()          ← 이걸 깜빡하면 문제 발생
# #
# #
# # [as f 의 의미]
# #   열린 파일을 f 라는 이름으로 부르겠다는 뜻입니다.
# #   f 대신 다른 이름을 써도 되지만 관례상 f 를 많이 씁니다.

# print("\n" + "=" * 60)
# print(" 2-1. 파일 쓰기")
# print("=" * 60)

memo = DATA / "memo.txt"

with open(memo, "w", encoding="utf-8") as f:
    f.write("첫 번째 줄입니다\n")  # \n 을 직접 넣어야 줄이 바뀜
    f.write("두 번째 줄입니다\n")
    f.write("세 번째 줄입니다\n")

print(f"  '{memo.name}' 파일을 만들었습니다")
print("   VS Code 왼쪽 탐색기에서 data 폴더를 열어 확인해 보세요")

#  \n 을 빼먹으면?
#   f.write("첫줄") 과 f.write("둘째줄") 을 연달아 쓰면
#   "첫줄둘째줄" 이 되어 버립니다.
#   print 와 달리 write 는 줄바꿈을 자동으로 넣지 않습니다.


# #  ---------------------------------------------------------
# # 2-2. 파일 읽기 - 세 가지 방법
# # -------------------------------------------------------------
# print("\n" + "=" * 60)
# print(" 2-2. 파일 읽기")
# print("=" * 60)

# ── 방법 1) read() : 파일 전체를 하나의 문자열로
with open(memo, "r", encoding="utf-8") as f:
    content = f.read()

# print("  [방법1 - read()]")
# print(content)
# print("  자료형:", type(content).__name__)
# print("  -> 파일 전체가 문자열 하나로 들어옵니다")

# ── 방법 2) readlines() : 줄 단위 리스트로
with open(memo, "r", encoding="utf-8") as f:
    lines = f.readlines()

# print("\n  [방법2 - readlines()]")
# print("   ", lines)
# print("  -> 각 줄 끝에 \\n 이 그대로 붙어 있는 것에 주의!")
# print("  줄 수:", len(lines))

# ── 방법 3) for 문으로 한 줄씩   ← 실무에서 가장 많이 씀
print("\n  [방법3 - for 문]")
with open(memo, "r", encoding="utf-8") as f:
    line_no = 1
    for line in f:
        print(f"    {line_no}번째 줄: {line.strip()}")
        line_no += 1

# #   방법 3이 좋은 이유
# #   파일이 아무리 커도 한 줄씩만 메모리에 올립니다.
# #   read() 로 1GB 파일을 읽으면 메모리에 1GB 를 통째로 올려서
# #   컴퓨터가 멈출 수도 있습니다.
# #
# #   strip() 이 뭔가요?
# #   문자열 앞뒤의 공백과 줄바꿈을 없애줍니다.
# #     "  안녕  \n".strip()   ->   "안녕"
# #   파일을 읽으면 줄 끝에 \n 이 붙어 오므로 거의 항상 씁니다.
# #
# #   비슷한 것들
# #     .strip()    앞뒤 모두
# #     .lstrip()   왼쪽(앞)만
# #     .rstrip()   오른쪽(뒤)만


# #  ---------------------------------------------------------
# # 2-3. 이어쓰기 모드 "a" => append 역할
# # -------------------------------------------------------------
# print("\n" + "=" * 60)
# print(" 2-3. 이어쓰기")
# print("=" * 60)

# 파일명 memo에 "나중에 추가한 줄 (-> 줄바꿈)"을 추가
with open(memo, "a", encoding="utf-8") as f:  # "a" = append
    f.write("나중에 추가한 줄\n")

# 파일명 memo를 읽어오기
with open(memo, "r", encoding="utf-8") as f:
    print(f.read())

# print("""
#    "w" 와 "a" 의 차이를 꼭 기억하세요

#     "w" 로 열면   기존 내용이 전부 사라지고 새로 씀
#     "a" 로 열면   기존 내용 뒤에 이어 붙임

#     실무 예시
#     로그 파일에 기록을 쌓을 때  ->  "a"
#     결과 파일을 새로 만들 때    ->  "w"
# """)


# ---------------------------------------------------------
# 2-4. 파일이 없을 때
# -------------------------------------------------------------
#
# 없는 파일을 열려고 하면 FileNotFoundError 가 납니다.
# 대응 방법이 두 가지 있습니다.

print("\n" + "=" * 60)
print(" 2-4. 없는 파일 다루기")
print("=" * 60)

ghost = DATA / "없는파일.txt"

# ── 방법 1) 미리 확인하기
print("  [방법1 - exists() 로 미리 확인]")
if ghost.exists():
    with open(ghost, "r", encoding="utf-8") as f:
        print(f.read())
else:
    print(f"     {ghost.name} 은(는) 없습니다")

# ── 방법 2) try / except
print("\n  [방법2 - try/except]")
try:
    with open(ghost, "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print(f"     {ghost.name} 을(를) 찾을 수 없습니다")


# 어느 쪽을 쓸까요
# 보통 방법 2를 권합니다.
#   - 확인하는 순간과 여는 순간 사이에 파일이 사라질 수도 있음
#   - 권한 문제 등 exists() 로는 못 잡는 상황도 있
# 다만 "있으면 읽고 없으면 새로 만든다" 같은 경우엔
# exists() 로 미리 확인하는 게 읽기 좋습니다.


# # ---------------------------------------------------------
# # 2-5. 안전하게 읽는 함수 만들기
# # -------------------------------------------------------------
# # 앞으로 계속 쓸 수 있게 함수로 만들어 둡시다.

print("\n" + "=" * 60)
print(" 2-5. 재사용 가능한 함수로")
print("=" * 60)


def read_text(path, default=""):
    # 파일을 읽어 문자열로 돌려준다. 없으면 default를 돌려준다
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return default


def read_lines(path):
    # 파일을 읽어 줄 리스트로 돌려준다 (줄바꿈 제거). 없으면 빈 리스트
    try:
        with open(path, "r", encoding="utf-8") as f:
            result = []
            for line in f:
                result.append(line.strip())
            return result
    except FileNotFoundError:
        return []


def write_lines(path, lines):
    # 줄 리스트를 파일로 저장한다
    with open(path, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")
    return path


print("  있는 파일 :", read_lines(memo))
print("  없는 파일 :", read_lines(ghost), " <- 에러 대신 빈 리스트")

# diary = write_lines(
#     DATA / "diary.txt",
#     [
#         "2026-01-01 새해 첫날",
#         "2026-01-02 회사 첫 출근",
#         "2026-01-03 야근",
#     ],
# )
# print("  새로 만든 파일 :", diary.name)


# ---------------------------------------------------------
# 2-6. 실전: 여러 파일을 한 번에 처리하기
# -------------------------------------------------------------
#
# 1부에서 배운 glob 과 2부에서 배운 파일 읽기를 합칩니다.

print("\n" + "=" * 60)
print(" 2-6. 여러 파일 한꺼번에 읽기")
print("=" * 60)

total_lines = 0
success = 0
failed = []

for p in sorted(DATA.glob("*.txt")):
    try:
        lines = read_lines(p)  # 함수 read_lines 가져오기
        total_lines += len(lines)  # 변수 lines에 저장된 자료 개수를 더하기
        success += 1  # 성공 횟수 체크
        print(f"     {p.name}: {len(lines)}줄")
    except Exception as e:
        # 모든 에러를 잡아서 기록하고 다음 파일로
        failed.append((p.name, str(e)))

print(f"\n  총 {success}개 파일, {total_lines}줄")


if failed:
    print("  실패한 파일:")
    for name, reason in failed:
        print(f"     {name}: {reason}")

#   핵심 패턴
#   for 안에 try 를 넣으면, 파일 하나가 깨져 있어도
#   나머지는 정상 처리됩니다.
#   3부, 4부에서 이 패턴을 계속 씁니다.


# ---------------------------------------------------------
# 2-7. 파일 정리 - 이름 변경과 삭제
# -------------------------------------------------------------
print("\n" + "=" * 60)
print(" 2-7. 파일 관리")
print("=" * 60)

temp = DATA / "임시파일.txt"

# 만들기
with open(temp, "w", encoding="utf-8") as f:
    f.write("곧 지워질 파일\n")
print("  만들었습니다:", temp.name)

# 이름 바꾸기
renamed = DATA / "이름변경됨.txt"
temp.rename(renamed)
print("  이름을 바꿨습니다:", renamed.name)

# 삭제하기
renamed.unlink()
print("  삭제했습니다")


# 삭제 주의
# unlink() 는 휴지통을 거치지 않고 ★바로 영구 삭제★ 됩니다.
# 복구할 수 없습니다.
# 실무에서는 삭제 코드를 쓰기 전에 반드시
#   ① 경로를 print 해서 확인하고
#   ② 백업을 만들고
#   ③ 그 다음에 실행하세요
# rename 은 '옮기기'로도 쓸 수 있습니다
#   (DATA / "a.txt").rename(BASE / "백업" / "a.txt")
# 단, 대상 폴더가 미리 있어야 합니다.


# ============================================================
#                     3 부 .  C S V
# ============================================================

# ---------------------------------------------------------
# 3-1. CSV 란 무엇인가
# -------------------------------------------------------------
#
# CSV = Comma Separated Values (쉼표로 구분된 값)
#
# 이름이 거창하지만 그냥 텍스트 파일 입니다.
# 2부에서 배운 방법으로 열면 내용이 다 보입니다.
#
#
# [생긴 모습]
#
#   이름,부서,연봉
#   김철수,영업,4500
#   이영희,개발,5200
#
#   - 첫 줄은 보통 '헤더' (열 이름)
#   - 한 줄이 한 건의 데이터 (엑셀의 한 행)
#   - 쉼표가 칸 구분 (엑셀의 셀 경계)
#
#
# [엑셀 파일(.xlsx)과 뭐가 다른가요?]
#
#   xlsx : 서식, 수식, 차트, 여러 시트가 들어간 복잡한 압축 파일
#          메모장으로 열면 깨진 글자만 나옵니다
#
#   csv  : 그냥 글자. 서식도 수식도 없음
#          가볍고, 어떤 프로그램에서든 읽을 수 있습니다
#
#     그래서 프로그램끼리 데이터를 주고받을 땐 CSV 를 씁니다.
#     엑셀에서도 "다른 이름으로 저장 > CSV" 로 만들 수 있습니다.

print("\n" + "=" * 60)
print(" 3-1. 실습용 CSV 만들기")
print("=" * 60)

e_file = DATA / "employees.csv"

# 2부에서 배운 파일 쓰기로 CSV 를 만들어 봅니다
rows = [
    "이름,부서,연봉,입사년도",
    "김철수,영업,4500,2019",
    "이영희,개발,5200,2020",
    "박민수,개발,4800,2021",
    "최지은,영업,5100,2018",
    "정하늘,인사,4200,2022",
]

with open(e_file, "w", encoding="utf-8") as f:
    for items in rows:  # noqa: FURB122
        f.write(items + "\n")

print(f"  '{e_file.name}' 생성 완료")

# 직접 확인해 보세요
#  ① VS Code 탐색기에서 data 폴더 > employees.csv 클릭
#     -> 글자 그대로 보입니다
#  ② 같은 파일을 엑셀로 열어보세요
#     -> 표로 보입니다

# 같은 파일인데 프로그램에 따라 다르게 보이는 겁니다.


#  ---------------------------------------------------------
# 3-2. 방법 1: 손으로 쪼개기 (split)
# -------------------------------------------------------------
#
# 2부에서 배운 파일 읽기 + 문자열 나누기만으로 해봅니다.
#
# split(",") 은 문자열을 쉼표 기준으로 잘라 리스트로 만듭니다.
#
#   "김철수,영업,4500".split(",")
#   ->  ['김철수', '영업', '4500']

print("\n" + "=" * 60)
print(" 3-2. split 으로 직접 파싱하기")
print("=" * 60)

with open(e_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# 첫 줄은 헤더
header = lines[0].strip().split(",")
print("  열 이름:", header)

# 두 번째 줄부터가 데이터
print("\n  [데이터]")
for line in lines[1:]:  # [1:] = 1번 인덱스부터 끝까지
    parts = line.strip().split(",")
    print("     ", parts)


# 벌써 불편한 점들이 보입니다
#  ① strip() 으로 줄바꿈을 매번 직접 지워야 함
#  ② lines[1:] 처럼 헤더를 직접 건너뛰어야 함
#  ③ 모든 값이 문자열 -> 연봉을 더하려면 일일이 int() 변환
#  ④ parts[2] 처럼 '번호'로 접근해야 함
#     (연봉이 몇 번째였더라? 열 순서가 바뀌면 코드가 다 틀어짐)


# ---------------------------------------------------------
# 3-3. split 의 결정적 한계
# -------------------------------------------------------------
#
# 값 안에 쉼표가 들어 있으면 어떻게 될까요?
#
# CSV 규칙에서는 이럴 때 값을 따옴표로 묶습니다.
#
#   홍길동,"서울시 강남구, 테헤란로",5000
#          └────────┬──────────┘
#            이 전체가 하나의 값
#
# 그런데 split(",") 은 따옴표를 이해하지 못합니다.

print("\n" + "=" * 60)
print(" 3-3. split 이 실패하는 경우")
print("=" * 60)

tricky = '홍길동,"서울시 강남구, 테헤란로",5000'

print("  원본:", tricky)
print("  split 결과:", tricky.split(","))
print(f"  -> 칸이 3개여야 하는데 {len(tricky.split(','))}개가 되었습니다!")
print()

# 쉼표(',')는 흔히 들어간다.
# => split(",") 만으로 제대로 처리하기 힘들다
# => 그래서 파이썬에서 'CSV 모듈'이 따로 있는거다


#  ---------------------------------------------------------
# 3-4. 방법 2: csv 모듈의 reader
# -------------------------------------------------------------
#
# [문법]
#
# import csv

with open(e_file, "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)  # row 는 리스트
#
#
# [newline="" 이 뭔가요?]
#
#   csv 모듈을 쓸 때의 약속입니다. 안 쓰면 윈도우에서
#   빈 줄이 하나씩 끼어 들어가는 문제가 생깁니다.
#   이유를 깊이 알 필요는 없습니다.
#   "csv 모듈을 쓸 땐 newline='' 을 붙인다" 로 외우세요.

print("\n" + "=" * 60)
print(" 3-4. csv.reader")
print("=" * 60)

with open(e_file, "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print("     ", row)


# split 과 비교해서 달라진 점
# - strip() 을 안 써도 줄바꿈이 알아서 처리됨
# - 따옴표 안의 쉼표를 제대로 인식함
# - 각 줄이 자동으로 리스트가 됨


# 따옴표 처리를 직접 확인해 봅시다
ingan_file = DATA / "ingan.csv"
with open(ingan_file, "w", encoding="utf-8", newline="") as f:
    f.write("이름,주소,연봉\n")
    f.write('홍길동,"서울시 강남구, 테헤란로",5000\n')

print("  [따옴표 안에 쉼표가 있어도]")
with open(ingan_file, "r", encoding="utf-8", newline="") as f:
    for row in csv.reader(f):
        print(f"      {row}  -> 칸 {len(row)}개")


# ---------------------------------------------------------
# 3-5. 방법 3: DictReader   이걸 쓰세요
# -------------------------------------------------------------
# csv.reader 는 각 줄을 '리스트'로 줍니다.
#   row[0], row[1], row[2] ...
#   -> 몇 번째가 뭐였는지 기억해야 합니다
#
# csv.DictReader 는 각 줄을 '딕셔너리'로 줍니다.
#   row["이름"], row["부서"], row["연봉"]
#   -> 훨씬 읽기 쉽고, 열 순서가 바뀌어도 안전합니다
#
# 첫 줄을 자동으로 헤더로 인식해서 키로 씁니다.

print("\n" + "=" * 60)
print(" 3-5. csv.DictReader")
print("=" * 60)

with open(e_file, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)  # 첫 줄을 헤더로 자동 인식
    for row in reader:
        print(f"{row['이름']} / {row['부서']} / {row['연봉']}만원")

# 한 줄이 실제로 어떻게 생겼는지 보겠습니다
print("\n  [한 줄의 실제 모습]")
with open(e_file, "r", encoding="utf-8", newline="") as f:
    # csv 값들 리스트에 담기
    bin_ls = []
    for row in csv.DictReader(f):
        bin_ls.append(row)
        print("     ", row)
        print("      자료형:", type(row).__name__)
        # break  # 첫 줄만 보고 중단
    print(bin_ls)


#  딕셔너리를 배운 게 여기서 쓰입니다.
#  DictReader 는 한 줄을 딕셔너리로 바꿔줍니다.
#    {'이름': '김철수', '부서': '영업', '연봉': '4500', ...}
#  => 앞으로는 DictReader 를 기본으로 쓰세요.


#  ---------------------------------------------------------
# 3-6. ★중요★  CSV 의 모든 값은 문자열이다
# -------------------------------------------------------------
#
# 이걸 모르면 반드시 한 번은 당합니다.
#
#   "4500" + "5200"  ->  "45005200"   (문자열 이어붙이기!)
#   4500 + 5200      ->  9700          (원하는 결과)
#
# CSV 파일에는 자료형 정보가 없습니다. 그냥 글자만 있죠.
# 그래서 파이썬은 전부 문자열로 읽어옵니다.
# 계산하려면 반드시 int()나 float()로 바꿔야 합니다. (형변환 필수)

# print("\n" + "=" * 60)
# print(" 3-6. 문자열 vs 숫자")
# print("=" * 60)

# print("  '4500' + '5200' =", "4500" + "5200", "   <- 이어붙이기!")
# print("  4500 + 5200     =", 4500 + 5200, "   <- 제대로 된 덧셈")

# print("\n  [CSV 에서 읽은 값의 자료형 확인]")
with open(e_file, "r", encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        print(f"연봉 값: {row['연봉']!r} 자료형: {type(row['연봉']).__name__}")
        break


# !r 은 값을 따옴표까지 포함해서 보여줍니다.
#'4500' 처럼 따옴표가 보이면 문자열, 4500 이면 숫자입니다.

# 매번 파일 열고 변환하는 코드를 쓰면 번거롭습니다.
# 함수로 만들어 두면 한 줄로 끝납니다.


def to_int(value, default=0):
    # 문자열을 정수로 바꾼다, 실패하면 default로 바꾼다
    try:
        return int(str(value).strip())
    except (ValueError, TypeError):
        return default


def read_csv(path, encoding="utf-8"):
    # CSV를 읽어 딕셔너리 리스트로 돌려준다. 없으면 빈 리스트
    try:
        with open(path, "r", encoding=encoding, newline="") as f:
            rows = []
            for row in csv.DictReader(f):
                rows.append(row)
    except FileExistsError:
        pass
    return rows


def load_e(path):
    # 직원 CSV를 읽고 숫자 항목을 변환해서 돌려준다
    rows = read_csv(path)
    for row in rows:
        row["연봉"] = to_int(row["연봉"])
        row["입사년도"] = to_int(row["입사년도"])
    return rows


e_list = load_e(e_file)
print(f"{len(e_list)}명의 데이터를 읽었습니다")
print(f"첫 번째 사람: {e_list[0]}")
print("연봉의 자료형:", type(e_list[0]["연봉"]).__name__, " <- 이제 숫자!")
print()

# salaries = []
# for e in e_list:
#     salaries.append(e["연봉"])

# print("연봉 목록:", salaries)
# print("인원     :", len(salaries), "명")
# print("합계     :", sum(salaries), "만원")
# print("평균     :", round(sum(salaries) / len(salaries), 1), "만원")
# print("최고     :", max(salaries), "만원")
# print("최저     :", min(salaries), "만원")


# 필터링 작업
# print("개발팀만 호출하기")
# for e in e_list:
#     if e["부서"] == "개발":
#         print(f"{e['이름']} - {e['연봉']}만 원")
# print()

# print("연봉 5000 이상")
# for e in e_list:
#     if e["연봉"] >= 5000:
#         print(f"{e['이름']}(소속 부서:{e['부서']}) {e['연봉']}만 원")
# print()

# ============================================================
#                    4 부 .  실    전
# ============================================================

# 4-1. ★핵심★ 그룹별로 묶기
# -------------------------------------------------------------
#
# 이게 데이터 분석의 기본 동작입니다.
#
# [하고 싶은 일]
# 부서별로 인원, 연봉 합계, 평균을 구하기
#
# [방법]
# 딕셔너리를 '누적 통'으로 쓰면 됩니다.
# - 처음 보는 부서면 0으로 시작
# - 이미 본 부서면 기존 값에 더하기

# 빈 딕셔너리 생성
dept_total = {}
dept_count = {}

for e in e_list:
    dept = e["부서"]
    pay = e["연봉"]
    # .get(키 0)은 키가 없으면 0으로 돌려준다
    dept_total[dept] = dept_total.get(dept, 0) + pay
    dept_count[dept] = dept_count.get(dept, 0) + 1

print(f"{'부서':<6}{'인원':>4}{'평균':>10}")


# for dept in dept_total:
#     avg = dept_total[dept] / dept_count[dept]
#     print(f"{dept:<6}{dept_count[dept]:>4}{dept_total[dept]:>9}{avg:>10.1f}")


# ---------------------------------------------------------
# 집계 함수로 만들기
# ---------------------------------------------------------
# 같은 코드를 상품별, 지점별에도 쓸 수 있게 함수로 뺍니다.


def sum_by(rows, group_key, value_key):
    # """
    # group_key 별로 value_key 를 합산한 딕셔너리를 돌려준다
    # rows      : 딕셔너리 리스트
    # group_key : 묶을 기준 키   (예: "부서")
    # value_key : 합산할 값의 키 (예: "연봉")
    # """
    result = {}
    for row in rows:
        key = row[group_key]
        result[key] = result.get(key, 0) + row[value_key]
    return result


def count_by(rows, group_key):
    # """group_key 별 개수를 센 딕셔너리를 돌려준다"""
    result = {}
    for row in rows:
        key = row[group_key]
        result[key] = result.get(key, 0) + 1
    return result


def make_bar(value, unit=1000, mark="■"):
    # """숫자를 막대그래프 문자열로 만든다"""
    return mark * int(value / unit)


by_dept = sum_by(e, "부서", "연봉")
cnt_dept = count_by(e, "부서")

print("  [부서별 연봉 합계]")
for dept, total in by_dept.items():
    print(f"     {dept:<5}{total:>7}만원  ({cnt_dept[dept]}명)  {make_bar(total, 500)}")

# 같은 함수를 입사년도별로도 쓸 수 있습니다
print("\n  [입사년도별 인원]")
by_year = count_by(e, "입사년도")
for year in sorted(by_year):
    print(f"     {year}년: {by_year[year]}명  {make_bar(by_year[year], 1, '●')}")

# print("""
#   ★ 함수로 만들어 두니 부서별, 연도별에 그대로 재사용됩니다.
#     이게 함수를 만드는 이유입니다.
# """)


#  ---------------------------------------------------------
# 4-3. CSV 쓰기 - 그리고 엑셀 한글 깨짐 문제
# -------------------------------------------------------------
#
# [문법]
#
#   with open(경로, "w", encoding="utf-8-sig", newline="") as f:
#       writer = csv.writer(f)
#       writer.writerow(["열1", "열2"])       # 한 줄 쓰기
#       writer.writerows([[1, 2], [3, 4]])    # 여러 줄 한 번에
#
#
# ★★★ encoding="utf-8-sig" 에 주목하세요 ★★★
#
#   그냥 "utf-8" 로 저장하면
#   엑셀에서 열 때 한글이 깨집니다
#
#   [왜 그럴까요?]
#     엑셀은 파일을 열 때 "이거 무슨 인코딩이지?" 를 스스로 추측합니다.
#     그런데 한국어 윈도우에서는 cp949 라고 잘못 찍는 경우가 많습니다.
#
#   [utf-8-sig 는 뭐가 다른가요?]
#     파일 맨 앞에 아주 작은 표시를 붙입니다. (BOM 이라고 부릅니다)
#     "나는 UTF-8이야" 라는 이름표 같은 겁니다.
#     엑셀이 그걸 보고 제대로 열어줍니다.
#
#
#   [정리]
#     읽을 때        encoding="utf-8"
#     엑셀용 저장    encoding="utf-8-sig"
#
#   실무에서 "왜 엑셀로 열면 글자가 깨지죠?" 의 99%가 이것 때문입니다.

# print("\n" + "=" * 60)
# print(" 4-3. 결과를 CSV 로 저장하기")
# print("=" * 60)

# result_file = DATA / "부서별_집계.csv"

# with open(result_file, "w", encoding="utf-8-sig", newline="") as f:
#     writer = csv.writer(f)

#     writer.writerow(["부서", "인원", "연봉합계", "평균연봉"])  # 헤더

#     for dept in by_dept:
#         avg = round(by_dept[dept] / cnt_dept[dept], 1)
#         writer.writerow([dept, cnt_dept[dept], by_dept[dept], avg])

# print(f"  '{result_file.name}' 저장 완료")
# print("   이 파일을 엑셀로 열어보세요. 한글이 안 깨집니다.")

# # 저장한 파일 확인
# print("\n  [저장된 내용]")
# with open(result_file, "r", encoding="utf-8-sig", newline="") as f:
#     for row in csv.reader(f):
#         print("     ", row)

# #    읽을 때도 utf-8-sig 로 열었습니다.
# #   utf-8 로 열면 첫 번째 값 앞에 이상한 글자가 붙어 보입니다.
# #   (BOM 표시가 그대로 읽히기 때문)


# # ---------------------------------------------------------
# # 4-4. DictWriter 로 저장하기
# # -------------------------------------------------------------
# #
# # DictReader 로 읽었으면, 쓸 때도 DictWriter 가 편합니다.
# # 열 이름을 지정하면 순서를 알아서 맞춰줍니다.

# print("\n" + "=" * 60)
# print(" 4-4. DictWriter")
# print("=" * 60)


# def save_csv(path, rows, fieldnames, encoding="utf-8-sig"):
#     """딕셔너리 리스트를 CSV 로 저장한다"""
#     with open(path, "w", encoding=encoding, newline="") as f:
#         writer = csv.DictWriter(f, fieldnames=fieldnames)
#         writer.writeheader()  # 헤더 자동 작성
#         writer.writerows(rows)  # 여러 줄 한 번에
#     return Path(path)


# new_people = [
#     {"이름": "신입A", "부서": "개발", "연봉": 3800},
#     {"이름": "신입B", "부서": "영업", "연봉": 3600},
#     {"이름": "신입C", "부서": "인사", "연봉": 3500},
# ]

# new_file = save_csv(DATA / "신입사원.csv", new_people, ["이름", "부서", "연봉"])

# print(f"  '{new_file.name}' 저장 완료")
# with open(new_file, "r", encoding="utf-8-sig") as f:
#     print(f.read())

# # [fieldnames 설명]
# #   어떤 열을 어떤 순서로 쓸지 지정합니다.
# #   딕셔너리에 이 목록에 없는 키가 있으면 에러가 납니다.
# #   반대로 목록에 있는데 딕셔너리에 없으면 빈 칸이 됩니다.


# #  ---------------------------------------------------------
# # 4-5. 실전: 지저분한 데이터 정리하기
# # -------------------------------------------------------------
# #
# # 실제 데이터는 절대 깨끗하지 않습니다.
# # 실무에서 흔히 만나는 문제들입니다.
# #
# #   - 값 앞뒤에 공백이 있음      " 4500 "
# #   - 값이 비어 있음             ""
# #   - 숫자 자리에 글자가 있음     "오천"
# #   - 단위가 붙어 있음           "4,500원"
# #
# # 이걸 어떻게 처리하느냐가 실무 능력입니다.

# print("\n" + "=" * 60)
# print(" 4-5. 지저분한 데이터 다루기")
# print("=" * 60)

# dirty = DATA / "dirty.csv"
# with open(dirty, "w", encoding="utf-8", newline="") as f:
#     f.write("이름,연봉\n")
#     f.write("김철수, 4500 \n")  # 공백이 섞임
#     f.write("이영희,\n")  # 값이 비어 있음
#     f.write("박민수,오천\n")  # 숫자가 아님
#     f.write("최지은,5100\n")  # 정상
#     f.write("정하늘,4200원\n")  # 단위가 붙음

# # ── 1차 시도: to_int 로만 처리
# clean = []
# problems = []

# with open(dirty, "r", encoding="utf-8", newline="") as f:
#     # enumerate(..., start=2) : 2번부터 번호를 매김
#     #   왜 2부터? 1번 줄은 헤더이므로 데이터는 2번 줄부터입니다.
#     #   나중에 "몇 번째 줄이 문제인지" 알려줄 때 씁니다.
#     for line_no, row in enumerate(csv.DictReader(f), start=2):
#         name = row["이름"].strip()
#         raw = row["연봉"].strip()

#         if raw == "":
#             problems.append((line_no, name, "값 없음"))
#             continue  # 다음 줄로

#         try:
#             clean.append({"이름": name, "연봉": int(raw)})
#         except ValueError:
#             problems.append((line_no, name, f"숫자 아님: {raw}"))

# print("  [1차 시도 - 단순 변환]")
# print(f"    정상 {len(clean)}건 / 문제 {len(problems)}건")
# for line_no, name, reason in problems:
#     print(f"      {line_no}번째 줄 {name}: {reason}")


# # ── 2차 시도: 값을 정리하는 함수를 만들어서 더 살려내기
# def clean_number(value, default=None):
#     """단위와 쉼표를 제거하고 숫자만 뽑아낸다

#     '4,500원'  ->  4500
#     ' 30개 '   ->  30
#     '오천'      ->  None (또는 default)
#     """
#     if value is None:
#         return default

#     text = str(value).strip()

#     # 제거할 문자들을 하나씩 없앱니다
#     for remove in [",", "원", "만원", "개", "명", "건", "%", " "]:
#         text = text.replace(remove, "")

#     if text == "":
#         return default

#     try:
#         return int(text)
#     except ValueError:
#         return default


# print("\n  [clean_number 함수 테스트]")
# print("     ' 4500 '   ->", clean_number(" 4500 "))
# print("     '4,500원'  ->", clean_number("4,500원"))
# print("     '4200원'   ->", clean_number("4200원"))
# print("     '오천'      ->", clean_number("오천"))
# print("     ''         ->", clean_number(""))

# # 2차 처리
# recovered = []
# still_bad = []

# with open(dirty, "r", encoding="utf-8", newline="") as f:
#     for line_no, row in enumerate(csv.DictReader(f), start=2):
#         name = row["이름"].strip()
#         n = clean_number(row["연봉"])
#         if n is None:
#             still_bad.append((line_no, name, row["연봉"]))
#         else:
#             recovered.append({"이름": name, "연봉": n})

# print("\n  [2차 시도 - clean_number 적용]")
# print(f"    정상 {len(recovered)}건 / 문제 {len(still_bad)}건")
# for r in recovered:
#     print("     ", r)

# print(f"\n   1차에서 {len(clean)}건이던 게 {len(recovered)}건으로 늘었습니다.")
# print("    '4200원' 이 살아났습니다. 정리 함수를 잘 만들면 버리는 데이터가 줄어듭니다.")

# # ── 문제 목록도 파일로 남기기
# err_file = DATA / "오류목록.csv"
# with open(err_file, "w", encoding="utf-8-sig", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["줄번호", "이름", "원본값"])
#     writer.writerows(still_bad)

# print(f"\n  '{err_file.name}' 저장 완료")
# print("""
#   ★ 실무 포인트
#     문제 데이터를 그냥 버리지 마세요.
#     "몇 번째 줄이 왜 문제인지" 목록을 파일로 만들어 두면
#     담당자에게 보내 수정을 요청할 수 있습니다.

#     "10건 중 2건 실패, 목록은 첨부합니다" 라고 보고할 수 있어야 합니다.
# """)


# #  ---------------------------------------------------------
# # 전체 정리
# # -------------------------------------------------------------
# #
# #   1부. 경로
# #   │
# #   │   from pathlib import Path
# #   │
# #   │   BASE = Path(__file__).parent   # 이 파일의 폴더
# #   │   DATA = BASE / "data"           # 데이터 폴더
# #   │   DATA.mkdir(exist_ok=True)      # 없으면 만들기
# #   │
# #   │   DATA.glob("*.csv")             # 파일 목록 찾기
# #
# #
# #   2부. 텍스트 파일
# #   │
# #   │   # 읽기
# #   │   with open(경로, "r", encoding="utf-8") as f:
# #   │       for line in f:
# #   │           print(line.strip())
# #   │
# #   │   # 쓰기
# #   │   with open(경로, "w", encoding="utf-8") as f:
# #   │       f.write("내용\n")
# #
# #
# #   3부. CSV
# #   │
# #   │   import csv
# #   │
# #   │   # 읽기
# #   │   with open(경로, "r", encoding="utf-8",
# #   │             newline="") as f:
# #   │       for row in csv.DictReader(f):
# #   │           print(row["열이름"])
# #   │
# #   │   # 쓰기 (엑셀용)
# #   │   with open(경로, "w", encoding="utf-8-sig",
# #   │             newline="") as f:
# #   │       writer = csv.writer(f)
# #   │       writer.writerow(["열1", "열2"])
# #
# #
# #   4부. 집계
# #   │
# #   │   result = {}
# #   │   for row in rows:
# #   │       key = row["부서"]
# #   │       result[key] = result.get(key, 0) + row["연봉"] │
# #
# #
# #
# #   ★ 반드시 기억할 7가지
# #     1. 경로는 Path(__file__).parent 기준으로 잡는다
# #     2. encoding="utf-8" 을 항상 붙인다 (한글 깨짐 방지)
# #     3. 엑셀로 열 파일은 encoding="utf-8-sig" 로 저장
# #     4. 파일은 with 로 연다 (자동으로 닫힘)
# #     5. "w" 는 기존 내용을 지운다. 이어쓰려면 "a"
# #     6. csv 모듈을 쓸 땐 newline="" 을 붙인다
# #     7. CSV 의 모든 값은 문자열. 계산하려면 int() 변환
# #
# #

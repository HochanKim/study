# """
# ============================================================
#  미니 프로젝트 2 - 도서관 관리 시스템
# ============================================================

#  [예상 소요 시간]  3시간

#  [사용하는 것]
#    클래스, 상속, 캡슐화, 파일 입출력, 예외 처리, CSV

#  [만들 것]
#    도서를 등록하고 대출과 반납을 관리하며
#    기록을 파일로 저장하는 프로그램

#  [진행 방법]
#    단계가 9개로 나뉘어 있습니다. 순서대로 완성하세요.
#    각 단계 아래의 [확인] 코드 주석을 풀어 결과를 맞춰보세요.

#    앞 단계의 클래스를 뒤에서 계속 쓰므로 순서대로 하는 것이 좋습니다.
# ============================================================
# """
from pathlib import Path
import csv

BASE = Path(__file__).parent
DATA = BASE / "data"
DATA.mkdir(exist_ok=True)


# =============================================================
# 1단계. Book 클래스 만들기
# =============================================================
#
# 클래스 이름
#   Book
#
# 만들 때 받을 값
#   book_id   도서번호
#   title     제목
#   author    저자
#   category  분류
#


# 그 외에 필요한 값
#   대출 상태 (처음에는 대출 가능)
#   빌린 사람 이름 (처음에는 없음)
#   누적 대출 횟수 (처음에는 0)
#
# 메서드
#   borrow(who)
#     이미 대출 중이면 False 를 돌려주고 아무것도 하지 않는다
#     빌릴 수 있으면 상태를 바꾸고 누적 횟수를 1 늘린 뒤 True 를 돌려준다
#
#   give_back()
#     대출 중이 아니면 False 를 돌려준다
#     반납하면 상태를 되돌리고 True 를 돌려준다
#
#   is_available()
#     대출 가능하면 True
#
#   show()
#     대출 중일 때  "B001 사피엔스 / 유발 하라리 / 인문 / 대출중(김철수) / 누적 1회"
#     가능할 때     "B001 사피엔스 / 유발 하라리 / 인문 / 대출가능 / 누적 1회"
#
# borrow 와 give_back 이 True/False 를 돌려주는 이유는
# 나중에 Library 클래스에서 성공 여부를 판단하기 위해서입니다.
# -------------------------------------------------------------
# [확인]
class Book:
  def __init__(self, book_id, title, author, category):
    self.book_id = book_id
    self.title = title
    self.author = author
    self.category = category
    #  대출 상태 (처음에는 대출 가능)
    self.rented = "대출 가능"
    #   빌린 사람 이름 (처음에는 없음)
    self.rent_person = ""
    #   총 대출 횟수 (처음에는 0)
    self.rent_cnt = 0

  def borrow(self, who):
    if self.rent_person == "":
      self.rent_person = who
      self.rented = "대출 불가"
      self.rent_cnt += 1
      return True
    else:
      return False
  
  def give_back(self):
    if self.rented == "대출 가능":
      return False
    else:
      self.rented = "대출 가능"
      self.rent_person = ""
      return True
  
  def is_available(self):
    if self.rented == "대출 가능":
      return True
  
  def show(self):
    if self.rented == "대출 불가":
      print(f"{self.book_id} {self.title} / {self.author} / 대출 중 ({self.rent_person}) / 누적 {self.rent_cnt}회")
    elif self.rented == "대출 가능":
      print(f"{self.book_id} {self.title} / {self.author} / 대출 가능 / 누적 {self.rent_cnt}회")

# [출력]
#   B001 사피엔스 / 유발 하라리 / 인문 / 대출가능 / 누적 0회
#   대출 결과: True
#   B001 사피엔스 / 유발 하라리 / 인문 / 대출중(김철수) / 누적 1회
#   재대출 결과: False
#   반납 결과: True
#   B001 사피엔스 / 유발 하라리 / 인문 / 대출가능 / 누적 1회

b = Book("B001", "사피엔스", "유발 하라리", "인문")
b.show()
print("대출 결과:", b.borrow("김철수"))
b.show()
print("재대출 결과:", b.borrow("이영희"))
print("반납 결과:", b.give_back())
b.show()
print()


# =============================================================
# 2단계. EBook 클래스 (상속)
# =============================================================
#
# 클래스 이름
#   EBook       (Book 을 물려받는다)
#
# 만들 때 받을 값
#   Book 이 받는 것에 더해 file_size (MB) 를 받는다
#
# 달라지는 점
#   전자책은 동시에 여러 명이 빌릴 수 있다.
#   그래서 borrow 는 항상 성공하고, 누적 횟수만 늘어난다.
#   대출 상태는 항상 대출 가능이다.
#
# 메서드
#   borrow(who)
#     누적 횟수만 1 늘리고 항상 True 를 돌려준다
#
#   show()
#     "E001 파이썬 입문 / 홍길동 / IT / 전자책(15MB) / 누적 3회" 형태
# -------------------------------------------------------------
# [확인]
class EBook (Book):
  def __init__(self, book_id, title, author, category, file_size):
    super().__init__(book_id, title, author, category)
    self.size = file_size

  def borrow(self, who):
    super().borrow(who)
    if self.rent_person:
      self.rent_person = who
      self.rented = "대출 가능"
      self.rent_cnt += 1
      return True

  def show(self):
      print(f"{self.book_id} {self.title} / {self.author} / {self.category} / {self.size}MB / 누적 {self.rent_cnt}회")

# [출력]
#   E001 파이썬 입문 / 홍길동 / IT / 전자책(15MB) / 누적 0회
#   True
#   True
#   True
#   E001 파이썬 입문 / 홍길동 / IT / 전자책(15MB) / 누적 3회

e = EBook("E001", "파이썬 입문", "홍길동", "IT", 15)
e.show()
print(e.borrow("김철수"))
print(e.borrow("이영희"))
print(e.borrow("박민수"))
e.show()
print()

# =============================================================
# 3단계. Member 클래스
# =============================================================
#
# 클래스 이름
#   Member
#
# 만들 때 받을 값
#   member_id  회원번호
#   name       이름
#
# 그 외에 필요한 값
#   현재 빌린 책 목록 (처음에는 비어 있음)
#   최대 대출 권수는 3권으로 고정
#
# 빌린 책 목록은 밖에서 직접 바꿀 수 없도록 밑줄을 붙여 보관하세요.
#
# 메서드
#   can_borrow()
#     3권 미만이면 True
#
#   add_book(book_id)
#     빌린 목록에 추가한다
#
#   remove_book(book_id)
#     빌린 목록에서 뺀다. 없으면 아무것도 하지 않는다
#
#   get_books()
#     빌린 책 목록을 새 리스트로 돌려준다 (원본이 바뀌면 안 됨)
#
#   show()
#     "M001 김철수 / 대출 2권 / ['B001', 'B002']" 형태
# -------------------------------------------------------------
# [확인]

class Member:
  def __init__(self, member_id, name):
    self.id = member_id
    self.name = name
    # 현재 빌린 책 목록 (처음에는 비어 있음)
    self._book_list = []
    # 대출 권수 (최대 3권)
    self.rented_cnt = 0

  def can_borrow(self):
    if self.rented_cnt >= 3:  # noqa: RUF100, SIM103
      return False
    else:
      return True
    
  def add_book(self, book_id):
    self._book_list.append(book_id)
    self.rented_cnt += 1
    return self._book_list
  
  def remove_book(self, book_id):
    self._book_list.remove(book_id)
    if len(self._book_list) == 0:
      return False
  
  def get_books(self):
    get_ls = []
    for books in self._book_list:
      if len(self._book_list) > 3:
        return False
      get_ls.append(books) 
    return get_ls
  
  def show(self):
    print(f"{self.id} {self.name} / 대출 {len(self._book_list)}권 / {self._book_list}")


# [출력]
#   M001 김철수 / 대출 0권 / []
#   빌릴 수 있나? True
#   M001 김철수 / 대출 3권 / ['B001', 'B002', 'B003']
#   빌릴 수 있나? False
#   목록 복사본 수정 후: ['B001', 'B002', 'B003']

m = Member("M001", "김철수")
m.show()
print("빌릴 수 있나?", m.can_borrow())
m.add_book("B001")
m.add_book("B002")
m.add_book("B003")
m.show()
print("빌릴 수 있나?", m.can_borrow())

copied = m.get_books()
copied.append("B999")
print("목록 복사본 수정 후:", m.get_books())
print()

# =============================================================
# 4단계. Library 클래스 - 기본 틀
# =============================================================
#
# 클래스 이름
#   Library
#
# 만들 때 받을 값
#   name  도서관 이름
#
# 그 외에 필요한 값
#   도서 목록 (딕셔너리. 키는 도서번호, 값은 Book 객체)
#   회원 목록 (딕셔너리. 키는 회원번호, 값은 Member 객체)
#   대출 기록 (리스트. 나중에 파일로 저장할 것)
#
# 메서드
#   add_book(book)
#     도서를 등록한다. 이미 있는 번호면 False, 성공하면 True
#
#   add_member(member)
#     회원을 등록한다. 이미 있는 번호면 False, 성공하면 True
#
#   find_book(book_id)
#     도서를 찾아 돌려준다. 없으면 None
#
#   find_member(member_id)
#     회원을 찾아 돌려준다. 없으면 None
#
#   count()
#     (도서 수, 회원 수) 를 함께 돌려준다
# -------------------------------------------------------------
# [확인]

class Library:
  def __init__(self, name):
    self.name = name
    # 도서 목록
    self.having_book = {}
    # 회원 목록
    self.member = {}
    # 대출 기록
    self.record = []

  def add_book(self, book):
    # 책 추가
    if (book.book_id in self.having_book) is False:
      self.having_book[book.book_id] = book
      print(self.having_book[book.book_id].rented)
      return True
    # 이미 있는 책일 경우 (책 번호 중복 시)
    return False

  def add_member(self, member):
    # 회원 추가
    if (member.id in self.member) is False:
          self.member[member.id] = member
          # print(self.member[member.id].name)
          return True
    # 이미 있는 회원일 경우 (회원 번호 중복 시)
    return False

  def find_book(self, book_id):
    # 도서 찾기
    if (book_id in self.having_book) is True:
      return self.having_book.get(book_id)
    return None
    

  def find_member(self, member_id):
    # 회원 찾기
    if (member_id in self.member) is True:
          return self.member.get(member_id)
    return None

  def count(self):
    # 등록된 책과 회원 수
    books_cnt = len(self.having_book)
    members_cnt = len(self.member)
    return books_cnt, members_cnt

  def borrow(self, member_id, book_id):
    # 대여 여부
    if (member_id in self.member) is False:
      print(f"없는 회원: {member_id}")
      return False

    if (book_id in self.having_book) is False:
      print(f"없는 도서: {book_id}")
      return False

    # 각 클래스의 객체 가져오기
    member = self.member[member_id]
    book = self.having_book[book_id]

    if member.rented_cnt >= 3 :
      print(f"대출 한도 초과: {member.name} (3권)")
      return False

    if book.borrow(member.name):
      # 클래스 Book의 매서드 borrow 호출
      self.detail = {}
      self.detail["구분"] = "대출"
      self.detail["회원"] = member.name
      self.detail["도서"] = book.title

      self.record.append(self.detail)

      print(f"{member.name} -> {book.title} 대출 완료")
      return True
    print(f"이미 대출 중 => {book.title}")
    return False

  def give_back(self, member_id, book_id):
    # 각 클래스의 객체 가져오기
    member = self.member[member_id]
    book = self.having_book[book_id]
    for b in self.record:
      if b.get("도서") == self.having_book.get(book_id).title :
        book.give_back()
        self.record.remove(b)
        print(f"{member.name} -> {book.title} 반납 완료")
        return True
    print(f"빌린 책이 아닙니다: {self.having_book.get(book_id).title}") 
        
    for dicts in self.record:
      if b == {}:
        self.record.remove(dicts)

  def list_books(self, available_only=False):
    print("[중앙도서관 도서 목록]")
    avail_book_cnt = 0
    for book in self.having_book.values():
      if available_only and not book.is_available():
        continue
      book.show()
      avail_book_cnt += 1 
    print(f"총 {avail_book_cnt}권")

  def search(self, keyword):
    return True


    


# [출력]
#   도서 등록: True
#   중복 등록: False
#   도서 수 3, 회원 수 2
#   찾기 성공: 사피엔스
#   찾기 실패: None

lib = Library("중앙도서관")
print("도서 등록:", lib.add_book(Book("B001", "사피엔스", "유발 하라리", "인문")))
print("중복 등록:", lib.add_book(Book("B001", "다른책", "다른저자", "인문")))
lib.add_book(Book("B002", "총균쇠", "재레드 다이아몬드", "인문"))
lib.add_book(EBook("E001", "파이썬 입문", "홍길동", "IT", 15))
lib.add_member(Member("M001", "김철수"))
lib.add_member(Member("M002", "이영희"))

books, members = lib.count()
print(f"도서 수 {books}, 회원 수 {members}")
print("찾기 성공:", lib.find_book("B001").title)
print("찾기 실패:", lib.find_book("B999"))


# =============================================================
# 5단계. 대출과 반납 처리
# =============================================================
#
# Library 클래스에 메서드를 추가하세요.
#
#   borrow(member_id, book_id)
#     아래 순서로 확인하고, 실패하면 이유를 출력한 뒤 False 를 돌려준다
#
#       회원이 없으면      "없는 회원: M999"
#       도서가 없으면      "없는 도서: B999"
#       3권을 다 빌렸으면   "대출 한도 초과: 김철수 (3권)"
#       이미 대출 중이면    "이미 대출 중: 사피엔스"
#
#     성공하면
#       책과 회원 정보를 갱신하고
#       대출 기록에 남긴 뒤
#       "김철수 -> 사피엔스 대출 완료" 를 출력하고 True 를 돌려준다
#
#     대출 기록은 딕셔너리로 남기세요.
#       {"구분": "대출", "회원": "김철수", "도서": "사피엔스"}
#
#   give_back(member_id, book_id)
#     회원이나 도서가 없으면 위와 같이 처리한다
#     그 회원이 빌린 책이 아니면 "빌린 책이 아닙니다: 사피엔스"
#     성공하면 기록을 남기고 "김철수 -> 사피엔스 반납 완료" 출력
#
#   ※ 전자책(EBook)은 여러 명이 빌릴 수 있으므로
#     "이미 대출 중" 검사에 걸리지 않아야 합니다.
#     is_available() 이 항상 True 를 돌려주면 자연스럽게 해결됩니다.
# -------------------------------------------------------------
# [확인]
# [출력]
#   김철수 -> 사피엔스 대출 완료
#   이미 대출 중: 사피엔스
#   없는 회원: M999
#   없는 도서: B999
#   김철수 -> 파이썬 입문 대출 완료
#   이영희 -> 파이썬 입문 대출 완료
#   김철수 -> 사피엔스 반납 완료
#   빌린 책이 아닙니다: 총균쇠

print()
lib.borrow("M001", "B001")
lib.borrow("M002", "B001")
lib.borrow("M999", "B001")
lib.borrow("M001", "B999")
lib.borrow("M001", "E001")
lib.borrow("M002", "E001")
lib.give_back("M001", "B001")
lib.give_back("M001", "B002")
print()

# =============================================================
# 6단계. 조회 기능
# =============================================================
#
# Library 클래스에 메서드를 추가하세요.
#
#   list_books(available_only=False)
#     도서 목록을 출력한다
#     available_only 가 True 면 대출 가능한 것만 출력한다
#
#       [중앙도서관 도서 목록]
#         B001 사피엔스 / 유발 하라리 / 인문 / 대출가능 / 누적 1회
#         ...
#       총 3권
#
#   search(keyword)
#     제목이나 저자에 keyword 가 들어간 도서 리스트를 돌려준다
#     대소문자는 구분하지 않는다
#
#   by_category()
#     분류별 권수를 딕셔너리로 돌려준다
#     {"인문": 2, "IT": 1}
#
#   most_borrowed(n=3)
#     누적 대출 횟수가 많은 순으로 n 권을 돌려준다
# -------------------------------------------------------------
# [확인]
lib.list_books()
print()
# lib.borrow("M002", "B001")
lib.list_books(available_only=True)
# print()
# print("검색 '파이썬':", [b.title for b in lib.search("파이썬")])
# print("분류별:", lib.by_category())
# print("인기 도서:", [(b.title, b.borrow_count) for b in lib.most_borrowed(2)])


# =============================================================
# 7단계. CSV 로 저장하기
# =============================================================
#
# Library 클래스에 메서드를 추가하세요.
#
#   save_books(path)
#     도서 목록을 CSV 로 저장한다
#     열: 도서번호, 제목, 저자, 분류, 상태, 누적대출
#     상태는 "대출가능" 또는 "대출중" 으로 적는다
#     저장한 파일 경로를 돌려준다
#
#   save_history(path)
#     대출 기록을 CSV 로 저장한다
#     열: 구분, 회원, 도서
#     기록이 없으면 헤더만 저장한다
#
#   ※ 엑셀에서 한글이 깨지지 않게 저장해야 합니다.
#     어떤 encoding 을 써야 할까요?
# -------------------------------------------------------------
# [확인]
# [출력]
#   저장 완료: books.csv
#   저장 완료: history.csv
#   ['도서번호', '제목', '저자', '분류', '상태', '누적대출']
#   ['B001', '사피엔스', '유발 하라리', '인문', '대출가능', '1']
#   ...

# p1 = lib.save_books(DATA / "books.csv")
# print("저장 완료:", p1.name)
# p2 = lib.save_history(DATA / "history.csv")
# print("저장 완료:", p2.name)
#
# with open(DATA / "books.csv", "r", encoding="utf-8-sig", newline="") as f:
#     for row in csv.reader(f):
#         print(row)


# =============================================================
# 8단계. CSV 에서 불러오기
# =============================================================
#
# Library 클래스에 메서드를 추가하세요.
#
#   load_books(path)
#     CSV 에서 도서를 읽어 등록한다
#     파일이 없으면 "파일이 없습니다: books.csv" 를 출력하고
#     0 을 돌려준다
#     읽은 도서 수를 돌려준다
#
#     한 줄이라도 이상하면 그 줄만 건너뛰고 계속 진행한다
#     (예: 누적대출 자리에 숫자가 아닌 값이 들어있는 경우)
#     건너뛴 줄은 "3번째 줄 오류: ..." 형태로 출력한다
#
#   ※ 여기서 예외 처리가 필요합니다.
#     파일이 없을 때와 값이 이상할 때를 각각 처리하세요.
# -------------------------------------------------------------
# [확인]
# [출력]
#   파일이 없습니다: 없는파일.csv
#   불러온 도서: 0권
#   불러온 도서: 3권
#   새 도서관 도서 수: 3

# lib2 = Library("분관")
# print("불러온 도서:", lib2.load_books(DATA / "없는파일.csv"), "권")
# print("불러온 도서:", lib2.load_books(DATA / "books.csv"), "권")
# books, members = lib2.count()
# print("새 도서관 도서 수:", books)


# =============================================================
# 9단계. 종합 리포트
# =============================================================
#
# Library 클래스에 메서드를 추가하세요.
#
#   report()
#     아래 형태의 리포트를 출력한다
#
#       ============================================
#        중앙도서관 운영 리포트
#       ============================================
#       도서 3권 / 회원 2명
#       대출 가능 2권 / 대출 중 1권
#
#       [분류별]
#         인문 2권
#         IT 1권
#
#       [인기 도서]
#         1. 파이썬 입문 (2회)
#         2. 사피엔스 (1회)
#
#       [회원 현황]
#         M001 김철수 / 대출 1권
#         M002 이영희 / 대출 1권
#
#       [최근 기록]
#         대출 김철수 -> 사피엔스
#         ...
#       ============================================
#
#     최근 기록은 마지막 5건만 보여주세요.
#     앞에서 만든 메서드들을 재사용하세요.
# -------------------------------------------------------------
# [확인]
# lib.report()


# =============================================================
# 도전 과제 (시간이 남으면)
# =============================================================
#
# 1) 메뉴가 있는 프로그램으로 만들기
#      1. 도서 목록    2. 도서 검색    3. 대출
#      4. 반납         5. 리포트       6. 저장 후 종료
#
# 2) 연체 기능 추가하기
#    Book 에 대출일을 기록하고,
#    14일이 지나면 연체로 표시하세요.
#    datetime 모듈을 쓰면 됩니다.
#
# 3) 회원 등급 만들기
#    VipMember 클래스를 만들어 최대 대출 권수를 5권으로 하세요.
#    Library 의 borrow 는 고치지 않아도 동작해야 합니다.
#    (can_borrow 만 덮어쓰면 됩니다)
# -------------------------------------------------------------
# -------------------------------------------------------------
# import란 무엇인가? (가져오기)
# -------------------------------------------------------------

# "이미 누가 만든 코드를 가져다 쓰겠다" (import: 가져오다)

# [왜 필요한가?]
# -> 프로그래밍의 어느 원칙 => "바퀴를 다시 발명하지 마라"

# 제곱근 계산, 날짜 처리, 무작위 숫자 뽑기
# 이미 전 세계 개발자들이 만들어 둔 것이 있다 => 이걸 가져다 쓰는 게 'import'

# [가져올 수 있는 코드는 세 종류]

# 1) 표준 라이브러리
#   => 파이썬을 설치하면 자동으로 딸려온다
#   => math, random, csv, datetime, os, pathlib 등
#   => import만 하면 바로 쓸 수 있다

# 2) 외부 패키지
#   => 따로 설치해야 한다
#   => pandas, numpy, matplotlib, requests 등
#   => pip install로 설치한 뒤 import 한다

# 3) 내가 만든 파일
#   => 같은 폴더에 있는 내 .py 파일
#   => my_tools.py 같은 거
#   => 파일 이름으로 import하여 가져오기 가능

# 세 가지 모두 import하는 방법은 똑같다

# 만약 math 없이 제곱근을 직접 구하려면 복잡한 계산이 필요하다
# 하지만 import 한 줄이면 끝난다

# # 방법1) 통째로 가져오기
# # import '모듈 이름'
# # 쓸 때는 항상 '모듈 이름.함수 이름'으로 사용
# import math # math 가져오기

# print("16의 제곱근:", math.sqrt(16))
# print("원주율:", round(math.pi, 4))
# print("2의 10제곱:", math.pow(2, 10))
# print("올림:", math.ceil(3.2))
# print("내림", math.floor(3.8))


# # 방법2) 별칭 붙이기
# # import '모듈 이름' as 짧은 이름 (별칭 사용)
# # 모듈 이름이 길면 짧게 줄여 사용이 가능

# import math as m
# print(m.sqrt(16))


# 방법3) 특정 함수만 콕 집어 오기
# from 모듈 이름 import 함수 이름
# 모듈 이름 없이 바로 쓸 수 있다


# -------------------------------------------------------------
# 어떤 걸 사용해야 하나
# -------------------------------------------------------------

# import math -> math.sqrt()  //  안전하고 명확, 기본적
# import pandas as pd // 이름이 길 때 (ex. pd.read_csv)
# import from math import sqrt  //  짧지만 위험할 수 있음
# => [from ... import가 왜 위험한가?]
# ====> pow = 100 // 같은 이름의 변수를 만듦 => pow(2, 3) <- 에러가 발생, 숫자를 함수처럼 부르게 됨

# 모듈 이름을 붙여쓰면 (math.pow) 이런 충돌이 생기지 않는다

# 코드를 읽을 때도 차이가 난다
# sqrt(16) <- 이게 어디서 온 함수? // math.sqrt(16) <- math에서 왔구나


# # [별칭(as)은 언제 쓰나?]
# # => 데이터 분석에서는 별칭이 '사실상 표준'이다

# # import pandas as pd
# # imoprt numpy as np
# # import matplotlib.pyplot as plt 등등

# # 전 세계 모든 개발자들이 쓰는 관례이므로
# # 다르게 쓰지 않는다

# import random as rd

# print("주사위 굴리기:", rd.randint(1, 6))
# print("무작위 선택:", rd.choice(["김밥", "라면", "돈까스"]))

# my_list = [1, 2, 3, 4, 5]
# rd.shuffle(my_list) # 리스트 순서를 섞음
# print("섞은 리스트:", my_list)
# print("중복 없이 6개:", sorted(rd.sample(range(1, 46), 6)))


# -------------------------------------------------------------
# import하면 정확히 무슨 일이 일어나나?
# -------------------------------------------------------------

# import my_tools를 실행하면 팡치썬은 이렇게 한다.
# 1) my_tools.py 파일을 찾는다
#   => 찾는 순서: 현재 폴더 -> 파이썬 설치 폴더 -> 패키지 폴더

# 2) 그 파일을 위해서 아래로 한 번 실행한다
#   => def문들이 실행되면서 함수가 메모리에 등록된다
#   ====> 여기서 중요한 건 2번
#   ====> 파일을 실행한다? => my_tools.py 안에 print문이 있으면 실행된다

# 3) my_tools라는 이름으로 사용할 수 있게 한다


# # -------------------------------------------------------------
# # 설치 없이 바로 쓰는 것들
# # -------------------------------------------------------------

# import datetime
# import os

# today = datetime.date.today()
# now = datetime.datetime.now()

# print("날짜와 시간")
# print("오늘 날짜:", today)
# print("현재 시각:", now)
# print("현재 시각:", now.strftime("%H시 %M분"))

# # 요일 구하기 (0 = 월요일, 6= 일요일)
# week = ["월", "화", "수", "목", "금", "토", "일"]
# # print(today.weekday(), "뭐지?")
# print("오늘은?:", week[today.weekday()], "요일")

# # 날짜 계산
# tomorrow = today + datetime.timedelta(days=1)
# next_week = today + datetime.timedelta(days=7)

# # timedelta 없이 내일, 다음주, 다다음주 계산
# import datetime

# today = datetime.date.today()

# # def future(year, month, day):
# #   future_date = datetime.date(year=year, month=month, day=day)
# #   return future_date

# # print(future(2026, 8, 19))
# # print(future(2026, 8, 25))
# # print(future(2026, 9, 1))

# def future(today, next_num):
#   next_day_ordinal = today.toordinal() + next_num
#   next_day = datetime.date.fromordinal(next_day_ordinal)
#   return next_day

# print(future(today, 1))
# print(future(today, 7))
# print(future(today, 14))

# [자주 쓰는 표준 라이브러리]
# math: 수학 계산 (제곱근, 올림, 내림)
# random: 무작위 (뽑기, 섞기, 난수)
# csv: CSV 파일 읽고 쓰기
# pathlib: 경로 다루기
# os: 운영체제 기능
# json: JSON 데이터 (웹에서 많이 쓰는 형식)
# re: 문자열 패턴 찾기

# -------------------------------------------------------------
# 2. 같은 폴더의 파일 불러오기
# -------------------------------------------------------------

# 같은 폴더에 있는 my_tools.py를 가져오기
# ※ 중요: .py를 빼고 파일 이름만 쓴다 => import my_tools (O)

import my_tools

# 모듈 안의 변수도 가져다 쓸 수 있다
print("모듈 버전:", my_tools.VERSION)
print("작성자:", my_tools.AUTHOR)

print("\n [숫자 변환 함수들]")
print(" to_int(' 4500 ') =", my_tools.to_int(" 4500 "))
print(" to_int('사천오백') =", my_tools.to_int("사천오백"), "<= 실패하면 기본값 반환")
print(" to_int('사천오백', -1) =", my_tools.to_int("사천오백", -1), "<= 실패하면 -1로 반환")
print(" clean_number('4,500원') =", my_tools.clean_number("4,500원"))

print("\n [통계 함수들]")
print(" get_average([90, 85, 100]) =", my_tools.get_average([90, 85, 100]))
print(" find_max([3, 9, 1]) =", my_tools.find_max([3, 9, 1]))
print(" find_min([3, 9, 1]) =", my_tools.find_min([3, 9, 1]))

# -------------------------------------------------------------
# 3. 내 모듈에도 별칭 적용 가능
# -------------------------------------------------------------

import my_tools as mt

from my_tools import make_bar, format_money
print("\n [골라오기]")
print("make_bar(5000) =", make_bar(5000))
print("make_bar(5000) =", format_money(12345))
print("\n [골라오기]")


# -------------------------------------------------------------
# 4. __name__ 의 정체
# -------------------------------------------------------------
# import하면 그 파일이 한 번 실행된다
# 그런데 파일 내 테스트 코드 등이 있는데 다 실행되면 곤란하다
# 그걸 막는 게 이 블록

# if __name__ == "__main__":
#     테스트 코드

# [원리]
# 파이썬 파일마다 '__name__'이라는 변수를 자동으로 생성
# 직접 실행한 파일 -> '__name__'은 "__main__"
# import된 파일 -> '__name__'은 파일 이름
# "지금 내가 직접 실행된 건가?"를 알 수 있다

# 앞 뒤 밑줄 두 개는 무슨 뜻?
# => 파이썬을 특별하게 다루는 이름이라는 표시
# => '__name__', '__file__' 등등
# => 직접 만들 일은 거의 없고 있는걸 읽기만 하면 된다

print(__name__)
print("my_tools의 '__name__':", my_tools.__name__)

# 지금 실행 중인 파일은 -> "__main__"
# if __name__ == "__main__":
#     print("자체 테스트")

# 터미널에서 my_tools.py를 실행하면
# "테스트 출력이 나온다"

# -------------------------------------------------------------
# 5. 모듈 만들 때 규칙
# -------------------------------------------------------------

# 1) 관련 있는 함수끼리 모아둔다
# => 숫자 변환끼리, 통계끼리, 파일 처리끼리 등등

# 2) 각 함수에 설명을 단다
# => def 바로 아래에 설명을 쓴다
# => 'docstring'이라고 한다

# 3) 실행 코드는 if __name__ = "__main__": 안에 넣는다

# 4) 파일 맨 위에는 이 파일이 뭔지 적는다

# [docstring]이 좋은 이유
# - help()로 설명을 볼 수 있다
# - VS code에서 함수 이름에 마우스를 올리면 설명이 뜬다


# -------------------------------------------------------------
# 6. pip 외부 패키지 설치
# -------------------------------------------------------------

# pandas, numpy는 파이썬에 딸려오지 않는다 => 직접 설치 필요
# 설치는 파이썬 코드가 아닌 터미널에서

# [자주 쓰는 pip 명령어]

# pip install pandas -> 설치
# pip install pandas numpy -> 여러 개 한번에
# pip install pandas==2.0.0 -> 특정 버전 설치
# pip list -> 설치된 목록 보기
# pip show pandas -> 정보 보기
# pip install --upgrade pandas -> 최신으로 업데이트
# pip uninstall pandas -> 삭제


# [윈도우에서 pip가 안 먹힐 때]
# python -m pip install pandas => 이렇게 쓰면 대부분 해결된다
#  "지금 실행 중인 파이썬의 pip를 쓰겠다"는 뜻
# 파이썬이 여러 개 깔려 있을 때 특히 중요

# [회사 컴퓨터에서 설치 안 될 때]
# 사내망 방화벽에 막혀있을 수 있다
# IT팀, 보안팀에 문의하거나 프록시 설정 필요


# -------------------------------------------------------------
# 6. 가상 환경
# -------------------------------------------------------------

# 프로젝트마다 별도의 작은 환경을 만든다
# 각 환경은 서로 완전히 독립적

# python -m venv venv -> 가상환경 만들기


# -------------------------------------------------------------
# 7. import가 안될 때 체크리스트
# -------------------------------------------------------------
# ModuleNotFoundError: No module named 'pandas' 
# => 이 에러를 만나면 위에서부터 코드 확인 
# => 대부분 5번이 원인

# 1) 설치를 했는가?
# => 터미널에서 pip list로 목록을 확인

# 2) 이름을 정확히 썼는가?
# => 대소문자 구분
# => Pandas(X)
# => NumPy(X)

# 3) 내 파일 이름이 패키지 이름과 같지 않은가?
# => 자주 발생하는 실수
# => 내 파일을 random.py로 저장하고 import random을 가져오면 파이썬이 내 파일을 가져온다
# => csv.py, json.py, math.py 등도 마찬가지
# => 기존 모듈과 다른 파일 이름으로 사용 (ex. my_random,py 등)

# 4) 같은 폴더에 있는가?
# => 내가 만든 모듈일 때 해당
# => my_tools.py가 이 파일과 같은 폴더에 있어야 한다

# 5) 파이썬이 여러 개 깔려 있지 않은가?
# => 가장 흔한 원인
# => A 파이썬을 설치했는데 B 파이썬으로 실행하는 경우
# 해결방법
# => VS CODE 오른쪽 하단, cmd 등으로 파이썬 버전 확인
# => Ctrl + Shift + P => "Python: Select Interpreter" 선택
# => 또는 설치할 때 이렇게 쓰기 / python -m pip install pandas

# -------------------------------------------------------------
# 8. import가 안될 때 체크리스트
# -------------------------------------------------------------

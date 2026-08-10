# 주의
# `except:` 단독 사용이나 `except Exception:` 남발은 실무에서 지양합니다.
# 어디서 무엇이 잘못됐는지 묻히기 때문입니다. 잡을 예외를 명시적으로 지정하세요.
# ---

# # 문제 1. 서버 로그 분석기

# 운영 서버 로그를 파싱해서 에러 리포트를 뽑는 모듈을 만듭니다.
# 실제 로그에는 항상 깨진 줄이 섞여 있습니다. 한 줄 때문에 전체 분석이 멈추면 안 됩니다.

# ## 입력 데이터

# ```python
# logs = [
#     "2026-08-05 10:12:01|INFO|api.order|주문 생성 성공",
#     "2026-08-05 10:12:04|ERROR|api.payment|카드 승인 실패",
#     "2026-08-05 10:13:22|WARN|api.order|재고 부족 경고",
#     "2026-08-05 10:15:40|ERROR|api.payment|타임아웃",
#     "2026-08-05 10:16:03|ERROR|api.auth|토큰 만료",
#     "2026-08-05 10:18:55|INFO|api.auth|로그인 성공",
#     "잘못된 로그 라인",
#     "2026-08-05 10:20:11|ERROR|api.payment",
#     "",
# ]
# ```

# ## 데이터 규격

# - 로그 한 줄의 형식은 `시간|레벨|모듈|메시지` 이며 구분자는 `|` 입니다.
# - 메시지 안에는 `|` 가 들어가지 않습니다. 따라서 `split("|")` 결과의 길이가 정확히 4 여야 정상입니다.
# - 줄 번호는 1번부터 셉니다.
# - `level` 값은 `INFO`, `WARN`, `ERROR` 세 종류입니다.

# ## 구현할 함수

# | 함수 | 설명 |
# |---|---|
# | `parse_line(line)` | 한 줄을 `{"time", "level", "module", "msg"}` 딕셔너리로 변환.<br>필드 개수가 4가 아니면 `ValueError` 를 `raise` 한다 |
# | `parse_logs(lines)` | 각 줄에 `parse_line` 을 호출하되 `try / except ValueError` 로 감싸 실패한 줄은 건너뛴다.<br>`(성공_레코드_리스트, 실패_줄번호_리스트)` 튜플 반환 |
# | `count_by(records, key)` | 지정한 키를 기준으로 개수를 센 딕셔너리 반환 |
# | `top_error_modules(records, n=3)` | `level` 이 `"ERROR"` 인 레코드만 골라 모듈별 개수를 세고,<br>많은 순으로 상위 n개를 `[(모듈명, 개수), ...]` 형태로 반환 |
# | `make_report(lines)` | 위 함수들을 조합해 최종 리포트 딕셔너리 반환 |

# ## 함수 동작 예시

# 아래는 동작 형식을 보여주기 위한 별도 예시입니다. 위 `logs` 데이터의 정답이 아닙니다.

# ```python
# parse_line("2026-01-01 00:00:00|INFO|api.demo|테스트")
# # -> {'time': '2026-01-01 00:00:00', 'level': 'INFO',
# #     'module': 'api.demo', 'msg': '테스트'}

# parse_line("깨진 줄")
# # -> ValueError 발생 (필드 개수 1개)
# ```

# ```python
# sample = [
#     {"level": "INFO",  "module": "api.a"},
#     {"level": "ERROR", "module": "api.a"},
#     {"level": "ERROR", "module": "api.a"},
#     {"level": "ERROR", "module": "api.b"},
# ]

# count_by(sample, "level")
# # -> {'INFO': 1, 'ERROR': 3}

# top_error_modules(sample, n=2)
# # -> [('api.a', 2), ('api.b', 1)]

# top_error_modules(sample, n=5)      # 모듈이 2개뿐이므로 있는 만큼만
# # -> [('api.a', 2), ('api.b', 1)]
# ```

# ## 세부 규칙

# - `top_error_modules` 는 모듈 개수가 n보다 적으면 있는 만큼만 반환합니다.
# - 개수가 같은 모듈끼리의 순서는 채점하지 않습니다.
# - `count_by` 는 레코드에서 값을 꺼낼 때 반드시 `record[key]` 를 사용합니다.
#   `record.get(key)` 를 쓰면 안 됩니다. (아래 요구사항 참고)

# ## 요구사항

# - [ ] `parse_line` 은 잘못된 줄을 직접 처리하지 않는다. `raise` 로 던지고, 건너뛸지 말지는 호출한 쪽(`parse_logs`)이 판단한다 →

# **역할 분리**
# - [ ] `count_by` 는 잘못된 키에 대한 `KeyError` 를 잡지 않는다. `record[key]` 에서 자연스럽게 발생하는 예외를 그대로 위로 전파시킨다.
#       (호출자가 존재하지 않는 키를 넘긴 것은 데이터 문제가 아니라 코드 버그이므로, 조용히 넘어가면 안 되기 때문)
# - [ ] `except:` 단독 사용 금지. 반드시 `except ValueError` 처럼 예외 타입을 명시할 것
# - [ ] `print` 는 마지막 출력부에서만 사용한다. 나머지 모든 함수는 값을 반환할 것

# ## 출력 형식

# 아래 항목이 모두 나오면 됩니다. 서식과 문구는 자유롭게 꾸며도 됩니다.

# ```
# 총 ○줄 중 ○줄 파싱 성공 (실패 ○줄: ○, ○번째 줄)
# 레벨별: INFO ○건 / WARN ○건 / ERROR ○건
# 에러 다발 모듈 TOP: 모듈명(○), 모듈명(○)
# ```

# ## 확인 과제 (제출 코드에는 남기지 않음)

# `count_by(records, "levl")` 처럼 일부러 오타 난 키를 넘겨 보세요.
# 프로그램이 `KeyError: 'levl'` 로 즉시 멈추는 것이 **정상 동작**입니다.
# 왜 이 예외는 잡지 않고 터뜨리는 것이 맞는지 한 문장으로 설명해 보세요.

# ## 심화 과제

# `parse_logs` 에 `strict=False` 기본값 인자를 추가하세요.
# `strict=True` 인 경우 깨진 줄을 건너뛰지 않고 `ValueError` 를 그대로 위로 전달하도록 만듭니다.

# ## 힌트

# - 문자열 분리 후 길이 검사: `parts = line.split("|")` → `len(parts)`
# - 예외 던지기: `raise ValueError("메시지")`
# - 빈 문자열 `""` 를 `split("|")` 하면 `[""]` (길이 1) 이 나옵니다
# - 개수 누적에는 `dict.get(키, 0)` 패턴이 유용합니다
# - 값 기준 정렬에는 `sorted(..., key=..., reverse=True)` 를 사용합니다
# - 딕셔너리를 (키, 값) 쌍으로 순회: `for k, v in counts.items():`
# - 줄 번호와 함께 순회: `for i, line in enumerate(lines, start=1):`
# ---


# # 문제 2. 회원 가입 데이터 정제 (ETL)

# 외부 시스템에서 넘어온 회원 데이터를 DB에 넣기 전에 검증·정제합니다.
# 실패한 데이터는 버리지 말고 사유와 함께 따로 모아 담당자에게 전달해야 합니다.

# ## 입력 데이터

# ```python
# raw_users = [
#     {"name": " 김철수 ", "email": "CHULSOO@Test.COM ", "phone": "010-1234-5678", "age": "28"},
#     {"name": "이영희", "email": "younghee@test.com", "phone": "01098765432", "age": "35"},
#     {"name": "", "email": "noname@test.com", "phone": "010-1111-2222", "age": "40"},
#     {"name": "박민수", "email": "invalid-email", "phone": "010-3333-4444", "age": "22"},
#     {"name": "최지우", "email": "jiwoo@test.com", "phone": "010-5555-6666", "age": "abc"},
#     {"name": "정수진", "email": "sujin@test.com", "phone": "010-777"},
#     {"name": "한동훈", "email": "donghoon@test.com", "phone": None, "age": "31"},
# ]
# ```

# ## 구현할 함수

# | 함수 | 설명 |
# |---|---|
# | `clean_text(value)` | 앞뒤 공백 제거.<br>`None` 등 문자열이 아닌 값이 들어오면 `AttributeError` 가 발생하므로,<br>`try / except AttributeError` 로 잡아 빈 문자열 `""` 를 반환한다 |
# | `normalize_email(email)` | 앞뒤 공백 제거 + 소문자 변환 |
# | `normalize_phone(phone)` | 숫자만 남긴 뒤 `010-1234-5678` 형식의 문자열로 변환.<br>예외를 잡지 않고 그대로 던진다 — 숫자가 11자리가 아니면 `ValueError` 를 `raise`,<br>`None` 이 들어오면 `TypeError` 가 자연 발생 |
# | `to_age(value)` | `int(value)` 변환을 `try / except (ValueError, TypeError)` 로 감싸고,<br>실패하면 `None` 을 반환한다 |
# | `validate(user)` | 회원 1건의 검증 실패 사유를 문자열 리스트로 반환 (통과 시 빈 리스트 `[]`) |
# | `process(raw_users)` | `(성공_리스트, 실패_리스트)` 튜플을 반환 |

# ## 함수 동작 예시

# 아래는 동작 형식을 보여주기 위한 별도 예시입니다. 위 `raw_users` 데이터의 정답이 아닙니다.

# ```python
# clean_text("  홍길동  ")            # -> '홍길동'
# clean_text(None)                   # -> ''          (AttributeError를 잡아 처리)

# normalize_email("  HONG@Test.COM ") # -> 'hong@test.com'

# normalize_phone("01000001111")     # -> '010-0000-1111'
# normalize_phone("010-0000-1111")   # -> '010-0000-1111'
# normalize_phone("010-123")         # -> ValueError 발생 (숫자 6자리)
# normalize_phone(None)              # -> TypeError 발생

# to_age("30")                       # -> 30
# to_age("서른")                      # -> None
# to_age(None)                       # -> None
# ```

# ## 검증 규칙 — `validate(user)`

# 아래 순서대로 검사하고, 해당하는 사유 문자열을 리스트에 순서대로 담습니다.
# 하나가 실패해도 중단하지 말고 끝까지 다 검사합니다.

# | 순서 | 항목 | 검사 방법 | 실패 시 사유 문자열 |
# |---|---|---|---|
# | 1 | 이름 | `clean_text(user.get("name"))` 결과가 빈 문자열이면 실패 | `"이름 없음"` |
# | 2 | 이메일 | `normalize_email` 결과에 `@` 와 `.` 이 둘 다 있어야 통과 | `"이메일 형식 오류"` |
# | 3-a | 나이 | `user["age"]` 접근이 `KeyError` 면 실패 (이때 3-b는 건너뜀) | `"age 항목 누락"` |
# | 3-b | 나이 | `to_age(...)` 결과가 `None` 이면 실패 | `"나이가 숫자가 아님"` |
# | 4-a | 전화번호 | `normalize_phone(...)` 이 `TypeError` 를 던지면 실패 | `"전화번호 값 없음"` |
# | 4-b | 전화번호 | `normalize_phone(...)` 이 `ValueError` 를 던지면 실패 | `"전화번호 자릿수 오류"` |

# > 중요: `phone` 값은 `clean_text` 를 거치지 않고 원본 그대로 `normalize_phone` 에 넘깁니다.
# > (`clean_text` 를 먼저 통과시키면 `None` 이 `""` 으로 바뀌어 "값 없음"과 "자릿수 오류"를 구분할 수 없게 됩니다)

# ## `process` 처리 순서

# 각 회원 1건마다 아래를 반복합니다.

# ```
# 1. reasons = validate(user)
# 2. reasons 가 비어 있으면
#      → 정제된 딕셔너리를 만들어 성공 리스트에 추가
#    비어 있지 않으면
#      → {"data": user, "reasons": reasons} 를 실패 리스트에 추가
# 3. finally 로 "처리 시도" 카운터를 1 증가
# 4. 모두 끝나면 (성공 리스트, 실패 리스트) 를 반환
# ```

# 성공 항목의 딕셔너리 형태 (값은 예시):

# ```python
# {"name": "홍길동", "email": "hong@test.com", "phone": "010-0000-1111", "age": 30}
# ```

# `age` 는 문자열이 아니라 정수여야 합니다.

# ## 요구사항

# - [ ] 데이터 7건 중 한 건이라도 예외로 프로그램이 죽으면 미완성. 끝까지 다 돌아야 한다
# - [ ] `to_age` 처럼 "예외를 잡아서 안전한 값을 반환하는 함수" 와, `normalize_phone` 처럼 "예외를 던지고 판단은 호출자에게 넘기는 함수" 를 의도적으로 구분해 작성할 것
#       → 이 둘의 차이를 말로 설명할 수 있어야 합니다
# - [ ] `finally` 를 활용해 처리 시도 건수를 집계할 것
# - [ ] 정제 함수는 잘게 쪼개고, 조립은 `process` 한 곳에서만 할 것
# - [ ] `except:` 단독 사용 금지

# ## 출력 형식

# 아래 항목이 모두 나오면 됩니다. 서식과 정렬은 자유입니다.
# 회원을 가리키는 식별자는 이름이 있으면 이름, 이름이 비었으면 이메일을 사용합니다.

# ```
# [처리 시도] ○건
# [성공] ○건
# [실패] ○건
#  - 식별자 : 사유1, 사유2
#  - 식별자 : 사유1
# ```

# ## 심화 과제

# 사용자 정의 예외 클래스를 만들어 리팩터링하세요.

# ```python
# class InvalidUserError(Exception):
#     pass
# ```

# `validate` 가 실패 사유를 반환하는 대신 이 예외를 `raise` 하고,
# `process` 에서 `except InvalidUserError as e` 로 잡아 사유를 꺼내도록 구조를 바꿉니다.

# ## 힌트

# - 문자에서 숫자만 골라내려면 `str.isdigit()` 을 활용합니다
# - 문자열 일부를 잘라내려면 슬라이싱 `s[시작:끝]` 을 사용합니다
# - 키 안전 접근: `user.get("name")` / 키 누락을 감지하려면 `try: user["age"] except KeyError:`
# - `try / except / else` 를 쓰면 "예외가 없을 때만" 실행할 코드를 분리할 수 있습니다
# - 사유 누적: `reasons = []` 를 만들고 조건마다 `reasons.append("...")`
# - 튜플 반환과 언패킹: `return ok, ng` → `success, failed = process(raw_users)`
# - 여러 사유를 한 줄로: `", ".join(reasons)`
# - 예외 타입이 헷갈리면 파이썬 셸에서 직접 실행해 확인할 것
# ---

# ## 채점 기준
# | 항목 | 배점 | 확인 포인트 |
# |---|---|---|
# | 함수 분리 | 30 | 하나의 함수가 하나의 역할만 하는가 |
# | 예외 타입 명시 | 20 | `except:` 단독 / `except Exception:` 남발이 없는가 |
# | `try` 블록 범위 | 15 | 예외가 날 수 있는 최소 범위만 감쌌는가 |
# | 반환값 설계 | 20 | 예외를 `print` 로만 흘려보내지 않고 반환값에 반영했는가 |
# | `raise` vs `return None` | 15 | 어느 쪽을 왜 선택했는지 설명할 수 있는가 |
# | 합계 | 100 | |

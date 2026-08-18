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

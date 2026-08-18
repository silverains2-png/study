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

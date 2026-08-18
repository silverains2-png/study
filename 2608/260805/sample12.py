logs = [
    "2026-08-05 10:12:01|INFO|api.order|주문 생성 성공",
    "2026-08-05 10:12:04|ERROR|api.payment|카드 승인 실패",
    "2026-08-05 10:13:22|WARN|api.order|재고 부족 경고",
    "2026-08-05 10:15:40|ERROR|api.payment|타임아웃",
    "2026-08-05 10:16:03|ERROR|api.auth|토큰 만료",
    "2026-08-05 10:18:55|INFO|api.auth|로그인 성공",
    "잘못된 로그 라인",
    "2026-08-05 10:20:11|ERROR|api.payment",
    "",
]


def parse_line(line) -> dict:

    logs_line = line.split("|")

    if len(logs_line) != 4:
        raise ValueError(f"ValueError 발생 (필드 개수 {len(logs_line)}개)")

    result = {
        "time": logs_line[0],
        "level": logs_line[1],
        "module": logs_line[2],
        "msg": logs_line[3],
    }

    return result


def parse_logs(lines) -> tuple:

    suc_record = []
    fail_line = []

    for idx, line in enumerate(lines, start=1):
        try:
            record = parse_line(line)
            suc_record.append(record)

        except ValueError:
            fail_line.append(idx)

    result = (suc_record, fail_line)

    return result


def count_by(records, key) -> dict:

    result = {}

    return result


# | `count_by(records, key)` | 지정한 키를 기준으로 개수를 센 딕셔너리 반환 |
# | `top_error_modules(records, n=3)` | `level` 이 `"ERROR"` 인 레코드만 골라 모듈별 개수를 세고,
# <br>많은 순으로 상위 n개를 `[(모듈명, 개수), ...]` 형태로 반환 |
# | `make_report(lines)` | 위 함수들을 조합해 최종 리포트 딕셔너리 반환 |

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

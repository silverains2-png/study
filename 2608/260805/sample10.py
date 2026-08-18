logs = [
    "INFO",
    "INFO",
    "WARN",
    "INFO",
    "ERROR",
    "INFO",
    "INFO",
    "WARN",
    "INFO",
    "INFO",
    "INFO",
    "INFO",
    "WARN",
    "INFO",
    "INFO",
    "INFO",
    "WARN",
    "ERROR",
    "ERROR",
    "ERROR",
]

warn_count = logs.count("WARN")
error_count = logs.count("ERROR")
error_rate = round(error_count / len(logs) * 100, 1)


print(f"총 로그 : {len(logs)}")
print(f"ERROR : {error_count} / WARN : {warn_count}")
print(f"에러율 : {error_rate:.1f}%")

if logs[-1] and logs[-2] and logs[-3] == "ERROR":
    print("CRITICAL - 연속 장애 감지")
elif error_rate >= 20:
    print("CRITICAL")
elif error_rate >= 10 or warn_count >= len(logs) / 2:
    print("WARNING")
else:
    print("HEALTHY")

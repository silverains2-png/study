from pathlib import Path
import csv
import os

print("\n" + "=" * 60)
print(" 1-3. 기준 폴더 정하기")
print("=" * 60)

BASE = Path(__file__).parent  # 이 파일이 있는 폴더
DATA = BASE / "data"  # 그 안에 data 폴더
DATA.mkdir(exist_ok=True)  # 폴더 만들기

print("  기준 폴더  :", BASE)
print("  데이터 폴더:", DATA)
print(" 이제 어디서 실행하든 항상 같은 곳을 가리킵니다")


print("\n" + "=" * 60)
print(" 1-6. 파일 목록 다루기")
print("=" * 60)

# 실습을 위해 파일 몇 개를 만들어 둡니다 (내용은 2부에서 자세히)
for name in ["report_1월.txt", "report_2월.txt", "report_3월.txt", "note.md"]:
    with open(DATA / name, "w", encoding="utf-8") as f:
        f.write(f"{name} 의 내용입니다\n")

print("  [data 폴더 전체]")
for p in sorted(DATA.iterdir()):  # sorted 로 이름순 정렬
    print("     ", p.name)

print("\n  [txt 파일만]  glob('*.txt')")
for p in sorted(DATA.glob("*.txt")):
    print("     ", p.name)

print("\n  [report 로 시작]  glob('report*')")
for p in sorted(DATA.glob("report*")):
    print("     ", p.name)
print("\n" + "=" * 60)
print(" 2-1. 파일 쓰기")
print("=" * 60)

memo = DATA / "memo.txt"

with open(memo, "w", encoding="utf-8") as f:
    f.write("첫 번째 줄입니다\n")  # \n 을 직접 넣어야 줄이 바뀜
    f.write("두 번째 줄입니다\n")
    f.write("세 번째 줄입니다\n")

print(f"  '{memo.name}' 파일을 만들었습니다")
print("   VS Code 왼쪽 탐색기에서 data 폴더를 열어 확인해 보세요")
#  ---------------------------------------------------------
# 2-2. 파일 읽기 - 세 가지 방법
# -------------------------------------------------------------
print("\n" + "=" * 60)
print(" 2-2. 파일 읽기")
print("=" * 60)

# ── 방법 1) read() : 파일 전체를 하나의 문자열로
with open(memo, "r", encoding="utf-8") as f:
    content = f.read()

print("  [방법1 - read()]")
print(content)
print("  자료형:", type(content).__name__)
print("  -> 파일 전체가 문자열 하나로 들어옵니다")

# ── 방법 2) readlines() : 줄 단위 리스트로
with open(memo, "r", encoding="utf-8") as f:
    lines = f.readlines()

print("\n  [방법2 - readlines()]")
print("   ", lines)
print("  -> 각 줄 끝에 \\n 이 그대로 붙어 있는 것에 주의!")
print("  줄 수:", len(lines))

# ── 방법 3) for 문으로 한 줄씩   ← 실무에서 가장 많이 씀
print("\n  [방법3 - for 문]")
with open(memo, "r", encoding="utf-8") as f:
    line_no = 1
    for line in f:
        print(f"    {line_no}번째 줄: {line.strip()}")
        line_no += 1


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

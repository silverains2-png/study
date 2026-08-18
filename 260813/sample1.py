# input으로 입력을 받을건데 end 가 나올때까지 무한대로 받음
# input("리스트를 입력해 주세요 (end 입력시 종료) : ")
# LOVE ATTACK (리센느), ...
# end 종료

# 파일명 top100 으로 저장

from pathlib import Path

BASE = Path(__file__).parent
DATA = BASE / "test_data"
DATA.mkdir(exist_ok=True)

songs = []

while True:
    song = input("리스트를 입력해 주세요 (end 입력시 종료) : ")

    if song == "end":
        break

    songs.append(song)

FILE = DATA / "top100.txt"

with open(FILE, "w", encoding="utf-8") as f:
    for song in songs:
        f.write(song + "\n")

print("저장완료")

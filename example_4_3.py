from typing import Generator

def iter_odds() -> Generator[int, int, None]:
    i = 1
    while True:
        yield i
        i = i + 2

for num in iter_odds():
    if num > 50:
        break
    print(num)

from typing import Iterator

def iter_odds() -> Iterator[str]:
    i = 1
    while True:
        yield i
        i = i + 2

for num in iter_odds():
    if num > 50:
        break
    print(num)

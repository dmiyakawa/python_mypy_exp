def add1(a, b):
    return a + b


def add2(a: int, b: int) -> int:
    return a + b


def add3(a: str, b: str) -> int:
    return a + b


print(add1(1, 2))
print(add2(1, 2))
print(add3(1, 2))

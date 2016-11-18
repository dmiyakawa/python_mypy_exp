from typing import Generator

def adder_generator(init_i: int) -> Generator[int, int, int]:
    i = init_i
    while True:
        sent_value = yield i
        if not sent_value:
            break
        i = i + sent_value
    return i

gen = adder_generator(10)
try:
    print(next(gen))
    print(gen.send(8))
    print(gen.send(1))
    gen.send(0)
except StopIteration as e:
    print('Last value: {}'.format(e.value))


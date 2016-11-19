from typing import Union


def func(val: Union[int, str]):
    print(val)


val = 10  # type: Union[int, str]

func1(val)

val = 'test'

func1(val)

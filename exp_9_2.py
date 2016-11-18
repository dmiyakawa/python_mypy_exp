from typing import List

def func1() -> List[int]:
    return [1, 2, 3]

def func2(val: str):
    print('Value is : {}'.format(val))

func2(func1())

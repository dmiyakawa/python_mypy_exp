from typing import Union


def get_value() -> Union[int, str]:
    val = input('Input a value: ')
    if val.isdigit():
        return int(val)
    else:
        return val

print(abs(get_value()))

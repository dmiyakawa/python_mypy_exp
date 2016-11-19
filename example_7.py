from typing import Union, List


def append_val(val: Union[int, List[int]]) -> List[int]:
    if isinstance(val, list):
        return val + [1]
    else:
        return [val, 1]
    
lst = append_val(None)

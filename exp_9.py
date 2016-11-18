def func1():
    return [1, 2, 3]

def func2(val: str):
    print('Value is : {}'.format(val))

func2(func1())

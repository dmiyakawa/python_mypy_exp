def func1(val: int):
    print(val)

    
def func2(val: str):
    print(val)

v = 10

func1(v)

del v

v = 'test'

func2(v)

class MyException(Exception):
    pass


exc = None

try:
    print('例外出すなよ！絶対出すなよ！')
    yes = input('例外を出しますか？(はい/yes): ')
    if type(yes):
        exc = MyException('例外！')
    if exc:
        raise exc
except MyException:
    print('はい例外出たー。例外出ちゃったー。')

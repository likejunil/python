"""
. isinstance()
. open()
. read()
. write()
. close()
"""


class A:
    pass


class B(A):
    pass


class C:
    pass


def to_bytes(data) -> bytes:
    if isinstance(data, bytes):
        return data
    elif isinstance(data, str):
        return data.encode('utf-8')
    else:
        return b''


def to_str(data) -> str:
    if isinstance(data, str):
        return str
    elif isinstance(data, bytes):
        return data.decode('utf-8')
    else:
        ''


def check_instance(target) -> None:
    if isinstance(target, range):
        print(f'{target}은 ragne 클래스의 객체이다.')
    elif isinstance(target, object):
        print(f'{target}은 object 클래스의 객체이다.')
    elif isinstance(target, A):
        print(f'{target}은 A 클래스의 객체이다.')
    elif isinstance(target, B):
        print(f'{target}은 B 클래스의 객체이다.')
    elif isinstance(target, C):
        print(f'{target}은 C 클래스의 객체이다.')
    else:
        print(f'{target}은 알 수 없는 클래스의 객체이다.')


if __name__ == '__main__':
    b1 = to_bytes('준일')
    print(b1)
    s1 = to_str(b1)
    print(s1)

    a = A()
    b = B()
    c = C()

    check_instance(range(1, 2))
    check_instance(enumerate("준일", 1))

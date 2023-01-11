from typing import Union, Final, Optional, Callable, List, Tuple, Set, Dict
from collections.abc import *

"""
1. 파일을 읽고 쓰는 것에 대해 학습한다.
2. 타입 에노테이션(힌트)를 적극적으로 사용한다.

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


def to_bytes(data: Union[str, bytes]) -> bytes:
    if isinstance(data, bytes):
        return data
    elif isinstance(data, str):
        return data.encode('utf-8')
    else:
        return b''


def to_str(data: Union[str, bytes]) -> str:
    if isinstance(data, str):
        return str
    elif isinstance(data, bytes):
        return data.decode('utf-8')
    else:
        ''


def check_instance(target) -> None:
    if isinstance(target, C):
        print(f'{target}은 C 클래스의 객체이다.')
    elif isinstance(target, B):
        print(f'{target}은 B 클래스의 객체이다.')
    elif isinstance(target, A):
        print(f'{target}은 A 클래스의 객체이다.')
    elif isinstance(target, Generator):
        print(f'{target}은 Generator 클래스의 객체이다.')
    elif isinstance(target, Iterator):
        print(f'{target}은 Iterator 클래스의 객체이다.')
    elif isinstance(target, Iterable):
        print(f'{target}은 Iterable 클래스의 객체이다.')
    else:
        print(f'{target}은 알 수 없는 클래스의 객체이다.')


if __name__ == '__main__':
    name = '준일'
    b1 = to_bytes(name)
    print(b1)
    s1 = to_str(b1)
    print(s1)

    a = A()
    b = B()
    c = C()

    check_instance(name)
    check_instance(b1)
    check_instance(s1)
    check_instance(a)
    check_instance(b)
    check_instance(c)
    check_instance(range(1, 2))
    check_instance(enumerate("준일", 1))

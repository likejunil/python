from collections import defaultdict
from typing import List, Tuple, Dict, Set, Generator, Iterable

# https://www.daleseo.com/python-typing/
# https://www.daleseo.com/python-mypy/

"""
-------------------------------------------
 sequence : 순서가 있는 데이터의 나열
-------------------------------------------
1) 무엇을 담는가?
    1.1) container : 서로 다른 타입의 데이터를 담을 수 있는 박스
        list, tuple, collections.deque
    1.2) flat : 같은 타입의 데이터만 담을 수 있는 박스
        str, bytes, bytearray, array.array, memoryview

2) 가변인가 불변인가?
    2.1) immutable : str, bytes, tuple
    2.2) mutable : 그 외의 모든 것들
"""


def func1() -> None:
    """
    __iter__ 의 의미를 이해한다.
    __iter__ 를 구현하여 반복적인 요소 반환을 가능하게 한다.

    map, filter 를 이해한다.
    이러한 class 들의 생성자는 iter 를 인자로 받는다.

    comprehension 을 이해한다.
    iter 의 모든 요소를 사용하여 최종 결과를 반환하기 때문에 메모리 사용이 크다.
    (list, dict, set 모두 가능)

    . map()
    . filter()

    . ord() -> int:
    . chr() -> str:
    . bin() -> str:
    . oct() -> str:
    . hex() -> str:
    """

    data: str = '준일!@#$%^&*()_+'
    print(f'문자열=|{data}| type=|{type(data)}|')

    ucode_list: List[int] = [ord(m) for m in data]
    print(f'문자열을 정수로 변환=|{ucode_list}| type=|{type(ucode_list)}|')
    print(f'"list comprehension" 을 사용하여 정수를 문자열로 변환=|{[chr(m) for m in ucode_list]}|')

    # map
    m1: map = map(ord, data)
    print(f'type=|{type(m1)}| value=|{m1}|')
    # filter
    f1: filter = filter(lambda x: x > 40, m1)
    print(f'type=|{type(f1)}| value=|{f1}|')
    # list
    l1: List[int] = list(f1)
    print(f'type=|{type(l1)}| value=|{l1}|')

    v_chr = '준'
    v_ord = ord(v_chr)
    v_bin = bin(v_ord)
    v_oct = oct(v_ord)
    v_hex = hex(v_ord)
    print(f'chr=|{v_chr}:{type(v_chr)}| '
          f'ord=|{v_ord}:{type(v_ord)}| '
          f'bin=|{v_bin}:{type(v_bin)}| '
          f'oct=|{v_oct}|{type(v_oct)}| '
          f'hex=|{v_hex}|{type(v_hex)}')


def func2() -> None:
    """
    generator 를 이해한다.
    iter 로부터 모든 요소를 적용한 최종 결과를 바로 생성하지 않는다.
    한 번에 하나씩 요소를 적용하여 단계별 결과를 반환한다.
    효율적인 메모리 사용에 적합하다.
    """

    data = '효진!@#$%^&*()_+'
    print(f'문자열=|{data}| type=|{type(data)}|')

    # generator
    ucode_generator: Generator[int] = (ord(n) for n in data)
    print(f'value=|{ucode_generator}| type=|{type(ucode_generator)}|')


def func3() -> None:
    """
    Sequence 를 정렬하는 방법을 이해한다.
    원본을 수정하는 방법
    원본을 보존하는 방법

    . sort() -> None:
    . sorted() -> list:
    """

    fruit_list = ['apple', 'strawberry', 'orange', 'grape', 'banana']
    print(f'1.원래의 과일 목록=|{fruit_list}|')

    sorted_fruit = sorted(fruit_list, reverse=True, key=lambda x: x[-2])
    print(f'2.정렬한 과일 목록(원본 보존)=|{sorted_fruit}|')
    print(f'2.원래의 과일 목록=|{fruit_list}|')

    fruit_list.sort(reverse=True, key=len)
    print(f'3.정렬한 과일 목록(원본 수정)=|{fruit_list}|')


def func4() -> None:
    """
    Dict 를 활용하는 방법을 학습한다.

    . setdefault()
    . collections.defaultdict()
    . hash()
    """

    source = (
        ('a', '1'),
        ('a', '2'),
        ('b', '3'),
        ('b', '4'),
        ('b', '5'),
    )

    # dict comprehension, unpacking 사용
    a_dict = {k: v for k, v in source}
    print(f'dict comprehension=|{a_dict}|')

    #
    b_dict = {}
    for k, v in source:
        if k not in b_dict:
            b_dict[k] = [v]
        else:
            b_dict[k].append(v)
    print(f'b_dict=|{b_dict}|')

    # dict 에서 하나씩 꺼낸다는 것은 key 를 꺼내는 것이다.
    # dict 에서 하나의 entry 를 꺼내면 tuple 로 나온다.
    for m in b_dict:
        print(f'type=|{type(m)}| value=|{m}|')
    for m in b_dict.keys():
        print(f'type=|{type(m)}| value=|{m}|')
    for m in b_dict.values():
        print(f'type=|{type(m)}| value=|{m}|')
    for m in b_dict.items():
        print(f'type=|{type(m)}| value=|{m}|')

    # dict 의 기본값을 지정할 수 있다.
    c_dict = defaultdict(list)
    d_dict = {}
    for k, v in source:
        c_dict[k].append(v)

        # setdefault() 는 인자로 주어진 key 에 해당하는 value 를 반환한다.
        # 해당 key 가 있으면 value 를 반환한다.
        # 해당 key 가 없으면 두번째 인자를 value 로 엔트리를 생성하고 value 를 반환한다.
        d_dict.setdefault(k, []).append(v)

    print(f'c_dict=|{c_dict}|')
    print(f'd_dict=|{d_dict}|')

    tmp_dict = {'a': 1}
    value1 = tmp_dict.setdefault('a', 2)
    value2 = tmp_dict.setdefault('b', 2)
    print(f'value1=|{value1}| value2=|{value2}| tmp_dict=|{tmp_dict}|')


if __name__ == '__main__':
    func1()
    func2()
    func3()
    func4()

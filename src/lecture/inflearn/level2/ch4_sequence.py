from collections import defaultdict
from types import MappingProxyType
from typing import List, Tuple, Dict, Set, Generator, Iterable
from functools import reduce
from dis import dis

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

    map, filter, reduce 를 이해한다.
    이러한 class 들의 생성자는 iter 를 인자로 받는다.

    comprehension 을 이해한다.
    iter 의 모든 요소를 사용하여 최종 결과를 반환하기 때문에 메모리 사용이 크다.
    (list, dict, set 모두 가능)

    . map()
    . filter()
    . reduce()
    . range()
    . enumerate()

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

    # reduce
    r1: reduce = reduce(lambda prev, curr: prev + curr, l1)
    print(f'type=|{type(r1)}| value=|{r1}|')
    r2: reduce = reduce(lambda prev, curr: prev * curr, range(3, 10), 2)
    print(f'type=|{type(r2)}| value=|{r2}|')

    # range
    v_range = range(1, 3)
    print(f'range=|{type(v_range)}|')
    for m in v_range:
        print(f'type=|{type(m)}| value=|{m}|')

    # enumerate
    v_enumerate = enumerate(v_range, 1)
    print(f'enumerate=|{type(v_enumerate)}|')
    for m in v_enumerate:
        print(f'type=|{type(m)}| value=|{m}|')

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

    # generator 는 메모리에 관련된 효율적 해법에 도움이 된다.
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

    # 원본을 보존하는 정렬
    sorted_fruit = sorted(fruit_list, reverse=True, key=lambda x: x[-2])
    print(f'2.정렬한 과일 목록(원본 보존)=|{sorted_fruit}|')
    print(f'2.원래의 과일 목록=|{fruit_list}|')

    # 원본 자체를 변경하는 정렬
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
    # iterator 로부터 직관적으로 쉽게 dict 를 생성할 수 있다.
    a_dict = {k: v for k, v in source}
    print(f'dict comprehension=|{a_dict}|')

    # 중복되는 키가 많을 경우 다음과 같은 방법이 가능하다.
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
    for k, v in source:
        c_dict[k].append(v)
    print(f'c_dict=|{c_dict}|')

    # setdefault() 는 인자로 주어진 key 에 해당하는 value 를 반환한다.
    # 해당 key 가 있으면 value 를 반환한다.
    # 해당 key 가 없으면 두번째 인자를 value 로 엔트리를 생성하고 value 를 반환한다.
    tmp_dict = {'a': 1}
    value1 = tmp_dict.setdefault('a', 2)
    value2 = tmp_dict.setdefault('b', 2)
    print(f'value1=|{value1}| value2=|{value2}| tmp_dict=|{tmp_dict}|')

    # dict 를 추가, 변경, 삭제가 불가능한 상태로 변경할 수 있다.
    frozen_dict = MappingProxyType(tmp_dict)
    print(f'frozen_dict=|{frozen_dict}| type=|{type(frozen_dict)}|')
    try:
        frozen_dict['c'] = 3
    except TypeError as e:
        print(f'{e}')


def func5() -> None:
    """
    set 의 특징을 이해한다.
    """

    # 아래의 문장이 효율이 좋다.
    print(dis('set([1])'))
    print(dis('{1}'))

    # 일반적인 집합
    tmp_set = {1}
    tmp_set.add(2)
    print(f'tmp_set=|{tmp_set}|')

    # 추가, 변경, 삭제가 불가능한 집합
    frozen_set = frozenset(['blue', 'red', 'white'])
    print(f'type=|{type(frozen_set)}| value=|{frozen_set}|')
    try:
        frozen_set.add('green')
    except AttributeError as e:
        print(f'{e}')


if __name__ == '__main__':
    func1()
    func2()
    func3()
    func4()
    func5()

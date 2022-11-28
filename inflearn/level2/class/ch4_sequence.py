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
    """

    data: str = '준일!@#$%^&*()_+'
    print(f'name=[${data}, type=[${type(data)}]]')

    ucode_list: List[int] = [ord(m) for m in data]
    print(f'type=[${type(ucode_list)}] value=[${ucode_list}]')
    print([chr(m) for m in ucode_list])

    # map
    m1: map = map(ord, data)
    print(type(m1))
    # filter
    f1: filter = filter(lambda x: x > 40, m1)
    print(type(f1))
    # list
    l1: List[int] = list(f1)
    print(l1)


def func2() -> None:
    """
    generator 를 이해한다.
    iter 로부터 모든 요소를 적용한 최종 결과를 바로 생성하지 않는다.
    한 번에 하나씩 요소를 적용하여 단계별 결과를 반환한다.
    효율적인 메모리 사용에 적합하다.
    """

    data = '효진!@#$%^&*()_+'
    print(f'name=[${data}, type=[${type(data)}]]')

    ucode_generator: Generator[int] = (ord(n) for n in data)
    print(f'type=[${type(ucode_generator)}] value=[${ucode_generator}]')


def func3() -> None:
    """
    Sequence 를 정렬하는 방법을 이해한다.
    원본을 수정하는 방법
    원본을 보존하는 방버
    """

    fruit_list = ['apple', 'strawberry', 'orange', 'grape', 'banana']
    print(f'1.원래의 과일 목록: ${fruit_list}')

    sorted_fruit = sorted(fruit_list, reverse=True, key=lambda x: x[-2])
    print(f'2.정렬한 과일 목록(원본 보존): ${sorted_fruit}')
    print(f'2.원래의 과일 목록: ${fruit_list}')

    fruit_list.sort(reverse=True, key=len)
    print(f'3.정렬한 과일 목록(원본 수정): ${fruit_list}')


if __name__ == '__main__':
    func1()
    func2()
    func3()

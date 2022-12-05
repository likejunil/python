from collections import abc

"""
 . 참조
    https://shoark7.github.io/programming/python/iterable-iterator-generator-in-python

 . 제일 먼저 알아야 할 것은 Abstract Base Class(ABC) 이다.
 . collections.abc 에는 파이썬의 가장 기본이 되는 내장모듈(list, tuple, set, dict)의 자료구조 뿐만 아니라 \
    다른 자료구조들의 뼈대가 되는 추상 자료 클래스가 관리되고 있다.
    - Container
    - Sequence
    - Collection
    - Mapping
    - ...
 . 그 중에서도 가장 기본이 되는 것은 Iterable, Iterator, Generator 이다. 
    
 . Iterable 은 __iter__ method 를 갖는다.
 . Iterable, Iterator 를 이해하기 위해서는 Iterator Procotol 을 먼저 이해해야 한다.
 . Iterator Protocol 이란 Iterable 과 Iterator 를 구체적으로 구현하기 위한 규칙(약속)을 의미한다.
 . iterate 는 반복을 의미한다.
 . 따라서 iterable 은 반복(순회) 가능을 의미한다.
 . for 문의 in 절 뒤에 오는 것들은 모두 iterable 이다. 
 . list, tuple, set, dict 는 모두 오직 Iterable 만을 상속 받는다. 
 
 . Iterable.__abstractmethods__ 를 실행하면 Iterable 를 상속받는 클래스가 구현해야 하는 method 를 알 수 있다.
 . Iterable 은 __iter__ method 를 가지며, 이는 호출될 때마다 새로운 Iterator 를 반환해야 한다.
 . iter() method 는 인자의 __iter__ 를 호출한다.
 . 따라서 iter() method 에 list | tuple | set | dict 를 인자로 넘겨주면 Iterator 가 반환된다.
 . iter(Iterable object) -> Iterator object (항상 새로운 instance)
 .  
 . Iterator 는 상태를 갖는다.
 . 같은 Iterable 에서 생성된 Iterator 들도 각각 자신만의 상태를 갖는다.
 . 여기서 상태란 Iterator 가 반복(순회)하기 위한 요소의 위치값이라고 볼 수 있다.
 . Iterator 는 Iterable 을 상속받고, __next__ 라는 abstract method 를 갖는다.
 . 즉, Iterator 는 __iter__, __next__ 2개의 method 를 갖는다.
 . __next__ 는 반복(순회)하면서 현재 위치가 기리키는 요소를 반환한다.
 . 더 이상 반환할 값이 없으면 StopIteration 예외를 발생시킨다.
 . 정리하면 Iterator 는 다음 3가지 조건을 만족한다.
    - __iter__ 는 자기 자신을 반환한다.
    - __next__ 는 다음 요소를 반환한다.
    - 더 이상 반환할 요소가 없다면 __next__ 에서 StopIteration 예외를 발생시킨다.
 . Iterator 객체는 한 번 사용하면 더 이상 사용할 수 없다. (1회용)
 . 
 . Generator 는 Iterator 를 상속받는다.
 . __iter__, __next__ 이외에 close, send, throw method 를 갖고 있다.
 . Generator 는 Iterator 와 달리 모든 요소를 모두 생성하여 간직하지 않는다.
 . yield 를 사용하여 필요한 타이밍에만 필요한 요소를 생성하여 반환한다.
 . 따라서 메모리를 효율적으로 사용할 수 있다는 장점이 있다.
 . 또한 co-routine 을 구현하기 위한 근간이 된다.
"""


class Range(object):
    """
    < class Range > : 학습을 위해 만들어 본 Iertable class
    . __iter__ method 를 구현해야 한다.
    . __iter__ 는 Iterator 객체를 생성하여 반환해야 한다.
    """

    def __init__(self, start: int, end: int, step: int):
        self.start = start
        self.end = end
        self.step = step
        print(f'Range 초기화: start=|{start}| end=|{end}| step=|{step}|')

    # def __iter__(self):
    #     return MyRange(self.start, self.end, self.step)

    """
    Iterator 클래스를 사용하여 생성하는 것도 가능하지만..
    다음과 같이 직접 Iterator(Generator) 를 생성하여 반환하는 것도 가능하다. 
    """

    def __iter__(self):
        print(f'나는 Iterable 의 iter 함수에서 생성된 generator 이다.')
        curr = self.start
        while True:
            if curr < self.end:
                ret = curr
                curr = curr + self.step
                yield ret
            if curr >= self.end:
                return


class MyRange(Range):
    """
    < class MyRange > : 학습을 위해 만들어 본 Iterator class
    . 형식적으로는 __iter__, __next__ method 만 구현하면 된다.
    . 나열된 데이터를 정해진 순서에 따라 차례대로 반환할 수 있으면 된다.
    """

    def __init__(self, start: int, end: int, step: int):
        super().__init__(start, end, step)
        self.curr = self.start
        print(f'MyRange 초기화: start=|{start}| end=|{end}| step=|{step} curr=|{self.curr}||')

    def __next__(self) -> int:
        if self.curr >= self.end:
            raise StopIteration
        ret = self.curr
        self.curr = self.curr + self.step
        return ret


def my_generator(start: int, end: int, step: int):
    """
    < func my_generator > : 학습을 위해 만들어 본 generator func
    generator 는 iterator 를 반환하는 함수이다.
    따라서 본 함수를 호출하면 iterator 가 반환된다.
    """

    print(f'나는 generator 함수에서 생성된 generator 이다.')
    curr = start
    while True:
        if curr < end:
            ret, curr = curr, curr + step
            print('yield 직전..')
            yield ret
            print('yield 직후..')
        else:
            return


def print_all_iter(it):
    while True:
        try:
            print(next(it))
        except StopIteration as e:
            print(e)
            break


def func1() -> None:
    r = Range(1, 10, 2)
    print(f'Range 는 Iterable 이다. '
          f'issubclass(Range, Iterable)=|{issubclass(Range, abc.Iterable)}|')

    i = iter(r)
    print(f'Iterable 은 iter() 를 통해 Iterator 를 반환한다. '
          f'iterator=|{isinstance(i, abc.Iterator)}| '
          f'generator=|{isinstance(i, abc.Generator)}|')

    print_all_iter(i)
    # for x in i:
    #     print(x)


def func2():
    g = my_generator(1, 10, 2)
    print(f'isinstance(g, Generator)=|{isinstance(g, abc.Generator)}| '
          f'issubclass(Generator, Iterator)=|{issubclass(abc.Generator, abc.Iterator)}|')

    print_all_iter(g)
    # for x in g:
    #     print(x)


if __name__ == '__main__':
    func1()
    func2()

"""
왜 Iterator 가 던지는 StopIteration 은 처리하면서
generator 가 던지는 StopIteration 은 처리하지 않는가?

Iterator 는 명시적으로 StopIteration 을 발생시켜야 하고
Generator 는 함수 자체를 종료시키면 저절로 StopIteration 이 발생한다.
"""

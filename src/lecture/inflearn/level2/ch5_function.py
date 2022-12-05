from inspect import signature
from typing import Union

"""
함수에서 주의깊게 봐야할 속성은 __call__, __code__ 2가지이다.
도움이 되는 함수는 callable(), signature() 이다.
partial() 함수의 특징!을 이해한다.
"""


class A:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print('__call__ 이 호출되었다.')
        ret = 0
        for m in args:
            ret = ret + m
        return ret


def f(a: int, b: int) -> int:
    return a + b


def func1() -> None:
    """
    함수에는 클래스에는 없는 10개의 속성이 있다.
    클래스에는 함수에는 없는 1개의 속성이 있다.
    모두에게 공통으로 25개의 속성이 있다.

    중요한 것은 함수도 클래스라는 것이다.
    파이썬은 모든 것이 클래스로부터 생성된다.
    """
    s1 = set(sorted(dir(A)))
    s2 = set(sorted(dir(f)))
    print(f'클래스 A=|{type(A)}| len=|{len(dir(A))}| dir=|{dir(A)}|\nlen=|{len(s1)}| set=|{s1}|')
    print(f'함수 f=|{type(f)}| len=|{len(dir(f))}| dir=|{dir(f)}|\nlen=|{len(s2)}| set=|{s2}|')
    print(f'함수에만 len=|{len(s2 - s1)}| value=|{s2 - s1}|')
    print(f'클래스에만 len=|{len(s1 - s2)}| value=|{s1 - s2}|')
    print(f'모두 len=|{len(s1.intersection(s2))}| value=|{s1.intersection(s2)}|')


def func2() -> None:
    """
    주어진 대상이 호출이 가능한지 아닌지 callable() 함수를 통해 확인할 수 있다.
    __call__ 속성을 가지면 callable() 은 True 를 반환한다.
    __call__ 함수는 함수도 클래스도 객체도 모두 가질 수 있다.

    1. 함수의 경우, 함수를 호출하면 __call__ 이 실행된다.
    2. 객체를 실행시키면 __call__ 이 실행된다.
    3. 무엇이든 () 연산자를 적용하면 __call__ 이 실행된다.
    """

    a = A()
    print(f'callable(함수)=|{callable(f)}|')
    print(f'callable(클래스)=|{callable(A)}|')
    print(f'callable(객체)=|{callable(a)}|')

    print(f'함수.__call__=|{f.__call__(1, 2)}|')
    print(f'클래스.__call__=|{A.__call__(a, 1, 2)}|')
    print(f'객체.__call__=|{a.__call__(1, 2)}|')
    print(f'객체 a()=|{a(1, 2)}|')


def func3():
    """
    일반적으로 __code__ 속성은 함수만 갖고 있다.
    해당 함수에 대한 코드가 위치한 파일과 라인의 정보가 출력된다.
    hasattr() 함수로 대상 객체가 특정 속성을 갖고 있는지 확인할 수 있다.
    """

    a = A()
    print(f'f.__code__=|{f.__code__}|')
    if hasattr(f, '__code__'):
        print(f'함수는 __code__ 속성을 갖고 있다.')
    if hasattr(A, '__code__'):
        print(f'클래스는 __code__ 속성을 갖고 있다.')
    if hasattr(a, '__code__'):
        print(f'객체는 __code__ 속성을 갖고 있다.')


def func4():
    """
    signature() 는 주어진 인자의 함수 시그니처를 반환한다.
    """

    s = signature(f)
    print(f'type(s)=|{type(s)}| signature()=|{s}|')


class Average:
    def __init__(self):
        self.data = []

    def __call__(self, num: Union[int, float]) -> float:
        self.data.append(num)
        average = sum(self.data) / len(self.data)
        print(f'데이타=|{self.data}| 평균=|{average:.2f}|')
        return average


def create_closure():
    """
    closure 를 반환하는 함수
    """

    data = []

    def avg_closure(num: Union[int, float]) -> float:
        data.append(num)
        average = sum(data) / len(data)
        print(f'데이타=|{data}| 평균=|{average:.2f}|')
        return average

    return avg_closure


def func5():
    avg = Average()
    avg(9.3)
    avg(9.9)
    avg(11)

    closure = create_closure()
    closure(4.2)
    closure(4.9)
    closure(12)


if __name__ == '__main__':
    func1()
    func2()
    func3()
    func4()
    func5()

# lambda
# callable()
# hasattr(target, '__call__) 속성 확인
# partial()
# 변수의 스코프 확인
# 클래스로 클로저 구현
# 함수로 클로저 구현
# 데코레이션 구현

# hasattr(target, '__iter__') 확인
# isinstance(target, collections.abc.Iterable) 확인
# iter(), next()
# for 문 구현
# range 구현
# iterator 구현
# generator 구현
# yield 이해
# itertools 이해
# 병행성(concurrency)과 병렬성(parallel)의 차이 이해

# itertools.count()
# itertools.takewhile()
# itertools.filterfalse()
# itertools.accumulate()
# itertools.chain()
# itertools.product()
# itertools.groupby()

#
import itertools


def func1():
    """
    한 번 거짓이 나타나면 그 뒤에는 참인 조건이 있더라도 진행하지 않는다.
    """

    r = itertools.takewhile(lambda x: x < 10, [1, 4, 11, 4, 9, 20])
    for m in r:
        print(m)


def func2():
    """
    데카르트의 곱은 데이터의 관계를 표현하기 위한 좌표계를 만들 때 사용할 수 있다.
    """

    p = itertools.product('ABC', [1, 2, 3])
    for m in p:
        print(m)


if __name__ == '__main__':
    func1()
    func2()

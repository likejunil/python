class A:
    pass


def f():
    pass


def func1() -> None:
    s1 = set(sorted(dir(A)))
    s2 = set(sorted(dir(f)))
    print(f'클래스 A=|{type(A)}| len=|{len(dir(A))}| dir=|{dir(A)}|\nlen=|{len(s1)}| set=|{s1}|')
    print(f'함수 f=|{type(f)}| len=|{len(dir(f))}| dir=|{dir(f)}|\nlen=|{len(s2)}| set=|{s2}|')
    ret = s2 - s1
    print(f'함수에만 len=|{len(ret)}| value=|{ret}|')


if __name__ == '__main__':
    func1()

# lambda
# callable()
# hasattr(target, '__call__) 속성 확인
# partial()
# 변수의 스코프 확인
# 클래스로 클로저 구현
# 함수로 클로저 구현
# 데코레이션 구현

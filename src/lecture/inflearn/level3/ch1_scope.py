"""
. scope
. global
. nonlocal
. locals
. globals

 - 파이썬의 경우 변수를 읽을 때와 쓸 때 작용하는 방식이 다르다.
 - 파이썬의 변수 scope 는 함수를 기준으로 한다.
 - global 사용은 최대한 자제한다. (버그의 어머니)
 - globals(), loclas() 는 각각의 scope 에 담긴 속성들을 dict 로 반환한다.

"""


def same_object():
    # 파이썬에서는 모든 것이 객체이다.
    a = 1
    print(id(a))
    # 1이라는 같은 객체를 담는다.
    b = 1
    print(id(b))
    # 따라서 a, b 는 같은 객체에 대한 주소를 담고 있다.
    if a is b:
        print(f'a 와 b 는 같은 객체이다.')

    # 다른 객체를 담는다.
    a = 2
    print(f'a=|{a}|')
    print(f'b=|{b}|')


apple = 1
grape = 2


def check_globals():
    a = 1
    b = 2

    # globals() 는 dict 이다.
    gl = globals()
    print(f'globals() => type=|{type(gl)}| value=|{gl}|')

    # locals() 는 dict 이다.
    lc = locals()
    print(f'locals() => type=|{type(lc)}| value=|{lc}|')


if __name__ == '__main__':
    same_object()
    check_globals()

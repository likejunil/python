"""
. meta class 는 class 를 만드는 역할을 한다.
. type class 는 class 를 생성하는 class 이다.
. 즉, type 은 meta class 이다.
. type 은 모든 class 의 class 이다.

class A:
    pass
a = A()

. a 는 A 의 instance 이다.
. A 는 type 의 instance 이다.
. type(A) is A.__class__ is type is a.__class__.__class__

. 동적으로 class 를 생성할 수 있다.
. type(생성할 클래스의 이름, 상속받을 클래스들의 튜플, 추가하려는 속성들)

. type 을 상속 받아서 custom meta class 를 만들 수 있다.
. custom meta class 는 3가지를 구현해야 한다.
    - __new__(metacls, bases, namespace):
        ...
        # 메모리 할당 및 ...
        return super().__new__(metacls, bases, namespace)

    - __init__(self, bases, dict):
        # 초기화 작업 및 ...
        ...

    - __call__(self, *args, **kwargs)
        ...
        # 생성된 클래스를 실행하여 instance 를 만들 때..
        return super().__call__(self, *args, **kwargs)

. custom meta class 는 type 을 상속받고 결국 type 의 기능을 호출한다.
. 다만 type 의 기능을 호출하기 전에 자신이 하고 싶은 일을 끼워넣을 뿐이다.
. 스스로 메모리를 할당하고 클래스의 인스턴스를 생성하는 일을 하지는 못한다.

"""


class A:
    """
    클래스를 만드는 첫번째 방법:
    class 키워드를 사용하여 클래스를 만든다.
    """
    pass


def func1():
    """
    클래스를 만드는 두번째 방법:
    type 클래스에 3개의 인자를 넣어 클래스를 만든다.
    """

    # A
    print(f'type(A)=|{type(A)}| __base__=|{A.__base__}| __dict__=|{A.__dict__}|')

    # B
    B = type("B", (), {})
    print(f'type(B)=|{type(B)}| __base__=|{B.__base__}| __dict__=|{B.__dict__}|')

    # C
    C = type("C", (B,), dict(name="준일", age=48))
    print(f'type(C)=|{type(C)}| __base__=|{C.__base__}| __dict__=|{C.__dict__}|')


if __name__ == '__main__':
    func1()

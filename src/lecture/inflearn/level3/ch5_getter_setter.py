"""
@property 에 대해서 학습한다.
1. pythonic style
2. 변수에 대한 제약을 설정한다.
3. Getter, Setter 와 동등한 효과를 준다. (캡슐화, 은닉화, 모듈성 등)

# @property
# @{m}.setter
# @{m}.deleter

"""


class A:
    def __init__(self):
        self.a = 1
        self.b = 2


def func1():
    a = A()
    print(a.a)
    print(a.b)
    print(a.__dict__)
    print(dir(a))

    del a.b
    print(a.__dict__)
    print(dir(a))

    a.b = 2
    a.c = 3
    print(a.__dict__)
    print(dir(a))


if __name__ == '__main__':
    func1()

"""
@property 에 대해서 학습한다.
1. pythonic style
2. 변수에 대한 제약을 설정한다.
3. Getter, Setter 와 동등한 효과를 준다. (캡슐화, 은닉화, 모듈성 등)

# @property
# @{m}.setter
# @{m}.deleter

"""


class C:
    def __init__(self, name):
        print('C 가 생성되었습니다.')
        self.name = name

    def hello(self):
        print(f'안녕하세요, {self.name}입니다. ')


class A:
    """
    A 클래스에는 apple 이라는 속성이 있지만, __dict__ 를 통해 조회하면 없다.
    apple 이라는 속성은, 해당 속성에 연결된 함수를 호출하기 위한 방아쇠일 뿐이다.
    """

    def __init__(self, value):
        print(f'초기화 함수(init)를 호출합니다.')
        self.__value = value

    @property
    def apple(self):
        print(f'getter 를 호출합니다.')
        return self.__value

    @apple.setter
    def apple(self, value):
        print(f'setter 를 호출합니다.')
        self.__value = value

    @apple.deleter
    def apple(self):
        print(f'deleter 를 호출합니다.')
        del self.__value


class B:
    def __init__(self, value):
        print(f'초기화 함수(init)를 호출합니다.')
        self.__value = value

    def get(self):
        print(f'getter 를 호출합니다.')
        return self.__value

    def set(self, value):
        print(f'setter 를 호출합니다.')
        self.__value = value

    def delete(self):
        print(f'deleter 를 호출합니다.')
        del self.__value

    # getter, setter, deleter 이상 3개의 함수를 모아서 apple 속성에 연결한다.
    # 이제 apple 속성을 조회, 변경, 삭제를 할 경우 해당 함수들이 실행된다.
    # 이것은 @property 를 다른 방법으로 구현한 것과 같다.
    apple = property(get, set, delete, '')


def func(obj):
    print(obj, obj.__dict__, hasattr(obj, 'apple'), type(obj.apple))
    obj.apple = 3
    print(obj.apple)
    print(obj, obj.__dict__, hasattr(obj, 'apple'), type(obj.apple))

    del obj.apple
    print(obj, obj.__dict__, hasattr(obj, 'apple'))


if __name__ == '__main__':
    """
    초기화 함수(init)를 호출합니다.
    getter 를 호출합니다.
    getter 를 호출합니다.
    <__main__.A object at 0x104c2a0d0> {'_A__value': 1} True <class 'int'>
    setter 를 호출합니다.
    getter 를 호출합니다.
    3
    deleter 를 호출합니다.
    getter 를 호출합니다.
    <__main__.A object at 0x104c2a0d0> {} False
    """
    c = C('준일')
    obj1 = A(c)
    func(obj1)

    """
    초기화 함수(init)를 호출합니다.
    getter 를 호출합니다.
    getter 를 호출합니다.
    <__main__.B object at 0x104c2a130> {'_B__value': 2} True <class 'int'>
    setter 를 호출합니다.
    getter 를 호출합니다.
    3
    deleter 를 호출합니다.    
    getter 를 호출합니다.
    <__main__.B object at 0x104c2a130> {} False
    """
    obj2 = B(2)
    func(obj2)

"""
객체(a)가 어떤 객체(b)를 static 속성으로 가지고 있을 때.. (instance 속성에는 적용되지 않는다.)
속성 객체(b)를 읽거나 객체를 수정 및 삭제할 경우 실행되는 함수를 정의할 수 있다.
. __get__(self, obj, objtype)
. __set__(self, obj, value)
. __delete__(self, obj)

a = A()
a.b = 10        => __set__(b, a, 10)
print(a.b)      => __get__(b, a, A)
del a.b         => __delete__(b, a)

"""


class Child:
    def __init__(self, name):
        print(f'Child 클래스의 초기화 진행=|{name}|')
        self.name = name
        self.age = 0

    def __repr__(self):
        return f'name=|{self.name}| age=|{self.age}|'

    def __set__(self, instance, value):
        print(f'Child 객체 값 입력, name=|{self.name}| value=|{value}|')
        if isinstance(value, str):
            self.name = value
        elif isinstance(value, int):
            self.age = value
        else:
            raise TypeError('이름은 문자열, 나이는 숫자를 입력해 주세요.')

    def __get__(self, instance, owner):
        print(f'Child 객체 값 조회, name=|{self.name}| age=|{self.age}|')
        # return dict(name=self.name, age=self.age)
        return self

    def __delete__(self, instance):
        print(f'Child 객체 삭제, name=|{self.name}|')
        self.name = None
        self.age = 0

    def old(self, year: int = 1):
        print(f'Child 객체 나이 먹음, name=|{self.name}|')
        self.age += year


class Parent(object):
    daughter = Child('효진')

    def __init__(self):
        self._son = Child('준일')

    def __repr__(self):
        return f'나의 아들=|{self._son}| 나의 딸=|{self.daughter}|'


if __name__ == '__main__':
    # 생성
    print('===== 생성 =====')
    parent = Parent()

    # 수정
    print('===== 수정 =====')
    parent.daughter = '슈퍼효진'
    parent.daughter = 43

    # 조회
    print('===== 조회 =====')
    d = parent.daughter
    if isinstance(d, Child):
        d.old(44)
    print(parent)

    # 삭제
    print('===== 삭제 =====')
    del parent.daughter
    print(parent)
    print('작업 완료')

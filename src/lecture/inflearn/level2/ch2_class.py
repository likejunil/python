"""
. 모든 클래스는 type 클래스로부터 만들어진다.
. 모든 클래스는 object 클래스를 상속받는다.
. type 은 클래스를 만들고 클래스는 인스턴스를 만든다.
. 클래스와 인스턴스 모두 객체이다.
.
"""

if __name__ == '__main__':
    class Family:
        last_name = '권'
        member_count = 0

        def __init__(self, name):
            self.name = name
            # 클래스 속성을 변경할 때는 반드시 클래스의 이름으로 접근해야만 한다.
            Family.member_count += 1

        def __repr__(self):
            # 클래스 속성을 조회할 때는 인스턴스의 이름으로 접근하는 것이 가능하다.
            # 클래스 속성과 인스턴스 속성의 이름이 같을 때는.. 접근자를 주의해서 사용해야 한다.
            return f'이름=|{self.name}| 수=|{self.member_count}|'

        @classmethod
        def get_info(cls):
            return f'"{cls.last_name}"씨 가족의 구성원은 {cls.member_count}명 입니다.'


    f1 = Family('준일')
    print(f1)
    f2 = Family('효진')
    print(f2)
    f3 = Family('강')
    print(f3)
    print(Family.get_info())

    # 인스턴스를 통해 클래스 속성에 접근하여 값을 대입하면..
    # 새로운 인스턴스 속성이 생성된다.
    f3.member_count = 100
    print(f3, Family.get_info(), sep='\n')

    print()
    print(f'======= object 클래스의 정보 =======\n'
          f'value=|{object}|\n'
          f'type=|{type(object)}|\n'
          f'__dict__=|{object.__dict__}|\n'
          f'dir()=|{dir(object)}|')

    print()
    print(f'======= Family 클래스의 정보 =======\n'
          f'value=|{Family}|\n'
          f'type=|{type(Family)}|\n'
          f'__dict__=|{Family.__dict__}|\n'
          f'dir()=|{dir(Family)}|\n'
          f'only=|{set(dir(Family)) - set(dir(object))}|')

    family = Family(1)
    family.member_count = 100
    print()
    print(f'======= Family 인스턴스의 정보 =======\n'
          f'value=|{family}|\n'
          f'type=|{type(family)}|\n'
          f'__dict__=|{family.__dict__}|\n'
          f'dir()=|{dir(family)}|\n'
          f'only=|{set(dir(family)) - set(dir(Family))}|')

import datetime as dt
from sys import getsizeof

"""
 클래스를 사용하는 이유? 객체지향적 프로그래밍을 하는 이유?
 결국은 보다 효율적으로 코딩을 하기 위해서이다.
 효율적으로 코딩을 하려면..
 -------------------------------------------------------------------
 1. 최대한 중복을 피해야 한다. 그래야 코드의 양이 줄어든다.
 2. 유지 보수가 편해야 한다. 최대한 적은 노력으로 해결해야 한다.
 -------------------------------------------------------------------

 만약 한 번 코딩을 마무리 하고 다시는 그 코드를 돌아볼 일이 없다면..
 버그도 발생하지 않고 새로운 기능을 추가하거나 대체하는 일도 없다면..
 그냥 편한대로 작성하면 된다.
 하지만 현실에선 99.999999999999% 그런 일은 발생하지 않는다.
 반드시 유지 보수가 편하도록 프로그래밍을 해야한다.

 SOLD 에 입각한 프로그래밍을 하는 이유가 있다.
 1) Single Responsibility Principle
    하나의 덩어리(함수이든 클래스이든 모듈이든 컴포넌트이든)는 하나의 기능에만 책임을 져야 한다.
    여러가지 기능을 한꺼번에 책임지려고 하면 기능끼리 서로 간섭이 생기고 문제가 전파될 가능성이 크다.
    1 만큼 고치기 위해 10 만큼 들여다보아야 하는 경우가 생긴다.
    a 를 개선하기 위해 전혀 상관없는 b, c 도 신경써야 하는 경우가 생긴다.
    즉, 유지보수가 어려워진다.
    하나의 기능만을 구현해야 해당 기능을 필요로 하는 곳에서 재사용하기가 쉽다.
    즉, 코드 중복을 피할 수 있다.

 2) Open Closed Principle
    기능의 확장에는 열려있고 기존 소스의 변경에는 닫혀있어야 한다.
    기능을 추가하거나 변경할 때 기존의 소스를 변경하는 일이 없어야 한다.
    그래야 유지보수가 쉬워진다.
    사실 이것이 핵심이다.
    나머지 모든 원칙들은 이것을 위해 존재한다.
    Single Responsibility Principle 도 이 원칙을 위해 존재한다고 볼 수 있다.
    여러가지 기능이 독립적이지 못하고 서로 얽혀 있으면 Open Closed Principle 을 지키기 어렵다.

 3) Liskov Substitusion Principle
    자식의 자료형으로 부모의 자리에 입력될 수 있어야 한다.
    이러한 다형성(Polymorphism) 덕분에 Open CLosed Principle 을 지킬 수 있다.
    하나의 인터페이스를 정의하고 다양한 자식 구현체를 생성하여 유연하게 기능을 변경 및 확장할 수 있다.

 4) Interface Segregation principle
    필요한 기능만 정의된 itnerface 를 설계하고 구현해야 한다.
    불필요한 기능이 정의된 interface 를 구현하는 일은 모든 면에서 비효율적이고 문제가 생길 가능성을 남겨둔다.
    그러므로 interface 에 대하여 Single Responsibility Principle 에 입각한 설계를 적용해야 한다.
    그래야 Open Closed Principle 을 지킬 수 있다.

 5) Dependency Inversion Principle
    클래스나 함수 등 특정 기능의 의존 방향이 유지되어야 한다.
    의존성이 양방이 될 경우 기능 대체가 어려워진다.
    A -> B -> C 의 경우 C 를 C' 로 대체하는데 무리가 없다.
    반면 A -> B -> C -> A 라면 C 를 C' 로 대체할 때 반드시 A 에 대한 의존성을 확인해야만 한다.
    이것은 유연한 기능 확장에 닫혀 있을 뿐만 아니라 A, B 모두를 변경해야만 하는 최악의 상황까지 닥칠 수 있다.
    역시 Open Closed Principle 을 지킬 수 없게 된다.

 객체지향 프로그래밍은 하나의 관점에 대한 데이터와 기능을 모아서 덩어리를 만든다.
 더불어 인터페이스와 상속이라는 다형성을 제공한다.
 객체지향의 이러한 장점이 SOLID 에 입각한 프로그래밍을 가능하게 한다.
 객체지향 방법에는 여러가지가 있으나 파이썬은 클래스를 활용하고 있다.
 그리고 이것이 파이썬을 사용할 때 클래스를 적극적으로 사용해야 하는 이유이다.
"""


class Person(object):
    """
    Person class
    author: june1
    date: 2022.11.26
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '이름=[{}], 나이=[{}]'.format(self.name, self.age)

    def __repr__(self):
        return "{{'name': '{}', 'age': {}}}".format(self.name, self.age)

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


# -----------------------------------
# 출력에 관련한 함수들
# -----------------------------------
def about_print():
    """
    어떤 객체를 표현하고 싶을 때 3가지 방법이 있다.
    1. __str__ 을 작성하여 해당 객체를 표현하는 문자열을 반환한다.
    2. __repr__ 을 작성하여 해당 객체를 문자열로 표현(해당 문자열로부터 다시 객체를 생성할 수 있음)한다.
    3. Object 객체로부터 표현 방법을 상속받아 사용한다.

    . 일반적으로 print() 를 호출하면 __str__ 이 적용된다.
    . __str__ 이 정의되지 않은 경우 __repr__ 이 적용된다.
    . 어떤 객체의 요소일 경우 __repr__ 이 적용된다.
    . __str__, __repr__ 모두 적용되지 않은 경우 Object 로부터 상속받은 방법을 사용한다.
    """

    print("+" * 20, "출력", "+" * 20)
    june1 = Person('준일', 48)
    print("1) object ::", june1)
    print("2) str ::", str(june1))
    print("3) repr ::", repr(june1))

    ret_repr = repr(june1)
    ret_eval = eval(ret_repr)
    print("4) repr,eval ::", ret_eval)

    # list 를 출력할 때는 __repr__ 을 사용
    person_list = []
    person_list.append(Person('lion', 10))
    person_list.append(Person('dog', 20))
    print("5) list ::", person_list)

    # 개발자가 첨부한 해당 클래스에 대한 주석 확인
    print("6) doc ::", Person.__doc__)
    print()


# -----------------------------------
# 해당 객체에 대한 정보
# -----------------------------------
def about_object():
    """
    파이썬은 모든 것이 객체이다.
    파이썬의 객체는 클래스로부터 생성된다.
    type() method 에 특정 객체를 인자로 전달하면..
    해당 객체를 생성한 클래스를 알려준다.
    이러한 값은 해당 객체의 __class__ 속성에 담겨 있다.

    객체 자체에 대한 비교는 is 연산자로 확인하며
    값에 대한 비교는 == 연산자를 사용한다.
    """

    hyojin1 = Person('효진', 43)
    hyojin2 = Person('효진', 43)
    print("+" * 20, "객체에 대한 정보", "+" * 20)
    print("1) __dict__ ::", hyojin1.__dict__)
    print("2) dir ::", dir(hyojin1))
    print("3) type ::", type(hyojin1))
    print("4) __class__ ::", hyojin1.__class__)
    print("5) isinstance ::", isinstance(hyojin1, Person))
    print("6) id(address) ::", id(hyojin1))
    print("7) is(reference) ::", hyojin1 is hyojin2)
    print("8) ==(value) ::", hyojin1 == hyojin2)
    print()


# -----------------------------------
# 파이썬의 데이터 타입
# -----------------------------------
def about_datatype():
    """
    파이썬3에서는 정수에 대하여 overflow 가 없다.
    얼마든지 원하는 큰 수를 대입하여 사용할 수 있다.
    다른 언어와는 다르게 복소수를 지원한다.
    """

    print("+" * 20, "데이터 타입에 대한 정보", "+" * 20)
    b_list = [bool(), True]
    i_list = [int(), 1]
    f_list = [float(), 3.14159265358979]
    c_list = [complex(), 1 + 2j]
    s_list = [str(), "ok"]
    list_list = [list(), [1, 2]]
    tuple_list = [tuple(), (3,)]
    set_list = [set(), {1, 2}]
    dict_list = [dict(), {'name': 'june1', 'age': 48}]
    byte_list = ["".encode('utf-8'), "준일".encode('utf-8')]
    type_list1 = [
        b_list,
        i_list,
        f_list,
        c_list,
        s_list,
        list_list,
        tuple_list,
        set_list,
        dict_list,
        byte_list,
    ]
    for i, n in enumerate(type_list1):
        for j in (0, 1):
            print("{}-{}. id=[{}] | value=[{}] | bool=[{}] | type=[{}] | size=[{}]"
                  .format(i, j, id(n[j]), n[j], bool(n[j]), type(n[j]), getsizeof(n[j])))

    type_list2 = [
        None,
        about_datatype,
        Person,
        Person('a', 1),
        dt.datetime.now(),
    ]
    for i, n in enumerate(type_list2):
        print("{}. id=[{}] | value=[{}] | bool=[{}] | type=[{}] | size=[{}]"
              .format(i, id(n), n, bool(n), type(n), getsizeof(n)))
    print()


if __name__ == '__main__':
    about_print()
    about_object()
    about_datatype()

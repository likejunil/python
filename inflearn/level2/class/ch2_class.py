class Person(object):
    """
    Person 클래스
    name: 이름
    age: 나이
    """
    total_person = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.total_person += 1

    def __repr__(self):
        return '"name": {}, "age": {}'.format(self.name, self.age)

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __del__(self):
        Person.total_person -= 1

    def get_name(self):
        return self.name

    @classmethod
    def get_total_person(cls):
        return cls.total_person

    @staticmethod
    def size():
        if Person.total_person < 2:
            return "small"
        elif Person.total_person < 5:
            return "middle"
        else:
            return "big"


class Student(Person):
    """
    Student 클래스
    major: 전공
    grade: 학년
    """
    id_list = []

    def __init__(self, name, age, student_id, major, grade):
        super().__init__(name, age)
        self.id = student_id
        self.major = major
        self.grade = grade
        Student.id_list.append(student_id)

    def __repr__(self):
        return super().__repr__() + '\n' \
               + '"id": {}, "major": {}, "grade": {}'.format(self.id, self.major, self.grade)

    def __eq__(self, other):
        return self.id == other.id

    @classmethod
    def get_id_list(cls):
        return cls.id_list[:]


if __name__ == '__main__':
    s1 = Student('준일', 48, '9515', '수학', 4)
    s2 = Student('효진', 43, '9515', '법학', 3)
    print(s1)
    print(s2)
    print('제 이름은 {} 입니다.'.format(s1.get_name()))

    total_person = Person.get_total_person()
    print('총 인구수=[{}]'.format(total_person))
    print('규모=[{}]'.format(Person.size()))

    id_list = Student.get_id_list()
    print('학생 아이디=[{}]'.format(id_list))

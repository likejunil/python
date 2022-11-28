from collections import namedtuple

if __name__ == '__main__':
    """
    일반적인 tuple 은 각각의 요소에 index 를 통해서 접근한다.
    namedtuple 은 마치 dict 와 같이 각각의 요소에 key(name)를 통하여 접근할 수 있다.
    """

    # Point = namedtuple("_3D", ['x', 'y', 'z'])
    # Point = namedtuple("_3D", ('x', 'y', 'z'))
    # Point = namedtuple("_3D", {'x', 'y', 'z'})
    # Point = namedtuple("_3D", "x, y, z")
    Vector = namedtuple("_3D", "x y z")
    print(Vector, type(Vector))
    v1 = Vector(1.2, 3.4, 1.0)
    v2 = Vector(2.9, -1.1, 2.1)

    print(v1, type(v1))
    print(v1[0], v1[1], v1[2])
    print(v1.x, v1.y, v1.z)

    Point = namedtuple("_2D", "x y")
    print(Point, type(Point))
    temp_dict = {'x': 9, 'y': 12}
    p1 = Point(**temp_dict)
    print(p1)

    temp_tuple = (1, 2)
    p2 = Point(*temp_tuple)
    print(p2)

    temp_list = [4, 2]
    p3 = Point(*temp_list)
    print(p3)

    temp_set = {10, 20}
    p4 = Point(*temp_set)
    print(p4)

    temp_str = "18"
    p5 = Point(*temp_str)
    print(p5)

    asdict = p4._asdict()
    print(type(asdict), asdict)

"""
pip install multipledispatch
. multipledispatch 사용법을 학습한다.

# from multipledispatch import dispatch
# @dispatch(int, int)
# def product(x, y):
#       ...
#
# @dispatch(int, int, int)
# def product(x, y, z):
#       ...


"""


class Sample:
    def __init__(self):
        self.count = 0

    def print_args(self, *args, **kwargs):
        """
        외부에서 함수를 호출할 때..
        다양한 개수의 인자가 주어지면 packing 을 통해 tuple 을 생성하여 전달된다.
        key, value 형태의 인자들을 넘기면 packing 을 통해 dict 를 생성하여 전달된다.
        """

        print(f'type=|{type(args)}| value=|{args}|')
        print(f'type=|{type(kwargs)}| value=|{kwargs}|')

        """
        함수 인자가 아닌 일반 할당에서는.. 
        unpacking 의 결과를 다시 list 로 packing 하여 돌려준다.
        """
        first, *middle, last = args
        print(f'type=|{type(middle)}| value=|{middle}|')

        self.count += 1


s = Sample()
s.print_args(1, 2, 3, 4, 5, name='준일', age=48, sex='남자')

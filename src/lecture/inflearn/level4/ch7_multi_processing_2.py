"""
<< 프로세스 사이에서 데이터를 공유하는 방법 >.
. Manager 를 사용한다.
m = Manager()
m.list() <= 공유하려는 데이터의 타입


"""
from multiprocessing import Process, Manager, Array, current_process


def func():
    m = Manager()
    m_list = m.list()


if __name__ == '__main__':
    func()

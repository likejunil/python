"""
<< 1 >>
from multiprocessing import Process, current_process
import os

p = Process(target=, args=)
p.start()
p.join()
p.is_alive()
p.terminate()

os.getpid()
current_process().name


<< 2 >>
from concurrent.futures import ProcessPoolExecutor, as_completed
as_completed()


<< 3 >>
from multiprocessing import Process, current_process, Value, Array, shared_memory, Manager
share_value = Value('f', 3.14)
print(share_value.value)
share_list = Array('i', range(50))
print(share_list.value)


<< 4 >>
from multiprocessing import Queue, Pipe
q = Queue()
q.put(message)
message = q.get()

p, c = Pipe()
p.send(message)
message = c.recv()
"""

from multiprocessing import Process, current_process
import os


def proc_func(a, b, c):
    print(f'자식 프로세스, name=|{current_process().name}| pid=|{os.getpid()}| 시작')
    print(f'a={a}, b={b}, c={c}')
    print(f'자식 프로세스, name=|{current_process().name}| pid=|{os.getpid()}| 종료')


def func1():
    print(f'부모 프로세스, name=|{current_process().name}| pid=|{os.getpid()}| 시작')
    p1 = Process(name='준일', target=proc_func, args=(1, 2, 3,))
    p1.start()

    p1.join()
    print(f'부모 프로세스, name=|{current_process().name}| pid=|{os.getpid()}| 종료')


if __name__ == '__main__':
    func1()

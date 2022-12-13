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

"""

from multiprocessing import Process


def proc_func():
    pass


def func1():
    process = Process(name='준일', target=proc_func, args=(1,))


if __name__ == '__main__':
    func1()

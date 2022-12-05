"""
- concurrent.futures 는 비동기 실행을 위한 고수준의 API 를 제공한다.
- multi-threading, multi-processing API 가 통일되어 있다.
- GIL(global interpreter lock)의 개념을 알아야 한다. (python 만의 특징)

import os
import time
from concurrent import futures
# futures 안에 다음의 module 들이 사용되고 있다.
# import threading
# import multiprocessing

with futures.ProcessPoolExecutor() as executor
with futures.ThreadPoolExecutor() as executor
executor.map(func, *iterables) => 모두가 실행이 완료되기를 기다린다.

task_list = []
task = executor.submit(fn, /, *args, **kwargs)
task_list.append(task)

ret = futures.wait(task_list, timeout=1) => 시간 제약을 주고 결과를 판단한다.
ret.done, ret.not_done 확인
ret.done[].result()

for m in futures.as_completed(task_list): => 먼저 끝나는 순서대로 결과를 받는다.
    m.result()
    m.done()
    m.cancelled

"""



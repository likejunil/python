"""
- concurrent.futures 는 비동기 실행을 위한 고수준의 API 를 제공한다.
- multi-threading, multi-processing API 가 통일되어 있다.
- GIL(global interpreter lock)의 개념을 알아야 한다. (python 만의 특징)
    . GIL 의 특성 때문에 multi-threading 이 무조건 좋은 것은 아니다. (in python)
    . multi-processing, CPython 에서는 GIL 의 영향을 받지 않는다.

import os
import time
from concurrent import futures
# futures 안에 다음의 module 들이 사용되고 있다.
# import threading
# import multiprocessing

with futures.ProcessPoolExecutor() as executor
with futures.ThreadPoolExecutor() as executor
    # --------------------
    # 첫번째 방법 (하나의 함수를 여러개의 인자로 동시에 실행하고 모두가 완료되기를 기다린다.)
    # --------------------
    result = executor.map(func, *iterables)

    # --------------------
    # 두번째 방법 (시간 제약을 주고 결과를 기다린다.)
    # --------------------
    task_list = []
    task = executor.submit(fn, /, *args, **kwargs)
    task_list.append(task)
    ret = futures.wait(task_list, timeout=10) => 시간 제약을 주고 결과를 판단한다.

    ret.done(성공한 결과들의 목록)
    ret.not_done(성공하지 못한 결과들의 목록)
    m.result() for m in ret.done

    # --------------------
    # 세번째 방법 (무조건 먼저 끝나는 것부터 순서대로 결과를 받는다.)
    # --------------------
    task_list = []
    task = executor.submit(fn, /, *args, **kwargs)
    task_list.append(task)
    for m in futures.as_completed(task_list):
        m.result()
        m.done() -> True | False
        m.cancelled

"""


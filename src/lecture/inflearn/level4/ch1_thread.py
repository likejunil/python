"""
concurrent.futures 는 3.2 이상에서 포함되는 표준 라이브러리이다.

<< mutex 사용하기 >>
lock = threading.Lock()

1) 첫번째 방법
lock.acquire()
...
lock.release()

2) 두번째 방법
with lock:
    ...

<< 생산자, 소비자 패턴 >>
import queue
pipe = queue.Queue(maxsize)
pipe.put(in)
out = pipe.get()
pipe.empty()
pipe.qsize()


event = threading.Event()
event.set() -> 1
event.clear() -> 0
event.wait() -> 1:반환, 0:대기
event.is_set() -> 현재 상태

"""

import logging
import time
from threading import Thread, Lock
from concurrent.futures import ThreadPoolExecutor


def thread_func(*args):
    # map(func, *iterables) 의 경우 첫번째 인자로 주어지는 함수는 인자를 하나만 받을 수 있다.
    # 2개 이상의 인자를 받고 싶으면 tuple 로 묶어서 전달한다.
    # 따라서 tuple 안에 tuple 이 있을 경우를 처리해야 한다.
    get_args = args if len(args) > 1 else args[0]
    name, data = get_args
    logging.info(f'{name} => 쓰레드가 실행되었습니다.')

    s = time.time()
    total: int = 0
    for m1 in data:
        total += m1
    e = time.time()

    logging.info(f'{name} => 쓰레드를 종료합니다. ({e - s:.6f}초 시간 소요)')
    return total


def log():
    # 문자열 출력 방식
    # print('%(fruit)s, %(color)s' % {'fruit': 'apple', 'color': 'red'})
    logging.basicConfig(
        # 메시지 표현 형식
        format='%(asctime)s %(message)s',
        # 메시지 대상 지정
        level=logging.INFO,
        # 시간 표현 형식
        datefmt='%Y-%m-%d %H:%M:%S')


def func1():
    logging.info('main => 쓰레드 공부를 시작합니다.')

    # 인자는 반드시 tuple 로 전달한다.
    # join() 을 호출하지 않아도 sub-thread 는 무사히 진행된다.
    # daemon 옵션은 모든 thread 가 True 여야만 적용된다.
    daemon_opt = False
    t = (Thread(name="red", target=thread_func, args=('준일', range(10_000_000)), daemon=daemon_opt),
         Thread(name="black", target=thread_func, args=('효진', range(20_000_000)), daemon=daemon_opt),
         Thread(name="green", target=thread_func, args=('이강', range(30_000_000)), daemon=daemon_opt))
    logging.info('main => 쓰레드 생성 완료')

    for m in t:
        # m.daemon = True
        m.start()
        logging.info(f'{m.getName()} daemon=|{m.isDaemon()}|')

    logging.info('main => 쓰레드들 실행 완료')

    # 다른 thread 의 종료를 기다릴 것인가?
    for m in t:
        m.join()

    # logging.debug('main(debug) => 쓰레드를 종료합니다.')
    logging.info('main(info) => 쓰레드를 종료합니다.')
    # logging.warning('main(warning) => 쓰레드를 종료합니다.')
    # logging.error('main(error) => 쓰레드를 종료합니다.')
    # logging.critical('main(critical) => 쓰레드를 종료합니다.')


def func2(mode=2):
    logging.info("futures 를 통한 thread handling 학습을 시작합니다.")

    max_workers = 4
    if mode == 1:
        executor = ThreadPoolExecutor(max_workers=max_workers)
        ret1 = executor.submit(thread_func, '준일', range(40_000_000))
        ret2 = executor.submit(thread_func, '효진', range(20_000_000))
        logging.info(f'첫번째 쓰레드 실행 결과=|{ret1.result()}|')
        logging.info(f'두번째 쓰레드 실행 결과=|{ret2.result()}|')
    else:
        args = [
            ('준일', range(10_000_000)),
            ('효진', range(20_000_000))
        ]
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            ret = executor.map(thread_func, args)
            logging.info(list(ret))

    logging.info('main(info) => 쓰레드를 종료합니다.')


def func3():
    """
    << mutex 사용 >>
    . 특정 자원에 대해 2개 이상의 쓰레드가 경합을 벌이는 상황 만들기
    . threading.Lock() 함수 사용
    """

    class A:
        def __init__(self):
            self.value = 0
            self.value_lock = Lock()

        def inc(self, value: int, hell: bool = False) -> int:
            if not hell:
                self.value_lock.acquire()
            # -----------------------------
            self.value += value
            # -----------------------------
            if not hell:
                self.value_lock.release()

    def thread_task(name, obj, count):
        hell = True
        # hell = False
        for m in range(count):
            obj.inc(m, hell)
        print(f'{name}-thread 가 반환하는 결과는 {obj.value}입니다.')
        return obj.value

    a = A()
    f_list = []
    with ThreadPoolExecutor(max_workers=2) as executor:
        f_list.append(executor.submit(thread_task, '준일', a, 1_000_000))
        f_list.append(executor.submit(thread_task, '효진', a, 1_000_000))

    for t in f_list:
        print(t.result())

    print(f'thread 종료, 최종 결과는 {a.value}입니다.')


def func4():
    """
    Queue 와 Event 사용하여 producer, consumer 패턴 사용하기
    """
    pass


if __name__ == '__main__':
    log()
    # func1()
    # func2(2)
    func3()

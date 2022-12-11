"""
"""

import sys
import logging
from threading import Thread
import time


def thread_func(name: str, data):
    logging.info(f'{name} => 쓰레드가 실행되었습니다.')

    s = time.time()
    total: int = 0
    for m1 in data:
        total += m1
    e = time.time()

    logging.info(f'{name} => 쓰레드를 종료합니다. ({e - s:.6f}초 시간 소요)')


if __name__ == '__main__':
    # 문자열 출력 방식
    print('%(fruit)s, %(color)s' % {'fruit': 'apple', 'color': 'red'})
    logging.basicConfig(
        # 메시지 표현 형식
        format='%(asctime)s %(message)s',
        # 메시지 대상 지정
        level=logging.INFO,
        # 시간 표현 형식
        datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('main => 쓰레드 공부를 시작합니다.')

    # 인자는 반드시 tuple 로 전달한다.
    # join() 을 호출하지 않아도 sub-thread 는 무사히 진행된다.
    # daemon 옵션은 모든 thread 가 True 여야만 적용된다.
    t1 = Thread(target=thread_func, args=('준일', range(1_000_000)), daemon=True)
    t2 = Thread(target=thread_func, args=('효진', range(2_000_000)), daemon=True)
    t3 = Thread(target=thread_func, args=('이강', range(3_000_000)), daemon=True)
    logging.info('main => 쓰레드 생성 완료')

    for m in (t1, t2, t3):
        # m.daemon = True
        m.start()
        print(f'{m.getName()} daemon=|{m.isDaemon()}|')
    logging.info('main => 쓰레드들 실행 완료')

    # 다른 thread 의 종료를 기다릴 것인가?
    # for m in t:
    #     m.join()

    # logging.debug('main(debug) => 쓰레드를 종료합니다.')
    logging.info('main(info) => 쓰레드를 종료합니다.')
    # logging.warning('main(warning) => 쓰레드를 종료합니다.')
    # logging.error('main(error) => 쓰레드를 종료합니다.')
    # logging.critical('main(critical) => 쓰레드를 종료합니다.')

    # sys.exit()

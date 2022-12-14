"""
<< thread_local >>
threading.local()
쓰레드마다 독립적인 공간에 제공되는 객체이다.

"""
import threading

import requests
import time
from concurrent.futures import ThreadPoolExecutor

max_workers = 3
# threading.local() 은 쓰레드마다 독립적으로 사용하는 객체를 제공한다.
thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, 'session'):
        thread_local.session = requests.Session()
        print(f'type(thread_local)=|{type(thread_local)}|\n'
              f'isinstance(thread_local, dict)=|{isinstance(thread_local, dict)}|')
    return thread_local.session


def request_site(url):
    session = get_session()
    # print(f'session.headers=|{session.headers}|')

    with session.get(url) as res:
        print(f'url=|{url}| 수신 상태=|{res.status_code}| 수신받은 데이터의 길이=|{len(res.content)}|')


def request_all_sites(urls):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 모두가 완료될 때까지 기다린다.
        executor.map(request_site, urls)


def main():
    s_time = time.time()
    # ---------------------------------------------------------
    urls = [
               'https://naver.com',
               'https://google.com',
               'https://daum.net',
           ] * 5
    request_all_sites(urls)
    # ---------------------------------------------------------
    e_time = time.time()

    print(f'총 소요시간={e_time - s_time:.6f}')


def assgn():
    class A:
        def __init__(self, value):
            self.value = value

    a = A(9)
    print(a.value)
    a.value2 = 10
    print(a.value2)
    """
    # 객체의 속성을 다음과 같이 추가하는 것은 TypeError 를 발생시킨다.
    # a['value2'] = 11
    """

    """
    dict 를 생성하는 방법은 다음과 같이 3가지가 있다.
    """
    d1 = dict([('a', 1), ('b', 2)])
    d2 = dict(a=1, b=2)
    d3 = {'a': 1, 'b': 2}
    print(d1['a'])
    """
    dict 의 경우 다음과 같이 속성에 접근할 수는 없다.
    # print(d1[a])
    # print(d1.a)
    """


if __name__ == '__main__':
    main()
    # assgn()

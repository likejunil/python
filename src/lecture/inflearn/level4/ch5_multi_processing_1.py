import os
import time
import multiprocessing
from concurrent.futures import ProcessPoolExecutor
import requests

session = None
max_process = 10


def set_global_session():
    print(f'몇 번 호출되었을까?')
    global session
    if session is None:
        session = requests.Session()


def request_site(url):
    if session is None:
        print(f'누가 이곳을 지나갈 것인가?')
        set_global_session()

    with session.get(url) as res:
        print(f'url=|{url}| 수신 상태=|{res.status_code}| 수신받은 데이터의 길이=|{len(res.content)}|')


def request_all_sites_1(urls):
    # initializer 는 각각의 프로세스가 실행되기 전에 실행해야 할 작업을 담고 있다.
    print(f'현재 본 컴퓨터는 {os.cpu_count()}개의 cpu 를 갖고 있습니다.')
    with multiprocessing.Pool(initializer=set_global_session, processes=max_process) as pool:
        # 모두가 완료될 때까지 기다린다.
        pool.map(request_site, urls)


def request_all_sites_2(urls):
    print(f'현재 본 컴퓨터는 {os.cpu_count()}개의 cpu 를 갖고 있습니다.')
    with ProcessPoolExecutor(max_workers=max_process) as pool:
        # 모두가 완료될 때까지 기다린다.
        pool.map(request_site, urls)


def main():
    s_time = time.time()
    # ---------------------------------------------------------
    urls = [
               'https://naver.com',
               'https://google.com',
               'https://daum.net',
           ] * 5
    request_all_sites_1(urls)
    # request_all_sites_2(urls)
    # ---------------------------------------------------------
    e_time = time.time()

    print(f'총 소요시간={e_time - s_time:.6f}')


if __name__ == '__main__':
    main()

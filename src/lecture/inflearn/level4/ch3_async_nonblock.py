"""
<< non-block, async >>
서비스를 요청하는 쪽과 서비스를 처리하는 쪽이 존재한다.
client, server
block, non-block
sync, async

<< cpu-bound, io-bound >>


<< requests >>
. HTTP 를 사용하기 위해 사용하는 python library

요청 함수
requests.post()
requests.put()
requests.delete()
res = requests.get()

여러가지 상태 정보를 유지하고 싶다면 Session 사용
s = requests.Session()
s.get()
한 번 생성한 session 은 재사용이 가능하다.

함수 파라미터 종류
params <= get, query string
data <= post, application/x-www-form-urlencoded
json <= post, application/json
headers
cookies
timeout

응답
res.status_code
res.headers
res.context
res.text <= utf-8
res.encoding
res.json()
res.cookies

"""

import requests
import time


def request_site(url, session):
    print(f'session.headers|{session.headers}|')
    with session.get(url) as res:
        print(f'url=|{url}| 수신 상태=|{res.status_code}| 수신받은 데이터의 길이=|{len(res.content)}|')


def request_all_sites(urls):
    with requests.Session() as s:
        for u in urls:
            request_site(u, s)


def main():
    s_time = time.time()
    # ---------------------------------------------------------
    urls = [
        'https://naver.com',
        'https://google.com',
        'https://daum.net',
    ]
    request_all_sites(urls)
    # ---------------------------------------------------------
    e_time = time.time()

    print(f'총 소요시간={e_time - s_time:.6f}')


if __name__ == '__main__':
    main()

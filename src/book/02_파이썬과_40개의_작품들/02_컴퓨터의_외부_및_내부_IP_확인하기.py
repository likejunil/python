"""
컴퓨터의 외부 및 내부 IP 를 확인하는 방법을 학습한다.
"""

import socket


def get_ip_address() -> str:
    """
    호스트 이름을 통해 로컬 주소를 확인한다.

    :return: 로컬 주소
    """
    host_name = socket.gethostname()
    ip_addr = socket.gethostbyname(host_name)
    # print(f'컴퓨터 이름=|{host_name}|')
    # print(f'호스트 정보(IP 주소)=|{ip_addr}|')
    return ip_addr


def get_ip_address_by_conn(addr: str, port: int) -> str:
    """
    - 원격에 접속하여 socket 을 생성한다.
    - socket 을 통해 로컬 ip-addr 을 확인한다.

    :param addr: 접속할 원격 주소
    :param port: 접속할 원격 포트
    :return: 로컬 주소
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((addr, port))
    # print(f'접속 디스크립터=|{sock}|')
    # print(dir(sock))
    # print(f'원격 주소=|{sock.getpeername()}|')
    # print(f'로컬 주소-|{sock.getsockname()}|')
    return sock.getsockname()[0]


if __name__ == "__main__":
    addr1 = get_ip_address()
    print(f'|{addr1}|')

    google_addr = "www.google.co.kr"
    google_port = 443
    addr2 = get_ip_address_by_conn(google_addr, google_port)
    print(f'|{addr2}|')

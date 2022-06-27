import requests
from bs4 import BeautifulSoup, element
from datetime import datetime
import time

# -----------------------
# variable
# -----------------------
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
}


# -----------------------
# function
# -----------------------
def request_naver(arg_code: str, arg_page: int) -> BeautifulSoup:
    """
    naver에 주식 일일 시세를 조회한다.

    :param arg_code: 6자리 종목 코드 ex) "005930", "000660"
    :param arg_page: 페이지 정보 ex) 1, 2
    :return: BeautifulSoup 객체
    """
    url = "https://finance.naver.com/item/sise_day.naver"
    ret = requests.get(url="{}?code={}&page={}".format(url, arg_code, arg_page), headers=headers)
    if ret.status_code == 200:
        return BeautifulSoup(ret.text, 'html.parser')


def get_tr_list(arg_soup: BeautifulSoup) -> element.ResultSet:
    """
<<<<<<< HEAD
    인자로부터 첫번째 <table class='type2'> 태그를 찾고..
    해당 table 에 종속된

    :param arg_soup:
    :return:
=======
    table.type2 태그로부터 tr.onmouseover='mouseOver(this) 태그들을 검색하여 반환한다.

    :param arg_soup: parsing 된 html 데이타
    :return: tr 태그들을 담은 ResultSet
>>>>>>> 5d25d49dc3798c093423a7402ee01aef13af8d77
    """
    table_attr_class = "type2"
    tr_attr_dict = {'onmouseover': 'mouseOver(this)'}

    return arg_soup.find("table", class_=table_attr_class) \
        .find_all("tr", attrs=tr_attr_dict)


def get_td_list_from_tr_list(arg_list: list, tr_elements: element.ResultSet):
    """
    주어진 tr_list 로부터 td 들을 검색하고 내용을 list 에 담아 반환한다.

    :param arg_list: td 의 text 를 담을 list
    :param tr_elements: td 를 검색할 대상 tr_list
    :return: td 의 text 가 "" 일 경우 함수 종료
    """
    for tr in tr_elements:
        td_elements = tr.select("td")
        ret = []
        for td in td_elements:
            td_data = td.text.strip()
            if td_data == "":
                return
            ret.append(td_data)
        arg_list.append(ret)


def convert_data(arg_list: list):
    """
    주어진 행렬(이중 list) 에서 데이터를 하나씩 꺼내어 변환 후 다시 저장한다.
    첫 번째 데이터는 날짜 타입으로 변환하고 그 외의 것들은 숫자 타입으로 변환한다.
    날짜 타입으로 변환할 데이터는 "2022.03.15" 와 같은 문자열이다.
    숫자 타입으로 변환할 데이터는 "33,336" 와 같은 문자열이다.

    :param arg_list: 행렬(이중 list)
    :return:
    """
    for d1 in arg_list:
        for i, d2 in enumerate(d1):
            if i == 0:
                d1[i] = datetime.strptime(d2, "%Y.%m.%d")
            else:
                d1[i] = int(d2.replace(",", ""))


def get_key_list(arg_list: list, arg_i: int) -> set:
    """
    주어진 행렬(이중 list) 에서 특정 컬럼의 값들을 set 에 저장하여 반환한다.
    특정 컬럼의 값들을 기준으로, 주어진 행렬과 다른 행렬이 같은지 다른지 확인한다.

    :param arg_list: 행렬(이중 list)
    :param arg_i: 특정 컬럼의 index
    :return: 특정 컬럼들을 모아 생성한 set
    """
    ret = set()
    for data in arg_list:
        ret.add(data[arg_i])
    return ret


def get_data_by_page(arg_code: str, arg_page: int) -> list:
    """
    naver 에 일일 시세(특정 종목의 특정 페이지)를 조회하여 list 로 생성 및 반환한다.

    :param arg_code: 조회하려는 종목의 코드 6자리
    :param arg_page: 조회하려는 페이지
    :return: 시세 종목을 담은 list
    """
    # 총 10일치의 데이터
    page_data_list = []
    soup = request_naver(arg_code, arg_page)
    tr_list = get_tr_list(soup)
    get_td_list_from_tr_list(page_data_list, tr_list)
    convert_data(page_data_list)
    return page_data_list


def get_data_by_page_with_wait(arg_code: str, arg_page: int, sec: int) -> list:
    """
    naver 에 일일 시세(특정 종목의 특정 페이지)를 조회하여 list 로 생성 및 반환한다.
    조회를 완료한 후 주어진 시간만큼 대기한다.

    :param arg_code: 조회하려는 종목의 코드 6자리
    :param arg_page: 조회하려는 페이지
    :param sec: 조회를 완료하고 주어진 시간만큼 대기
    :return: 시세 종목을 담은 list
    """
    ret = get_data_by_page(arg_code, arg_page)
    time.sleep(sec)
    return ret


def get_code_func():
    """
    종목 코드 목록을 불러와서 로컬 변수에 담는다.
    종목 코드를 하나씩 불러서 반환하는 함수를 반환한다.

    :return:
    """
    # 추후 외부에서 종목 코드 목록을 불러오는 방법으로 수정한다.
    item_code_list: list = ["005930"]
    index: int = 0

    def pick() -> list:
        nonlocal index
        if index >= len(item_code_list):
            return ""
        ret = item_code_list[index]
        index += 1
        return ret

    return pick


def days_proc(arg_code: str):
    """
    data 디렉토리에서 해당 종목의 파일을 연다.
    가장 최근 데이터의 날짜를 확인한다.
    최근 데이터의 날짜와 오늘 날짜를 기준으로 조회해야 할 데이터의 날짜를 정한다.
    데이터를 조회한다.
    조회한 데이터를 파일에 기록한다.

    :param arg_code: 조회할 종목의 코드
    :return:
    """

    # ------------------------
    # 1. 파일을 연다.
    # ------------------------

    # total_data_list: list = []
    # prev_key_set: set = set()
    #
    # page: int = 1
    #
    # data_list = get_data_by_page(arg_code, page)
    # key_set = get_key_list(data_list, 0)
    # if prev_key_set == key_set:
    #     return
    # prev_key_set = key_set
    # page += 1
    # for d in data_list:
    #     total_data_list.append(d)


# -----------------------
# main
# -----------------------
if __name__ == "__main__":
    """
    본 소스의 목적은 매일 코스피, 코스닥 종목들에 대하여 일일 시세(시고저종)를 불러와서 파일로 저장하는 것이다.
    data 디렉토리에 종목별로 별도의 파일이 존재한다.
    """
    pick_code = get_code_func()
    while True:
        code: str = pick_code()
        if code == "":
            break
        days_proc(code)

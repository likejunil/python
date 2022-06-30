import requests
from bs4 import BeautifulSoup, element
from datetime import datetime
import time
import pandas as pd

# -----------------------
# variable
# -----------------------
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
}

NO_DATA: str = ""


# -----------------------
# function
# -----------------------
def request_day_sise_to_naver(arg_code: str, arg_page: int) -> BeautifulSoup:
    """
    naver 에 주식 일일 시세를 조회한다.\n
    함수 내부에 url 을 갖고 있다.\n
    종목 코드와 페이지 번호를 인자로 받기 때문에 모든 일일 시세를 확보할 수 있다.\n

    :param arg_code: 6자리 종목 코드
    :param arg_page: 페이지 번호
    :return: BeautifulSoup 객체
    """
    url = "https://finance.naver.com/item/sise_day.naver"
    ret = requests.get(url="{}?code={}&page={}".format(url, arg_code, arg_page), headers=headers)
    if ret.status_code == 200:
        return BeautifulSoup(ret.text, 'html.parser')


def get_tr_list(arg_soup: BeautifulSoup) -> element.ResultSet:
    """
    첫 번째 table 로부터 tr 들을 검색하여 반환한다.\n
    table 과 tr 선택 기준은 태그의 속성에 따른다.\n
    속성 정보는 본 함수의 변수에 문자열 상수로 담겨 있다.\n

    :param arg_soup: table 데이터가 담긴 BeautifulSoup
    :return: tr 태그들을 담은 ResultSet
    """
    table_attr_class = "type2"
    tr_attr_dict_key = "onmouseover"
    tr_attr_dict_value = "mouseOver(this)"

    # ret = arg_soup.select_one("table.{}".format(table_attr_class)) \
    #     .select("tr[{}='{}']".format(tr_attr_dict_key, tr_attr_dict_value))
    ret = arg_soup.find("table", class_=table_attr_class) \
        .find_all("tr", attrs={tr_attr_dict_key: tr_attr_dict_value})
    return ret


def get_td_list_from_tr_list(arg_list: list, tr_elements: element.ResultSet):
    """
    인자로 tr 목록이 주어진다.(tr_elements: bs4.element.ResultSet)\n
    각각의 tr 에 대하여 td 들을 뽑아낸다.(bs4.element.Tag)\n
    td 태그의 value 들을 모아서 list 를 만든다.(list)\n
    td 태그의 value 중에 하나라도 "" 가 나타나면 함수를 종료한다.\n
    list 를 arg_list 에 담는다.(list[list])\n

    :param arg_list: td 의 value(text) 를 모은 list 를 담을 list
    :param tr_elements: td 를 검색할 대상 tr 목록
    :return: td 의 value(text) 가 "" 일 경우 함수 종료
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


def convert_naver_day_sise(arg_list: list):
    """
    주어진 행렬(이중 list) 에서 데이터를 하나씩 꺼내어 변환 후 다시 저장한다.\n
    첫 번째 데이터는 날짜 타입으로 변환하고 그 외의 것들은 숫자 타입으로 변환한다.\n
    날짜 타입으로 변환할 데이터는 "2022.03.15" 와 같은 날짜 정보의 문자열이다.\n
    숫자 타입으로 변환할 데이터는 "33,336" 와 같이 쉼표를 포함한 숫자들의 문자열이다.\n

    :param arg_list: 행렬(이중 list)
    :return:
    """
    l1: list
    for l1 in arg_list:
        for i, d1 in enumerate(l1):
            # ------------------------------
            # 첫 번째 데이터는 날짜 타입으로 변환
            # ------------------------------
            if i == 0:
                l1[i] = datetime.strptime(d1, "%Y.%m.%d")
            else:
                l1[i] = int(d1.replace(",", ""))


def get_key_list(arg_list: list, arg_i: int) -> set:
    """
    주어진 행렬(이중 list)에서 특정 컬럼의 값들을 뽑아내어 set 으로 반환한다.\n
    특정 컬럼의 값들을 기준으로 주어진 행렬과 다른 행렬이 같은지 다른지 확인한다.\n

    :param arg_list: 행렬(이중 list)
    :param arg_i: 선택하려는 컬럼의 index
    :return: 선택한 컬럼들을 모아 생성한 set
    """
    ret = set()
    for l1 in arg_list:
        ret.add(l1[arg_i])
    return ret


def get_days_sise_by_page(arg_code: str, arg_page: int) -> pd.DataFrame:
    """
    naver 에 일일 시세(특정 종목의 특정 페이지)를 조회하여 list 로 생성 및 반환한다.\n

    :param arg_code: 조회하려는 종목의 코드 6자리
    :param arg_page: 조회하려는 페이지
    :return: 시세 종목을 담은 pd.DataFrame
    """
    # 총 10일치의 데이터
    ret_list = []
    soup = request_day_sise_to_naver(arg_code, arg_page)
    tr_list = get_tr_list(soup)
    get_td_list_from_tr_list(ret_list, tr_list)
    convert_naver_day_sise(ret_list)
    ret = pd.DataFrame(ret_list)
    return ret


def get_code_func():
    """
    종목 코드 목록을 불러와서 로컬 변수에 담는다.\n
    종목 코드를 하나씩 불러서 반환하는 함수를 반환한다.\n

    :return: 종목 코드를 하나씩 불러오는 함수를 반환한다.
    """
    # 추후 외부에서 종목 코드 목록을 불러오는 방법으로 수정한다.
    item_code_list: list = ["005930"]
    index: int = 0

    def pick() -> list:
        nonlocal index
        if index >= len(item_code_list):
            return NO_DATA
        ret = item_code_list[index]
        index += 1
        return ret

    return pick


def days_proc(arg_code: str) -> None:
    """
    data 디렉토리에서 해당 종목의 파일을 연다.\n
    가장 최근 데이터의 날짜를 확인한다.\n
    데이터가 아무것도 없다면 1980년 1월 3일을 가장 최근의 날짜로 간주한다.\n
    (최근 데이터 날짜 < date <= 오늘 날짜) 시세 정보를 조회한다.\n
    조회한 데이터를 파일에 기록한다.\n

    :param arg_code: 조회할 종목의 코드
    :return:
    """
    # 1. 파일을 연다.
    # ------------------------
    file_name: str = "./data/{}.csv".format(arg_code)
    pd.read_csv(file_name)

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
    '''
    본 소스의 목적은 매일 코스피, 코스닥 종목들에 대하여 일일 시세(시고저종)를 불러와서 파일로 저장하는 것이다.\n
    data 디렉토리에 종목별로 별도의 파일이 존재한다.\n
    '''
    pick_code = get_code_func()
    while True:
        code: str = pick_code()
        if code == NO_DATA:
            break
        days_proc(code)

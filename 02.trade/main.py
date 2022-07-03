import requests
from bs4 import BeautifulSoup, element
from datetime import datetime
import pandas as pd

# -----------------------
# variable
# -----------------------
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
}

NO_DATA: str = ""
DATE: str = "날짜"
CLOSE: str = "종가"
OPEN: str = "시가"
HIGH: str = "고가"
LOW: str = "저가"
VOLUME: str = "거래량"
DIFF: str = "전일비"
COLUMNS = [DATE, CLOSE, DIFF, OPEN, HIGH, LOW, VOLUME]


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
    ret = pd.DataFrame(ret_list, columns=COLUMNS)
    return ret


def load_data(arg_filename: str) -> pd.DataFrame:
    """
    시세 데이터가 담겨 있는 csv 파일을 읽어서 DataFrame 을 생성 반환한다.
    DATE 컬럼을 datetime 타입으로 변환한다.
    datetime 타입을 파일에 기록하면 str 으로 변환되기 때문이다.
    만약 DATE 컬럼에 대하여 오름차순으로 정렬한다.

    :param arg_filename: 읽고자 하는 파일의 이름
    :return: 파일의 내용이 담긴 DataFrame 객체
    """
    df = pd.read_csv(arg_filename)
    df[DATE] = pd.to_datetime(df[DATE])
    return df.sort_values(by=DATE, ascending=True, na_position='last')


def save_data(arg_filename: str, arg_df: pd.DataFrame) -> None:
    """
    DataFrame 의 index 를 DATE 로 변경한다.
    DataFrame 을 파일에 저장한다.

    :param arg_filename: DataFrame 을 저장할 파일의 이름
    :param arg_df: 파일에 저장할 DataFrame 객체
    :return:
    """
    if arg_df.index.name is None:
        arg_df = arg_df.set_index(DATE)
    elif arg_df.index.name != DATE:
        arg_df = arg_df.reset_index().set_index(DATE)
    arg_df.sort_values(by=DATE, ascending=True, na_position='last').to_csv(arg_filename)


def load_code_list() -> list[str]:
    """
    추후 종목 목록을 외부에서 불러와 넘겨준다.\n

    :return: 코스피, 코스닥 시장의 종목 코드를 담은 list
    """
    return ["005930", "000660"]


def get_code_func():
    """
    종목 코드 목록을 불러와서 로컬 변수에 담는다.\n
    종목 코드를 하나씩 불러서 반환하는 함수를 반환한다.\n

    :return: 종목 코드를 하나씩 불러오는 함수를 반환
    """
    item_code_list: list = load_code_list()
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
    load_df = load_data("{}.csv".format(arg_code))
    last_date = load_df.iloc[-1][DATE]

    page: int = 1
    while True:
        new_df: pd.DataFrame = get_days_sise_by_page(arg_code, page)
        cond: bool = new_df[DATE] == last_date
        if len(new_df[cond]) > 0:
            break


def main_proc():
    """
    본 소스의 목적은 매일 코스피, 코스닥 종목들에 대하여 일일 시세(시고저종)를 불러와서 파일로 저장하는 것이다.\n
    data 디렉토리에 종목별로 별도의 파일이 존재한다.\n

    :return:
    """
    pick_code = get_code_func()
    while True:
        ret_code: str = pick_code()
        if ret_code == NO_DATA:
            break
        days_proc(ret_code)


# -----------------------
# main
# -----------------------
if __name__ == "__main__":
    main_proc()

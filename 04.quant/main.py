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
    table_attr_class = "type2"
    tr_attr_dict = {'onmouseover': 'mouseOver(this)'}

    return arg_soup.find("table", class_=table_attr_class) \
        .find_all("tr", attrs=tr_attr_dict)


def get_td_list_from_tr_list(arg_list: list, tr_elements: element.ResultSet):
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
    for d1 in arg_list:
        for i, d2 in enumerate(d1):
            if i == 0:
                d1[i] = datetime.strptime(d2, "%Y.%m.%d")
            else:
                d1[i] = int(d2.replace(",", ""))


def get_key_list(arg_list: list, arg_i: int) -> set:
    ret = set()
    for data in arg_list:
        ret.add(data[arg_i])
    return ret


def get_data_page(arg_page: int) -> list:
    # 총 10일치의 데이터
    page_data_list = []
    soup = request_naver(code, arg_page)
    tr_list = get_tr_list(soup)
    get_td_list_from_tr_list(page_data_list, tr_list)
    convert_data(page_data_list)
    return page_data_list


def get_data_by_page_with_wait(arg_page: int, sec: int) -> list:
    ret = get_data_page(arg_page)
    time.sleep(sec)
    return ret


# -----------------------
# main
# -----------------------
if __name__ == "__main__":
    code: str = "005930"

    total_data_list: list = []
    prev_key_set: set = set()

    page: int = 651
    wait_time: int = 1
    while True:
        data_list = get_data_by_page_with_wait(page, wait_time)
        key_set = get_key_list(data_list, 0)
        if prev_key_set == key_set:
            break
        prev_key_set = key_set
        page += 1
        for d in data_list:
            total_data_list.append(d)

    print(total_data_list)

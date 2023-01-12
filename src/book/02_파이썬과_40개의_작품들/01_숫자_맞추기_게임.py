"""
1부터 100사이의 임의의 수를 생성하고 생성된 임의의 수를 맞추는 게임
임의의 숫자를 입력하면 생성된 숫자보다 높은지 낮은지 혹은 정답인지를 알려준다.
정답을 맞힌 경우 몇 번 만에 맞추었는지 결과를 알려준다.
"""

from random import randint


def generate_number(min_val: int = 1, max_val: int = 99):
    """
    임의의 숫자를 생성하고 반환한다.

    :param min_val: 임의의 숫자 최소값
    :param max_val: 임의의 숫자 최대값
    :return: 생성된 임의의 숫자
    """
    r = randint(min_val, max_val)
    # print(f'{r} 값을 생성하였습니다.')
    return r


def _read_number():
    """
    - 사용자로부터 키보드를 통해 숫자를 읽는 클로저 함수를 생성하고 반환한다.
    - 사용자로부터 숫자를 읽은 횟수를 로컬 영역에 저장한다.

    :return: 클로저 함수
    """
    try_count = 0

    def f():
        """
        사용자로부터 키보드를 통해 숫자를 읽는다.

        :return: 사용자가 입력한 숫자
        """
        nonlocal try_count
        try_count += 1
        say = f'{try_count}번째 도전입니다. 숫자를 맞춰보세요.'

        while True:
            i = input(say)
            try:
                n = int(i)
            except ValueError as e:
                print(f'에러가 발생했습니다. 메시지=|{e}|')
                print(f'숫자를 입력해 주세요.')
            else:
                print(f'{n}을 입력하셨습니다.')
                return n

    return f


def _is_correct(answer):
    """
    사용자가 제시한 숫자와 정답을 비교하는 클로저 함수를 생성하고 반환한다.

    :param answer: 정답 숫자
    :return: 클로저 함수
    """
    correct = answer

    def f(guess):
        """
        - 사용자가 제시한 숫자가 정답인지 확인한다.
        - 정답이 아닐 경우 대소 비교 정보를 제공한다.

        :param guess: 사용자가 제시한 숫자
        :return: 정답 여부
        """
        if correct == guess:
            print(f'{guess}! 정답입니다.')
            return True
        elif correct > guess:
            print(f'{guess}(은)는 정답보다 낮은 숫자입니다.\n')
            return False
        elif correct < guess:
            print(f'{guess}(은)는 정답보다 높은 숫자입니다.\n')
            return False

    return f


def main_proc(target):
    """
    사용자로부터 숫자를 읽고 정답과 비교하며 게임을 진행한다.

    :param target: 맞추어야 할 숫자
    """
    read_number = _read_number()
    is_correct = _is_correct(target)

    while True:
        guess = read_number()
        correct = is_correct(guess)
        if correct:
            break


def number_game():
    """
    - 임의의 숫자를 생성한다.
    - 사용자로부터 임의의 숫자를 입력 받는다.
    - 사용자가 도전한 횟수를 기록한다.
    - 정답과 비교하여 높은지 낮은지 정답인지 판단한다.
    - 해당 결과를 알려준다.
    """
    target = generate_number()
    main_proc(target)


if __name__ == "__main__":
    number_game()

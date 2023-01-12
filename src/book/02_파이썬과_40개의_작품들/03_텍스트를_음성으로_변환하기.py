"""
gtts(google translate text to speech) 는 문자를 음성으로 변환해주는 라이브러리이다.
playsound 는 mp3 를 파이썬에서 재생해주는 라이브러리이다.
playsound 의 경우 PyObjC 를 필요로 한다.
"""

from gtts import gTTS
from playsound import playsound


def play_text(_text: str):
    """
    - 인자로 주어진 텍스트를 mp3 로 변환하여 저장한다.
    - 저장한 mp3 파일을 음성으로 출력한다.

    :param _text: 음성으로 변환할 텍스트
    """
    mp3_name = './sample.mp3'
    tts = gTTS(text=_text, lang='ko')
    tts.save(mp3_name)
    playsound(mp3_name)


def play_file(file_path: str):
    """
    - 인자로 주어진 파일을 읽어서 play_text 함수를 호출한다.

    :param file_path: 텍스트를 읽을 파일 이름
    """
    with open(file_path, 'rt', encoding='utf8') as f:
        read = f.read()
    play_text(read)


if __name__ == "__main__":
    filename = './sample.txt'
    play_file(filename)

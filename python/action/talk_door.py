#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class TalkDoor(ActionBase):

    REST_DURATION = 2 * 60.
    SERIFS = [
        "のれんの、のはノリがよいの、のじゃ",
        "のれんの、れはレインボーの、れじゃ",
        "のれんの、んはウィンドウの、んじゃ",
        "オイラが若いころはこんなにたくさん人はいなかったのう",
        "オイラも長く生きたもんじゃのぅ",
        "オイラも若いこと仲良くしたいのう。インスタとかいうストーリーに上げてくれんかのう？？",
        "のれん占い！今日はてんびん座の人が一位じゃ！",
    ]

    def __init__(self, speaker):
        super(TalkDoor, self).__init__(speaker)

    def check(self, data):
        # 入り口側、人がいる
        duration = data["now"] - self._last_running_time
        is_exist = data["motions"][1] > 0

        return duration > self.REST_DURATION and is_exist and random.random() > .5

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif

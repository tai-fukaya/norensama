#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class HelloGuide(ActionBase):

    # 1min
    REST_DURATION = 60.
    SERIFS = [
        "のれんクーイズ！家の軒下、店の上部に横に長く張られたのれんを何のれんという？正解は水引きのれん！",
        "のれんクーイズ！切り込みの垂れをつけず、大風呂敷のような一枚布で、上端を軒先に、下端を道路側にせり出させて固定したのれんを何のれんという？",
        "のれんには、のれん！",
        "日本橋には日本初の百貨店が生まれ、中央通りはいつも賑やかじゃったよ",
        "日本橋の魚市場は、そら賑やかじゃったよ。現在の豊洲市場も見て見たいのお",
        "日本橋は、江戸時代、パリやロンドンよりも巨大な、世界屈指の都市だったんじゃ",
        "日本橋は、明治以降は金融期間が集中する日本経済の中心地じゃったよ",
        "日本橋は五街道の起点なんじゃ",
        "日本橋は最近、再び栄えているように思えるのー",
        # "日本銀行本店は、1974年に国の重要文化財指定されたんじゃ",
    ]

    def __init__(self, speaker):
        super(HelloGuide, self).__init__(speaker)

    def check(self, data):
        # 案内側、人が入る
        duration = data["now"] - self._last_running_time
        is_in = data["motions"][0] == 1

        return duration > self.REST_DURATION and is_in and random.random() > .3

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif

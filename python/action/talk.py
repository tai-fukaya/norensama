#-*-coding:utf-8-*-
import random
import time

from action_base import ActionBase

class Talk(ActionBase):

    REST_DURATION = 60.
    SERIFS = [
        "茶色ののれんは、タバコ屋に多かったのじゃぞ",
        "白いのれんはお菓子やさんか、薬屋さんに多かったのじゃぞ",
        "藍色ののれんは。酒屋や呉服屋に多かったのじゃぞ",
        "オイラはのれんさまである。名前はまだ無い。気づいたらのれんになっておった",
        "おなかすいたんじゃ",
        "本当に大事なものは、意外とすぐ近くにあるのじゃぞ",
        "あんたは、のれん語が、わかるのか！？",
        "オイラもツイッターをはじめてみたんじゃ",
        "オイラが見えるのか？",
        "のれんになった気持ちがわかるか？",
        "神様、仏様、のれんさま、なのじゃ",
        "この場所も変わったのう、じゃが、今も、いい街じゃ。",
        "実はこの暖簾日本で一番大きいかもしれんのじゃ",     
        "嫌なことがあっても、すぐに風に揺られて忘れてしまうのじゃ",
        "みんなコレドに集合ー！",
        "みんなに話しかけられてオイラは幸せ者じゃ",
        "映画を見てみたいのう",
        "世界中からオイラに会いに来ないかのう",
        "江戸の奴らは細かい事にはこだわらず、意地っ張りで喧嘩早く、駄洒落ばかり言い、涙にもろく正義感に溢れる、そんな奴らばかりじゃった",
    ]

    def __init__(self, speaker):
        super(Talk, self).__init__(speaker)

    def check(self, data):
        # 人がいる
        duration = data["now"] - self._last_running_time
        is_exist = sum(data["motions"]) > 0

        return duration > self.REST_DURATION and is_exist and random.random() > .5

    def run(self, data):
        serif = self.SERIFS[int(random.random()*len(self.SERIFS))]
        self._sp.say(serif)
        time.sleep(1.)
        self._last_running_time = time.time()

        return serif

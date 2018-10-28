#-*-coding:utf-8-*-
import random
import threading
import time

import _secret as config
# StatusManager
from status import StatusManager

from speaker import Speaker
from ifttt import Ifttt
# Action
from action import Yureyure, Hello, Joke, TimeSignal, ForceSpeak, CoredoIntroduction, CoredoIntroductionAM9, CoredoIntroductionLunch, CoredoIntroductionNight, CoredoBoyaki, CoredoAnswerHanashi, CoredoAnswerAisatsu, CoredoAnswerSonota, CoredoIntroductionNight, CoredoBoyaki, CoredoAnswerHanashi, CoredoAnswerAisatsu, CoredoAnswerDare, CoredoAnswerIkku, CoredoAnswerGehin, CoredoAnswerSize, CoredoAnswerToshi, Month11day1, Month11day2, Month11day3, Month11day4, Month11day5, Month11day6, Month11day7, Month11day8, Month11day9, Month11day10, Month11day11
from action.blow import Yurayura, Soyosoyo, Byubyu


class Norensama(object):

    def __init__(self):
        self._speaker = Speaker()
        self._ifttt = Ifttt({
            "api_key": config.IFTTT_APIKEY
        })

        self._status = StatusManager()
        self._actions = [
            Yureyure(self._speaker),
            Hello(self._speaker),
            Joke(self._speaker),
            TimeSignal(self._speaker),
            CoredoIntroduction(self._speaker),
            CoredoIntroductionAM9(self._speaker),
            CoredoIntroductionLunch(self._speaker),
            CoredoIntroductionNight(self._speaker),
            CoredoBoyaki(self._speaker),
            CoredoAnswerHanashi(self._speaker),
            CoredoAnswerAisatsu(self._speaker),
            CoredoAnswerSonota(self._speaker),
            CoredoAnswerDare(self._speaker),
            CoredoAnswerIkku(self._speaker),
            CoredoAnswerGehin(self._speaker),
            CoredoAnswerSize(self._speaker),
            CoredoAnswerToshi(self._speaker),
            Month11day1(self._speaker),
            Month11day2(self._speaker),
            Month11day3(self._speaker),
            Month11day4(self._speaker),
            Month11day5(self._speaker),
            Month11day6(self._speaker),
            Month11day7(self._speaker),
            Month11day8(self._speaker),
            Month11day9(self._speaker),
            Month11day10(self._speaker),
            Month11day11(self._speaker),
        ]
        self._blow_actions = [
            # よわい
            Soyosoyo(self._speaker),
            # 横揺れ
            Yurayura(self._speaker),
            # 波
            Byubyu(self._speaker)
        ]
        # セリフの強制実行
        self._force_speak_action = ForceSpeak(self._speaker)

        self._blow_action_index = 1

    def select_blow_action(self, data = {}):
        acc = data.get("accelerometer")
        if acc is None:
            return
        self._blow_action_index = acc.get("status", 0)

    def main(self):
        print("main")
        status_thread = threading.Thread(target=self._status.update)
        status_thread.daemon = True
        status_thread.start()

        self._status.set_serif_names(self._force_speak_action.get_serif_names())
        self.select_blow_action()
        selected_time = time.time()

        self._actions[27].run({})
        
        while True:
            time.sleep(1.)

            data = self._status.get_data()
            # 10分に一回、ゆれの音を決める
            if time.time() - selected_time > 60.:
                self.select_blow_action(data)
                # その音で、IFTTT

            # 風のまね
            self._blow_actions[self._blow_action_index].run(data)

            # 強制起動もここでやる
            if self._force_speak_action.check(data):
                message = self._force_speak_action.run(data)
                # 一定時間発言していないキーワードだったら、ツイート


            # RT、フォロー、された場合は、ここでいう
            if random.random() > .95:
                # TODO ちょっとこのファイルが再生時間長いので、カットする
                self._speaker.say("iphone")
                continue

            print("search action")
            # このタイミングで、反応があると、ちがうこともいう
            runable_action = [x for x in self._actions if x.check(data)]
            if runable_action:
                start = time.time()
                idx = int(random.random()*len(runable_action))
                message = runable_action[idx].run(data)
                # 一定時間発言していないキーワードだったら、ツイート
                
                print(time.time() - start)

if __name__ == "__main__":
    noren = Norensama()
    noren.main()

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
from action import Hello, Joke, TimeSignal, ForceSpeak, CoredoIntroduction, CoredoIntroductionAM9, CoredoIntroductionLunch, CoredoIntroductionNight, CoredoBoyaki, CoredoAnswerHanashi, CoredoAnswerAisatsu, CoredoAnswerSonota, CoredoIntroductionNight, CoredoBoyaki, CoredoAnswerHanashi, CoredoAnswerAisatsu, CoredoAnswerDare, CoredoAnswerIkku, CoredoAnswerGehin, CoredoAnswerSize, CoredoAnswerToshi
from action.blow import Yurayura, Soyosoyo, Byubyu


class Norensama(object):

    def __init__(self):
        self._speaker = Speaker()
        self._ifttt = Ifttt({
            "api_key": config.IFTTT_APIKEY
        })

        self._status = StatusManager()
        self._actions = [
            # 風の音系
            Soyosoyo(self._speaker),
            Yurayura(self._speaker),
            Byubyu(self._speaker),
            # あいさつ
            Hello(self._speaker),
            Joke(self._speaker),
            TimeSignal(self._speaker),
            # コレド紹介
            CoredoIntroduction(self._speaker),
            CoredoIntroductionAM9(self._speaker),
            CoredoIntroductionLunch(self._speaker),
            CoredoIntroductionNight(self._speaker),
            # クソウンチク
            CoredoBoyaki(self._speaker),
            # ツイッター
            CoredoAnswerHanashi(self._speaker),
            CoredoAnswerAisatsu(self._speaker),
            CoredoAnswerSonota(self._speaker),
            CoredoAnswerDare(self._speaker),
            CoredoAnswerIkku(self._speaker),
            CoredoAnswerGehin(self._speaker),
            CoredoAnswerSize(self._speaker),
            CoredoAnswerToshi(self._speaker),
        ]

        # セリフの強制実行
        self._force_speak_action = ForceSpeak(self._speaker)

        self._blow_action_index = 1

    def main(self):
        print("main")
        status_thread = threading.Thread(target=self._status.update)
        status_thread.daemon = True
        status_thread.start()

        self._status.set_serif_names(self._force_speak_action.get_serif_names())

        self._actions[16].run({})
        
        while True:
            time.sleep(1.)

            data = self._status.get_data()

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

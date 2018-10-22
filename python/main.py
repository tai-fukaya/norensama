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
from action import Yureyure, Hello, Joke, TimeSignal, ForceSpeak
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
        
        print(acc.acc_x, acc.acc_y, acc.acc_z)
        acc_x = abs(acc.acc_x)
        if acc_x > .5:
            self._blow_action_index = 2
        elif acc_x > .2:
            self._blow_action_index = 1
        else:
            self._blow_action_index = 0

    def main(self):
        print("main")
        status_thread = threading.Thread(target=self._status.update)
        status_thread.daemon = True
        status_thread.start()

        self.select_blow_action()
        selected_time = time.time()
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
